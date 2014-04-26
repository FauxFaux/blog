#!/usr/bin/env python3
from lxml import etree
from datetime import datetime
from sys import argv

RSS_DATE_FORMAT = '%a, %d %b %Y %H:%M:%S %z'

# http://foo/bar/baz/ -> baz
def last_element_of_url(url):
    return url.split("/")[-2]

def parse_rss_date(string):
    return datetime.strptime(string, RSS_DATE_FORMAT)

with open(argv[1]) as f:
    tree = etree.parse(f)

for item in etree.ETXPath("//item")(tree):
    title = item.find("title").text
    slug = last_element_of_url(item.find("link").text)
    date = parse_rss_date(item.find("pubDate").text)
    content = item.find("{http://purl.org/rss/1.0/modules/content/}encoded").text

    datafile = date.strftime("%Y-%m-%d-") + slug + ".md"
    with open(datafile, 'w') as f:
        f.write("title: %s\n" % title)
        f.write("slug: %s\n" % slug)
        f.write("date: %s\n" % date)
        f.write("\n")
        f.write(content)


