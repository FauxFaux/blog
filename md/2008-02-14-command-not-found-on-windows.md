title: Command-Not-Found on Windows
slug: command-not-found-on-windows
date: 2008-02-14 06:34:41+00:00

(Okay, not quite.)

After <a href="http://blogs.warwick.ac.uk/bweber/entry/untitled_entry_1/">some</a> <a href="http://www.fredemmott.co.uk/blog_133">posers</a> started duplicating the functionality of the <a href="http://packages.ubuntu.com/command-not-found">Ubuntu command-not-found package</a>, I thought I may as well have a go on a <em>sensible</em> OS.

Unfortunately for me, it turns out that Windows CMD doesn't offer, as such, a function that's run when a command isn't found, so I had to add my own (everyone loves screenshots of text, right?):

<a href="http://faux.uwcs.co.uk/cmd-not-found-patch.png"><img src="http://faux.uwcs.co.uk/cmd-not-found-patch.png" alt="My beautiful assembly defeating Ollydbg's highly competent analysis" /></a>

For those of you who can't read my beautiful hand-coded assembler, when a command isn't found, my patched cmd.exe will now attempt to load "<abbr title="command not found">cnf</abbr>.dll" from the system path, and pass the command-line to a function, imaginatively named cnf, in that dll.

Stage two, obviously, is to get some kind of useful reply...

<code>
// cl /Fecnf.dll /EHsc cnf.cpp /link /dll /dynamicbase /subsystem:console
#define UNICODE
#include &lt;iostream&gt;

extern "C" { __declspec(dllexport) void __stdcall cnf(const wchar_t*); }

using std::wcout; using std::endl;

void __stdcall cnf(const wchar_t* command)
{
	wcout &lt;&lt; L"I'm sorry, it looks like you tried to call ``" &lt;&lt; command &lt;&lt; "'', but the command doesn't exist!" &lt;&lt; endl &lt;&lt; endl;
	wcout &lt;&lt; L"Did you want to try /your mother/ instead?" &lt;&lt; endl;
}
</code>

I started writing a loader that'd apply the patch on-the-fly/to all existing instances of cmd, but I kind of ran out of care (it should be safe, it's about a sixty-byte patch). If anyone can think of any actual applications of this...