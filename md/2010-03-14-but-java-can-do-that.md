title: But Java /can/ do that!
slug: but-java-can-do-that
date: 2010-03-14 09:05:25+00:00

I recently attended a talk at FOSDEM by <a href="http://tirania.org/blog/">Miguel de Icaza</a>, a fellow enemy of "Free" software.

He, like most .NET users, is desperately seeking features to differentiate his second-rate platform from the wonderfulnessness of Java.

He showed .NET expressions, a wonderful feature whereby the actual nature of a predicate can be retrieved at runtime and optimal, say, SQL can be built to match it.  

He, however, claimed that Java lacks this feature.  This is not the case.

<a href="//git.goeswhere.com/?p=dmnp.git;a=blob;f=expr/src/test/java/com/goeswhere/dmnp/expr/ExpressionTest.java">ExpressionTest</a> shows various uses of this in Java; basically:

<pre>Expression.toSQL(new Predicate&lt;FooDTO&gt;() { @Override public boolean matches(FooDTO t) { t.a == 7; } });</pre>

will return:

<pre>(a = 7)</pre>

Obviously this remains slightly more verbose while the Java lambda proposals are finalised, but the feature is hardly missing!

Similarily,
<pre>return (t.a == 7 || t.a == 8 || t.a == 9) && "pony".equals(t.b);</pre>

becomes:

<pre>(a = 7 AND b = 'pony') OR 
(a = 8 AND b = 'pony') OR
(a = 9 AND b = 'pony')</pre>

And, etc.

<a href="//git.goeswhere.com/?p=dmnp.git;a=tree;f=expr/src/main/java/com/goeswhere/dmnp/expr">The implementation</a>, if the devil compels you to look.
