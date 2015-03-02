#!/usr/bin/env python3

from collections import namedtuple, defaultdict
from glob import glob
import os
import re

#python3-datetime
from datetime import datetime
from dateutil import parser

# python3-markdown
from markdown import markdown

# python3-jinja2
import jinja2

templates = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

Item = namedtuple('Item', ['title', 'slug', 'date', 'content'])

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
        files[slug] = Item(headers['title'], slug, parser.parse(headers['date']), f.read())

dates=sorted(set(((item.date.strftime('/%Y/%m'), item.date.strftime('%Y-%m'))
    for item in files.values())), reverse=True)

def url_of(item):
    return item.date.strftime("/%Y/%m/") + item.slug + "/"

def write_page(path, template, title, **args):
    if not title:
        title='Faux\' blog'
    else:
        title='Faux\' blog: ' + title

    with open_out(path) as f:
        f.write(templates.get_template('index.html').render(
            content=templates.get_template(template).render(args),
            dates=dates,
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
    items=sorted(items, reverse=True, key=lambda item: item.date)
    per_page=6
    chunks=[items[x:x+per_page] for x in range(0, len(items), per_page)]
    for idx, chunk in enumerate(chunks):
        path=base_path
        prev=None
        next=None
        if 0 != idx:
            path=path + 'page/' + str(idx+1) + '/'
            if 1 != idx:
                prev=base_path + 'page/' + str(idx) + '/'
            else:
                prev=base_path

        if len(chunks)-1 != idx:
            next=base_path + 'page/' + str(idx+2) + '/'

        write_page(path + 'index.html', 'list.html', title,
                items=chunk,
                next=next, prev=prev,
                render_post=render_post)

write_list('', files.values(), None)

def by_date(format, items):
    ret = defaultdict(list)
    for item in files.values():
        ret[item.date.strftime(format)].append(item)
    return ret

for by_dates in [by_date('%Y/%m/', files.values()), by_date('%Y/', files.values())]:
    for month, items in by_dates.items():
        write_list(month, items, month)

for static in ['main.css']:
    with open_out('static/' + static) as f:
        f.write(templates.get_template(static).render())
