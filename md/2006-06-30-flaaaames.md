title: Flaaaames!
slug: flaaaames
date: 2006-06-30 19:06:20+00:00

All reason has failed, it's time for some transparent flaming of <a href="http://blog.entek.org.uk/?p=34">Laurence's response</a> to <a href="http://blog.prelode.com/?p=39">my previous post</a>.

<blockquote>I do not have the time or inclination to install each one to find out if it is in the default package selection, ...</blockquote>

Don't worry, I'm more than happy to do it for you. It appears that (k)<a href="irc://irc.eu.freenode.net/#ubuntu">Ubuntu</a>, <a href="http://www.linuxforums.org/forum/mandriva-linux-help/8819-re-installing-repairing-gcc-other-packages-text-mode.html">Mandriva</a>, <a href="http://www.fedoraforum.org/forum/showthread.php?t=111732&highlight=gcc">Fedora</a> and <a href="http://www.last.fm/forum/4/_/87209">SUSE</a> don't ship with the packages in their default install.

<blockquote>..and even if not it’s still a single tick-box away and can be installed from the installation media rather than a large download away.</blockquote>

Where did you get this installation media from, just out of interest? Did you download them, say, a DVD iso? Sounds rather large, if you aren't going to be installing most of the packages by default. Maybe you didn't download them and paid someone like <a href="http://www.thelinuxshop.co.uk/catalog/">The Linux Shop</a> to ship them to you? You may not be aware that <a href="http://www.microsoft.com/">Microsoft</a> offer a similar service, for instance, they allow you to <a href="http://www.qmedia.ca/launch/psdk.htm">order the platform sdk on a low-cost cd</a>.


<blockquote>..it took 3 searches and 20 minutes following various links to find a download page for Visual Studio Express Edition.</blockquote>

I think we might need pictures here.

<ol>	<li>First of all we're going to visit the website of a popular search engine, known as <a href="http://www.google.co.uk/">Google</a>. You may have heard of it. We're looking for "Visual Studio Express Edition", so go ahead and enter it into the box, noquotes.
<img src="http://faux.uwcs.co.uk/perm/search1.png" alt="Google's home page with the I'm Feeling Lucky button highlighted" />
Click "I'm feeling lucky", as indicated in the above image.</li>
	<li>This'll get you to the <a href="http://msdn.microsoft.com/vstudio/express/">Visual Studio Express Edition home page</a>. From here, we have to decide which version of <abbr title="Visual Studio Express Edition">VSEE</abbr> we're after <em>For Windows Development</em>. At random, I've picked the C++ edition, so click <a href="http://msdn.microsoft.com/vstudio/express/visualc/">Visual C++ 2005 Express Edition</a>. Another screen capture is provided if you are having problems locating the link:
<img src="http://faux.uwcs.co.uk/perm/search2.png" alt="Visual Studio 2005 editions" /></li>
	<li>We're aiming to download it, so, here, click on the large <a href="http://msdn.microsoft.com/vstudio/express/visualc/download/">DOWNLOAD NOW</a> link. <img src="http://faux.uwcs.co.uk/perm/search3.png" alt="Large Download Now image." /> No arrows required here, I hope.</li>

	<li>Again, click "<a href="http://go.microsoft.com/fwlink/?LinkId=51410&clcid=0x409">Download</a>": <img src="http://faux.uwcs.co.uk/perm/search4.png" alt="Download link with subtle indication arrows." /></li>
	<li>That's all. If, however, you'd prefer to manually download the file as apposed to use Microsoft's download manager, you may want to select <a href="http://msdn.microsoft.com/vstudio/express/support/install/">manual installation instructions</a> here.</li>
</ol>

By my count, that's four mouse clicks from the google home-page. The Direct-X SDK is three.

<blockquote>Additionally, once downloaded and installed I still have to add the library paths for DirectX’s libraries to the search paths for any project requiring them.</blockquote>

Visual Studio has a global library path, very useful for these library things. It even has a nice GUI to configure it! To access it, under Visual Studio 2005, follow: Tools -> Options -> Projects and Solutions -> VC++ Directories -> Show directories for: Library files.

Any path added to there will be searched by your project.


<blockquote>...As far as I can tell (I may be wrong) this ’standard’ is a defacto standard and applications do not have to comply if they do not want to....</blockquote>

I wasn't refering to the labeling of the menus, I was refering to the fact that they will be accessible via. alt keys (if they exist at all), and that windows will attempt to fill in any access keys that the application has failed to specify, meaning that you'll always have a consistent interface.


Hope that helps :)