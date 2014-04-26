title: OpenTTDIRC
slug: openttdirc
date: 2006-01-25 08:01:01+00:00

I updated my patch for OpenTTD to add a simplistic IRC client today, it now builds fine against r3426, assuming you can add a single c file to your build scripts (I've only got it for Visual Studio 2005 (for which there isn't a project file in svn yet), so no matter what build system/os you're using it will need updating).

I belive it's cross platform, although I'm yet to check that as yet.

The current one is written in a MUD-style, with all the channels going into one window. For low-traffic channels this is equally, if not more effective than having multiple windows (especially with the cunning context-logging, so you don't have to /msg the same channel/person more than once in a row).

Mutliple windows really isn't practical, as far as I know no pure-IRC clients do non-MDI multi-windowing. A tabstrip could work, it'd also be resonably effective in other areas of OpenTTD (load/scenario/create-game dialog is effectively the same thing anyway, it just has a few different views, etc.), definitely worth looking into at some point.