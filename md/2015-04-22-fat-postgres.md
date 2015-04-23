title: Fat data and Postgres
slug: fat-postgres
date: 2015-04-22T22:11:48+0100

I spend a reasonable portion of my life dealing with Medium Data: columnar files (typically CSV)
you can easily fit on disc, can easily fit in disc cache after compression, and can
probably fit in RAM after some pre-processing; files slightly too big to open in
modern versions of Excel, and far, far too big for LibreOffice Calc or Apple's Pages.

Sometimes, I like to load these files into a database table to have a look around; say,
to look at the distinct values in some columns.  I was slightly surprised to find, however,
that
[most](http://www.postgresql.org/about/)
[database](https://docs.oracle.com/cd/B19306_01/server.102/b14237/limits003.htm)
[engines](https://www.sqlite.org/limits.html)
have a column limit around the 1,000-2,000 column mark.


I've got a fat dataset, ~2,000 columns, 600MB total.  Let's load it into Postgres anyway.

My first attempt was to insert it directly from [psycopg2](http://initd.org/psycopg/)
(all operations inside a single transaction):

    for line in file:
        cur.execute("""insert into big values (%s)""", (line,))

This results in binaries all over your db (thanks, Python!), and takes ~90s.

Fixing:

    cur.execute("""insert into big values (%s)""", (line.decode('utf-8'),))

...gets it down to 60s.  I'm not sure where the performance is coming from here.  More
efficient/aggressive compression for
[TOAST](http://www.postgresql.org/docs/9.4/static/storage-toast.html)ing of the non-binary text,
even though it's bit-identical (as all the data is (close enough) to low-ascii)?
More likely that the wire format and/or the driver code for strings has had more love.

Right!  Data's in the db.  Can't turn it into columns directly, so ... wait, there's no limit on array
lengths!

    create table arrays as select regexp_split_to_array(line, E'\t') arr from big;

... yeah.  Well, it was a good idea.  I didn't wait for this to complete, but I estimate 1h45m.  Not
sure what's slow here... maybe compiling the regexp, or it not expecting such a large array to be
returned, such as would happen if you were heavily optimised for statements like:

    ... regexp_split_to_array(line, E'\t')[3] ...

Never mind.  Python can probably do a better job!

    cur.execute("""insert into arr values (%s)""", (line.decode('utf-8').split('\t'),))

Much to my surprise, Python actually does do a better job.  8m55s, around 50% of the time spent in Python,
so would probably be a lot faster in a non-naive implementation, or after a JIT had fixed it up.

This table is actually usable:

    select max(array_length(line, 1)) from arr2;
    ...
    Execution time: 1971.869 ms

Good sign!  Right, now, on to some data analysis.  Let's look at the distinct values in each column:

    echo select $(for i in {1..1959};echo "count(distinct line[$i]) line$i,") \
        | sed 's/,$/ from arr;/' \
        | psql -U big -x

For those that don't read shell, or are confused by the zshisms, this generates:

    select count(distinct line[1]) line1, count(distinct line[2]) line2, ... from arr;

And it returns:

    ERROR:  target lists can have at most 1664 entries

I actually had to look this error up.  You can't select more than that totally random number
of results at a time.  Bah!  I set it going on 1,600 columns, but also got bored of that running after
around 20m.

It's worth noting at this point that Postgres does most operations on a single thread, and that this
isn't considered a serious problem.  It's not ideal for many of my usecases, but it's also not all that
hard to get some parallelism in the client.

Let's parallelise the client:

    P=8
    COLS=1959
    echo {1..$COLS} | xargs -n $(($COLS/$P+$P)) -P $P \
        zsh -c 'echo select $(for i in "$@"; echo "count(distinct line[$i]) line$i,")' \
        '| sed "s/,\$/ from arr;/"' \
        '| psql -U big -x'

(I really need to find a good way to manage parallelism in shell without xargs.  Wait, no.  I really need
to stop writing things like this in shell.)

This takes around 17m total, and consumes a minimum of 20gb of RAM.  But, at least it works!

For comparison:

 * [pandas](http://pandas.pydata.org/) can ingest and compute basic stats on the file
    in ~1m / 6gb RAM (although it's cheating and only supporting numerics).
 * shell (`cut -f $i | sort -u | wc -l`) would take about 1h20m.
 * Naive Java implementation took me 4m to write from scratch, and takes about 35s to compute the answer.

In summary: Don't use Postgres for this, and Java wins, as usual.

<!--more-->

All timings done on an i7-4770k (4 physical, 8 virtual), 24gb RAM, ssd, btrfs + lzo compression, amd64 Linux.
PostgreSQL 9.3 with some basic tuning (`shared_buffers`, `effective_cache_size`, `synchronous_commit`, etc.).
