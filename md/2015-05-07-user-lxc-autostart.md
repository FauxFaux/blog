title: lxc-autostart for limited users, on systemd
slug: user-lxc-autostart
date: 2015-05-07T11:43:50+0100

[lxc](https://linuxcontainers.org/) comes with a tool named `lxc-autostart` which can help you start
your containers at boot, all you have to do is set `lxc.start.auto = 1` in the config file and it will
start your containers for you... if you're running your containers as root.

For convenience and security, I'm not running my containers as root.  Normally, if I wanted to start
something on boot, as a limited user (or possibly as a service), I'd use the `cron` `@reboot` hack:

    $ crontab -l
    @reboot /usr/bin/lxc-autostart

This, however, fails for `lxc-autostart` (and for `lxc-start`, for the same reason): `cron` runs your
command in a bizarre environment which, importantly, doesn't have the user's cgroups setup properly.
These are setup somewhere scary (`pam`?), and `cron` apparently doesn't do a proper log-in for your user.
You can observe the failure with some:

    * * * * * cat /proc/self/cgroup

...which will show you have junk cgroups, which makes `lxc-start` angry with terrible, terrible errors:

    cgmanager[1041]: cgmanager:do_create_main: pid 5679 (uid 1000 gid 1000) may not create under /run/cgmanager/fs/blkio/system.slice/autostart.service
    cgmanager[1041]: cgmanager:do_create_main: pid 5679 (uid 1000 gid 1000) may not create under /run/cgmanager/fs/cpu/system.slice/autostart.service
    ...
    cgmanager[1041]: cgmanager: Invalid path /run/cgmanager/fs/blkio/system.slice/autostart.service/lxc/utopic
    cgmanager[1041]: cgmanager:per_ctrl_move_pid_main: Invalid path /run/cgmanager/fs/blkio/system.slice/autostart.service/lxc/utopic
    cgmanager[1041]: cgmanager: Invalid path /run/cgmanager/fs/cpu/system.slice/autostart.service/lxc/utopic
    cgmanager[1041]: cgmanager:per_ctrl_move_pid_main: Invalid path /run/cgmanager/fs/cpu/system.slice/autostart.service/lxc/utopic
    ...

The easiest way for a limited user to solve this is, as far as I'm aware, `ssh` to `localhost`.
Limited users can't configure `sudo` to be passwordless, and can't `su` without entering their password on a
proper terminal, meaning neither work from `cron`.

    $ ssh-keygen -t ed25519
    $ ssh-copy-id localhost
    $ crontab -l
    @reboot /usr/bin/ssh me@localhost /usr/bin/lxc-autostart

This was working great, until the Ubuntu Vivid upgrade, which has bought the wonders of `systemd`.

Under `systemd`, the `@reboot` entries are sometimes processed before `sshd` has started, so the above
*massive hack* fails.

    $ crontab -l
    @reboot sleep 10 && /usr/bin/ssh ...

NO.  NO NO NO.

Under `systemd`, we can write a simple service file that does the auto-start.  `systemd` understands cgroups,
so if you ask it to run a service as a `User=`, it'll run the service in the user's cgroup, right?
Nope: It runs everything in the service cgroup.  Fair enough.

However, as the service is started as root, we can use `su`.
A `systemd` service: `/etc/systemd/system/autostart.service`:

    [Unit]
    Description=lxc-autostart
    After=network.target

    [Install]
    WantedBy=multi-user.target

    [Service]
    Type=oneshot
    ExecStart=/bin/su me -c '/usr/bin/lxc-autostart'

And install it:

    $ sudo systemctl enable lxc-autostart.service

This seems to work.  I'm not sure if the `After=` is necessary;
[`network.target` is a complex beast](http://www.freedesktop.org/wiki/Software/systemd/NetworkTarget/)
but I still feel safer waiting for something to be alive.

