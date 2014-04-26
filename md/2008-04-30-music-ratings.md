title: Music ratings
slug: music-ratings
date: 2008-04-30 23:43:30+00:00

I've just commited some code to my <a href="http://sourceforge.net/projects/taglibhandler">Taglib Property Handler</a> that will (at least, hopefully) extract rating tags from files. This is proving rather hard to test, however, as I have nearly no test material.

In short, if you use or know about an application that adds rating information to files, please tell me about it. Currently, I've only really looked at some apps that are bundled with Windows and <a href="http://www-scf.usc.edu/~haowang/foo_rating/download.php">foo_rating</a>'s behaviour.

Windows asks that the <a href="http://msdn.microsoft.com/en-us/library/bb787554.aspx">rating be specified</a> in a range between zero (unrated) and 100 (five stars), with a curiously un-even scale in the middle. It also offers the capability to return a simple rating; the number of stars (out of five).

This is fine, until you realise that there seems to be no standard, defacto or otherwise, for the range of values or the location to write rating information in the file*.

Based on the limited sample above, the code I committed attempts to find a tag named "rating" in the file, and takes it's integer value. If it is below five, it is used as a star rating, if it's below 100, it's used directly, and if it's below 255, it's mapped onto the 100 range. While this effectively deals with the cases I have encountered so far, it is, obviously, full of discontinuities. After the above mapping function, the input 4 is greater than everything below 75 (the value used to represent four stars), etc.

This should allow apps that follow the Windows (percentage) standard and the "number of stars" standard to coexist happily, but may cause strange issues when unexpected rating systems are used.
Unfortunately, even if I'm aware of curious rating systems, there's little I can do about them, as, at this point in the code only the current file is visible, not others in the set (directory etc.). If someone is using 0 -> 10, everything six and above is going to show as one star. :(


(* The exception to this is, of course, <a href="http://www.id3.org/id3v2.4.0-frames">id3v2</a>, which specifies the POPM ("popularimeter", 4.17) tag, which contains an octet value (0->255) for a user rating. I have never seen an app that writes these, nor a file containing them, and, as such, id3v2 files go through the same process as everything else as a fallback.)