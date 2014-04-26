title: Remote backups.
slug: remote-backups
date: 2006-01-23 23:54:54+00:00

I was trying today to think of an effective way to securely copy files to another, restricted machine.

The idea of this being that no matter what happens to the source machine, the backups will always still exist (unless something nasty happens to the remote machine, too).

The simple way to do this securely against interception and the source machine having a physical faliure of some kind is to use an ssh-key+scp to copy archives across from a cron job.

This, however, means you have an ssh key lying around on the source machine; it doesn't even protect the backups against accidental overwriting, let alone intentional.

Firewalling and lack of access on the target machine means that running a server would be challenging, I'm yet to think of a good, safe solution.