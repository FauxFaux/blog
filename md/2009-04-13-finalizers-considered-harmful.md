title: Finalizers considered harmful
slug: finalizers-considered-harmful
date: 2009-04-13 14:24:23+00:00

I diagnosed an interesting problem at work recently; our application, when running on some enterprise platforms was eventually (over a number of days) running out of memory, grinding to a halt then fatally OutOfMemoryErroring, regardless of how much heap it was given.

<a href="http://www.eclipse.org/mat/">Eclipse Memory Analysis Tool</a> (via. <a href="http://www.ibm.com/developerworks/java/jdk/tools/mat.html">DTFJ</a> for the IBM heapdumps) is rather resource hungry, needing massively increased the heap (~7gb, i.e. can't be run on an 32-bit machine) and stack size (~8mb).  However, once the heap dump had been loaded (1h+), it was reasonably obvious (after <a href="https://bugs.eclipse.org/bugs/show_bug.cgi?id=266231" title="Eclipse bug #266231 (resolved: fixed)">#266231</a>) what was happening:

The finalizers wern't being processed fast enough.

The finalization thread is run at a lower priority, and, seemingly, on the configurations on these machines/OS/JVM combinations, it was getting no time at all.

For historical reasons, quite a few large classes in our codebase have:

<code>void finalize() {}</code>

..in, that is, finalizers that do nothing at all.  These empty finalizers still have to be run before the object can be collected, however, so they simply wern't, quickly leaking memory. The more that was leaked, the slower the JVM was running, so the less time the finalization thread had, a vicious cycle.

I couldn't find many other people experiencing this on the internet, I can only assume that people simply don't use finalizers, which can only be a good thing.

One guy had a rather more interesting solution:
<code>
public static void main(String[] args)
{
&nbsp;&nbsp;new Object()
&nbsp;&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;@Override protected void finalize() throws Throwable
&nbsp;&nbsp;&nbsp;&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;super.finalize();
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Thread.currentThread().setPriority(Thread.MAX_PRIORITY);
&nbsp;&nbsp;&nbsp;&nbsp;}
&nbsp;&nbsp;};
&nbsp;&nbsp;// ...
}
</code>

The worst thing is, I can't really see any disadvantages to this...