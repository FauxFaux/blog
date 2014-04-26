title: Adobe and Acrobat Reader
slug: adobe-and-acrobat-reader
date: 2006-04-27 02:34:27+00:00

<a href="http://blog.prelode.com/?p=22">As I mentioned before</a>, <a href="http://www.adobe.com/">Adobe</a>'s <a href="http://adobe.com/products/acrobat/readstep2.html">Acrobat Reader</a> has issues with DEP.

At that point, I was running as Administrator, which I'm no-longer doing. (Try it, it really does work if you know what you're doing.. yeah, I know, that's the wrong way around, limited accounts should be for those who don't know what's going on).

Installers for some applications say things like "This installer must be run as administrator.", or "This may not work unless run as administrator.", it turns out that most of them are lying. The ones that won't attempt run can normally be attacked with great tools like Jared Breland's <a href="http://www.legroom.net/modules.php?op=modload&name=Open_Source&file=index&page=software&app=uniextract">Universal Extractor</a>.

Adobe, being the great company that they are, have decided to take a different approach. Running the Acrobat Reader (7.07) setup file as non-admin gives you the incredibly useful error message:

<code>
---------------------------
FEAD® 2.5 Optimizer©
---------------------------
Access is denied.


File: C:/Program Files/Adobe/Acrobat 7.0/Setup Files/RdrBig707/ENU

---------------------------
OK   
---------------------------
</code>

Good work, guys.

Even better, trying to unpack the setup file manually suggests that they've used a "modified" version of <a href="http://upx.sf.net/">UPX</a> (new version released recently, btw). I wonder where the (GPL) source for it is?

Note: <a href="http://ryanvm.net/msfn/">RyanVM's alternate installer</a> also (apparently) fails, but silently.

<strong>Update!</strong>

RyanVM's alternate installer, while not working by itself, seems to be in a format that <a href="http://www.rarlabs.com/">WinRAR</a> can extract. Opening up the archive gives a resonably sane directory structure, from which you can just extract the "reader" folder, and everything seemingly works fine... not sure what all of those other files are for, as they're clearly not required.