title: The Date and Time control panel is a calendar
slug: the-date-and-time-control-panel-is-a-calendar
date: 2006-05-27 20:17:20+00:00

Following <a href="http://blog.prelode.com/?p=33">my fun with MacroMaker</a>, I decided to try something slightly more challenging, something that seems to irritate quite a few people running as LUA... the fact that you can't access the Date and Time control panel, even in read only mode.

The only (sensible) work-around is to <a href="http://support.microsoft.com/?id=300022">allow the user to change the date and time</a>, but this raises quite a few security concerns, as a few applications depend on the system's clock being close enough to correct.

Anyway, I wanted to run the Date and Time control panel applet as a limited user, just so I can use it as a calendar. Cracking tutorial follows, page down if you aren't interested.

The file we're hoping to attack is %windir%\system32\timedate.cpl, copy it somewhere sensible. As it happens .cpl files are just dlls, unfortunately <a href="http://www.ollydbg.de/">OllyDbg</a>'s LoadDLL wrapper does't seem to understand them. If you check the association, they're set to open with rundll32, ie.

<code>rundll32.exe shell32.dll,Control_RunDLL "c:\desktop\timedate.cpl"</code>

The DDE stuff doesn't seem to matter, luckily.

Fire up OllyDbg, the file we're trying to debug is rundll32.exe (make a copy of it if you want, but, as you're running as LUA you can't damage it anyway), with the argument string shown above.

Here is where my knowledge of OllyDbg sucks, I have no idea how to get it to pause on a specific module's loading (which isn't done in rundll32, so isn't breakpointable). Without being able to attach OllyDbg to the timedate.cpl before the code we're intersted in (whatever the security check might be), none of the breakpoints will be effective. Damaging the code (manual INT3s) won't help, either.

Having traced (miles) through the code to the point where the module is loaded, it's easier just to hit ctrl+f9 (execute 'till return) 30 times, and the module will have been loaded. Trust me on this. :)

Jump to it from the "Executable modules" window, right click -> search for -> all intermodular calls. The security functions we're looking for are the ones starting with "Zw", ie. ZwAdjustPrivilegesToken, ZwClose and ZwOpenProcessToken. I have no idea where the "Zw" comes from, but I'm guessing that they aren't the standard functions, they are, instead, the <a href="http://www.sysinternals.com/Information/NativeApi.html">"Nt" variants of the functions, as documented by Sysinternals</a>, although this is irrelevant... breakpoint them all, and hit run (F9).

At this point, OllyDbg stops at the LoadLibraryW call. How infuriating. Hit run (F9) again.

Next stop is at one of the ZwOpenProcessToken, aha. The code we're looking at:
<code>
58735FCF:
call DWORD PTR DS:[< &ntdll.NtOpenProcessToken>]
test eax,eax
jge short timedate.58735FE0
xor eax,eax
jmp timedate.58736066
</code>

Step over (F8) it, and you'll notice that it's returned 0 into EAX. The (standard version of) <a href="http://msdn.microsoft.com/library/en-us/secauthz/security/openprocesstoken.asp?frame=true">OpenProcessToken's documentation</a> suggests that it returns a boolean, so our zero would be 'false', as in, function failed.

Hit F8 again, and OllyDbg helpfully tells us that the jump is taken. This (obviously, if you test it by modifying the register) isn't what we want, so edit the code. The <code>'test'</code> and <code>'jge'</code> instructions aren't required, so replace them with <code>mov eax,1</code>. OllyDbg will fill in the NOPs for you.

Code fragment now looks something like:
<code>
58735FCF:
call DWORD PTR DS:[< &ntdll.NtOpenProcessToken>]
mov eax,1
nop
jmp timedate.58736066
</code>

Save the changes to the file, and restart the app. It works! The rest of the calls are either ignored, or have sensible error handling, great.

The applet still thinks it can change the time, but notices (and silently ignores) the case when it can't. Same with the timezone.

The next step would be to be able to make this change on the fly.. overwriting the existing control panel applet with the modified one is, even though it <em>shouldn't</em> make any difference, pushing it a bit. Plus, then it'd even work from the taskbar.

As far as I know, there are no security risks involved in what I just did.. note that everything (apart from reading the association for .cpl files (which I've duplicated above so you don't need to)) was done as a limited user.

If you're too lazy to make the changes yourself, I've got a binary here (for my personal use only, of course): <a href="http://faux.uwcs.co.uk/timedate_lua.cpl">timedate_lua.cpl</a> (<a href="http://faux.uwcs.co.uk/timedate_lua.cpl.asc">sig</a>).

<strong>Note:</strong> Don't try this one at home, either, kids.

Oh, and for anyone who didn't get the title, it's a response to <a href="http://blogs.msdn.com/oldnewthing/archive/2005/06/21/431054.aspx">The Old New Thing's 'The Date/Time control panel is not a calendar'</a>, which is clearly lies.