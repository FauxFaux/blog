title: Violating CORS with just nginx
slug: violating-cors-nginx
date: 2015-04-10 22:36:41+01:00

I have come across a number of situations where I "want" to write an application mostly in Javascript,
but it needs to access a couple of resources from other people's websites, which would be blocked by CORS.
Previously, at this point, I'd have either given up and written the page in PHP, or at least had a PHP
script somewhere doing the fetch and returning the content. Looking around, I can find many examples of
both; none pretty.

It turns out, however, that PHP is hard to host generally, it's slow, it frequently has security issues,
and isn't deployed anywhere fun... for example, on your CDN nodes.  Rightly so.

You can solve this problem using (regex)
[location](http://nginx.org/en/docs/http/ngx_http_core_module.html#location)s and
[proxy_pass](http://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_pass).
For example, let's say we want our dynamic webpage to request something from `api.micro.mug`:

    location = /viral {
        proxy_pass https://api.micro.mug/3/gallery/hot/viral/0.json;
    }

Done!  Our client app (served from the same server block, as `index.html`), can now...

    $.getJSON('viral', function(data) {
        ....

.. at will (or manually, if you hate libraries).

You have full control over the connection, so you can add headers.  For example, you might want to add
a required header with [proxy_set_header](http://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_set_header):

    proxy_set_header Neutralization 'ChitDoI abcdef0123456'

You can take this further by accepting information from the client, as path parameters.  You may have
a monitoring page for `example.com`, which wants to check the /status on various `foo.example.com`s.

    location ~ /status/([a-z0-9.-]+\.example\.com)$ {
        proxy_pass https://$1/api/status;
        proxy_connect_timeout 2s;
        proxy_read_timeout 2s;
    }

The regex here is slight paranoia; maybe you could accept `.+`?  Who knows
[what problems](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-0235) that could cause.

The client is also simple, again, with libraries:

    $.ajax('status/foo.example.com')
        .done(function() { $('#foo').text('ok'); })
        .fail(function(xhr) { $('#foo').text(xhr.status); });

... or whatever.

As I mentioned previously, this can be *directly on* the CDN or load balancer nodes,
and is static content.  This makes it very likely that the status page will be up.

