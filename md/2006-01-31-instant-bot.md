title: Instant Bot
slug: instant-bot
date: 2006-01-31 01:43:45+00:00

I was bored, result: Low-byte-count lua-bot, to meet the specs on <a href="http://www.we11er.co.uk/ircbots/">http://www.we11er.co.uk/ircbots/</a>.

This could be made shorter by removing quite a lot of the whitespace, including, possibly the \rs. It could be made even shorter by shortening the variables names. It could be made faster by nesting the if-end blocks. It could (quickly) be made more flexible by not hardcoding the command and it's response.

Possibly the easiest way to make it shorter would be to export some of the code to a library (such as perl's MNet::IRC), which is, imho, cheating.

Etc.

Anyway, the code:
<code>
socket=require("socket")
tcp=socket.tcp()
tcp:connect("irc.uwcs.co.uk", 6667)
tcp:send("USER luabot 8 * :Faux's LuaBOT\r\nNICK LuaBOT\r\nPRIVMSG NickServ IDENTIFY password")

while true do
line = tcp:receive()
if line == nil then break end

_,_, pongkey = line:find("^PING(.*)$")
if pongkey ~= nil then tcp:send("PONG" .. pongkey .. "\r\n") end

_,_, code = line:find("^[^ ]+ ([0-9]+) ")
if code == "376" then tcp:send("JOIN #luabot\r\n") end

_,_, channel, args = line:find("^:[^ ]+ [A-Z0-9]+( [^ ]+ ):?!say (.*)$")
if (args ~= nil) then tcp:send("PRIVMSG" .. channel .. ":" .. args .. "\r\n") end
end
</code>

Have fun.