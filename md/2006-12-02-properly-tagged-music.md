title: Properly tagged music.
slug: properly-tagged-music
date: 2006-12-02 20:56:54+00:00

Alternately: Why <a href="http://foobar2000.org/">Foobar2000</a> and Picard suck.

I like properly tagged music.

Obviously it's nice to be able to get your computer to tell you what song you're playing, but, if you need to be told, you probably aren't a fan of it anyway. Maybe you ripped your cds and <a href="http://cdexos.sf.net/">your cd-ripper</a> tagged the files from <a href="http://www.freedb.org/">FreeDB</a>, or similar, and you've ended up with the names in block-caps, or with all the lovely crazy characters removed?

I'd hope that most people would care enough to fix tags that are (incorrectly) written in block-caps (<a href="http://www.winamp.com/">Winamp</a> users probably wouldn't notice), but most people wouldn't bother correcting an album by ᛏᛣᚱ (yay, runes) that's been mistagged as Týr or Tyr, for instance, mainly due to the effort involved.

There are quite a few automatic solutions to manually fixing these tags, starting with FreeDB that's already been mentioned, my favourite being <a href="http://musicbrainz.org/">MusicBrainz</a>. 

They have a <strong>wonderful</strong> tool called Picard that will allow you to get information from their database into your files, including the correct spelling of <a href="http://musicbrainz.org/artist/50fc4742-1389-45a0-8c6f-6a5159ae20c2.html" title="Show artist at MusicBrainz"><b>ᛏᛣᚱ</b></a>. <a href="http://musicbrainz.org/doc/PicardDownload">Picard</a> has a <a href="http://musicbrainz.org/doc/HowToTagFilesWithPicard">user guide</a>, I've written an <a href="http://faux.uwcs.co.uk/picardguide/">alternative Picard user guide</a> to illustrate the way I tag stuff.

Assuming you don't care about the correct usage of the artist names, nor having credit correctly given for remixes, etc., why would you bother to process your music with Picard?

Along with ensuring that the files have the correct normal tags (that you'd normally see), it also puts extra information from the MusicBrainz database into your files, for instace, the sort-order name of each artist. This allows you to do fun things with your playlist, for instance, what I do with Foobar:

<strong>Sort order:</strong>
<pre>$if(%MUSICBRAINZ_ARTISTID%%MUSICBRAINZ ARTIST ID%, ,)$if($strcmp(%MUSICBRAINZ ALBUM ARTIST ID%%MUSICBRAINZ_ALBUMARTISTID%,89ad4ac3-39f7-470e-963a-56509c546377),%album% - %MUSICBRAINZ ALBUM ID%%MUSICBRAINZ_ALBUMID%,%MUSICBRAINZ ALBUM ARTIST SORTNAME%%MUSICBRAINZ_ALBUMARTISTSORTNAME% - %MUSICBRAINZ ALBUM ARTIST ID%%MUSICBRAINZ_ALBUMARTISTID% - %album% - %MUSICBRAINZ ALBUM ID%%MUSICBRAINZ_ALBUMID%) - %album% - %tracknumber% - %album artist% - %title%</pre>

<strong>Playlist display:</strong>
<pre>%list_index%. 
$if(%MUSICBRAINZ_ARTISTID%%MUSICBRAINZ ARTIST ID%,,UT - )
$if($strcmp($longest(%MUSICBRAINZ ALBUM ARTIST ID%,%MUSICBRAINZ_ALBUMARTISTID%),89ad4ac3-39f7-470e-963a-56509c546377),
%album% - %tracknumber% - %album artist% - %title%,
%album artist% - %album% - %tracknumber% - %title%)
$tab()
%length%
</pre>

Note that both of those are whitespace-sensitive, the second is new-line insensitive, so has been split up slightly to make it at least sane to read.

<strong>What these do:</strong>

These mean that your playlist will read something like this:

<pre>
A Various Artists CD - 01 - Some Artist - Track Name
A Various Artists CD - 02 - Some Other Artist - Track Name
...
Jim Bob - Another Album - 01 - Track Name
Jim Bob - Some Album - 01 - Track Name
...
Canned Beans - Album #1 - 01 - Track Name
...
UT - BLERG
...
</pre>
etc, where "Jim Bob" is a person's name, so will have a <em>sort order</em> of "Bob, Jim", and "Canned Beans" is a band, so will have a sort order of "Canned Beans". The "UT - " prefix on files at the end of the playlist mean that they need tagging.

This has the wonderful effect of meaning that all of the albums by a single artist will be in the same place (as Jim Bob's are above) without Various Artist cds being broken up by artist, which makes no sense.

Now that I've got my playlist back to how I like it, back to the original title of this post, Picard (0.7.2) sucks for writing tags with completely different names to different types of file, for instance:

<pre>M:\Compilations\Clubland\Seven (cd1)>cat 01.mp3 | <a href="http://grail.cba.csuohio.edu/~somos/xxd.c">xxd</a> | <a href="http://gnuwin32.sourceforge.net/">head</a> -n 16 | tail -n 3
00000d0: 0000 034d 7573 6963 4272 6169 6e7a 2041  ...MusicBrainz A
00000e0: 6c62 756d 2041 7274 6973 7420 4964 0038  lbum Artist Id.8
00000f0: 3961 6434 6163 332d 3339 6637 2d34 3730  9ad4ac3-39f7-470</pre>

..against..

<pre>M:\Compilations\Clubland\Six (cd1)>head -n 2 "04.ogg" | xxd | head -n 19 | tail -n 3
0000100: 4d55 5349 4342 5241 494e 5a5f 414c 4255  MUSICBRAINZ_ALBU
0000110: 4d41 5254 4953 5449 443d 3839 6164 3461  MARTISTID=89ad4a
0000120: 6333 2d33 3966 372d 3437 3065 2d39 3633  c3-39f7-470e-963</pre>

Grr.

Foobar also needs a kick for making it so hard to deal with these (and debug them), along with being inconsistent (in undocumented ways) between the "sort" and the "display" shown above, which is also a major pain.
