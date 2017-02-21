title: Busy work: pasane and syscall extractor
slug: working-around-linux
date: 2017-02-21T15:41:24+00:00

Today, I wrote
[a load of Python](https://github.com/japaric/syscall.rs/pull/15/commits/847debb0a1de5f756fed124fea671ad722ba99ab#diff-b35c4def919470d7d2138ba45bed4adc)
and
a *load* of C to work around
pretty insane problems in Linux, my choice of OS for development.

---

[pasane](https://github.com/FauxFaux/pasane) is a command-line volume
control that doesn't mess up channel balance. This makes it unlike all
of the other volume control tools I've tried that you can reasonably
drive from the command line.

It's necessary to change volume from the command line as
I [launch commands in response to hotkeys](https://github.com/FauxFaux/rc/commit/91964555ae85a2464b8dc7bb37847eb5423645e8)
(e.g. to implement the `volume+` button on my keyboard). It's also
occasionally useful to change the volume via. SSH. Maybe there's another
option? Maybe something works via. dbus? This seemed to make the most
sense at the time, and isn't too awful.

Am I insane?

---

Next up: Some code to
[parse the list of syscalls from the Linux source tree](https://github.com/japaric/syscall.rs/pull/15/commits/847debb0a1de5f756fed124fea671ad722ba99ab#diff-b35c4def919470d7d2138ba45bed4adc).

It turns out that it's useful to have these numbers available in other
languages, such that you can pass them to [tools](/2017/02/seccomp-tool/),
so that you can decode raw syscall numbers you've seen, or simply so that
you can make the syscalls.

Anyway, they are not available in the Linux source. What? Yes, for most
architectures, this table is not available. It's there on `i386`, `amd64`,
and `arm` (32-bit), but not for anything else. You have to.. uh.. build
a kernel for one of those architectures, then compile C code to get the
values. Um. What?

This *is* insane.

The Python code (linked above) does a reasonably good job of extracting
them from this insanity, and generating the tables for a couple more
arches.

I needed to do this so I can copy a file efficiently. I think. I've kind
of lost track. Maybe I am insane.

