title: Everyday Shell
slug: everyday-shell
date: 2015-05-04T09:15:17+0100

A couple of people mocked my use of shell in [my last post](/2015/04/fat-postgres), so I thought
I'd write up a couple of problems I solved this week, to allow me to laugh at the solutions in the
future, and, more importantly, for you to laugh at them now.

White-space has been inserted into the examples for bloggability, but all these are what I actually wrote,
as one-liners.


### Downloading matching files

I've got the http:// URL of [an indexed directory](https://reproducible.debian.net/dbd/unstable/amd64/),
which contains a load of large files.  I want to download all the files with `-perl` and `.html` in their
names.

First thought: `wget` probably has a flag for this:

    wget -np --mirror --accept='*-perl*.html' https://example.com/foo/

This actually produces the right output, but... it downloads all the files, then deletes the ones that it
doesn't want to keep.  My guess is that it's sucking links out of the intermediate files.  Maybe this could
be fixed by limiting the recursion depth, instead of using mirror?  This isn't what I did, however:

    curl https://example.com/foo/ | \
       cut -d'"' -f 8 | \
       fgrep -- -perl | \
       sed 's,^,https://example.com/foo/,' | \
       wget -i-

Yep, that works.  Very unix-y solution, every tool only doing one thing.
Breaks horribly if the input is wrong.  Fast, as it only looks at files it needs, and `wget` manages a
connection pool for you (whereas `for u in $urls; wget $u` wouldn't).


### Line counts in a git repository

I've got a checkout of a git repository, and I want to know roughly how many lines of production code
there are in it.  It's a Java codebase, so most production code is in `*/src/main` or `client/src`.

    find -maxdepth 3 -name main -o -name client | xargs sloccount

Why didn't I use `-exec` here?  Probably paranoid of `-exec` with `-o`.  Correct solution:

    find -maxdepth 3 \( -name main -o -name client \) -exec sloccount {} +

Two massive problems, anyway:

1. There's a load of generated or downloaded code in those directories; build output, downloaded modules, ...
2. `sloccount` really hates taking multiple directories as input, especially when they have the
same (base)name, and just ignores some of them.

Next up, let's use `git ls-files` to skip ignored files:

    git ls-files | egrep 'src/main|client/src' | xargs cat | wc -l

Barfs as there's white-space in the file names, which I wasn't expecting.
Could probably work around it with some:

    ... | while read line; do cat $line; done | wc -l

...but we may as well fix the real problem.  `git ls-files` has `-z` for null-terminated output, and
xargs has `-0` for null-terminated input.  `grep` has `-Z` for null-terminated output... but I couldn't
find anything that would make it take null-terminated entries as input.  Sigh.

Wait, it's git.  We can just clone the repo.  ([`cdt`](https://github.com/FauxFaux/rc/blob/master/.zshrc)
`cd`s to a new `t`emporary directory)

    cdt; git clone ~/code/repo .

...then we can use find again:

    find \( \
            -name \*.java -iwholename '*src/main*' \
        -o \
            -name \*.js -iwholename '*client*' \
    \) -exec cat {} + | \
    grep -v '^$' | \
    egrep -v '^[ \t]*//' | \
    wc -l

Close enough to the expected numbers!  Now, let's backfill [graphite](http://graphite.wikidot.com/):

    (for rev in $(g rev-list --all | sed '1~50p'); do
        g co -q $rev
        echo code.production $(!!) $(g show --format=%at | head -n1)
    ) | grep -v ' 0 ' | nc localhost 2444

Woo!
