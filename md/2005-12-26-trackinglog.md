title: tracking.log
slug: trackinglog
date: 2005-12-26 20:37:18+00:00

I was having a look through my \System Volume Information folder earlier (not accessible to even Administrators, so I was using the "run cmd as SYSTEM" hax), and found a file called "tracking.log". Had a look in it.. binary, but 'strings' found a few of the machine names of other machines on my network. Susupicious, no?

Turns out it appears to just be part of the <a href="http://www.microsoft.com/resources/documentation/Windows/XP/all/reskit/en-us/prkc_fil_ngyp.asp">Distributed Link Tracking service</a>, keeping track of windows file sharing+nfs. Fair enough. Even shows in services.msc, description: "Maintains links between NTFS files within a computer or across computers in a network domain.".

Now I'm just wondering how badly (and easily) you can screw over, say, virus/spyware scanners running as the lowly administrator. Giving the administrator group only execute rights to a file would be lethal, (they wouldn't be able to do anything to it), removing "list files" access to the directory it's in makes them incapable of finding a file that changes it's name, too.

Heh heh heh..