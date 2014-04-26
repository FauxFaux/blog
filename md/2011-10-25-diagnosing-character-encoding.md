title: Diagnosing character encoding issues
slug: diagnosing-character-encoding
date: 2011-10-25 15:35:55+00:00

Natural language is horrible.  Unicode is an attempt to make it fit inside computers.

I'm going to <a href="http://www.explosm.net/comics/1463/">make up some terms</a>:
<ul>
	<li><strong>Symbol</strong>: A group of related lines representing what English people would call a letter</li>
	<li><strong>Glyph</strong>: A group of related lines that might be stand-alone, or might be combined to make a <strong>symbol</strong></li>
</ul>

And use some existing, well defined terms.  If you use one of these wrongly, people <em>will</em> get hurt:
<ul>
	<li><strong>Code point</strong>: A number between 0 and ~1.1 million that uniquely identifies a <strong>glyph</strong>.  They have numbers, written like U+0000, and names,</li>
	<li><strong>Encoding</strong>: A way of converting information to and from a stream of <strong>bytes</strong>,</li>
	<li><strong>Byte</strong>: The basic unit of storage on basically every computer; an octet, 8 bits.  This has <em>nothing to do with</em> letters, or characters, or... etc.</li>
</ul>

Let's start at the top:
<ul>
	<li>Here's an grave lower case 'a': <strong>à</strong>.  This is a <strong>symbol</strong>. 
		<ul>
			<li>It could be represented by a single <strong>glyph</strong>, the code point numbered "U+00E0" and named "Latin Small Letter A With Grave", like above,</li>
<li>It could be represented by two <strong>glyphs</strong>.
				<ul>
					<li>This looks identical, but is actually two <strong>glyphs</strong>; an 'a' (U+0061: "Latin Small Letter A") followed by a U+0300: "Combining Grave Accent".  These two <strong>glyphs</strong> combine to make an identical <strong>symbol</strong>.</li>
					<li>This is, of course, pointless in this case, but there are many symbols that can only be made with combining characters.  <strong>Normalisation</strong> is the process of simplifying these cases.</li>
					<li>Don't believe me?  Good.  Not believing what you see is an important stage of debugging.  Open my <a href="https://b.goeswhere.com/aa.html">grave a accent test page</a>, and copy the text into Notepad (or use the provided example), or any other Unicode-safe editor, and press backspace.  It'll remove just the accent, and leave you with a plain 'a'.  Do this with the first <strong>à</strong> and it'll delete the entire thing, leaving nothing.  See?  Different.</li>
					<li>Side note: The test used to be embedded into this post, but the blog software I use is helpfully normalising the combining character version back to the non-combining-character version, so they actually <strong>were</strong> identical.  Thanks, <a href="https://tom-fitzhenry.me.uk/blog/">tom</a>!</li>
				</ul>
			</li>
		</ul>
	</li>
	<li>So, let's assume we're going with the complex representation of the <strong>symbol</strong>, the two code points: U+0061 followed by U+0300. We want to write them to any kind of storage, be it a file, or a network, or etc.  We need to convert them to bytes: Encoding time.
		<ul>
			<li>Encodings generate "some" <strong>bytes</strong> to represent a <strong>code point</strong>.  It can be anywhere between zero and infinity.  There's really no way to tell.  Common encodings, however, will generate between one and six bytes per code point.  Basically everyone uses one of the following three encodings:</li>
			<li><strong>UTF-8</strong>: generates between one and six bytes, depending on the number of the code point.  Low-numbered code-points use less bytes, and are common in English and European languages.  Other languages will generally get longer byte sequences.  Common around the Internet and on Linux-style systems.</li>
			<li><strong>UTF-16</strong>: generates either two or four bytes per code point.  The vast majority of all real languages available today fit in two bytes.  Common in Windows, Java and related heavy APIs.</li>
			<li><strong>I have no idea what I'm doing</strong>: Anyone using anything else is probably doing so by mistake.  The most common example of this is ISO-8859-*, which means you don't care about non-Western-European people, i.e. 80% of the people in the world.  These generate one byte for every code point, i.e. junk for everything except ~250 selected code points.</li>
		</ul>
	</li>
	<li>Let's look at <strong>UTF-8</strong>.
		<ul>
			<li>First code point: U+0061.  This happens to be below U+007F, so is encoded in a single byte in UTF-8.  This happens to align with low-ASCII, a really old encoding that's a subset of ISO-8859.  The single byte is 0x61, 0b0110001.  Note that the first bit is '0'.</li>
			<li>Second code point: U+0300.  This is not below U+007F, so goes through the normal UTF-8 encoding process.  In one sentence, UTF-8 puts the number of bytes needed in the first byte, and starts every other byte with the bits "10".  In this case, we need two bytes, which are 0xCC, 0x80; 0b11001100, 0b1000000.  Note how the first byte starts with "110", indicating that there are two bytes (two ones, followed by a zero), and the second byte starts with "10".</li>
			<li>Note: All valid UTF-8 data can easily be validated and detected; if a byte has it's left-most bit set to '1', it must be part of a sequence.  No exceptions.</li>
			<li>Consider
<pre>$ xxd -c1 -b some.txt | grep -1 ': 1'
0000046: 01100001  a
0000047: 11001100  .
0000048: 10000000  .
</pre>, which shows the byte patterns outlined: The 'a' with the leading 0, then the two bytes of the combining character.  xxd is the only tool you should trust when diagnosing character encoding issues.  Everything else will try and harm you, <em>especially</em> your text editor and terminal.</li>
		</ul>
	</li>
	<li><strong>UTF-16</strong> is much easier to recognise and much harder to confuse with other things as, for most Western text (including XML and..), it'll be over 40% nulls (0x00, 0b00000000).</li>
	<li>Now you've done your conversion, you can write the bytes, to your file or network, and ensure that whoever is on the other end has enough information to work out what format the bytes are in.  If you don't tell them, they'll have to guess, and will probably get it wrong.</li>
</ul>

In summary:
<ul>
<li>Have some data, in bytes?  Don't pretend it's text, even if it looks like it is; find out or work out what encoding it's in and convert it into something you can process first.  It's easy to detect if it's UTF-8, UTF-16 or if you have a serious problem.</li>
<li>Have some textual information from somewhere?  Find an appropriate encoding, preferably UTF-8 or UTF-16, to use before you send it anywhere.  Don't trust your platform or language, it'll probably do it wrong.</li>
<li>Can't work out what's in a file?  Run it through xxd and look for nulls and bytes starting with '1'.  This'll quickly tell you if it's UTF-16, UTF-8 or effectively corrupt.</li>
</ul>

Hopefully that's enough information for you to know what you don't know.

For more, try <a href="http://www.joelonsoftware.com/articles/Unicode.html">Joel on Software: The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets (No Excuses!)</a>.