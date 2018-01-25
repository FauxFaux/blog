title: C# + DWM -> pretty!
slug: c-dwm-pretty
date: 2007-04-13 22:37:21+00:00

I was reading <a href="http://blogs.msdn.com/iliast/default.aspx">a nice, if slightly dated, set of articles about the new features in Windows Vista</a>, including <a href="http://arstechnica.com/reviews/os/pretty-vista.ars/">ars technica</a>'s rundown. This article mentions that not much of the functionality avaliable in the Desktop Window Manager (Aero to everyone else) is going to be exposed to third parties, which I think it a great shame.

However, quick investigation reveals that, at least, the thumbnaling stuff has an <abbr title="Application Programming Interface">API</abbr>.

B#'s blog shows how to get at the <a href="http://community.bartdesmet.net/blogs/bart/archive/2006/10/05/4495.aspx">DWM previews in .NET</a>, and the MSDN magazine shows how to <a href="http://msdn.microsoft.com/msdnmag/issues/07/04/aero/default.aspx">create pure glass windows</a>.

A quick combination (and about an hour trying to work out a decent layout algorithm) gives:

<img src="/files/FDWMlist0.png"/>

I've actually put a <a href="http://faux.uwcs.co.uk/perm/FDWMlist0.exe">FDWMlist.net binary</a> (<a href="http://faux.uwcs.co.uk/perm/FDWMlist0.exe.asc">sig</a>) up, for once, even though it's generally worse than the code I normally hide. :)

Any key to refresh. Any use may invalidate your Reliability Index. You have been warned.
