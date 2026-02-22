#!/usr/bin/env python3

import os
import re
import shutil
from collections import namedtuple, defaultdict
from datetime import datetime
from glob import glob

# python3-jinja2
import jinja2
import pytz
# python3-slimmer
#import slimmer
from dateutil import parser
# pip3 install --user feedgen
from feedgen.feed import FeedGenerator
# python3-markdown
from markdown import markdown

templates = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

feed_root = 'https://blog.goeswhere.com'
fg = FeedGenerator()
fg.id(feed_root)
fg.title('Faux\' Blog')
fg.author({'name': 'Chris West (Faux)'})
fg.language('en')
fg.link(href=feed_root, rel='alternate')
fg.description('Faux\' (mostly) technical blog')

tz = pytz.timezone('Europe/London')

Item = namedtuple('Item', ['title', 'slug', 'date', 'content', 'mtime'])


def open_out(path):
    path = 'out/' + path
    try:
        os.makedirs(os.path.dirname(path))
    except FileExistsError:
        pass
    return open(path, 'w')


files = {}
for name in glob("md/*.md"):
    headers = {}
    with open(name) as f:
        while True:
            s = f.readline()
            if len(s) < 3:
                break
            bits = [x.strip() for x in s.split(":", 1)]
            headers[bits[0]] = bits[1]
        slug = headers['slug']
        if not slug:
            raise 'No slug: ' + name
        files[slug] = Item(headers['title'], slug,
                           parser.parse(headers['date']), f.read(),
                           os.path.getmtime(name))


def url_of(item):
    return item.date.strftime("/%Y/%m/") + item.slug + "/"


def write_page(path, template, title, **args):
    if not title:
        title = 'Faux\' blog'
    else:
        title = 'Faux\' blog: ' + title

    with open_out(path) as f:
        f.write(
            #slimmer.html_slimmer(
                templates.get_template('index.html').render(
                    content=templates.get_template(template).render(args),
                    title=title))


def render_post(item, full=False):
    content = item.content
    more = False
    if '<!--more-->' in item.content:
        more = not full
        if more:
            content = re.sub('<!--more-->.*', '', content, flags=re.DOTALL)
        else:
            content = re.sub('<!--more-->', '<a name="more"></a>', content)

    return templates.get_template('post.html').render(
        content=markdown(content),
        url=url_of(item),
        date=item.date.strftime('%Y-%m-%d'),
        more=more,
        title=item.title)


for slug, item in files.items():
    sub = url_of(item)
    write_page(sub + 'index.html', 'single.html', item.title,
               render_post=render_post,
               item=item)


def write_list(base_path, items, title):
    items = sorted(items, reverse=True, key=lambda item: item.date)
    per_page = 6
    chunks = [items[x:x + per_page] for x in range(0, len(items), per_page)]
    for idx, chunk in enumerate(chunks):
        path = base_path
        prev = None
        next = None
        if 0 != idx:
            path = path + 'page/' + str(idx + 1) + '/'
            if 1 != idx:
                prev = base_path + 'page/' + str(idx) + '/'
            else:
                prev = base_path

        if len(chunks) - 1 != idx:
            next = base_path + 'page/' + str(idx + 2) + '/'

        write_page(path + 'index.html', 'list.html', title,
                   items=chunk,
                   next=next, prev=prev,
                   render_post=render_post)


write_list('all/', files.values(), None)


def by_date(format, items):
    ret = defaultdict(list)
    for item in sorted(files.values(), reverse=True, key=lambda item: item.date):
        ret[item.date.strftime(format)].append(item)
    return ret


for by_dates in [by_date('%Y/%m/', files.values()), by_date('%Y/', files.values())]:
    for month, items in by_dates.items():
        write_list(month, items, month)


def write_index(items):
    by_year = by_date('%Y', sorted(items, reverse=True, key=lambda item: item.date))

    write_page('index.html', 'front.html', None,
               by_year=sorted(by_year.items(), reverse=True, key=lambda pair: pair[0]))


write_index(files.values())

in_feed = sorted(files.values(), reverse=True, key=lambda item: item.date)[0:10]

for item in in_feed:
    fe = fg.add_entry()
    full_url = feed_root + url_of(item)
    fe.id(full_url)
    fe.link(href=full_url, rel='alternate')
    fe.title(item.title)
    fe.content(markdown(item.content))
    fe.updated(tz.localize(datetime.fromtimestamp(item.mtime)))
    fe.published(tz.localize(datetime.fromtimestamp(item.mtime)))

os.makedirs('out/feed/atom')
os.makedirs('out/feed/rss')
fg.atom_file('out/feed/atom/index.xml')
fg.rss_file('out/feed/rss/index.xml')
fg.rss_file('out/feed/index.xml')

for static in ['main.css']:
    with open_out('static/' + static) as f:
        f.write((templates.get_template(static).render()))

shutil.copytree('images', 'out/images')
