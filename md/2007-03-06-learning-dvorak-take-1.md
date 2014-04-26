title: Learning Dvorak, take 1.
slug: learning-dvorak-take-1
date: 2007-03-06 02:58:20+00:00

Having decided to look at <a href="http://en.wikipedia.org/wiki/Dvorak_Simplified_Keyboard">Dvorak</a> again, and having completely failed to find any software that was even remotely interesting (I couldn't cajole Typing of the Dead into working with Dvorak) to teach typing, I reverted to the classic "look at a layout and try and type with it".

I got bored of looking for the keys.

After having played with <abbr title="Scalable Vector Graphics">SVG</abbr>/javascript as an alternative to Flash with <a href="http://faux.no-ip.biz/motes.php">'motes'</a> (temporary hosting, might not be up), I thought I'd have a go at adjusting it into a <a href="http://faux.uwcs.co.uk/typetut.php?Everyone%20loves,%20magical%20trevor!%20It's%20the%20tricks%20that%20he%20does,%20they're%20ever%20so%20clever!%20Look%20at%20him%20now..">mini typing tutor</a>.

Note that that's almost completely clientside, the php is used only to dump the default message in the text box, which could be done in JavaScript (probably easier, too, die, <a href="http://php.net/magic_quotes">magic quotes</a>, die).

It completely doesn't work in <abbr title="Internet Explorer">IE</abbr> (I haven't tested any SVG plugins), and has a weird JavaScript array bug in Opera (still works, just doesn't look perfect). So, much to my shame, I'd suggest trying it in Firefox.

And, on a related note, it strikes me as odd that <strong>Scalable</strong> Vector Graphics use absolute coordinates for everything internally.
