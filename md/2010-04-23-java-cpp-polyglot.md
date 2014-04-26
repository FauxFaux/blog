title: Java/C++ polyglot
slug: java-cpp-polyglot
date: 2010-04-23 20:14:08+00:00

Today I discovered Java's "inline C++" keyword, //\u000a/*, which makes a Java/C++ <a href="http://en.wikipedia.org/wiki/Polyglot_(computing)">polyglot</a> pretty easy:

<code>
//\u000a/*
#include &lt;iostream&gt;

#define private
#define public
#define static
#define void int
struct {
&nbsp;&nbsp;std::ostream &println(const char *c) {
&nbsp;&nbsp;&nbsp;&nbsp;return std::cout &lt;&lt; c < < std::endl;
&nbsp;&nbsp;}
} out;

//*/
/*\u002a/
import static java.lang.System.out;

public class Polyglot {
//*/
&nbsp;&nbsp;public static void main(/*\u002a/String[] args//*/
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;) {
&nbsp;&nbsp;&nbsp;&nbsp;out.println("Hello from whatever language this is!");
&nbsp;&nbsp;}

/*\u002a/
}
// */
</code>

Eclipse deals.. <a href="http://faux.uwcs.co.uk/eclipse-polyglot.png">okay</a>.  The red-underlining in the commented sections is for the spelling. &lt;3
</code>