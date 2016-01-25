title: BlobOperations: A JDBC PostgreSQL BLOB abstraction
slug: bloboperations
date: 2015-12-23T23:09:35+0000

[BlobOperations](https://github.com/FauxFaux/bloboperations)
 provides a `JdbcTemplate`-like abstraction over `BLOB`s in
 PostgreSQL.

The [README](https://github.com/FauxFaux/bloboperations#bloboperations)
 contains most of the technical details.

It allows you to deal with large files; ones for which you don't want
 to load the whole thing into memory, or even onto the local storage
 on the machine.  Java 8 lambdas are used to provide a not-awful API:

    blops.store("some key", os -> { /* write to the OutputStream */);
    blops.read("other key", (is, meta) -> { /* read the InputStream */);

Here, the (unseekable) Streams are connected directly to the database,
 with minimal buffering happening locally.  You are, of course, free
 to load the stream into memory as you go; the target project for this
 library does that in some situations.

In addition to not being so ugly, you get free deduplication and
 compression, and a place to put your metadata, etc.  Please read
 the README for further details about the project.

---

And, some observations I had while writing it:

I continue to be surprised at how hard it is to find good advice on
 locking techniques and patterns for Postgres.  For example,

    SELECT * FROM foo WHERE pk=5 FOR UPDATE;

... does nothing if the `pk=5` doesn't exist (yet).  That is, there's
 no neat way to block until you know whether you can insert a record.
 Typically, you don't want to block, but if your code then progresses
 to do:

    var a = generateReallySlowThing();
    INSERT INTO foo (pk, bar) VALUES (5, a);
    COMMIT;

 ...it seems a shame to have waited for that slow operation, and then
 have the `INSERT` explode on you.  The "best" solution here appears
 to insert a blank record, commit, then lock the record, do your slow
 operation, and then update it.  As far as I'm aware, none of the
 [`UPSERT` related changes in PostgreSQL 9.5](https://wiki.postgresql.org/wiki/What's_new_in_PostgreSQL_9.5)
 help with this case at all.  I would love to link to a decent discussion
 of this... but I'm not aware of one.

 A similar case comes up later, where I wish for `INSERT ON CONFLICT DO NOTHING`,
  which is in PostgreSQL 9.5.  Soon.

