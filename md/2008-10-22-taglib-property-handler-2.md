title: Taglib Property Handler
slug: taglib-property-handler-2
date: 2008-10-22 21:04:51+00:00

Tonight marks the first public release of <a href="http://taglibhandler.sourceforge.net/">Taglib Property Handler</a>, an Explorer extension for Vista that allows it to read metadata from many audio file types:

<img src="http://b.goeswhere.com/tlph-casc640.png" alt="Explorer advanced search results for Cascada with TLPH installed" />

Currently, it's fully read-only, so there's minimal risk to your data, and the default install doesn't cause you to lose any existing functionality.

The <a href="http://taglibhandler.sourceforge.net/#atbl">list of supported properties</a> shows what the default handler supports for MP3 and WMA, and what TLPH supports so far.

This release comes after four months of swearing at Microsoft for the entire <a href="http://msdn.microsoft.com/en-us/library/bb266532.aspx">property handler</a> system being impossible to debug. Four months ago I had the handler working in Windows Explorer, but Windows Search would refuse to show any properties it provided. There're plenty of articles on <a href="http://blogs.msdn.com/benkaras/archive/2007/07/24/troubleshooting-why-isn-t-my-property-handler-getting-indexed.aspx">debugging this situation</a>, which I ran through hundreds of times, in the end this turned out to be caused by:
<ol>
	<li>Explorer accepting VT_BSTR and Windows Search not; solved by switching to <a href="http://msdn.microsoft.com/en-us/library/bb762305.aspx">InitPropVariantFromString</a>.</li>
	<li>Stupid mistakes with pointers. Oh, how I hate you.</li>
</ol>
