title: Repetitive crypto miscellany
slug: crypto-miscellany
date: 2012-05-15 19:34:18+00:00

HTTPS (HTTP over <a href="https://en.wikipedia.org/wiki/Transport_Layer_Security">TLS</a>) is the most accessible form of encryption for end users.  It protects against real <a href="http://justinsomnia.org/2012/04/hotel-wifi-javascript-injection/">annoyances</a> and <a href="http://codebutler.com/firesheep">attacks</a>.  I believe it's probably the most important thing to advocate, even among developers.
<ul>
<li>Paranoid internet user?  <a href="https://www.google.com/">Google</a> and <a href="https://duckduckgo.com/">DuckDuckGo</a> will run your search results over TLS.  Some websites, like <a href="https://www.facebook.com/settings?tab=security&section=browsing&view">Facebook</a>, allow you to specify that you always want to use HTTPS.  You should.</li>
<li>Want more?  <a href="https://www.eff.org/https-everywhere">HTTPS Everywhere</a> is a Chrome/Firefox extension that tries to upgrade your connection to HTTPS on any website where it's available.</li>
<li>Host a website?  HTTPS (HTTP over TLS) is <a href="https://startssl.com/">free</a>, easy to set up and isn't <a href="http://www.imperialviolet.org/2010/06/25/overclocking-ssl.html">CPU intensive any more</a> (for typical sites).  While you're there, enable <a href="https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security">HTTP STS</a>.</li>
<li><a href="http://convergence.io/">Yes</a>, CAs <a href="https://www.eff.org/files/colour_map_of_CAs.pdf" title="Organisations trusted by IE / Firefox">sucking</a> ruins <a href="https://code.google.com/p/chromium/issues/detail?id=107793" title="Chrome #107793: certificate information API">some</a> of <a href="https://www.net-security.org/secworld.php?id=11537" title="Rogue Google SSL certificate allowed MITM Gmail attacks">this</a>.</li>
</ul>

Cryptography, contrary to what you may have heard, is easy:
<ul>
<li><a href="http://chargen.matasano.com/chargen/2009/7/22/if-youre-typing-the-letters-a-e-s-into-your-code-youre-doing.html">Data at rest?</a>  <a href="http://www.gnupg.org/">GPG</a>.  Data in motion?  TLS.</li>
<li>You never, ever, ever want to use a "hash function" or a "cipher" directly.  Ever.</li>
<li>Storing details about passwords?  "Oh, I'll hash them with a hash function?  Lots!"  No.  Use <a href="https://en.wikipedia.org/wiki/PBKDF2">PBKDF2</a> (with 50,000 or more <a href="https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2010-3741">iterations</a>), <a href="http://codahale.com/how-to-safely-store-a-password/">bcrypt</a> or <a href="https://www.tarsnap.com/scrypt.html">scrypt</a>.</li>
<li>Offering any kind of integrity, oh, I'll use a hash function?  <a href="http://netifera.com/research/flickr_api_signature_forgery.pdf">No</a>.  <a href="https://en.wikipedia.org/wiki/HMAC">HMAC</a>.</li>
</ul>

Rough overview of primitive deprecation:
<ul>
<li>MD5 has been deprecated for all uses since last century.  Why do people still use it for anything?  Please mock anyone who does.</li>
<li>SHA-1 (from 1995) has been deprecated for <a href="http://csrc.nist.gov/groups/ST/hash/policy.html">most uses</a> since 2010.  Please don't use it for anything new, and start migrating away from it.</li>
<li>RC4 was designed in 1987 (25 years ago!), but is still supported everywhere because Windows XP (2001 technology) doesn't support AES for TLS.  It has no other advantages.</li>
<li>Don't compromise security for speed.  Why bother, if it's not going to be secure?  Don't use <a href="http://www.cryptopp.com/benchmarks-amd64.html">old benchmarks</a> for your decisions.  My five year old computer is about twice as fast as that.  Run real benchmarks, yourself.  Want something actually fast?  Use Salsa20/X.</li>
<li>Basically: SHA-2 (or <a href="https://en.wikipedia.org/wiki/SHA3">3</a>!), AES (in CBC or CTR mode) or, if you're desperate, Salsa20.</li>
</ul>

Rough overview of key recommendations:
<ul>
<li>2<sup>80</sup> security: 160-bit SHA-1, 1024-bit modulus on public keys (thanks, <a href="https://en.wikipedia.org/wiki/General_number_field_sieve">GNFS</a>), 160-bit <a href="https://en.wikipedia.org/wiki/Elliptic_curve_cryptography">EC keys</a>.  Attacking 2<sup>80</sup> combinations could plausibly be done in a human lifespan on a supercomputer or two; not enough.</li>
<li>2<sup>112</sup> security: 2048-bit modulus on public keys, currently believed to be okay until 2020-2030.</li>
<li>2<sup>128</sup> security: 256-bit SHA-2, 256-bit EC keys, 3096-bit modulus on public keys, etc. are likely to be fine for the foreseeable future.</li>
<li>2<sup>256</sup> security: 512-bit SHA-2, 512-bit EC keys, <strong>15360</strong>-bit modulus on public keys.  That's a big step up.</li>
<li>128-bit AES falls somewhere into the middle, i.e. use 192-bit AES after 2020.</li>
<li>Note that these dates are when you expect your data to still be relevant, or your system in use; not when you plan to design or release the thing.</li>
</ul>