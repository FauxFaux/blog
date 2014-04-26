title: Phantom phone-calls
slug: phantom-phone-calls
date: 2006-02-28 20:25:20+00:00

Phantom calls never used to be a problem for me.. adopting a simple "if you don't recognise the number, don't answer it" policy works fine.

This policy, however, is starting to break-down now I've started putting my mobile number on important documents.. things like CVs, not the kind of phone-call you want to miss.

Assuming you're not insistent on answering every phone call, you can just silence it and allow it to ring out, leaving you with the caller's number. You now have a (software-scale) long time to decide whether you want to call this person back.

For instance, I got a call from 01792474700, <a href="http://www.google.com/">Google</a> finds <a href="http://www.3g.co.uk/3GForum/showpost.php?p=187308&postcount=143">a post on 3g's forum</a> suggesting that they're trying to sell me a new phone.

Assuming that I was sitting at a computer with a reasonable speed internet connection I could have found that out while the phone was ringing, and decided not to answer it... a strong negative, attained quickly using only the internet, something you could possibly train a phone to do.

This is, unfortunately, not quite as obvious as it sounds.. it took me two google searches (second attempt was with a space) to find this result, and I'd never heard of 3g's forums before, I have no idea if it's a valid source, if it's a company or an individual with their contact details on the page, etc. You'd have to train your app to work out what context the message was in. This is feasible on PCs, but maybe not in java on current mobile phone processing power in ~3 seconds.

The majority of the calls you receive are unlikely to be strong negatives (when using google as your source, at least), strong positives are unlikely, too. The chance of being rung from the main company reception when being contacted about a job offer is relatively low, it's more likely that you'll be rung from someone's desk, which'll probably have a unique outside line.

The solution? As always, the solution is over-engineering.

Someone with a small volume of technical skill writes a small java app (and possibly some platform specific (ie. windows mobile) variants) that looks at your 'missed calls', ignores all the numbers in your address book and asks you about the numbers. The reply would be something in the range of Private, Unknown, Legitimate and Spam.

<ul>
	<li><strong>Private:</strong> Things only of interest to me. In theory these should be in your address book anyway.</li>
	<li><strong>Unknown:</strong> Numbers that you don't recognise and can't otherwise determine the purpose of, and that you don't feel like chasing up (ie. ringing back).</li>
	<li><strong>Legitimate:</strong> Numbers that you'd never ring, but rang you at your request/with your permission. ie. ring-backs.</li>
	<li><strong>Spam:</strong> Numbers you know to be malicious.
</li></ul>

To answer with either of the final two options you'd need to give a reason/reference/name.

These details are instantly shared with everyone. When querying the service you'd be given the total votes for each category for the given number.

Assuming you require users to have an account to submit, and this account is locked to a uk-mobile-number, the system is relatively hard to abuse.

The technology to do this is available now, the majority of current phones have java and GPRS (the cost would be minimal, the actual amount of data transfered is tiny). As mentioned above, platform-specific versions could have additional features (ie. the windows mobile version adding the votes to the "phone ringing" screen).

If anyone wants to implement this.. be my guest, I'm just too busy right now. If you can think of a way to get any commercial gain from it, good luck to you, at least you'll spend some of the returns advertising the service, it grows in power as it's user-count goes up.