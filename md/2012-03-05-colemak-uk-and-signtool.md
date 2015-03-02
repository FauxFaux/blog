title: Colemak UK and signtool
slug: colemak-uk-and-signtool
date: 2012-03-05 21:21:20+00:00

I've just uploaded a signed version of my "Colemak UK" (colemauk) keyboard layout: <a href="https://ssl.goeswhere.com/download/colemauk/colemauk.exe">colemauk installer</a> (<a href="https://ssl.goeswhere.com/download/colemauk/colemauk.exe.asc">asc</a>).

I remembered it wasn't signed when the Windows 8 beta started nagging me about it.  I allocated a 5-minute task on my "to-do" list to fix it.

However, taking the generated binaries from before (and verifying them with GPG), signtool is perfectly happy to sign the <code>MSI</code>s and the <code>DLL</code>s, but the <code>setup.exe</code>, the actual launcher that asks for elevation in the first place gives:

<pre>$ signtool sign /a setup.exe
Done Adding Additional Store
SignTool Error: SignedCode::Sign returned error: 0x80070057
        The parameter is incorrect.
SignTool Error: An error occurred while attempting to sign: setup.exe

Number of errors: 1
</pre>

Oh.

(Extensive) investigation with <a href="http://www.cgsoftlabs.ro/studpe.html">STUD_PE</a> reveals that the certificate table, the location where signtool is expecting to find current certificates and write new ones, is full of junk; an address and a block that reads past the end of the file.  While STUD_PE allows you to fix this, I elected to write a tool to automatically strip evidence of signatures from files: <a href="http://git.goeswhere.com/tinies.git/blob/HEAD:/unsigntool.cpp">unsigntool</a> (<a href="https://github.com/FauxFaux/tinies/blob/master/unsigntool.cpp">github</a>), the opposite of signtool.