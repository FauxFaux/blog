#!/bin/sh
set -eu
rm -rf out
./make.py
rsync -a --delete out/ /srv/blog-staging.goeswhere.com