title: Eclipse and database deadlocks
slug: eclipse-and-database-deadlocks
date: 2008-10-28 22:30:46+00:00

I encountered an interesting issue today.

I work with some code that relies heavily on the database it backs on to. Today, it was backed onto Microsoft SQL Server. Right after starting, it would deadlock.

Looking at the stack of randomly picked threads I found that one was waiting indefinitly for the server to return.

A quick glance at the SQL Server's Activity Monitor revealed that "process id" 3, was waiting for "process id" 1. "Process id" 1 was sleeping, but in a transaction.

That's helpful, I thought, I now know the problem, "process id" 1. So, where's it happening in code? Uh oh.

I poked around, and noticed that <code>com.microsoft.sqlserver.jdbc.SQLServerConnection</code> (no, not <code>com.microsoft.<strong>jdbc.sqlserver</strong>.SQLServerConnection</code>) has a piece of private implementation called <code>transactionDescriptor</code>, an 8-<code>byte</code> array including the process id on the SQL Server. I set a <a href="http://help.eclipse.org/ganymede/topic/org.eclipse.jdt.doc.user/reference/preferences/java/debug/ref-detail_formatters.htm">detail formatter</a> to show just this value.

Following this, Eclipse's find <a href="http://help.eclipse.org/ganymede/topic/org.eclipse.jdt.doc.user/reference/views/shared/ref-allinstances.htm">all instances</a> command comes into play, allowing you to search for all instances of <code>SQLServerConnection</code>,  then <a href="http://help.eclipse.org/ganymede/topic/org.eclipse.jdt.doc.user/reference/views/shared/ref-allinstances.htm">all references</a> to the specified connection. Both of these are only available in Java 6 and above, otherwise the command will be greyed out.

From here, you can (manually, as far as I know) search through the stack trace and hopefully find that one of your threads has the above class (or a class that refers to the class, or a class that refers to a class that...) in it's trace; the culprit.

A mere hour of my day, gone. :|