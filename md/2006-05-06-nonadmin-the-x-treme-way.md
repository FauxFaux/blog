title: nonadmin the 'x-treme' way
slug: nonadmin-the-x-treme-way
date: 2006-05-06 13:57:08+00:00

I was reading the <a href="http://nonadmin.editme.com/HowTo">nonadmin wiki</a> and found a link to <a href="http://www.leeholmes.com/blog/CrackingSoftwareToRunAsNonAdmin.aspx">Lee Holmes' Blog about cracking software to the extent that it will run without administrator access</a>.

I like this idea... the ability to fix 'broken' (NB: <a href="http://members.ij.net/anthonymathews/MacroMaker.htm">Macro Maker</a> was a terrible choice on Lee's part, due to the fact that the 'brokeness' is caused by the copy protection, meaning that any patches for it can't be redistributed) software via. binary patching is a great concept.

I tried running through Lee's (probably illegal) tutorial, it seems not to work. It may work if you've run the app as administrator in the past, or if you've opened up anything inside HKLM, but I'm yet to do either of these for any app I've needed to run.

I've used <a href="http://www.ollydbg.de/">OllyDbg</a> before, so I fired it up. First thing I tried was Search for -> All intermodular calls, which finds an awful lot of references to registry functions (mostly Reg*, but some SHSet/GetValues too).

I couldn't be bothered to fix all those, so I tried searching for the constant, HKEY_LOCAL_MACHINE (`<a href="http://gnuwin32.sourceforge.net/">fgrep</a> HKEY_LOCAL_MACHINE <a href="http://www.microsoft.com/downloads/details.aspx?FamilyId=484269E2-3B89-47E3-8EB7-1F2BE6D7123A">platform_sdk</a>\Include\*` gives you a value of 80000002). This gets a load of hits, too.

Surprisingly enough, I couldn't be bothered to fix all those, either. Essentially, what we're trying to do is fix everywhere that HKEY_LOCAL_MACHINE (80000002) (Windows <a href="http://en.wikipedia.org/wiki/Least_User_Access">LUA</a> accounts are much happier writing to HKEY_CURRENT_USER (80000001)) has been used as an argument to a function call.

Following my success with sed on various Linux machines (you don't want to know), I decided to try it the.. er.. 'x-treme' way (under the assumption that it'd break everything horribly). 

In most cases the value will have been PUSHed, ie.

<pre>PUSH 80000002</pre>

This assembles to:

<pre>68  02 00 00 80</pre>

Fire up <a href="http://www.chmaas.handshake.de/delphi/freeware/xvi32/xvi32.htm">XVI32</a>, open up the exe in question...

'Replace All' instances of our offending code <tt>68 02 00 00 80</tt> with the more LUA friendly <tt>68 01 00 00 80</tt>.

Save, exit, and try running the executable. It's not invalid (which is impressive) and it seems to actually work fine, but it still brings up one of those nasty error messages. Click OK and.. it works, fine. Next time I run it the error doesn't appear at all.

Quick check suggests that the whole app is working fine. Strange.

That really shouldn't work, should it?

<strong>Note:</strong> Don't try this at home, kids.