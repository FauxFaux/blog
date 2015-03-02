title: Java's ZipFile performance
slug: java-zipfile-performance
date: 2010-08-04 21:40:48+00:00

I have an application that scales well up to around five threads a core, due to the mix of IO and CPU that it does.

That is, you give it more threads, and the throughput increases; the overall time goes down.

The following graph shows, in blue, the Sun's java.util.zip.ZipFile time to complete a set of unzips on an increasing number of threads:

<img src="//b.goeswhere.com/zf-perf.png"/>

Wait, what the cocking shit.

<!--more-->
<hr />

The red line shows a pure Java implementation of ZipFile that scales expectedly well.  It's slower on one thread, unfortunately, but faster than the synchronised Sun ZipFile with two threads.

As expected, the performance of Sun's implementation massively increases (for large number of threads) if you manually synchronise on a global monitor around the ZipFile uses.  Red line unchanged:

<img src="//b.goeswhere.com/zf-sync-perf.png"/>

<hr />

Y-axis: Seconds.
X-axis: 2^(n-1) threads (i.e. levelling out at 3 due to it being tested on a quad-core machine and being entirely CPU bound).

Test: Opening rt.jar and summing all the bytes in files who's path contains an 'e'.
File entirely cached by the file-system.  JIT warmed.  Heap significantly larger than required.

Vista x64, Sun Java 1.6u20 x64 (i.e. server vm).

java -cp <a href="http://jazzlib.sf.net/">jazzlib-binary-0.07.zip</a>:. <a href="//b.goeswhere.com/ZipFileTester.java">ZipFileTester</a> somefile.zip