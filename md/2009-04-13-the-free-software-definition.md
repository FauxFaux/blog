title: The Free Software Definition
slug: the-free-software-definition
date: 2009-04-13 15:58:33+00:00

The GNU project publishes a <a href="http://www.gnu.org/philosophy/free-sw.html">list of four Freedoms</a> and recommend a single license*, the <a href="http://www.gnu.org/licenses/licenses.html#GPL">GPL</a>.

They claim the word "Free" for software available under the GPL.

Let us consider some developer freedoms, and some alternative licenses for blocks of code:
<style type="text/css">
  td { text-align: center }
  th { padding: .5em }
  td { padding: .2em }
  td,th { border: 1px solid black }
  .tick { background-color: #dfd }
</style>
<table><tr><th /><th>Link / Use</th><th>Four boring freedoms</th><th>Reuse the code</th><th>Sue author</th></tr>
<tr><td>Proprietary</td><td></td><td></td><td></td><td class="tick">✓</td></tr>
<tr><td>GPL</td><td></td><td class="tick">✓</td><td></td><td></td></tr>
<tr><td>Freeware**</td><td class="tick">✓</td><td></td><td></td><td></td></tr>
<tr><td>LGPL</td><td class="tick">✓</td><td class="tick">✓</td><td></td><td></td></tr>
<tr><td><a href="http://en.wikipedia.org/wiki/BSD_license">BSD</a>/<a href="http://en.wikipedia.org/wiki/MIT_license">MIT</a>/<a href="http://en.wikipedia.org/wiki/ISC_license">ISC</a>/etc.</td><td class="tick">✓</td><td class="tick">✓</td><td class="tick">✓</td><td></td></tr>
<tr><td><a href="http://en.wikipedia.org/wiki/Public_domain">PD</a>/<a href="http://sam.zoy.org/wtfpl/">WTFPL</a>***/etc.</td><td class="tick">✓</td><td class="tick">✓</td><td class="tick">✓</td><td class="tick">✓</td></tr>
</table>
<br />
Looking at this, it's reasonably obvious to me which licenses offer the most Freedom to the developer; that being the BSD/MIT/ISC family.

These are the licenses I use personally, and the licenses I use to define Free Software; I don't see how it can be taken any other way.

<!--more-->

--

<ul>
<li><strong>Link / use</strong>: The license allows you to use the software as a whole, <strong>for any purpose</strong> (i.e. it's free for use in assisting proprietary software and terrorism) (like freedom 0, but applicable to libraries).</li>
<li><strong>Four boring freedoms</strong>: Follows the four freedoms outlined by the GNU project.</li>
<li><strong>Reuse the code</strong>: The freedom to study and reuse the code, <strong>for any purpose****</strong> (especially for terroism).</li>
<li><strong>Sue the author</strong>: Generally, with proprietary software and with non-software licenses, you have the right to hold the author responsible for their work, at least, up to a certain value. The author may want to disown this responsibility.</li>
</ul>

--

* The <a href="http://www.gnu.org/licenses/why-not-lgpl.html">LGPL is discouraged</a>, the GDFL is not for software (<a href="http://wiki.debian.org/DFSGLicenses#LicensesthatareDFSG-incompatible" title="List of licenses which are not DFSG compliant">and generally considered non-free anyway</a>), the <a title="GNU Affero General Public License" href="http://www.gnu.org/licenses/licenses.html#AGPL">AGPL</a> is an extension of the GPL.

** I can't think of nearly any prominent Freeware libraries, either.  <a href="http://www.foobar2000.org/">Foobar2000</a>'s SDK?

*** The WTFPL's FAQ covers "Why is there no “no warranty” clause?", and also why Public Domain isn't really a license.

**** Apparently there's some confusion as to what I mean by "for any purpose". I include using the code inside other applications, regardless of their license, as a purpose.  That is, the GPL does not allow code reuse <strong>for any purpose</strong>, because it does not allow code reuse in proprietary applications.