title: Windows XP SP2 + DEP
slug: windows-xp-sp2-dep
date: 2006-02-06 15:58:59+00:00

Since <a href="http://nunzioweb.com/daz/">DoctorO</a> removed <a href="http://www.codeproject.com/tips/aggressiveoptimize.asp">AggressiveOptimize.h</a>'s broken optimisations from his <a href="http://www.winamp.com/">Winamp</a> plugins, I've been running Windows fine with NoExecute on "OptOut", ie. applications can choose not to have DEP applied to them.

Earlier, because I was bored, I decided to switch DEP from <a href="http://support.microsoft.com/default.aspx?scid=kb;en-us;875352">OptOut to AlwaysOn. More information on MSDN</a>. This removes the option for applications to opt-out.

So far (ie. in about 10 minutes) the following things have broken:

<ul>
	<li>Opera, closed on startup with a DEP error.</li>
	<li>Firefox, dies on startup: 'XPCOM:EventReceiver' attempts to write to memory that it isn't allowed to.</li>
	<li>Acrobat Reader, crashes after a few seconds of displaying the page with a DEP error.</li>
	<li>Internet Explorer 6 has DEP errored once or twice, I'm guessing this is a plugin.</li>
</ul>

Other things (such as Java6, apache2.2, mysql5, all of the drivers I have installed, etc.) were suprisingly fine.

If I can <a href="http://my.opera.com/community/forums/topic.dml?id=122829">get a working build of Opera</a>, there's nothing else on that list that I particularily need.. Acrobat Reader is convenient, but it'll be nice to have something substantial to complain to them about...

<b>Followup:</b>
<ol>
	<li><a href="http://www.opera.com/">Opera</a>'s issue appears to be that it's packed with <a href="http://aspack.com/">ASPack</a>, which just Doesn't Work, meaning their sales are going to drop off a bit at some point..</li>
	<li>Firefox's issue is, ironically, with the feedback agent. Deleting that fixes the problem.</li>
</ol>

The other two remain unstable, but IE is unnecessary now I have a non-IE browser working; and Acrobat Reader is now uninstalled.