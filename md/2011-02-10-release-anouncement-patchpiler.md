title: Release anouncement: PatchPiler!
slug: release-anouncement-patchpiler
date: 2011-02-10 23:52:28+00:00

Many people find modern version control systems confusing.  PatchPiler offers a new, simpler way to think about version control, offering you far more flexibility than <a href="http://git-scm.com/">certain other</a> version control systems.

All software development is the creation of patches; small changes to the state of the software.  PatchPiler's command-line tool, <code>papi</code>, lets you manage these patches efficiently.

<div style="height: 2em;"></div><hr style="clear: left"/><div style="height: 2em;"></div>

<img src="/files/papi-commit.png" style="float: left; padding: 2em"/><p>Like in other version control systems, <code>papi commit</code> adds a patch (yellow) to the existing stack of patches (green).  As with any modern version control system, you can have multiple outstanding patches on a pile.</p>

<div style="height: 2em;"></div><hr style="clear: left"/><div style="height: 2em;"></div>

<img src="/files/papi-new-pile.png" style="float: left; padding: 2em"/>

Sometimes you want to be working on multiple things at the same time, say yellow and blue things.  For this, there's <code>papi new-pile</code>.

It lets you name your new pile, let's call it blue.  This means you can pile patches on "blue" while continuing to pile patches on "yellow".  This is amazingly cool.  In fact, given that "blue" is completely unrelated to "yellow", somebody else can be piling patches on "blue" while you continue working on "yellow".

<div style="height: 2em;"></div><hr style="clear: left"/><div style="height: 2em;"></div>

<img src="/files/papi-copy.png" style="float: left; padding: 2em"/>

Frequently you'll want to copy patches between piles.

<code>papi copy</code> lets you copy a patch from one pile to another.

Something cool has happened in "yellow" and you want in?  Just copy it across!  The patch is now in both piles, but this is okay, as they're currently unrelated.

<div style="height: 2em;"></div><hr style="clear: left"/><div style="height: 2em;"></div>

<img src="/files/papi-update.png" style="float: left; padding: 2em"/>

<code>papi re-pile</code> allows you to catch-up with another pile's entire history.

It just "re-piles" your patches on top of the patches from the other pile. This doesn't affect the other pile; it's still a separate stream of development.

Note how it intelligently works out that the yellow patch in "blue"'s pile was already included earlier on, so it's no-longer necessary to copy it in.

<div style="height: 2em;"></div><hr style="clear: left"/><div style="height: 2em;"></div>

<img src="/files/papi-bless.png" style="float: left; padding: 2em"/>

You'll notice that the pile named "blue" now has all of the outstanding patches; this brings us on to the last command: <code>papi bless</code> marks changes as complete and removes any unnecessary piles.

This results in a nice, clean pile of patches, leaving you ready to continue developing.  The possibilities are endless!

<div style="height: 2em;"></div><hr style="clear: left"/><div style="height: 2em;"></div>
<!--more-->

Spoilers:  <code>papi</code> is just <code>git</code>.

<a href="/files/papi.svgz">Images' source</a>.
