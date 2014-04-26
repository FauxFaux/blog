title: GetWindowLongPtr and friends.
slug: getwindowlongptr
date: 2006-01-11 13:14:34+00:00

As mentioned in 
<a href="http://msdn.microsoft.com/msdnmag/issues/01/08/bugslayer/">this bugslayer post</a>, GetWindowLongPtr and SetWindowLongPtr are defined incorrectly when doing 32-bit compiles, meaning that my code is destined to create warnings until a fix is released. #pragma warnings do not count as fixes, sorry.

The warning (or error, if you're trying to build with treat warnings as errors) you get is:

<code>warning C4244: 'argument' : conversion from 'LONG_PTR' to 'LONG', possible loss of data</code>