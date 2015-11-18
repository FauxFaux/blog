title: Capturing users' ssh keys
slug: ssh-key-capture
date: 2015-10-04T21:54:36+0100

Four years ago, I was working on a project that would require users to connect
 to it over ssh.  At the time, asking typical users (even developers!) to send
 you an ssh public key was a bit of an involved operation.

The situation hasn't improved much.

For example, [github suggests generating the keys manually](https://help.github.com/articles/generating-ssh-keys/),
 then using Windows' `clip.exe` or `apt-get install xclip && xclip` (from the
 command line) to get the key into the clipboard, then pasting it into their
 web-interface.  Ugh.

The situation is a little better for [PuTTYTray](https://puttytray.goeswhere.com/),
 it has built-in support for SSH agent, and a [reasonably streamlined way to get keys
 into the clipboard](https://github.com/FauxFaux/PuTTYTray/wiki/Automatic-logins), but,
 then, we're still using the clipboard-into-the-web-interface story.  This was
 written in 2013-08, two years too late (although I'm sure the author could have been
 convinced to move the development forward).

For this project, I came up with a better way.

I realised I could simply ask the new user to ssh in, and capture their keys.  To
 distinguish concurrent users, I could issue them a fake username, and ask them to
 `ssh account-setup-for-USERNAME@my.service.com`.  When they do, I can capture their
 keys and automatically associate them with their account.  No platform specific
 commands, no unnecessary messing around in the terminal.

This is possible due to how ssh authentication works:

 * Client sends the username.
 * Server replies: Sure, you can try logging in with keys, or with passwords if you want.
 * Client sends Public Key 1.
 * Server replies: Nope, but you can try other keys or passwords.
 * Client sends Public Key 2.
 * Server replies: ...

That is, the standard ssh client will just send you all the user's public keys.

Note that this isn't ([normally](https://blog.filippo.io/ssh-whoami-filippo-io/))
 considered a security problem; the keys are public, after all, and the server isn't
 leaking any information by saying "nope".

As I was already running a [custom SSH server](https://mina.apache.org/sshd-project/)
 which practically required you to implement authentication yourself anyway, it was a
 simple step to add key capture to the account setup procedure.  I've uploaded a [stripped
 down version to github](https://github.com/FauxFaux/ssh-key-capture) if you want to see
 how it works.  For example,

Start the server:

    server% git clone https://github.com/FauxFaux/ssh-key-capture.git
    server% cd ssh-key-capture
    server% ./gradlew -q run

The user can try and login, but gets rejected (this isn't reqiured):

    john% ssh -p 9422 john@localhost
    Permission denied (publickey).

Server logs from the (unnecessary) failed authentication:

    KeyCapture - john trying to authenticate with RSA MIIBIjANBg...
    KeyCapture - john trying to authenticate with EC MFkwEwYHKoZ...

Tell the server that `john` has signed up, or wants to add keys, or...

    Enter a new user name, or blank to exit: john
    Ask 'john' to ssh to '18a74d9f-5c7d-41d0-8369-bae4aaba9867@...'

John now adds his keys, and hence can login:

    john% ssh -p 9422 18a74d9f-5c7d-41d0-8369-bae4aaba9867@localhost
    Added successfully!  You can now log-in normally.
    Connection to localhost closed.
    
    john% ssh -p 9422 john@localhost
    Hi!  You've successfully authenticated as john
    Bye!
    Connection to localhost closed.

Future work:

 * It could capture all of the user's keys (it currently just captures the first).
 * More meaningful behaviour after the first authenticaiton, or during the admin part of the setup?
 * Some way to do this on top of OpenSSH, or other tools people actually run in the wild.  PAM?

Update: There was some
 [decent discussion on reddit's /r/netsec](https://www.reddit.com/r/netsec/comments/3nhwqi/capturing_users_ssh_keys_directly_from_the/)
 about this post.
