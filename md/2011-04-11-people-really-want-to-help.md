title: Sometimes people really do just want to help...
slug: people-really-want-to-help
date: 2011-04-11 00:51:38+00:00

Late last year we were playing <a href="http://www.gravitysensation.com/trickytruck/">TrickyTrucks</a>.  

TrickyTrucks is okay fun single-player, but what really makes it fun is the competition.  For this, it has built in scoreboards, per track. Attempting to beat certain people's times on tracks <strong>is</strong> the fun.

What it lacks is a cross-track scoreboard, i.e. some kind of championship, and/or notifications of people beating your scores.  Even <a href="http://www.audio-surf.com/">Audiosurf</a>, one of the... most entertainingly engineered indie games recently, got this right.

I implemented one.

After some initial beta testing (and ensuring I was near the top of the championship), I messaged the TrickyTrucks author with <a href="//git.goeswhere.com/?p=tt.git;a=summary">the source of the scraper</a> and <a href="//git.goeswhere.com/?p=ttscores.git;a=summary">of the web interface</a>, asking for permission to link to <a href="//ttscores.goeswhere.com/">the website</a> on the official forum, so others could join us in competing for the championship title.

An aside, on licensing: Both of these components were released under the BSD.  That allows anyone, including the TrickyTrucks author, to use the code for any purpose, including incorporating it into his official website.  The component split was done such that there was a neat interface for him to implement on a non-scraper backend.  The best result for me would be for there to be an official API and an officially hosted version of the site, such that I never had to do anything ever again to continue appreciating it.

An aside, on development costs: Reverse engineering binary protocols is a nightmare.  Especially so with only access to a read client (with no source).  Especially so when there's no way to get the server to return things consistently or with user-specified plaintext.  Especially when the protocol has (what you believe to be) NIH compression.  Don't ever, ever try and pay someone to do this unless they really, really want to.

He replied that this would be fine, but only if I removed the link from the website to the source.  I, grudgingly (given it was already in the wild), did so and posted on the forum.

His response?  Delete the post, and change the server to have some additional, weak protection against 3rd-party clients.

<strong>What</strong>.  <strong>The</strong>.  <strong>Hell</strong>.


(Eventually he sent me details of an API to use, but I'd lost interest by then.)

<hr />

This post brought to you by <a href="http://developer.spotify.com/en/libspotify/overview/">libspotify</a> being <a href="http://getsatisfaction.com/spotify/topics/libspotify_crashes_on_loading_access_violation">incompatible</a> with most 3rd party DLLs, probably due to the copy protection on their DLL.  Copy protection.  On something that requires a paid account, verified against their server.  Please tell them what you think about this on <a href="http://getsatisfaction.com/spotify/topics/libspotify_crashes_on_loading_access_violation">my GetSatisfaction thread</a> (apparently this is what passes as a bug tracker these days).

This prompted me to waste ALL WEEKEND porting <a href="//git.goeswhere.com/?p=foo_input_spotify.git;a=summary">foo_input_spotify</a> to <a href="http://despotify.se/">libdespotify</a>.  foo_input_spotify will increase the value of their product.  Why are they making my life miserable?  Perhaps it's unintentional.  Time will tell.

