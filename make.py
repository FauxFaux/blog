#!/usr/bin/env python3

from markdown import markdown
from glob import glob

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
        headers['content'] = f.read()
        files[slug] = headers

print(len(files))

