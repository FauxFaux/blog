title: 2018 in (failed) projects
slug: year-of-projects
date: 2018-12-31T14:48:36+00:00

I have written a large mass of code this year, primarily in Rust.

With only one exception, none of this has reached the 'blog post' level
of maturity. Here lies a memorial for these projects, perhaps as
a reminder to me to resurrect them.

---

[Github's contribution chart](https://github.com/FauxFaux) gives a good
indication of just how much code has been written. Clearly visible are
some holidays, and the associated productivity peaks on either side:

![github contributions](/images/2018-12-31-gh-contributions.png)

---

Some focuses this "year" (Nov 2017+):

### Archives and storage

[contentin](https://github.com/FauxFaux/contentin) and
[splayers](https://github.com/FauxFaux/splayers) recursively unpack an
archive, supporting multiple formats. You have a `gzip` file, on an
[ext4 filesystem](https://github.com/FauxFaux/ext4-rs), inside a
`tar.bzip2` archive, inside a Debian package? No problem.

The aim here was to "ingest" large volumes of "stuff", either for
comparison (e.g. [diffoscope](https://diffoscope.org/), from the
Reproducible Builds project), or for indexing and search.

Speaking of which, [deb2pg](https://github.com/FauxFaux/deb2pg)
demonstrates various ways *not* to build an indexing search engine
for a large quantity of "stuff".

While working on these, I became a bit obsessed with how bad `gzip`
is. `gzip`ing a file, then running it through any kind of indexing,
or even other compression, gives very poor results. *Very* poor.
[rezip](https://github.com/FauxFaux/rezip-rs) is a tool to
*reversibly* transform `gzip` files into a more storable format.
It... never made it. I could complain for hours. See the [README](https://github.com/FauxFaux/rezip-rs/blob/master/README.md#rezip).

Much of this work was done against/for Debian. Debian's `apt` is
not a fun tool to use, so I started rewriting it. [fapt](https://github.com/FauxFaux/fapt)
can download lists, and provide data in a usable form (e.g. `ninja`
build files). [gpgrv](https://github.com/FauxFaux/gpgrv) is enough
of a `gpg` implementation for `fapt`.

Once you start rewriting `apt`, you might as well rewrite the rest
of the build and packaging system, right? [fbuilder](https://github.com/FauxFaux/fbuilder)
and [fappa](https://github.com/FauxFaux/fappa) are two ways not to
do that. `fappa` needed to talk to Docker, so [shipliftier](https://github.com/FauxFaux/shipliftier)
has a partial `swagger-codegen` implementation for Rust.

---

### Networking

Much of the way networking is done and explained for linux is not
ideal.

[netzact](https://github.com/FauxFaux/netzact) is a replacement for
the parts of `netstat` and `ss` that people actually use. It has the
performance of `ss`, but only one the horrible bugs: no documentation
at all. That one is probably fixable, at least!

[pinetcchio](https://github.com/FauxFaux/pinetcchio) continued into
its fourth year, I like to think I made it even worse this year.

[fdns](https://github.com/FauxFaux/fdns) was going to do something with
DNS but I can't really remember which thing I was going to fix first.
There's so much wrong with DNS.

[quad-image](https://github.com/FauxFaux/quad-image) is an image hosting
service. It works, I run it. I even tried to add new image formats, like
[heifers](https://github.com/FauxFaux/heifers). That was a mistake.

---

### IRC

I still use IRC. The protocol is bad, but at least there are working
clients. Slack Desktop still segfaults on start on Ubuntu 18.10, months
after release, because they don't understand how to use Electron and
nobody can fix it for them.

[unsnap](https://github.com/FauxFaux/unsnap) is an IRC title bot. Yes,
there are hundreds of others. No, I don't like working with other people's
untested code in untestable plugin frameworks. Thanks for asking.

[badchat](https://github.com/FauxFaux/badchat) is some kind of IRC thing.
This one might still have some life in it.

---

### CLI tools

[zrs](https://github.com/FauxFaux/zrs) is a re-implementation of `z`, the
directory changing tool. It's good, you should use it.

[sortuniq](https://github.com/FauxFaux/sortuniq) is a more efficient
`| sort | uniq`. It supports some of the flags that either tool supports.
This is probably enough of a blog post for that. I use it frequently.

