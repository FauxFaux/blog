title: HTTP2 slowed my site down!
slug: http2-slowdown
date: 2016-10-11 18:50:28+10:00

At work, we have a page which asynchronously fetches information for a dashboard.
This involves making many small [requests back to the proxy](/2015/04/violating-cors-nginx/),
which is exactly the kind of thing that's supposed to be faster under HTTP2.

However, when we enabled HTTP2, the page went from loading in around two seconds, to
taking over twenty seconds. This is bad. For a long time, I thought there was a bug in
`nginx`'s HTTP2 code, or in Chrome (and Firefox, and Edge..). The page visibly loads in blocks,
with exactly five second pauses between the blocks.

The `nginx` config is simply:

    resolver 8.8.4.4;
    location ~ /proxy/(.*)$ {
      proxy_pass https://$1/some/thing;
    }

.. where `8.8.4.4` is [Google Public DNS](https://developers.google.com/speed/public-dns/).

---

It turns out that the problem isn't with HTTP2 at all. What's happening is that `nginx`
is processing the requests successfully, and generating DNS lookups. It's sending these on
to Google, and the first few are getting processed; the rest are being dropped. I don't know
if this is due to the network (it's UDP, after all), or as Google think it's attack traffic.
The remainder of the requests are retried by `nginx`'s custom DNS resolver after 5s, and another
batch get processed.

So, why is this happening under HTTP2? Under http/1.1, the browser can't deliver requests
quickly enough to trigger this flood protection. HTTP2 has sped it up to the point that
there's a problem. Woo? On `localhost`, a [custom client](https://github.com/FauxFaux/http2dns)
can actually generate requests quickly enough, even over http/1.1.

`nginx` recommend not using their custom DNS resolver over the internet, and I can understand why;
I've had trouble with it before. To test, I deployed `dnsmasq` between `nginx` and Google:

    dnsmasq -p 1337 -d -S 8.8.4.4 --resolv-file=/dev/null

`dnsmasq` generates identical (as far as I can see) traffic, and is only slightly slower
(52 packets in 11ms, vs. 9ms), but I am unable to catch it getting rate limited. On production,
a much smaller machine than the one I'm testing, `dnsmasq` is significantly slower (100+ms),
so it makes sense that it wouldn't trigger rate limiting. `dnsmasq` does have `--dns-forward-max=`
(default `150`), so there's a nice way out there.

---

In summary: When deploying HTTP2, or any upgrades, be aware of rate limits in your, or other
people's, systems, that you may now be able to trigger.

