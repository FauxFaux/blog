#!/usr/bin/env python3

from collections import namedtuple
from glob import glob
import os


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
    return item.date.strftime("%Y/%m/") + item.slug + "/"

def write_page(path, template, **args):
    with open_out(path) as f:
        f.write(templates.get_template('index.html').render(
            content=templates.get_template(template).render(args),
            dates=dates,
            title='???'))

def render_post(item):
    return templates.get_template('post.html').render(
            content=markdown(item.content),
            url=url_of(item),
            date=item.date.strftime('%Y-%m-%d'),
            title=item.title)

for slug, item in files.items():
    sub = url_of(item)
    write_page(sub + 'index.html', 'single.html',
        render_post=render_post,
        item=item)

write_page('index.html', 'list.html',
            items=sorted(files.values(), reverse=True, key=lambda item: item.date),
            render_post=render_post)

for static in ['main.css']:
    with open_out('static/' + static) as f:
        f.write(templates.get_template(static).render())
