title: UWCS Progcomp Chain 6, Results
slug: uwcs-progcomp-chain-6-results
date: 2011-01-29 13:16:56+00:00

As a continuation of <a href="http://bucko909.livejournal.com/17203.html">bucko's progcomp chain</a>, I set <a href="http://faux.uwcs.co.uk/progcomp20110127/">Progcomp 6</a>.

The objective was to walk your way through a "maze" with huge constraints to make the problem simpler.

I believed the simplest solution to the problem was graph search with backtracking.  <a href="http://faux.uwcs.co.uk/progcomp20110127/winners/fauxnd.txt">My inefficient implementation</a> (<a href="http://faux.uwcs.co.uk/progcomp20110127/winners/faux.txt">with debugging</a>) of this is unbelievably fast; it can solve <a href="http://faux.uwcs.co.uk/progcomp20110127/lolmap.txt">a 300x5000 map</a> (>100 times the size of the original problem) in around 2 seconds.  The map generator ensures there are no problems set with trivial solutions (i.e. going in a straight line all the way down the map).  I thought that the effort of solving it by hand within the (6-second) time constraint would require far too much UI work, so keeping the problem size small enough to fit on the screen was fine.

I was wrong.  So wrong.

<a href="http://faux.uwcs.co.uk/progcomp20110127/winners/bucko.txt">bucko's Perl solution</a> was first, after 15 minutes, with a tree search implementation.  While easier to implement, this is much slower.

I'd carefully designed the page, submission process and timeout so that people who found curl / wget too much effort could submit the solution by copy-pasting; I could copy the result from the page (without the IE-only JS' assistance) into my solver, solve it, and copy the result back in ~5 seconds; hence the 6-second timeout.  bucko's solution sometimes doesn't finish in time, even on these tiny maps.  It'll never finish on the huge map.

fice was second, after 21 minutes.  Algorithm / code unknown, although I'm guessing there was auto-submission as no User-Agent was set.

<a href="http://queex.livejournal.com/">Queex</a> (outsider!) was third, after about 50 minutes, with <a href="http://faux.uwcs.co.uk/progcomp20110127/winners/Queex.java">his Java solution</a>.  He decided the problem wasn't complicated enough to write a "proper" solution for, and went for just trying to jiggle away from the edges.  Obviously it works fine, and I have no idea how to harden the map generator against it, except perhaps forcing you to go from the left edge to the right edge at least once.  It can only solve some of the maps, but this isn't important as it was a "solve once" problem.

Next up was <a href="http://faux.uwcs.co.uk/progcomp20110127/winners/Afal.js">Afal's js solution</a>.  He (correctly) guessed that the map generator only generates large walls every 10 spaces, worked out which side it was, and jiggled away from it a bit.  Apparently works most of the time.  Again he uses an in-browser implementation to avoid having to do any page parsing or post rubbish.

Afal then decided to submit 62,000 other solutions, which has made my log huge and writing this a pain.  Such a penis.  Such a penis.

<hr />

At this point an hour had passed and I turned the debugger on; when you die it tells you where and shows you what you submitted, etc.

james was next, with some more <a href="http://faux.uwcs.co.uk/progcomp20110127/winners/James.java">jiggling Java</a>, and a <a href="http://faux.uwcs.co.uk/progcomp20110127/winners/jamessh.txt">shell-script wrapper</a>.

<a href="http://mrwilson.uwcs.co.uk/">MrWilson</a> then submitted <a href="http://faux.uwcs.co.uk/progcomp20110127/winners/MrWilson.txt">a travesty</a>.  It generates random solutions and assumes loads of things about the map.  It works in nearly no cases.  I don't know how he can show his face in public after this.

<a href="http://faux.uwcs.co.uk/progcomp20110127/winners/Connorhd.txt">Connorhd</a> duplicated bucko's solution in php.

sadiq, tom, Softly, Trencha and Steve Brandwood also had a correct answer.

<hr />

Meta: I wrote my own <a href="http://faux.uwcs.co.uk/progcomp20110127/index.txt">solutions website</a> instead of using bucko's.  I got the logging all wrong.  I got the map size all wrong (not realising how <strong>lazy</strong> everyone is).

It took me about 90 minutes to do the map generator and my solution with debugger, and verifier.  Another 90 minutes was spent on the website.  That is, a ~3 hour time investment for causing hours of suffering and an entire night of entertainment.  Totally worth it.

Next up is <a href="http://bucko909.livejournal.com/17537.html">bucko's progcomp chain, link 7</a>, but tom still owes us a progcomp.