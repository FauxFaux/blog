title: Password policy
slug: password-policy
date: 2012-06-06 21:03:56+00:00

In light of today's supposed LinkedIn breach, it seems like an appropriate time to finally write up my password policy.

Many people have cottoned on to the idea that having the same password on different sites is a bad idea.  There's various technical solutions to this, such as generating a <a href="http://passhash.connorhd.co.uk/">site-specific</a> <a href="https://lastpass.com/">password</a>.  I, however, believe this scheme to be too inconvenient; they require you to always have access to the site or tool, and don't work well in public places.

What we're really trying to do here is:
<ol>
	<li>Have different passwords on different sites.</li>
	<li>Have passwords that are (very) hard to guess.</li>
	<li>Be as lazy as possible.</li>
</ol>

What the first means is: If an attacker is given my password for a specific site, they can't easily derive the password for any other site.  I am willing to risk the chance of them retrieving the password for multiple sites.

My proposal is to have a way to generate secure, site-specific passwords in one's head:
<ol>
	<li>Remember an excessively long password.</li>
	<li>Come up with some way to obscure the site name.</li>
	<li>Put the obscured site name in the middle of your long password, and use that password for the site.</li>
</ol>

That is:
<ol>
	<li>Remember an excessively long password: 14 characters is a good start.  <a href="https://pwgen.goeswhere.com/">(My) pwgen</a> can help you come up with suggestions.  Note that this password doesn't need to be full of capitals, numbers or symbols; the sheer length makes it secure.  "<code>c8physeVetersb</code>" is around a thousand times "more secure" (higher entropy) than "<code>A0Tv|6&m</code>".</li>
	<li>Come up with a set of rules to obscure the site name: For example, take the "letter in the alphabet after the first character of the site name", and "the last character of the site name, in upper case".  e.g. for "amazon", the obscured version of the site name would be "<code>bN</code>".</li>
	<li>Mix them together: e.g. I'm going to insert the first bit, <code>'b'</code> after the <code>'V'</code>, and the second bit, <code>'N'</code> after the last <code>'s'</code>, giving me "<code>c8physeV<b>b</b>esters<b>N</b>b</code>".</li>
	<li>Use this password on Amazon.</li>
</ol>

Even if Amazon are broken into, all the attacker will get (after many CPU-decades of password cracking), will be "<code>caphyseVbester5Nb</code>", which, even if they know you're using this password scheme (but not the details of your transformation), doesn't tell them anything about your password on any other site.

All you have to do is remember the alphabet (uh oh).

<!--more-->
<hr />

I additionally recommend:
<ul>
	<li>Sticking to alphanumerics (a-z, A-Z and 0-9); lots of sites have issues with other characters.  Even big ones.  Even if they seem to work first time.  Please, guys, stop failing at this.</li>
	<li>Sticking to 16 characters or shorter.  Many websites are arbitrarily limited around here.  Please, guys, stop doing this: It makes it look like you're not <a href="http://codahale.com/how-to-safely-store-a-password/">storing your passwords properly</a>.</li>
	<li>Having most of the security near the start of the password, so that when you encounter a <s>bank</s>website that limits you to eight characters, you can just drop the end without losing all of your security.  Not even going to comment on this.</li>
	<li>Keeping a list of sites you have accounts on, so you can change all the passwords at the same time, if you ever want to change scheme again.</li>
</ul>
