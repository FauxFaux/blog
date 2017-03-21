title: find-deleted: checkrestart replacement
slug: find-deleted-checkrestart
date: 2017-03-21T20:14:14+00:00

[checkrestart](https://manpages.debian.org/testing/debian-goodies/checkrestart.1.en.html), part of
[debian-goodies](https://packages.debian.org/debian-goodies),
checks what you might need to restart. You can run it after a system
update, and it will find running processes using outdated libraries.
If these can be restarted, and there's no new kernel updates, then
you can save yourself a reboot.

However, `checkrestart` is pretty dated, and has some weird behaviour.
It frequently reports that there are things needing a restart, but
that it doesn't feel like telling you what they are. (This makes me
moderately angry). It's pretty bad at locating services on a
systemd-managed system. It tries to look through Debian packages,
making it Debian specific (along with unreliable). This is especially
odd, because systemd knows what pid belongs to a unit, as does `/proc`,
and...

Instead of fixing it, I have rewritten it from scratch.

[find-deleted](https://github.com/FauxFaux/find-deleted) is a tool
to find deleted files which are still in use, and to suggest systemd
units to restart.

The default is to try and be helpful:

    % find-deleted
     * blip
       - sudo systemctl restart mysql.service nginx.service
     * drop
       - sudo systemctl restart bitlbee.service
     * safe
       - sudo systemctl restart fail2ban.service systemd-timesyncd.service tlsdate.service
     * scary
       - sudo systemctl restart dbus.service lxc-net.service lxcfs.service polkitd.service
    Some processes are running outside of units, and need restarting:
     * /bin/zsh5
      - [1000] faux: 7161 17338 14539
     * /lib/systemd/systemd
      - [1000] faux: 2082
      - [1003] vrai: 8551 8556

Here, it is telling us that a number of services need a restart.
The services are categorised based on some patterns defined in the
associated configuration file, `deleted.yml`.

For this machine, I have decided that restarting `mysql` and `nginx`
will cause a `blip` in the service to users; I might do it at an off-peak
time, or ensure that there's other replicas of the service available
to pick up the load.

My other categories are:

 * drop: A loss of service will happen that will be annoying for users.
 * safe: These services could be restarted all day, every day, and nobody would notice.
 * scary: Restarting these may log you out, or
    [cause the machine to stop functioning](https://github.com/systemd/systemd/issues/2748).
 * other: things which don't currently have a classification

If you're happy with its suggestions, you can copy-paste the above commands,
or you can run it in a more automated fashion:

    systemctl restart $(find-deleted --show-type safe)

This can effectively be run through provisioning tools, on a whole selection
of machines, if you trust your matching rules! I have done this with a much
more primitive version of this tool at a previous employer.

It can also print the full state that it's working from, using `--show-paths`.

