title: Java stacktraces straw man
slug: java-stacktraces-straw-man
date: 2011-06-05 22:58:15+00:00

It's a sad fact of life that many developers spend a good deal of time staring at stack traces.

My personal favorite situation is when you get to:
<pre>Exception in thread "main" java.lang.NullPointerException
&nbsp;&nbsp;&nbsp;&nbsp;at com.goeswhere.dmnp.linenos.B.foo(<a href="http://git.goeswhere.com/?p=dmnp.git;a=blob;f=linenos/src/test/java/com/goeswhere/dmnp/linenos/B.java;h=889c1de3871669b72c3f86abd981419e00f625f3;hb=HEAD">B.java</a>:13)</pre>

..and, line 13 is:

<pre>&nbsp;&nbsp;System.out.println(first.substring(1) + second.toUpperCase() + third.toLowerCase());</pre>

Basically, the end of any happiness.

<hr style="margin: 2em"/>

<a href="http://git.goeswhere.com/?p=dmnp.git;a=tree;f=linenos">LineNos</a> can fix this:

<pre>$ java -Xbootclasspath/p:linenos.jar -javaagent:linenos.jar=com/goeswhere com.goeswhere.dmnp.linenos.B
Exception in thread "main" java.lang.NullPointerException
&nbsp;&nbsp;&nbsp;&nbsp;at com.goeswhere.dmnp.linenos.B.foo(B.java:13), <b>attempting to invoke toUpperCase</b> #4
&nbsp;&nbsp;&nbsp;&nbsp;at com.goeswhere.dmnp.linenos.B.run(B.java:9)
&nbsp;&nbsp;&nbsp;&nbsp;at com.goeswhere.dmnp.linenos.B.main(B.java:5), attempting to invoke run #2</pre>

This is implemented entirely as a Java Agent; it requires no VM modifications and is portable anywhere that supports <a href="http://download.oracle.com/javase/6/docs/api/java/lang/instrument/Instrumentation.html#retransformClasses(java.lang.Class...)">instrumenters transforming classes</a> (i.e. everywhere that matters).

<hr style="margin: 2em"/>

It works by adding extra line numbers for each call on a line.  Currently it adds call-number*1000 to the line number, so that it's debuggable and easier to do in two phases, but this makes it much less efficient.

i.e., assuming Java allowed labels for line-numbers, it does:

<pre>13:
8013: System.out.println(
1013: [secret StringBuilder construction (used to implement String concatenation)]
2013: first.substring(1) 
3013: +
4013: second.toUpperCase()
5013: +
6013: third.toLowerCase()
7013: [secret StringBuilder#toString()]);</pre>

Thus, the real stacktrace looks like:
<pre>Exception in thread "main" java.lang.NullPointerException
&nbsp;&nbsp;&nbsp;&nbsp;at com.goeswhere.dmnp.linenos.B.foo(B.java:4013)
&nbsp;&nbsp;&nbsp;&nbsp;at com.goeswhere.dmnp.linenos.B.run(B.java:9)
...</pre>

It additionally overrides StackTraceElement#toString() to decompile the named class and report the invocation that's on that line, i.e. lookup line 4013 in the above bytecode, and report that it's an invocation of toUpperCase, thus giving the intended result.

<hr style="margin: 2em"/>

It has no run-time performance penalty beyond the extra time to load classes, and the increase in the size of line-number table (actually, I have no idea how this affects performance, but I can't imagine it's much).  Printing a stacktrace is slower, however (although, it probably wouldn't be much slower in a real implementation).  Also, it's a straw-man, so leaks memory, but this isn't an important part of the implementation.

A much better implementation would be to store the [Class<>, line-number] -> hint mapping instead of the whole file and doing decompilation; or to replace the entire line-number table with a bytecode number table (i.e. 1->1, 2->2, 3->..), and do it all at print-time.  Patches welcome.

<hr style="margin: 2em"/>

In summary: Dear Oracle, please make the JVM do this by default.  Lots of Love, Faux.