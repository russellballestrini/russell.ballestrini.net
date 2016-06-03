Security Professionals: Yes we appear vulnerable but that attack vector will never happen
#########################################################################################
:date: 2011-08-18 21:36
:author: Russell Ballestrini
:tags: Greatest Hits, Opinion, Security
:slug: security-professionals-yes-we-appear-vulnerable-but-that-attack-vector-will-never-happen
:status: published

In loom of recent internet attacks many institutions have started
scrambling in attempt to "strengthen" their security stance. I agree
that auditing our systems and networks for potential flaws seems
appropriate at this time to prevent getting "caught with our pants
down". Incidentally, I have recently witnessed the introduction of silly
and at times ineffective security adjustments. Many of these new
procedures, rules, and requirements do not make us more secure and worse
instill a false sense of security.

I have previously addressed the fallacy of absolute security. No system
is perfect. A successful security model accomplishes fortitude by
implementing layers like an onion. Through the use of security
layers we can significantly hamper attack vectors and create a safer
complex.

When analyzing a potential attack vector we must first determine our
current location in the security layers. This step serves two purposes:

-  to prevent wasting time and energy on vulnerabilities that don't
   matter at that point in our matrix.
-  to prevent causing outages and unneeded administrator and customer
   heartache.

If a vulnerability requires root or elevated privileges to occur, don't
waste your time resolving it. If the attacker already has root, you have
bigger problems on your hands.

**Some real life examples:**

#. Firewall denying a large range of IP addresses (like entire
   countries). This truly does not increase security, it just creates
   headaches for users. An attacker could just proxy to an open range
   (like a VPS based in a more trusted zone) and gain access from there.
   Also if you decide to ignore this advice and create blanket IP range
   deny rules, DON'T also block services intended to be internet-facing.
   For example, don't block your Internet-facing DNS server if it is
   authoritative for public domains. This will cause countless
   intermittent issues and will be a nightmare to diagnose.
#. Weekly Scanning for Windows viruses on network shares or data at
   rest. This hammers the servers for no reason. If all the desktops run
   antivirus then the file was already scanned when it was downloaded.
   That same file will be scanned again when retrieved on the share. If
   you want the warm and fuzzys of virus scanning network file shares,
   do it once a year. These scans waste time and resources. I feel even
   more outraged when asked to virus scan network shares hosted on UNIX
   servers or NAS.

I speculate that most of these arbitrary ideas come about because the
people in charge make uninformed decisions out of fear without first
consulting the appropriate subject matter experts.

Unfortunately, once a security mandate occurs it seems difficult to
expunge. People are just not willing to put their neck on the chopping
block to banish a legacy or silly mandates; So we end up living with
nonsensical rules and procedures.

|http://xkcd.com/936/|

.. |http://xkcd.com/936/| image:: /uploads/2011/08/password-strength.png
