#!/usr/bin/env python3

from markdown import markdown
from glob import glob
from collections import namedtuple
from datetime import datetime
from dateutil import parser
import os

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

def url_of(item):
    return item.date.strftime("%Y/%m/") + item.slug + "/"


for slug, item in files.items():
    sub = url_of(item)
    with open_out(sub + "index.html") as f:
        f.write(markdown(item.content))

with open_out("index.html") as f:
    for item in sorted(files.values(), reverse=True, key=lambda item: item.date):
        f.write('<a href="' + url_of(item) + '"><h1>' + item.title + '</h1></a>\n')
        f.write(markdown(item.content))
