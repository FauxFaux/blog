title: My gitolite set-up
slug: my-gitolite-set-up
date: 2011-12-29 18:12:34+00:00

I'm paranoid, but also poor.  I use <a href="https://github.com/sitaramc/gitolite">gitolite</a> to control access to <a href="http://git.goeswhere.com/">my git repositories</a>, because <a href="https://github.com/plans">github wanted $200/month</a> to meet half of my requirements, and wern't interested in negotiating (I tried).

Like github, I have two types of git repositories.  Public repositories; which show up on gitweb and git-daemon and etc., that everyone can access; and private repositories, which contain my bank details.

My conf file consists of:

<strong>A set of user groups:</strong> While gitolite supports multiple keys for one user, I prefer to treat my various machines as separate users, for reasons that'll become apparent later.
<code>@faux    = admin fauxanoia fauxhoki fauxtak
@trust   = @faux alice
@semi    = fauxcodd fauxwilf bob
</code>

<strong>A set of repositories</strong>, both public and private:
<code>@pubrepo = canslations
@pubrepo = coke
@pubrepo = cpptracer
...
@privrepo = bank-details
@privrepo = alices-bank-details
</code>

<strong>Descriptions</strong> for all the public repositories, so they show up in gitweb:
<code>repo    coke
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;coke = "Coke prices website"

repo    cpptracer
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cpptracer = "aj's cppraytracer, now with g++ support"
</code>

And <strong>permissions</strong>:
<code>repo    @pubrepo
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;RW+     =   @trust
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;RW&nbsp;     =   @semi
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;R&nbsp;&nbsp;       =   @all daemon gitweb
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;config  core.sharedRepository = 0664

repo    @privrepo
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;RW+     =   @trust
</code>

This allows trusted keys to do anything, and semi-trusted keys (i.e. ones on machines where there are other people with root) to only append data (i.e. they can't destroy anything, and can't make any un-auditable changes).


Next, to protect against non-root users on the host itself, I have <code>$REPO_UMASK = 0027;</code> in my .gitolite.rc.  This makes the repositories themselves inaccessible to other users.  However, gitweb needs to be able to read public repositories; the above <code>config core.sharedRepository = 0664</code> does this.

This leaves only <code>/var/lib/gitolite/projects.list</code> (which is necessary as non-git users can't ls <code>/var/lib/gitolite/repositories/</code>, so gitweb can't discover the project list itself), and <code>repositories/**/description</code>, again for gitweb.

For this, I have a gitolite-admin.git/hooks/post-update.secondary of:

<code>#!/bin/sh
chmod a+r /var/lib/gitolite/projects.list
find /var/lib/gitolite -name description -exec chmod a+r {} +
</code>

Now, gitweb can display public projects fine, and local users can't discover or steal private repositories.