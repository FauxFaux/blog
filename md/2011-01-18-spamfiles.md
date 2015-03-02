title: SpamFiles
slug: spamfiles
date: 2011-01-18 00:37:14+00:00

I've been whining for a while about <a href="//git.goeswhere.com/?p=scratch.git;a=blob;f=src/SpamFiles.java">SpamFiles</a>' speed on Windows.  It creates and writes small amounts of data to hundreds of files, then deletes them all.  It's orders of magnitude slower on Windows (all the way to Seven) than on Linux, due to NTFS.

It's just a synthetic benchmark though, right?  That is, it's reasonably irrelevant.  Or so I thought.

In a recent private project I was using Spring's JDBCTemplate with SQLite to write out a couple of hundred rows to an empty table.  JDBCTemplate defaults to autocommit and it's non-trivial to convince it not to do so.

The <a href="//git.goeswhere.com/?p=sqlitelulz.git;a=summary">relevant code</a> and <a href="http://faux.uwcs.co.uk/sqlitelulz-v01.jar">sqlitelulz.jar</a> shows why this is a problem:

<pre>
>java -jar sqlitelulz.jar 1000
Autocommit: 70.867652636 seconds
Manual commit: 0.107324493 seconds

$ java -jar sqlitelulz.jar 1000
Autocommit: 1.814235004 seconds
Manual commit: 0.075502495 seconds
</pre>

Yes, that's 660 times slower on Windows (and only 25 times slower on non-ntfs).  This time is entirely sqlite creating and deleting it's journal file.

Sadness.
