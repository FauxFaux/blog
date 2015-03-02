title: InstallShield unpacker
slug: installshield-unpacker
date: 2010-04-18 13:53:07+00:00

I couldn't find anything that would unpack the (<a href="http://handphone-solution.blogspot.com/2009/07/direct-download-for-ovi-maps-30-without.html">entirely unnecessary</a>) <a href="http://maps.nokia.com/ovi-services-and-apps/ovi-maps/downloads">Nokia map loader</a> set-up application, which is some InstallShield 7 nastiness.

<a href="//git.goeswhere.com/?p=deshield.git;a=blob;f=src/Deshield.java;h=8a74acececdb237829b9f2f694740bd47ec25ac5;hb=HEAD">deshield</a> can.  Given the number of magic numbers in it, I fully expect it not to work with other installers.

Why do they bother?  The data isn't even compressed; it's just bit-twiddled a little with the file-name, and this magic number: [ 0x13, 0x35, 0x86, 0x07 ].