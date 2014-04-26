title: Irssi screening guide.
slug: irssi-screening-guide
date: 2007-12-11 14:31:22+00:00

It's best to do this right first time, although, I'm sure, most people won't read this until their machine is about to go down and they're going to lose all their work. :)

<ol><li><strong>Add all your networks to <a href="http://www.irssi.org/">irssi</a>, pick any random name.</strong>

For instance:

<code>/network add freenode
/network add efnet
</code>

</li><li><strong>Add servers for the networks.</strong>

<code>/server add -network freenode irc.eu.freenode.net
/server add -network efnet irc.efnet.org
/server add -network efnet efnet.port80.se
</code>

</li><li><strong>Add channels to the networks.</strong>

<code>/channel add -auto #irssi freenode
/channel add -auto #defocus freenode
/channel add -auto #lulz efnet
</code>

"-auto" here means to auto-join the channel when connecting to the specified network.

Modified from <a href="http://irssi.org/documentation/tips">http://irssi.org/documentation/tips</a>, this alias will add all your current channels, and auto-join them:

<span style="font-family: monospace">/alias addallchannels script exec foreach my \$channel (Irssi::channels()) { Irssi::command("channel add -auto \$channel->{name} \$channel-&gt;{server}-&gt;{tag} \$channel-&gt;{key}")\;}</span>

</li><li><strong>/layout save</strong>

This makes all the tabs re-appear in the same place when you next load irssi.

</li><li><strong>/save</strong>

Commit all the work done above to disk. If you messed up, just /reload.

</li><li><strong>When you next load irssi...</strong>

<code>/connect freenode
/connect efnet</code>

All of the above mentioned commands have loads of extra options, go read the <span style="font-family: monospace">/help</span>. :)
</li></ol>