title: git --set-commit-id
slug: git-set-commit-id
date: 2010-12-14 14:04:51+00:00

People often complain that git's commit ids are too hard to remember and that they prefer the sequential ones generated by inferior version control systems.

Stock git doesn't have an option to pick the commit id for a commit; this seems like a grave omission.  I've prepared <a href="/files/0001-set-commit-id-option-for-commit.patch">a patch which offers git commit --set-commit-id</a>.

For example, everyone knows that the base commit in a repository should have a low number:

<pre>$ git init
Initialized empty Git repository in ./.git/
$ git add -A
$ git commit --set-commit-id 0000000 -a -m "Base."
Searching:  46% (12593/26843), done.
[master (root-commit) 0000000] Base.
 1 files changed, 1 insertions(+), 0 deletions(-)
 create mode 100644 myfile
</pre>


If you've already messed up your repository, a handy fixing script is provided:
<pre>$ git lg
* fe5e2ee - (HEAD, master) work, work, work, it's all I do
* a2c1ec8 - work, work, work
* e580e5e - work, work
* a6ad5ee - work
* 0000000 - base
$ sequentialise.sh 0000000 6
Stopped at a6ad5ee... work
Searching: 39% (10468/26843), done.
[detached HEAD 0000010] work
 1 files changed, 1 insertions(+), 0 deletions(-)
Stopped at e580e5e... work, work
Searching:  174% (46706/26843)
[...]
$ git lg
* 0000040 - (HEAD, master) work, work, work, it's all I do
* 0000030 - work, work, work
* 0000020 - work, work
* 0000010 - work
* 0000000 - base
</pre>

Much more usable!  This <a href="//git.goeswhere.com/?p=seqed.git;a=summary">example repository is available for inspection</a>.  gitweb doesn't show the commit ids on the log screen, but you can mouse-over and see them in the URLs.

Needless to say, this takes "a while".  sequentialise.sh defaults to 5 digits, i.e. enough for a million commits, and is reasonably fast on modern hardware.  6 digits is rather less tolerable.