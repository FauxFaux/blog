title: LXC, dnsmasq and nginx
slug: lxc-dnsmasq-nginx
date: 2015-04-10 23:23:40+01:00


I have started using [lxc](https://linuxcontainers.org/) extensively.  It's reasonably easy to
[set up lxc on modern Ubuntu](https://help.ubuntu.com/lts/serverguide/lxc.html) (I would argue that
it's easier than Docker), and, with it's ability to run as a limited user, is much more security friendly.
It also gels much better with the way I think about virtualisation and services; I don't want to be locked-in
to a vendor specific way of thinking or deploying.
All my tools and my muscle memory already understand `ssh` and shell.

A (long, oops) while ago, I spent a while diagnosing an interesting issue.  Upon reboot, `nginx` would be
unable to talk to some lxcs, but not others.  This would persist for an annoyingly long time; restarting
things would have very little effect.

It turned out that [dnsmasq](http://www.thekelleys.org.uk/dnsmasq/doc.html), which the Ubuntu setup
uses for dhcp and dns resolution on containers, has some very
[non-ideal behaviour](https://www.mail-archive.com/dnsmasq-discuss@lists.thekelleys.org.uk/msg08793.html)
(spoilers).  Let's have a look.

First, let's try and resolve a machine that's turned off:

    % lxc-ls -f example
    NAME    STATE    IPV4  IPV6  GROUPS  AUTOSTART
    ----------------------------------------------
    example STOPPED  -     -     -       NO

    % dig -t A example @10.0.3.1; dig -t AAAA example @10.0.3.1

    ;; ->>HEADER<<- opcode: QUERY, status: NXDOMAIN, id: 44338
    ;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1

    ;example.               IN  A

    ;; ->>HEADER<<- opcode: QUERY, status: NXDOMAIN, id: 23299
    ;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1

    ;example.                IN  AAAA

Here, we can see `dnsmasq` (listening on `10.0.3.1`) report that the name is not found.  My understanding of
DNS, at the time, was that this was correct.  You asked for a domain that didn't exist, and you get a
`NXDOMAIN`, right?  Turns out this is wrong, but let's go with my original understanding for now.

Let's start the machine, and see that it now has a name:

    % lxc-start -n example
    % lxc-ls -f example
    NAME    STATE    IPV4       IPV6  GROUPS  AUTOSTART
    ---------------------------------------------------
    example RUNNING  10.0.3.52  -     -       NO


    % dig -t A example @10.0.3.1

    ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 56889
    ;; flags: qr aa rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

    ;; ANSWER SECTION:
    example.         0   IN  A   10.0.3.52

Yep!  It's picked up the name, as expected.  Instantly.  No cache timeouts or anything... after all,
the thing managing the DHCP is the same as the thing managing the DNS, so it should all be instant, right?

Let's check `AAAA` again:


    % dig -t AAAA example @10.0.3.1

    ;; ->>HEADER<<- opcode: QUERY, status: NXDOMAIN, id: 5445
    ;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 0, ADDITIONAL: 1

    ;example.                IN  AAAA

Still returning `NXDOMAIN`, as I was expecting.

However, in this state, `nginx` will frequently fail to resolve the name "example".

`nginx` appears to send both a v4 (`A`) and v6 (`AAAA`) request to the configured DNS server simultaneously,
and will act on whichever response it sees first.  Again, I thought this would be okay; it will ignore the
missing v6 record, and continue with the v4 record?

Well, no.  That's not how DNS works.  In DNS, `NXDOMAIN` does not mean "I don't know".  It means "this
definitely doesn't exist".  This is *not* the appropriate error for something which is unknown.  `nginx`
sees the "this definitely doesn't exist" v6 response, and hence ignores the v4 response: it doesn't exist,
so couldn't possibly have a v4 response.

What dnsmasq is doing is forwarding the query for unknown names to the upstream DNS server, which is correctly
informing us that it will *never* give an answer for a single-word name.  dnsmasq is caching this response,
seperately for v6 and v4.  When the lxc boots, and gets its DHCP/DNS name assigned for v4, dnsmasq doesn't
purge the `NXDOMAIN` cache from v6.  I would call this a bug, but the people who understand DNS say otherwise.

The solution is simple: start dnsmasq with `domain-needed`.  This prevents it from forwarding requsets for
single words (like `example`) to the upstream server, so it never sees an `NXDOMAIN`, so you don't get into
this weird state.

On the Ubuntu setup, I am doing this by adding a config file to `/etc/default/lxc-net`:

    LXC_DHCP_CONFILE=/etc/dnsmasq-lxc-overrides.conf

... which itself can contain:

    domain-needed

... in addition to any other settings you might want to set, in the hope that dnsmasq might honour them.

(It won't.  More on that another time.)
