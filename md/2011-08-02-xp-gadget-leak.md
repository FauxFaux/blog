title: Windows XP End of Support Countdown Gadget
slug: xp-gadget-leak
date: 2011-08-02 18:31:39+00:00

<img src="/files/gadget-xpsupport.png" alt="Windows XP End of Support Countdown Gadget" style="float: left; padding: 1em"/>  The <a href="http://www.microsoft.com/download/en/details.aspx?id=11662">Windows XP End of Support Countdown Gadget</a> gives you a nice countdown until Windows XP, and, more importantly, IE6 will actually finally be unsupported.

It, however, leaks memory.  A lot of memory; about 1kb/second.  Noting that it's running all the time, and not important, this is rather inconvenient.

<a href="/files/0001-Leak-slower.patch">FTFY</a>.  Can't redistribute a patched "binary" as the original is not redistributable.
