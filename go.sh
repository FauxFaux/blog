#!/bin/sh
set -eu
rm -rf out
uv run make.py
rsync -a --delete out/ /srv/blog.goeswhere.com
rsync -a --delete files /srv/blog.goeswhere.com/
