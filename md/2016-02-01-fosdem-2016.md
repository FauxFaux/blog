title: Fosdem 2016
slug: fosdem-2016
date: 2016-02-01 12:41:28+00:00

I was at [Fosdem 2016](https://fosdem.org/2016/).  Braindump:

 * [Pottering on DNSSEC](https://fosdem.org/2016/schedule/event/systemd/):
 Quick overview of some things Team Systemd is working on, but primarily about
 adding DNSSEC to `systemd-resolvd`.
    * DNSSEC is weird, scary, and doesn't really have any applications
 in the real world; it doesn't enable anything that wasn't already possible.
 Still important and interesting for defence-in-depth.
    * Breaks in interesting cases, e.g. home routers inventing `*.home` or
   `fritz.box`, the latter of which is a real public name now.  Captive portal
   detection (assuming we can't just make those go away).
    * `systemd-resolvd` is a separate process with a client library; DNS resolution
    is too complex to put in libc, even if you aren't interested in in caching, etc.
 * [Contract testing for JUnit](https://fosdem.org/2016/schedule/event/junit_contracts/):
  Some library sugar for instantiating multiple implementations of an interface, and
  running blocks of tests against them.  Automatically running more tests when anything
  returns a class with any interface that's understood.
    * I felt like this could be applied more widely (or perhaps exclusively); if you're
   only testing the external interface, why not add more duck-like interfaces everywhere,
   and test only those?  Speaker disagreed, perhaps because it never happens in practice...
    * Unfortunately, probably only useful if you are actually an SPI provider, or e.g.
   Commons Collections.  This was what was presented, though, so not a big surprise.
    * The idea of testing mock/stub implementations came up.  That's one case where, at
   least, I end up with many alternative implementations of an interface that are supposed
   to test the same.  Also discussed whether `XFAIL` was a good thing, Rubby people suggested
   `WIP` (i.e. must fail or test suite fails) works better.
 * [Frida for closed-source interop testing](https://fosdem.org/2016/schedule/event/closed_source_interop/):
  This was an incredibly ambitious project, talk and demo.  ("We're going to try some live
  demos.  Things are likely to catch fire.  But, don't worry, we're professionals.").
    * Injects the V8 JS VM into arbitrary processes, and interacts with it from a normal JS
   test tool; surprisingly nice API, albeit using some crazy new JS syntaxes.  Roughly:
   `file.js`: `{foo: function() { return JVM.System.currentTimeMillis(); } }` and
   `val api = injectify(pid, 'file.js'); console.log(api.foo());`.
    * Great bindings for all kinds of language runtimes and UI toolkits, to enable messing with
   them, and all methods are overridable in-place, i.e. you can totally replace the `read`
   syscall, or the iOS `get me a url` method.  Lots of work on inline hooking and portable
   and safe call target rewriting.
    * Live demo of messing with Spotify's ability to fetch URLs... on an iPhone...  over the network.
   "System dialog popped up?  Oh, we'll just inject Frida into the System UI too...".
 * [USBGuard](https://fosdem.org/2016/schedule/event/usbguard/):
   People have turned off the maddest types of USB attack (e.g. autorun), but there's still
   lots of ways to get a computer to do something bad with an unexpected (modified) USB stick;
   generate keypresses and mouse movements, even a new network adaptor that may be chosen to send
   traffic to.
    * Ask the user if they expect to see a new USB device at all, and whether they think it should
   have these device classes (e.g. "can be a keyboard").  Can only reject or accept as a whole;
   kernel limitation.  UX WIP.
    * Potential for read-only devices; filter any data being exfiltrated at all from a USB stick,
   but still allow reading from them?  Early boot, maybe?  Weird trust model.  Not convinced you
   could mount a typical FS with USB-protocol level filtering of writes.
    * Mentioned device signing; no current way to do identity for devices, so everything is doomed
   if you have *any* keyboards.  Also mentioned CVEs in USB drivers, including
   [cdc-wdm](http://lxr.free-electrons.com/source/drivers/usb/class/cdc-wdm.c), which I reviewed
   during the talk and oh god oh no `goto` abuse.
 * [C safety, and whole-system ASAN](https://fosdem.org/2016/schedule/event/csafecode/):
   Hanno decided he didn't want his computer to work at all, so has been trying to make it start
   with ASAN in enforce mode on for *everything*.  Complex due to ASAN loading order/dependencies,
   and the fact that `gcc` and `libc` have to be excluded because they're the things being
   overridden.
    * Everything breaks (no real surprise there).  bash, coreutils, man, perl, syslog, screen, nano.
   Like with [Fuzzing Project](https://fuzzing-project.org/), people aren't really interested
   in fixing bugs they consider theoretical, but are really real on angry C compilers, or in the
   future.  Custom allocators have to be disabled, which is widely but not totally supported.
    * Are there times where you might want ASAN on in production?  Would it increase security
   (trading off outages), or would it add more vulnerabilities, due to huge attack surface?  ~2x
   slowdown at the moment, which is probably irrelevant.
    * Claimed ASLR is off by default in typical Linux distros; I believe Debian's `hardening-wrapper`
   enables this, but [Lintian reports poor coverage](https://lintian.debian.org/tags/hardening-no-relro.html),
   so maybe a reasonable claim.
 * [SSL management](https://fosdem.org/2016/schedule/event/sslmanagement/):
   Even in 2014, when Heartbleed happened, Facebook had not really got control of what was running
   in their infrastructure.  Public terminators were fine, but everything uses SSL.  Even CAs
   couldn't cope with reissue rate, even if you could find your certs.  Started IDSing themselves
   to try and find missed SSL services.
    * Generally, interesting discussion of why technical debt accumulates, especially in infra.
   Mergers and legacy make keeping track of everything hard.  No planning for things that seem
   like they'll never happen.  No real definition of ownership; alerts pointed to now-empty mailing
   lists, or to people who have left (this sounds very familiar).  That service you can't turn off
   but nobody knows why.
    * Some cool options.  Lots of ways to coordinate and monitor SSL (now), e.g. [Lemur](https://github.com/Netflix/lemur).
   EC certs are a real thing you can use on the public internet (instead of just me on my private
   internet), although I bet it needs Facebook's cert switching middleware.  HPKP can do report-only.
    * Common SSL fails that aren't publicly diagnosed right now: Ticket encryption with long-life keys
   (bad), lack of OCSP stapling and software to support that.
 * [Flight flow control](https://fosdem.org/2016/schedule/event/ada_optimizing/):
   Europe-wide flight control is complex, lots of scarce resources: runways, physical sky, radar codes,
   radio frequencies.  Very large, dynamic, safety-critical optimisation problem.
    * 35k flights/day.  4k available radar codes to identify planes.  Uh oh.  Also, route planning much
   more computationally expensive in 4D.  Can change routes, delay flights, but also rearrange ATC for
   better capacity of bits of the sky.
    * Massive redundancy to avoid total downtime; multiple copies of the live system, archived plans
   stored so they can roll-back a few minutes, then an independently engineered fall-back for some
   level of capacity if live fails due to data, then tools to help humans do it, and properly
   maintained capacity information for when nobody is contactable at all.
    * Explained optimising a specific problem in Ada; no actual Ada tooling so stuck with binary
   analysis (e.g. `perf`, `top`, ..).  Built own parallelisation and pipelining as there's no
   tool or library support.  Ada codebase and live system important, but too complex to change,
   so push new work into copies of it on the client.  Still have concurrency bugs due to shared state.
 * [glusterfs](https://fosdem.org/2016/schedule/event/gluster_roadmap/) and
 [beyond glusterfs](https://fosdem.org/2016/schedule/event/linux_petascale_storage/):
   Large-scale Hadoop alternative, more focused on reliability, and NFS/CIFS behaviour than custom
   API, but also offer [object storage](http://docs.openstack.org/developer/swift/) and others.
    * Checksumming considered too slow, so done out of band (but actually likely to catch problems),
   people don't actually want errors to block their reads (?!?).  Lots more things are part of a
   distributed system than I would have expected, e.g. they're thinking of adding support for
   geographical clustering, so you can ensure parts of your data are in different DCs, or that
   there is a copy near Australia (dammit).
    * The idea that filesystems have to be in kernel mode is outdated; real perf is from e.g.
   user-mode networking stacks.  Significantly lower development costs in user-mode means FSes
   are *typically* faster in user space, as the devs have spent more time (with more tooling
   modifiers) getting them to work properly: real speedups are algorithmical and not code.
    * Went on to claim that Python is fine, don't even need C or zero-copy (but do need to limit
   copies), as everything fun is offloaded anyway.  Ships binaries with debug symbols (1-5%
   slowdown) as it's totally irrelevant. Team built out of non-FS, non-C people writing C.
   They're good enough to know what not to screw up.
    * Persistent memory is coming (2TB of storage between DRAM and SSD speed), and cache
   people are behind.  [NFS-Ganesha](https://github.com/nfs-ganesha/nfs-ganesha) should be
   your API in all cases.
 * [What even are Distros?](https://fosdem.org/2016/schedule/event/distros_rethinking/):
   Distros aren't working, can't support things for 6mo, 5y, 10y or whatever as upstream and
   devs hate you.  Tried to build hierarchies of stable -> more frequently updated, but failed;
   build deps at the lower levels; packaging tools keep changing; no agreement on promotion;
   upstreams hate you.
    * PPAs?  They had invented yet another PPA host, and they're all still bad.  Packaging is
   so hard to use, especially as non-upstreams don't use it enough to remember how to use it.
    * Components/Modules?  Larger granularity installable which doesn't expose what it's made
   out of, allowing distros to mess it up inside?  Is this PaaS, is this Docker?  It really
   feels like it's not, and it's really not where I want to go.
    * Is containerisation the only way to protect users from badly packaged software?  Do we
   want to keep things alive for ten years?  I have been thinking about the questions this
   talk had for a while, but need a serious discussion before I can form opinions.
 * [Reproducible Builds](https://reproducible-builds.org/): Definitely another post some time.
    * Interesting questions about why things are blacklisted, and whether the aim is to support
   everything.  Yes.  Everything.  EVERYTHING.
 * [Postgres buffer manager](https://fosdem.org/2016/schedule/event/postgresql_improving_postgres_buffer_manager/):
   Explaining the internals of the shared buffers data structure, how it's aged poorly, what
   can be done to fix it up, or what it should be replaced with.  Someone actually doing proper
   CS data-structures, and interested in cache friendliness, but also tunability, portability,
   future-proofing, etc.
    * `shared_buffers` tuning advice (with the usual caveat that it's based on workload);
   basically "bigger is normally always better, but definitely worth checking you aren't
   screwing yourself".
    * Also talked about general IO tuning on Linux, e.g. `dirty_writeback`, which a surprising
   number of people didn't seem to have heard of.  Setting it to block earlier reduces maximum
   latency; numbers as small as 10MB were considered.
 * [Knot DNS resolver](https://fosdem.org/2016/schedule/event/knot_dns/):
   DNS resolvers get to do a surprising number of things, and some people run them at massive scale.
   Centralising caching on e.g. Redis is worthwhile sometimes.  Scriptable in Lua so you can get
   it to do whatever you feel like at the time (woo!).
    * Implements some interesting things: [Happy Eyeballs](https://en.wikipedia.org/wiki/Happy_Eyeballs),
   [QNAME minimisation](https://tools.ietf.org/html/draft-ietf-dnsop-qname-minimisation-09), built-in
   serving of pretty monitoring.  Some optimisations can break CDNs (possibly around skipping recursive
   resolving due to caching), didn't really follow.
 * [Prometheus monitoring](https://github.com/prometheus/prometheus):
   A monitoring tool.  Still unable to understand why people are so much more excited about it than
   anything else.  Efficient logging and powerful querying.  Clusterable through alert filtering.
    * "Pull" monitoring, i.e. multiple nodes fetch data from production, which is apparently contentious.
   I am concerned about credentials for machine monitoring, but the daemon is probably not that much worse.
 * [htop porting](https://fosdem.org/2016/schedule/event/htop/):
   Trying to convince the community to help you port to other platforms is hard.  If you don't,
   they'll fork, and people will be running an awful broken fork for years (years).
   Eventually resolved by adding the ability to port to BSD, then letting others do the OSX port.
 * [API design for slow things](https://fosdem.org/2016/schedule/event/design_linux_kernel_api/):
   Adding APIs to the kernel is hard.  Can't change anything ever.  Can't optimise for the sensible
   case because people will misuse it and you can't change it.  Can't "reduce" compile-time settings
   as *nobody* builds a kernel to run an app.
    * Lots of things in Linux get broken, or just never work to start with, due to poor test coverage,
   maybe the actually funded [kselftest](https://www.kernel.org/doc/Documentation/kselftest.txt) will
   help, but people can help themselves by making real apps before submitting apis, or
   at least real documentation.  e.g. `recvmsg` timeout was broken on release.  `timerfd` tested by
   manpage.
    * API versioning is hard when you can't turn anything off. `epoll_create1`, `renameat2`, `dup3`.
   `ioctl`, `prctl`, `netlink`, aren't a solution, but maybe `seccomp` is.  Capabilities are hard; 1/3rd of
   things just check SYS_ADMIN (which is ~= root).  Big argument afterwards about whether versioning
   can ever work, and what deprecation means.  Even worse for this than for Java, where this normally
   comes up.
 * Took a break to talk to some Go people about how awful their development process is.  CI is
 broken, packaging is broken, builds across people's machines are broken.  Everything depends on github
 and maybe this is a problem.
 * [Fosdem infra review](https://fosdem.org/2016/schedule/event/fosdem_infrastructure_review/):
   Hardware has caught up with demand, now they're just having fun with networking, provisioning
   and monitoring.  Some plans to make the conference portable, so others can clone it (literally).
   Video was still bad but who knows.  Transcoding is still awfully slow.
    * Fosdem get a very large temporary ipv4 assignment from IANA.  `/17`?  Wow.  Maybe being phased
   out as ipv6 and nat64 kind of works in the real world now.
    * Argument about why they could detect how many devices there were, before we realised mac
   hiding on mobile is probably disabled when you actually connect, because that's how people bill.
 * [HOT OSM tasking](https://fosdem.org/2016/schedule/event/keynote_crisis_response_through_open_mapping/):
   Volunteers digitising satellite photos of disaster zones, and ways to allocate and parallelise
   that.  Surprisingly fast; 250 volunteers did a 250k person city in five days, getting 90k buildings.
    * Additionally, provide mapping for communities that aren't currently covered, and train locals to
   annotate with resources like hospitals and water-flow information.
    * Interesting that sometimes they want to prioritise for "just roads", allowing faster mapping.
   Computer vision is still unbelievably useless; claiming 75% success rate at best on identifying if
   people even live in an area.
    * Lots of ethical concerns; will terror or war occur because there's maps?  Sometimes they ask residents
   and they're almost universally in favour of mapping.  Sometimes drones are donated to get better
   imagery, and residents jump on it.
 * Stats talk.  Lots of data gathered; beer sold, injuries fixed, network usage and locations.  Mostly mobile
   (of which, mostly android).  Non-mobile was actually dominated by OSX, with Linux a close second.  Ouch.

Take-aways: We're still bad at software, and at distros, and at safety, and at shared codebases.

Predictions: Something has to happen on distros, but I think people will run our current distros
(without containers for every app) for a *long* time.

