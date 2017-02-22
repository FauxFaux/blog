title: Tiny Windows utilities
slug: tiny-utilities
date: 2011-04-22 21:50:10+00:00

I have a set of tiny utilities that I use on a daily basis but have never bothered to release.

<strong>Updated:</strong> The binaries are on <a href="https://github.com/FauxFaux/tinies/releases">github releases</a>, and also a local mirror: <a href="/files/tinies-v002.zip">tinies v002 archive</a>.

<strike>All are in the <a href="/files/tinies-v001.7z">tinies v001 archive</a>, in both x64 and legacy format.  <a href="/files/tinies-syms-v001.7z">Symbols</a>, <a href="//git.goeswhere.com/?p=tinies.git;a=tag;h=refs/tags/v001">source and signatures</a> are available.</strike>  No installer is available; just drop them into your All Programs -> Startup folder.

<hr/>

<strong>shiftfocus.exe</strong> adds an extra set of hotkeys for focusing windows.  <code>Ctrl+win+arrow</code> focuses the window to that side of the current window.

This makes the most sense with Aero's Snap turned on.  If you have two windows "half-maximised" on a screen (i.e. one has been <code>win+left</code>'d, and the other <code>win+right</code>'d), then you can switch between them using <code>ctrl+win+left</code> and <code>ctrl+win+right</code>.

<hr/>

<strong>topkey.exe</strong> adds <code>win+w</code> to toggle a windows' always-on-top flag, and <strike><code>win+return</code></strike><code>ctrl+win+return</code> (as <code>win+return</code> is stolen by accessibility from Win7) to create a new command prompt "in the current directory".  (This works for Explorer windows, and things that have the directory at the start of the title, i.e. Notepad++.)

<hr/>

<strong>mousex.exe</strong> allows you to use an xbox360 controller as a mouse.  Different analogue sticks are different sensitivity.  A/B for left/right click.  Shoulder analogue controls for the scrollwheel.</p>

<hr/>

And, for more niche users:

<hr/>

<img style="float: left; padding: 2em" src="/files/powerstatustray.png"/>

<strong>powerstatustray.exe</strong> shows which drives are spun-up, and notifies you when a drive spins up or down.  (Yes, actually, this one was released before.)

<hr/>

<strong>keydump.exe</strong> shows what you can keylog by binding globally to DirectInput.  Most keylogging preventers/detectors completely ignore this, and/or only work through blacklisting, which is laughably pointless.  It doesn't bother translating numbers into keycaps, but it's obvious whether it's working and whether it's been detected.

<hr/>
Others, to date:
<ul>
<li>aukiller: Legacy XP application.</li>
<li>foobar2000-loader.exe: Demo of pre-loading a dll into an application via the debug api.</li>
<li>keytoputty.exe: Take input and send it to a running instance of putty, i.e. to allow input during full-screen applications.</li>
<li>loaddlls.exe just calls LoadLibrary on all it's arguments.</li>
<li>noelev.exe: Legacy implementation of setting <code>__COMPAT_LAYER=RunAsInvoker</code>.</li>
<li>quickkey.exe: Legacy XP application.</li>
<li>unrequireadmin.exe: An even less healthy implementation of noelev.exe.</li>
</ul>
