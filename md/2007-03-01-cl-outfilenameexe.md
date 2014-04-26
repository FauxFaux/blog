title: cl /out:filename.exe
slug: cl-outfilenameexe
date: 2007-03-01 21:00:23+00:00

I was minorly confused today as to why all of my lovely compiled programs were disappearing and, instead, I was left with some empty files called <strong>ut</strong>.

For example, a test C++ file:
<code>echo int main(){} > empty.cpp</code>

Compile it:
<code>&gt;cl empty.cpp
Microsoft (R) 32-bit C/C++ Optimizing Compiler Version 14.00.50727.762 for 80x86

Copyright (C) Microsoft Corporation.  All rights reserved.

empty.cpp
Microsoft (R) Incremental Linker Version 8.00.50727.762
Copyright (C) Microsoft Corporation.  All rights reserved.

/out:empty.exe
empty.obj
</code>

As it clearly says, this /out:puts to "empty.exe". Okay, I don't want it to output to "empty.exe", I want it to be called "full.exe". So, I add <strong>/out:full.exe</strong> to my build script (along with all the normal junk like /MD and /nologo), and the output is now:

<code>C:\Desktop>cl /nologo empty.cpp /out:full.exe
cl : Command line warning D9035 : option 'o' has been deprecated and will be removed in a future release
empty.cpp</code>

Curious, but only a warning, let's ignore it.

..and <strong>full.exe</strong> doesn't exist. Neither does <strong>empty.exe</strong>. There's just this empty, zero-byte (according to Explorer) file called "ut".

What's happening, and what's not immediately obvious if you don't read boring warnings, is that the compiler it outputting (<strong>/ofilename</strong> to write the output to filename) to "ut:wrong.exe", which is the <a href="http://support.microsoft.com/kb/105763">NTFS alternate data stream</a> called "wrong.exe". Woops.

For reference, the message comes from the linker, not the compiler, which does use <strong>/out:filename</strong>, and the non-deprecated version of <strong>/o</strong> for the compiler is <strong>/Fefilename</strong>. Much clearer and easier to remember. Not.
