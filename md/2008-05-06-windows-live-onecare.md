title: Windows Live OneCare
slug: windows-live-onecare
date: 2008-05-06 23:54:24+00:00

As I had no particular use of my CPU time over the weekend (I was busy force-feeding dogs ice-cream), I installed <a href="http://onecare.live.com/">Windows Live OneCare</a> (which has recently gained support for x64 flavours of Vista), following a promise to myself that I would install a virus scanner of some kind.

It happily scanned away, deleting three copies of the <a href="http://en.wikipedia.org/wiki/EICAR_test_file">deadly EICAR virus</a> (phew), this was (mostly) fine.

Following this, and OneCare assuring me that my system was free of viruses, spyware and other malware, awarded me the security status Fair:
<img src='http://faux.uwcs.co.uk/onecarefair.png' alt='OneCare - Fair, Fix, Backup' class='alignnone' />

The "problem" found was, apparently, that I have chosen to disable elevation upon "setup detection", a feature built into Vista (disableable via. Local Security Policy -> UAC: Detect Application Installs..) by Microsoft in a cunning plan to ensure that lazy software developers didn't need to bother learning how manifests work, and instead could just rename their application to "setup.exe" and pray. There is no way to ignore this "problem".

The second "problem" was that I do not use OneCare (nor optical media, as it happens) for my backups. This renders the overall "security" status useless.

Next irritation comes from the attempt to use the internet. OneCare blocks outgoing connections from unisnged (it costs £40 and an e-mail address to get a code-signing certificate via. <a href="https://author.tucows.com/">Tucows</a>, making this a terribly poor way to decide what to trust) apps by default (well, I hope, I couldn't work out how to turn it off), and shows the following dialog:

<img src='http://faux.uwcs.co.uk/onecarefirewall1.png' alt='Opera and Putty OneCare firewall elevation dialogs' class='alignnone' />

That's conforting, a shielded <a href="http://msdn.microsoft.com/en-us/library/bb760441.aspx">task dialog</a>. I'll click Allow on Opera's prompt and... wait, what's this?!

<img src='http://faux.uwcs.co.uk/onecarefirewall2.png' alt='Opera and Putty OneCare firewall dialogs, elevated' class='alignnone' />

I'm confused. Didn't I just say Opera was allowed through?

Also, a warning: Don't try the bottom button. It blocks the application for an indeterminate, unresettable period. Really inconvenient when you're attempting to use said application to write a blog report.

If you hadn't guessed by now, I don't like OneCare's UI. To sum it up:

<img src='http://faux.uwcs.co.uk/onecareloading.png' alt='OneCare\&#039;s loading dialog' class='alignnone' />

This is the dialog that you see when you <em>restore</em> OneCare from the system tray. No, not load from scratch. Restore. And, just in case you were worried, that's not a progress bar, it's just an "I'm doing stuff, honest!" bar.

Ignoring all those (and a few <a href="http://faux.uwcs.co.uk/onecaretrayicon.png">other bugs</a>), it seems to be a very capable bit of software. Maybe you're less irritable than me, go try the 90 day free trial! :)