title: NMEA -> MapPoint 2004 and Google Earth.
slug: nmea-mappoint-2004-and-google-earth
date: 2006-04-15 21:48:23+00:00

I've been playing around with GPS recievers, and the first thing I wanted to do turned out to be the hardest. Just to run through what I did, just in case anyone else wants to go through the same steps without the hours of googling and guessing. The overal aim was to get (and save) the data from my <a href="http://www.holox.co.uk/">HOLOX</a> BT-321 GPS reciever (which speaks NMEA) in some visualisable form using my <a href="http://shop.orange.co.uk/shop/show/handset/orange_spv_c550">Orange SPV 550</a> (<a href="http://www.htc.com.tw/">HTC</a> Hurricane) .
<ul>
	<li><strong>Saving the data: </strong> <a href="http://forums.devbuzz.com/tm.asp?m=37214&p=1&tmode=1">Devbuzz' forums</a> (thanks pdcira2) contain a modification of code given in Nick Gratton and Marshall Brian's book: '<a href="http://www.amazon.co.uk/gp/product/0130255920/202-6642317-1504635?v=glance&n=283155">Windows CE 3.0 Application Programming</a>' to read and parse data from a COM port and write it to a file. This code required a bit of modificaiton to make it play nice with <a href="http://msdn.microsoft.com/vstudio/">VS2005</a> and <a href="http://www.microsoft.com/windowsmobile/smartphone/default.mspx">Smartphone 2003</a>, my changes will be avaliable once I get my new site up, contact me if you're impatient.</li>
	<li><strong>Log file format: </strong> You should now have a file that contains a list of lines looking something like.. 
<code>
5213.8312|N|00004.2204|E|
</code>
As explained <a href="http://www.gpsinformation.org/dale/nmea.htm#RMC">on gpsinformation.org</a>, this represents the degrees (52) and minutes (13.8312) north (N), and the degrees (0) and minutes (4.2204) east (E).
</li>
	<li><strong>Applications: </strong> In this form, this information is completely useless to applications like <a href="http://www.microsoft.com/mappoint/default.mspx">Microsoft MapPoint 2004</a>. Although this is incredibly poorly documented, they require the latitude and longitude to be given in degrees, as a decimal, with positive for north and east.</li>
	<li><strong>Conversion: </strong> Once you know this, the conversion is pretty trivial. Assuming that all the points are N and E, you simply need to divide each part by 100, the divide the fractional part by 0.6, eg:
<code>
#!php
// Quick and nasty conversion for N,E NMEA data to decimal degrees.
< ?
function conv($i)
{
        return round(floor($i) + ($i-floor($i))/0.6, 4);
}

foreach (file('foo.txt') as $line)
{
        $out = "";
        $t=explode('|N|', str_replace('|E|', '', trim($line)));
        $out.= conv($t[0]/100);
        $out.= ",";
        $out.= conv($t[1]/100);
        echo $out . "\n";
}
</code></code></li>
	<li><strong>Importing: </strong> Now the conversion has been done, you have a file consiting of lines that look something like:
<code>
52.2305,0.0703
</code>
<ul>	<li>For MapPoint you can now use the 'Import Data Wizard' (Ctrl+I) on this file, telling it that the first column is latitude, the second longitude. It'll give you a load of pushpins representing your dataset, hopefully at the correct places. The example I've been using happens to be the thrilling A428/M11 junction in Cambridge.</li>
	<li>For Google Earth you need to do a little more processing. You can use <a href="http://www.gpsvisualizer.com/map?form=googleearth">GPS Visualizer's KML generator</a> to do it for you, simply delete everything in the "Or paste your data here:" box, and add "latitude,longitude" followed by the contents of your file, eg:
<code>
latitude,longitude
52.2305,0.0703
...etc.
</code>
This'll generate you a "kmz" file for download, poking it suggests that it's just a zipped "kml" file, rename it to .kml.zip, extract and have a poke.
You'll notice that it's just a list of space-seperated long,lat,alt, with all the altitudes being 0, pretty easy to generate yourself if you want.
</li>
</ul></li></ul>

Hope that saves someone a few hours.