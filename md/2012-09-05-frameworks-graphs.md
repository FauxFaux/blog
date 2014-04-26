title: Frameworks, libraries and graphs
slug: frameworks-graphs
date: 2012-09-05 21:37:40+00:00

<img src="https://b.goeswhere.com/framework-graph.png" style="float: left; padding: 2em" alt="The Framework Graph"/>

In&nbsp;his&nbsp;<a href="https://www.youtube.com/watch?v=i6Fr65PFqfk#t=17m17s">Serious&nbsp;Beard&nbsp;Talk</a>, delivered at DjangoCon 2008, Cal Henderson explains how he thinks frameworks affect productivity.  I would like to bring it up again, because it's still as relevant as ever, and it's hard to link busy software engineers to YouTube videos (of things that aren't cats).

A framework (or library?) exists to save you from doing common, repetitive tasks (he's thinking of things like mapping URIs to places, and reading and writing entities to the database) by providing a bunch of pre-existing code that'll do all this stuff for you:
<ul>
<li>If you decide to write all this stuff from scratch, you're going to be spending a lot of time developing boring, repetitive code (but maybe you're still doing it better than other people?), and you're not going to be delivering anything fancy.  Eventually, though, you'll get up to speed, and your well-understood, targeted framework/library will assist you in every way.</li>

<li>If you pick the framework route, it takes you a short amount of time to get one of the damn demos to start, then you get a whole load of stuff for free, but, eventually, you run into things the framework can't or won't do for you, and you have to work out how to ram your workflow down it's stupid throat aargh.  Your delivery speed plummets, but eventually you'll get it working, and you'll have some free good design and code reuse in there.  Now, with a decent grounding in how the framework works, and your extra flexibility layer, you can get back to the good stuff.</li>
</ul>

This results in roughly The Framework Graph, shown here, reproduced (in Paint) without permission.

I believe an unawareness of this Graph comes up frequently, even when not discussing frameworks directly:
<ul>
<li>I don't want to use a big complex library, it'll be simpler to do it myself.</li>
<li>I can't get it to do quite what I want, I'll start again from scratch.</li>
<li>I don't really understand why it makes this operation so hard, the tool must be broken.  (Hibernate, anyone?)</li>
<li>Why does it want all those parameters/config/values?  I just want it to work.</li>
</ul>

<hr style="margin: 2em"/>

I can pick many examples from my non-professional experience has come up, my favourite is (coincidentally!) That Graph Drawing Code:
<ul>
<li>I have two <a href="http://programmer.97things.oreilly.com/wiki/index.php/Reuse_Implies_Coupling">forks</a> of some disasterously [old and] terrible plotting code for <a href="https://git.goeswhere.com/dkarma.git/blob/06642815e24fb8f899549bf53fc67bf570e34b60:/dkarma.php#l410">generic popularity data visualisation</a> and <a href="https://git.goeswhere.com/polcom.git/blob/e533bbb43b43c83de44cf55013bbfe46fe14a35b:/index.php#l162">political compass aggregation</a>, and I have recommended (and/or forced) other people to use the same technique in their projects, mainly to avoid the tyrany of <code>gnuplot</code>.</li>

<li>For a more recent project <a href="http://faux.uwcs.co.uk/hdds.php">plotting hard drive prices</a>, I chose to finally give in and learn <code>gnuplot</code>.  It was a pain, but <a href="https://git.goeswhere.com/hdds.git/blob/HEAD:/grab/history.gnuplot">the resulting <code>gnuplot</code> code</a> is much neater than any of that PHP, and then I've got things like suprise svg support for free.  Plus, it means that I can quickly bang out other things, like my <a href="https://b.goeswhere.com/browserstats-2012-02.png">statcounter browser versions reinterpretation</a>.</li>
</ul>
This may not sound like a framework choice on the scale that he's talking about, but I urge you to consider the sheer horror of that PHP code.

In summary: The big horrible library/framework/tool/etc. will almost certainly provide you with more total productivity in the short (when most projects fail, at about the vertical line on the Graph), medium and long term, regardless of any pain it gives you.