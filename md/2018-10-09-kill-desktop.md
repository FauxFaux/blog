title: kill-desktop and TUIs
slug: kill-desktop
date: 2018-10-09T19:40:55+01:00

[kill-desktop](https://github.com/FauxFaux/kill-desktop) tries to get your
"X" applications to exit cleanly, such that you can shutdown, or reboot.

"Watch" the ["demo" in the repository readme](https://github.com/FauxFaux/kill-desktop#demo),
or try it out for yourself:

```
cargo install kill-desktop
```


Many people just reboot. This risks losing unsaved work, such as documents,
the play position in your media player, or even
[the shell history in your shell](https://bugzilla.redhat.com/show_bug.cgi?id=1141137).

This feature is typically built in to desktop environments, but somewhat
lacking in the more minimalist of linux window managers, such as my favourite,
[i3wm](https://i3wm.org/).

Even the more complex solutions, such as the system built into Windows, do
not deal well with naughty applications; ones that will just go hide in the
tray when you try to close them, or that show dialogs a while after you
asked them to exit.

`kill-desktop` attempts to solve this problem by keeping track of the state
of the system, and offering you ways to progress. If one of these naughty
hiding applications merely hides when you close the window, `kill-desktop`
doesn't forget. It tracks the process of that window, waiting for it to go
away. If it is not going away, you are able to ask the *process* to exit. Or
just shut down. It's probably a bad application anyway.

---

Interesting learnings from this project:

Firstly, writing an interface was a bit of a pain. I wanted to be able to
prompt the user for an action, but also be able to show them updates. It is
not possible to do this without
[threads](https://play.rust-lang.org/?gist=b2f0144b92a7ac4a5322ab2e1d5a6887&version=stable&mode=debug&edition=2015),
as there is no way to do a non-blocking read from `stdin`. This surprised me.

You can't even read a single character (think `Continue? y/n`) without messing
with the terminal settings, which needs very low level, non-portable libraries.

There are nicely packaged solutions to this problem, like
[`termion's async_stdin`](https://docs.rs/termion/1.5.1/termion/fn.async_stdin.html)
but this ended up messing with the terminal more than required (it puts it all
the way into `raw` mode, instead of stopping at `-icanon`). I
[wrote my own](https://github.com/FauxFaux/kill-desktop/blob/3bebe9fc3454f724c9a9a3fa24e2b537a2dff066/src/term.rs).

---

Secondly, it's amazing how a relatively simple application can end up tracking
[more state than expected](https://github.com/FauxFaux/kill-desktop/commit/1e338fb40fb381d9e4406148b006dee84af612ec), and
[manually diffing that state](https://github.com/FauxFaux/kill-desktop/commit/c7727611ce8a7fae04ade76a70675f17c0997db1).

I also spent time
[moving errors to be part of the domain](https://github.com/FauxFaux/kill-desktop/commit/1e338fb40fb381d9e4406148b006dee84af612ec#diff-639fbc4ef05b315af92b4d836c31b023R183),
which isn't even fully surfaced yet. It amazes me how much code ends up being
dedicated to error handling, even in a language with excellent terse error
handling. (Terminology from
[Feathers](https://www.youtube.com/watch?v=3RtLCav0Bp4).)

It's also ended up with *nine* dependencies, although between four and six of
those are for loading the (trivial) config file, which could be done better.

