title: Catchlogger
slug: catchlogger
date: 2010-02-13 11:06:36+00:00

Post seriousness: 70%.

<a href="/files/catchlogger-ea10174865343dc2b75eee69cc40b319f5981555.jar">Catchlogger [jar]</a> [<a href="//git.goeswhere.com/?p=dmnp.git;a=tree;f=ue/src/main/java/com/goeswhere/dmnp/ue;h=3b46444faa5c388b625e9ad8c98c0cd851686a79;hb=HEAD">git src</a>] checks that exceptions are being logged properly.

It's entirely fallible, but, if your codebase is prone to catching and ignoring exception, and you use log4j, it's Very Helpful.

For example:

<pre>try {
  foo();
} catch (IOException e) {
  logger.error("bar: failed to foo", e);
}</pre>

This is fine; an error has occurred and it's full stacktrace will be placed in the log4j configured log.

<pre>try {
  foo();
} catch (IOException e) {
  logger.error(e);
  logger.info("oh noes", e);
  e.printStackTrace();
}</pre>

None of these, however, will do anything useful.  The first logs just the toString() to the error log, info is too low-level to log exceptions at, and printStackTrace() doesn't necessarily go anywhere at all.

For this block, catchlogger will issue:
<pre>IOException e unused at (Test.java:15) in public main(String[] args) in path.</pre>


The JAR is huge as it pulls in the entire Eclipse compiler to parse the source.  BSD/MIT licensed.