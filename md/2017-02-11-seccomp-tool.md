title: Playing with prctl and seccomp
slug: seccomp-tool
date: 2017-02-11 21:10:55+00:00

I have been playing with low-level Linux security features, such as
[prctl no new privs](https://www.kernel.org/doc/Documentation/prctl/no_new_privs.txt)
and [seccomp](https://www.kernel.org/doc/Documentation/prctl/seccomp_filter.txt).
These tools allow you to reduce the harm a process can do to your system.

They're typically deployed as part of systemd, although the [default settings in
many distros are yet to be ideal](https://lwn.net/Articles/709755/). This is partly
because it's hard to confirm what a service actually needs, and partly because many services
*support* many more things than a typical user cares about.

For example, should a web server be able to make *outgoing* network connections?
Probably not, it's accepting network connections from people, maybe running some code,
then returning the response. However, maybe you're hosting some PHP that you want to be
able to fetch data from the internet? Maybe you're running your web-server as a proxy?

To address these questions, Debian/Ubuntu typically err on the side of "let it do whatever,
so users aren't inconvenienced". CentOS/RHEL have started adding a large
[selection of flags you can toggle](https://wiki.centos.org/TipsAndTricks/SelinuxBooleans)
to fiddle security (although through yet another mechanism, not the one we're talking about here..).

---

Anyway, let's assume you're paranoid, and want to increase the security of your services.
The two features discussed here are exposed in systemd as
[NoNewPrivileges=](https://www.freedesktop.org/software/systemd/man/systemd.exec.html#NoNewPrivileges=)
and
[SystemCallFilter=](https://www.freedesktop.org/software/systemd/man/systemd.exec.html#SystemCallFilter=).

The first, `NoNewPrivileges=`, prevents a process from getting privileges in any common way,
e.g. by trying to change user, or trying to run a command which has privileges (e.g. capabilities)
attached.

This is great. Even if someone knows your root password, they're still stuck:

    % systemd-run --user -p NoNewPrivileges=yes --tty -- bash
    $ su - root
    Password:
    su: Authentication failure
    
    $ sudo ls
    sudo: effective uid is not 0, is /usr/bin/sudo on a file system with the 'nosuid'
      option set or an NFS file system without root privileges?

The errors aren't great, as the tools have no idea what's going on, but at least it works!

This seems like a big, easy win; I don't need my `php` application to become a different
user... or do I? It turns out that the venerable `mail` command, on a `postfix` system,
eventually tries to run a setuid binary, which fails. And `php` defaults to sending mail
via. this route. Damn!

Let's try it out:

    % systemd-run --user -p NoNewPrivileges=yes --tty -- bash
    faux@astoria:~$ echo hi | mail someone@example.com
    faux@astoria:~$
    
    postdrop: warning: mail_queue_enter: create file maildrop/647297.680: Permission denied

Yep, `postdrop` is setgid (the weird `s` in the permissions string):

    % ls -al =postdrop
    -r-xr-sr-x 1 root postdrop 14328 Jul 29  2016 /usr/sbin/postdrop

It turns out that
[Debian dropped support for alternative ways to deliver mail](https://lists.freedesktop.org/archives/systemd-devel/2014-June/020212.html). So, we can't use that!

---

Earlier I implied that `NoNewPrivileges=`, despite the documentation, doesn't
remove all ways to get some privileges. One way to do this is to enter a new
user namespace (only widely supported by Ubuntu as of today). e.g. we can get
[`CAP_NET_RAW` (and its associated vulnerabilities)](https://people.canonical.com/~ubuntu-security/cve/2016/CVE-2016-8655.html)
through user namespaces:

    % systemd-run --user -p NoNewPrivileges=yes --tty -- \
        unshare --map-root-user --net -- \
        capsh --print \
            | fgrep Current: | egrep -o 'cap_net\w+'
    cap_net_bind_service
    cap_net_broadcast
    cap_net_admin
    cap_net_raw

To harden against this, I wrote
[drop-privs-harder](https://github.com/FauxFaux/tinies/blob/master/drop-privs-harder.c)
which simply breaks `unshare` (and its friend `clone`)'s ability to make new user
namespaces, using `seccomp`.

---

Unlike `NoNewPrivileges=`, `SystemCallFilter=` takes many more arguments, and
requires significantly more research to work out whether a process is going to work.
Additionally, `systemd-run` doesn't support `SystemCallFilter=`. I'm not sure why.

To assist people playing around with this (on amd64 only!), I wrote a tool named
[seccomp-tool](https://github.com/FauxFaux/tinies/blob/master/seccomp-tool.c)
and a front-end named
[seccomp-filter](https://github.com/FauxFaux/tinies/blob/master/seccomp-filter.py).

There's a [binary of `seccomp-tool`](https://b.goeswhere.com/seccomp-tool-v0.0.1)
available for anyone who doesn't feel like compiling it. It depends on only
`libseccomp2`. `sudo apt install libseccomp2`. It needs to be in your path as `seccomp-tool`.

`seccomp-filter` supports the
[predefined system call sets](https://www.freedesktop.org/software/systemd/man/systemd.exec.html#SystemCallFilter=)
from the systemd documentation, in addition to an extra set, named `@critical`,
which systemd seems to silently include without telling you. Both of these tools
set `NoNewPrivilges=`, so you will also be testing that.

Let's have a play:

    % seccomp-filter.py @critical -- ls /
    ls: reading directory '/': Function not implemented

Here, we're trying to run `ls` with only the absolutely critical syscalls enabled.
`ls`, after starting, tries to call `getdents()` ("list the directory"), and gets
told that it's not supported. Returning `ENOSYS` ("function not implemented") is
the default behaviour for `seccomp-filter.py`.

We can have a permissions error, instead, if we like:

    % seccomp-filter.py --exit-code EPERM @critical -- ls /
    ls: reading directory '/': Operation not permitted

If we give it `getdents`, it starts working... almost:

    % ./seccomp-filter.py --exit-code EPERM @critical getdents -- ls /proc
    1
    10
    1001
    11
    1112

Why does the output look like it's been piped through a pager? `ls` has tried
to talk to the terminal, has been told it can't, and is okay with that.
This looks the same as:

    seccomp-filter.py --blacklist ioctl -- ls /

If we add `ioctl` to the list again, `ls` pretty much works as expected,
ignoring the fact that it segfaults during shutdown. systemd's `@default`
group of syscalls is useful to include to remove this behaviour.

---

Next, I looked at what Java required. It turns out to be much better than
I expected: the JVM will start up, compile things, etc. with just:
`@critical @default @basic-io @file-system futex rt_sigaction clone`.

This actually works as a filter, too: if Java code tries to make a network
connection, it is denied. Or, er, at least, something in that area is denied.
Unfortunately, the JVM cra.. er.. "hard exits" for many of these failures,
as they come through as unexpected asserts:

e.g.

`Assertion 'sigprocmask_many(SIG_BLOCK, &t, 14,26,13,17,20,29,1,10,12,27,23,28, -1) >= 0' failed at ../src/nss-myhostname/nss-myhostname.c:332, function _nss_myhostname_gethostbyname3_r(). Aborting.`

It then prints out loads of uninitialised memory, as it doesn't expect
[uname to fail](https://github.com/FauxFaux/jdk9-hotspot/blob/master/src/os/posix/vm/os_posix.cpp#L237).
e.g.

`Memory: 4k page, physical 10916985944372480k(4595315k free), swap 8597700727024688k(18446131672566297518k free)`

`uname: [box][box]s[box]`

---

This demonstrates only one of the operation modes for `seccomp`. Note that, as of
today, the Wikipedia page is pretty out of date, and the manpage is outright misleading.
Consider reading
[man:seccomp_rule_add(3)](http://man7.org/linux/man-pages/man3/seccomp_rule_add.3.html),
part of libseccomp2, to work out what's available.

---

Summary: Hardening good, hardening hard. Run your integration test suite under
`seccomp-filter.py --blacklist @obsolete @debug @reboot @swap @resources` and see
if you can at least get to that level of security?

