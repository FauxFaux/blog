title: Updates: Dell's 2407WFP, Vista.
slug: updates-dells-2407wfp-vista
date: 2007-04-12 20:44:20+00:00

<a href="http://blog.prelode.com/?p=51">Before</a> I mentioned that my 2407 was getting terrible artifacts.

So...

It turns out they go away if you plug it into the other port on my graphics card.

Doh.


Also, I mentioned that I was using <a href="http://blog.prelode.com/?p=59">mostly Microsoft apps on Vista</a>. Some changes:
<ul>	<li>Windows Media Player has been sacrificed for <a href="http://foobar2000.org/">Foobar2000</a> for music, after it "removed" most of the id3 tags from my mp3 files.
<strong>Nitpickers' Corner</strong>: Technically, it didn't remove the tags at all. 
<ul>	<li>Windows Media Player (and Windows Explorer) (and, for other things, pretty much the entirety of Windows) likes things in UTF-16. Most of the files in my collection have both id3v2.3 and id3v2.4 tags.</li>
	<li>The 2.4 version of the tags, having been written by Picard (which, by default, writes UTF-8 tags (which I'd have probably picked anyway)), were not acceptable to WMP.</li>
	<li>In this situation, WMP reads the 2.3 version of the tags (which has some nasty limitations like, for instance, cutting off all fields at a certain length), and writes a second id3v2.4 block to the files, at the start.</li>
	<li>Next time anything attempts to read the file, it'll see WMP's 2.4 block (containing just the 2.3 information), skip over the real 2.4 block, and see the original 2.3 block, making it look like the tags have gone, whereas they're actually still in the file.</li>
</ul></li>
	<li>WMP is still in use for video playing, but most of it's decoding is now assisted by <a href="http://ffdshow-tryout.sf.net/">ffmpeg</a>, which is awesome.</li>
	<li>IE7 has now disappeared for Opera. Yaaaay, Opera.</li>

</ul>



