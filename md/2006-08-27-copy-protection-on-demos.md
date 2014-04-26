title: Copy Protection on Demos.
slug: copy-protection-on-demos
date: 2006-08-27 22:27:02+00:00

Why? Why is it necessary to bundle copy protection with demos? What is it actually protecting?

For a released game, you can quite fairly argue that any copy protection applied is useful (initially) to help deter piracy, but for a demo? The only thing I can think of here is the reliance on the copy protector's <a href="http://en.wikipedia.org/wiki/EXE_packer">packing</a> to prevent reverse engineering of the engine, an (eventually) futile task. The protection might hold for a month or so, but if you've actually released (or, at least, code-frozen) your product, what help is protecting your engine from the competition? They're apparently aiming for a later release date, and hence will be using a further developed engine regardless.

The alternative possibility being that the demo is limited in features up until the point where you supply an 'activation code' of some kind, an idea which has largely died out with this whole 'internet' thing (due to the ease of selling to customers and then distributing the release version of the game). See <a href="http://www.the-underdogs.info/game.php?id=1342">JetPack</a> and <a href="http://www.the-underdogs.info/game.php?gameid=2297">Zone66</a> for some games that had properly limited (with 'post off for the full version') demos, and some of the wonderful creations in the archives of <a href="http://rookscape.com/vbgaming/">Lucky's VB Gaming Forum</a> for some of the "greatest" home-grown copy protection schemes, ever.

Assuming, based on sheer size, that demos for modern games don't have all the game content bundled, and the developers aren't paranoid about people stealing their unpacked code, we're back to having no reason for copy protection on demos.

The only exception to this are demos (or non-sale releases) of games with network play, where you rely on the protection system to prevent the user damaging their client in some way, for instance <a href="http://www.trackmanianations.com/">Trackmania Nations</a>, in which you really shouldn't be relying on an external library to protect the play (it should, ideally, be impossible to cheat because the server checks everything it's sent).


Following that, back to the normal.. moaning about applications that don't work correctly as a limited user on Windows.

I recently downloaded the <a href="http://www.justcausegame.com/">Just Cause</a> <a href="http://www.justcausedemo.com/">demo</a>, and was (pleasantly) suprised to see that the installer is limited user aware, even offering to install into your Application Data directory, which would undoubtedly irritate some sys-admins (with roaming profiles turned on). That is, it works fine, right up until a few seconds before the end, where it dies with a error message quoting "Access Denied", with no other useful information. Woe. Looking at <a href="http://www.sysinternals.com/">Regmon / Filemon</a> logs doesn't give any further information, either.

That wasn't wholly unexpected, but having uninstalled it and re-run the set-up program as an administrator (which works fine), I try to run the demo (as either user), and get given:

<blockquote>
A required security module cannot be activated.
This program cannot be executed (5016).

Please have a look at <a href="http://www.securom.com/message.asp?m=module&c=5016">http://www.securom.com/message.asp?m=module&c=5016</a> for further, more detailed information.</blockquote>

(That link was dead at the time of writing, too.)

Lovely. Well, I certainly won't be buying the game, then. Good work, demo.