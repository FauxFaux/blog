title: History cleanliness in git
slug: history-cleanliness-in-git
date: 2011-04-07 23:36:16+00:00

This post is for documentation only.  It was going to be a rebuttal to <a href="http://jhw.dreamwidth.org/1868.html">jwh's Mercurial fanboyism</a> but I realised while writing it and re-reading his post that I have absolutely no idea what he's talking about, nor can I work out how to get <code>hg</code> to tell me.

Given a repo of:

<img src="/files/gitpics/naturist-full.png"/>

My proposals for alternatives to this simple workflow are as follows.  These all result in the same order of code going into the master branch, but have different histories.  (Actually, I think there's still mistakes in there but I'm tired of staring at the <a href="//git.goeswhere.com/?p=githistories.git;a=summary">horrible procedural script that generates it</a>, so it'll do).

<strong>1. </strong> A <strong>flat history</strong>, made by rebasing everything on top of master instead of merging:

<img src="/files/gitpics/flat-full.png"/>

<strong>2.</strong> <strong>Only merges on master</strong>, giving you the illusion of a neat history...

<img src="/files/gitpics/onlymerges-flat.png"/>

...but, underneath, loads of ugly information available:

<img src="/files/gitpics/onlymerges-full.png"/>

<strong>3.</strong> A hybrid, <strong>supercommits</strong>, whereby you keep a flat history but you maintain where branches were: 

<img src="/files/gitpics/supercommits-flat.png"/>

...or, with the history information visible:

<img src="/files/gitpics/supercommits-full.png"/>

<hr />

<strong>Thoughts:</strong>

Serious concurrent projects like git itself use the 'only merges on master' approach.  I strongly agree that they shouldn't be flattening the history; it's nice to be able to see groups of patches as they go into master, and to navigate the history of "feature commits", instead of the history of "developer changes".

The flat model seems to work much more like how I think about software development:
<ul>
	<li>You start working on something.</li>
	<li>You do your normal develop, commit, developer-test, commit cycle.</li>
	<li>Master moves on a bit while you're messing around.  The fact that you happened to start developing before a specific commit on master, instead of just after it (so it would be the root of your branch) is reasonably irrelevant; you may as well move the branch-root (or branch point) up to the top of master.</li>
	<li>Additionally, if you do a real merge, you need to test your changes.  This leads to more developer testing, and possibly more commits.</li>
	<li>What do you do with these commits?  Assuming your merge with master is still local you can fix it (this is git, you can fix anything), but it's inconvenient.</li>
	<li>When you've rebased, you can continue committing on your rebased branch like normal, with confidence that when you merge it'll all be fine (as it'll be a fast-forward merge).</li>
</ul>

'Supercommits' is a hybrid of these two; you can use the rebase-onto-master workflow from 'flat', but you can logically group your set of commits into a... family?  I like this idea, but haven't really implemented it in practice so can't really comment.

(Apologies for screenshots of text; I'm lazy, ansifilter was NOT WORKING and it's prettier than gitk.)
