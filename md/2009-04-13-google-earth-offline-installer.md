title: Google Earth "offline installer"
slug: google-earth-offline-installer
date: 2009-04-13 13:28:17+00:00

Google seem to be of the incorrect opion that you want your machine infected with Google Update.

The <a href="http://earth.google.com/download-earth.html">Google Earth download</a> is actually just a cunningly disguised Google Update installer, and it seems to think it needs elevation.

It extracts %TEMP%\GUXXXXX.tmp\GoogleUpdate.exe, then tries to run:

<pre>GoogleUpdate.exe /install "appguid={74AF07D8-FB8F-4d51-8AC7-927721D56EBB}&appname=Google%20Earth&needsadmin=true" /installelevated</pre>

Instead of this,

<pre>GoogleUpdate.exe /install "<strong>appguid={74AF07D8-FB8F-4d51-8AC7-927721D56EBB}&appname=Google%20Earth</strong>"</pre>

..will happily download and extract Google Earth to %TEMP%\7ZipSfx.XXX.  This is the unpacked offline installer, but the installer itself still attempts to elevate.  Luckily, it's already unpacked, in:

<pre>%TEMP%\7ZipSfx.XXX\program files\Google\Google Earth</pre>

Just copy this folder to somewhere convenient and run googleearth.exe.

--

For reference for other apps, the quoted argument to GoogleUpdate.exe is the last "line" in the downloaded GoogleEarthSetup.exe.