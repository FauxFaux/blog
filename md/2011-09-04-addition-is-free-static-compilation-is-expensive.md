title: Addition is free, static compilation is expensive
slug: addition-is-free-static-compilation-is-expensive
date: 2011-09-04 14:41:11+00:00

Summing the integers from 1 to 10,000,000?

<ul>
<li>Perl: 1.01 seconds</li>
<li>Python: 2.04 seconds</li>
<li>Java, including javac: 0.76 seconds</li>
<li>Java, including ecj: 0.61 seconds</li>
<li>Java, including javac, with -Xint: 1.01 seconds.</li>
<li>Java, including javac, with -Xint on the compiler too: 1.16 seconds.</li>
</ul>

<ul>
<li>-Xint disables practically all optimisations that Java offers, forcing the JVM into interpretation mode, so it'll operate much like perl and python do.</li>
<li>ecj is Eclipse's compiler for Java, a faster and cleaner implementation of javac that can run standalone.</li>
</ul>

i.e. including compilation time on an entirely unoptimised compiler, Java is still twice the speed of Python.

(This isn't really interesting or surprising to me, but the question comes up often enough that I'd like to have these here to link <a href="http://xkcd.com/386/">WRONG</a> people to.)

<!--more-->
<hr style="margin: 2em"/>

Testcases:
<code>
time (N=10000000; printf "class A { public static void main(String... arg) { long j = 0; for(long i = 0; i < $N; ++i) { j += i; } System.out.println(j); } }" > A.java && javac A.java && java A)
time (N=10000000; printf "class A { public static void main(String... arg) { long j = 0; for(long i = 0; i < $N; ++i) { j += i; } System.out.println(j); } }" > A.java && javac A.java && java -Xint A)
time (N=10000000; printf "class A { public static void main(String... arg) { long j = 0; for(long i = 0; i < $N; ++i) { j += i; } System.out.println(j); } }" > A.java && javac -J-Xint A.java && java -Xint A)
time (N=10000000; printf "class A { public static void main(String... arg) { long j = 0; for(long i = 0; i < $N; ++i) { j += i; } System.out.println(j); } }" > A.java && java -jar ecj.jar -source 1.5 A.java && java A)
time (N=10000000; printf "j = 0\nfor i in range(1,$N):\n\tj = j + i\nprint j" | python -)
time (N=10000000; printf 'my $j = 0; for ($i = 0; $i < '$N'; ++$i){ $j += $i; } print $j' | perl -w)
</code>


Versions, from Debian stable:
</code><code>
Python 2.6.6 (r266:84292, Dec 26 2010, 22:31:48)
perl, v5.10.1
OpenJDK Runtime Environment (IcedTea6 1.8.7) (6b18-1.8.7-2~squeeze1), OpenJDK 64-Bit Server VM (build 14.0-b16, mixed mode)
ecj 3.5.1
</code>