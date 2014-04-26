title: Indexing Service / Google Desktop
slug: indexing-service-google-desktop
date: 2006-03-16 21:34:40+00:00

It can't just be me, someone else must want a find tool that's:

<ul>
	<li><strong>simple</strong> - no checking the file-types, I don't want previews, I don't want to search inside the file.. I want to search based on the <em>file name</em>.</li>
	<li><strong>relatively fast</strong> - Google Desktop is fast, but it's faster than I can read, so it's irrelevant. Windows search is slow. To search my \SDK folder (4GB, 40k files, 4k folders) would take about 10 minutes.</li>
	<li><strong>outputs in a useful format</strong> - <a href="http://desktop.google.com/">Google Desktop</a>'s search results are <em>completely</em> useless. You can't open the file with anything apart from the default editor. You can't move/copy the file. You can't even find out where the file is. Windows Search's results are perfect for this.</li>
	<li><strong>not whory</strong> - It should not be using/interrupting/intercepting disk access. Ever. Both Indexing Service and Google Search do this.</li>
	<li><strong>work straight off</strong> - Google Desktop just does sweet FA when you install it.. and waiting for it to do something (by doing other things at the computer) makes it continue to do sweet FA. It should actually /do/ the search instead of moaning about the index being empty. It should be able to use the currently running search in it's index, anyway.</li>
</ul>

And, to completely contradict myself:
<ul>	<li>Some files' file names should be completely disregarded over other information, if it's available. For example: Music with metadata (ogg/vorbis, ogg/flac, id3/mp3) should disregard the file-system completely.</li></ul>

I plan to write this at some point, if you feel like doing so instead, feel free. If you don't release the source, I will write something better, I promise. :)