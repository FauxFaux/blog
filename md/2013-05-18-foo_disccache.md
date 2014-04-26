title: foo_disccache
slug: foo_disccache
date: 2013-05-18 09:48:37+00:00

(I've been saving up a load of tiny projects for one mega blog post.  Apparently that's not working.  Small project avalanche!)

<a href="https://github.com/FauxFaux/foo_disccache">foo_disccache</a> (possibly more correctly spelt foo_dis<strong>k</strong>cache) is a small <a href="http://www.foobar2000.org/">foobar2000</a> component to help smooth playback on machines with plenty of memory.

It tries to trick the OS into caching some of the files that are soon to be played, so playback won't need to stall (waiting for the disc) when the track comes to play.  This additionally allows the drive the music is being read from to spin down (saving noise/power) more frequently, and will assist with uninterrupted music playback when the system is under heavy IO load.

If you don't understand any of that, you almost certainly don't care.

Download and installation instructions are at Github.  Please use Github's issue tracker or wiki for discussion, not comments.
