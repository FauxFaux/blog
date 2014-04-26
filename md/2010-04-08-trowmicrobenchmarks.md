title: Tro^WMicrobenchmarks!
slug: trowmicrobenchmarks
date: 2010-04-08 18:51:41+00:00

This blog is far too low in trolling.  As a start, everyone knows that git is fast and svn is slow, but I wasn't aware quite how shocking the difference was.

The test: committing a file that slowly increases in size, and a new file, 200 times.

<strong>git</strong>: 2 seconds.
<strong>darcs</strong>: 10 seconds.
<strong>bzr</strong>: 70 seconds.
<strong>svn</strong>: 200 seconds.

No comment.

Reproduction steps follow.
<!--more-->

bzr 2.0.3 and git 1.5.6.5:
<code>time ($CMD init &amp;&amp; for i in $(seq 200); do echo $i &gt;&gt; foo && touch bar$i &amp;&amp; $CMD add * &&gt;/dev/null &amp;&amp; $CMD commit -m "Whoosh"; done)</code>

darcs (which, admittedly, took about 200 seconds to work out how to commit to) 2.0.2:
<code>time ($CMD init &amp;&amp; for i in $(seq 200); do echo $i &gt;&gt; foo &amp;&amp; touch bar$i &amp;&amp; $CMD add * &amp;&gt;/dev/null &amp;&amp; $CMD record -a -Aa -m "Whoosh"; done)</code>

svn 1.5.1:
<code>rm -rf ../repo; svnadmin create ../repo && svn co file:///var/tmp/repo . && time (for i in $(seq 200); do echo $i &gt;&gt; foo && touch bar$i && $CMD add * &amp;&amp; $CMD commit -m "Whoosh"; done)</code>