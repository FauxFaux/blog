title: Noelevate
slug: noelevate
date: 2008-12-22 00:17:37+00:00

In Windows Vista, Microsoft added manifests, a way for developers to <strong>require</strong> that their applications run as administrator, or not at all. This takes control away from the user, me, who I trust, and gives it to some developer (who I might not). While it's possible to edit the file to remove these manifests, this is hard to do safely and automatically.

I thought it'd be fun to directly fix the problem.

It seems that, like <a href="http://blog.prelode.com/?p=69"><em>some other things</em></a>, as far as I can see, there's no support for this.

Luckily, it's an even smaller patch than last time. I won't show it, it's simply erasure of a <code>jmp</code>. It's a terrible solution to the problem, and the binary only contains fixes for <code>kernel32.dll</code> as seen on x64 SP1 and x32 SP1 as of now, it could break at any point. I implore nobody to use this utility seriously.

<a href="//b.goeswhere.com/noelev.exe">noelev</a> (<a href="//b.goeswhere.com/noelev.exe.asc">asc</a>) (<a href="//b.goeswhere.com/noelev.cpp">cpp</a>) (<a href="//b.goeswhere.com/noelev.pdb.7z">pdb</a>) works much like the reverse of the unix "sudo" command, running a command via. it makes it run <strong>without</strong> elevation.

It's not infectious, so it won't work for all applications (like some setup applications that unpack other installers), and, of course, some applications actually don't work without elevation.

A lot of Windows components actually appear to cope relatively gracefully with the unexpected lack of permissions, unlike, say, the nVidia components. I was hoping to find an entertaining failure to screenshot, but they're all boring. :(