title: Xming + Xlaunch
slug: xming-xlaunch
date: 2006-02-16 21:08:24+00:00

<a href="http://freedesktop.org/wiki/Xming">Xming</a> is a tiny (&lt;13MB with all the optional components), free implementation of an X server for Windows, many times smaller than an alternative, <a href="http://www.cygwin.com/">Cygwin</a>, my install of which is currently 344MB.

Until recently, Xming has been hard to use.. prompting someone to write Xlaunch; a wizard-like tool to make Xming work. Previous builds of it have had really stupid bugs (like, for instance, limiting the length of the machine name you were connecting to to 8 characters), but the latest version is better.

It's bundled with Xming, so all you have to do is <a href="http://sourceforge.net/project/showfiles.php?group_id=156984">download and install Xming</a>, and run Xlaunch.. irritatingly, the 20060209 release didn't create a shortcut to Xlaunch, only Xming, you have to find and run it manually. It'll probably be at <a href="file://c:/progra~1/xming/xlaunch.exe">c:\Program Files\xming\Xlaunch.exe</a>.

Simplest way to get it working: Multiple Windows, next. Start a program, next. Start program: xterm, Using putty. Here you need to fill in the machine you want to connect to, your username and password (unless you have ssh keys setup). Ignore the next screen, just hit next.

The next screen prompts you to 'Save configuration' which sensibly (yet irritatingly) doesn't save the password. This is ideal if you have ssh keys setup properly, but less so if you don't. It'd be fine if Xlaunch would prompt you for the password when running .xlaunch files, but it doesn't. So, if you don't have sshkeys, just click finish. 

In theory, you'll get an xterm, running from the remote machine. If somehting goes wrong, you'll get nothing (no error, no warning, etc.), and you have to guess what went wrong, good luck.

If it does work, it's far faster and much more secure than vnc, and it doesn't kill the remote machine anywhere near as much, and the "multiple windows" feature makes it far more useful.