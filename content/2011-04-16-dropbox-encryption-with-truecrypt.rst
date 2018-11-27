Dropbox Encryption with TrueCrypt
#################################
:date: 2011-04-16 12:50
:author: Russell Ballestrini
:tags: Greatest Hits, Opinion, Security
:slug: dropbox-encryption-with-truecrypt
:status: published
:summary:
  The best security acts like an onion.

`Derek Newton <https://dereknewton.com/2011/04/dropbox-authentication-static-host-ids/>`_
recently invoked discussion about insecurities in Dropbox authentication.
In his article he describes how an attacker could exploit Dropbox and gain access to unshared files.
The concerns he raised do appear accurate however we must remember that security is an onion.

|onion|

An onion, like security, has layers to protect its vital parts.
The vital parts are more vulnerable when its security model only possess one layer.
As we add layers to our security model, our system's protection grows exponentially.

In the case of Dropbox, the username and password act as the first
layer. Experts agree that a simple authentication layer will provide
enough protection for nonsensitive data. However when attempting to
protect sensitive data we must pair authorization with encryption.

Generally speaking file systems have maintained a sense of insecurity,
which makes them useful. Not encrypting files on Dropbox is akin to not
encrypting files on a shared PC. Sensitive data should always be
encrypted *regardless* of its location or media. We should treat
sensitive data-at-rest on Dropbox the same way we treat sensitive data
on local, optical or flash disk. *We should encrypt it!*

**So how does a user encrypt their Dropbox?**

My strongly opinionated solution uses TrueCrypt to create an encrypted
volume in the Dropbox directory. Simply treat the Dropbox like a normal
directory, follow the TrueCrypt documentation to build a volume, and
give Dropbox a chance to sync the data. When the sync completes, the
TrueCrypt volume will be mountable on each of your Dropbox enabled
computers.

I have to admit at first I was skeptical, but the software cooperates
surprisingly well and after the initial sync proceeding syncs occur
quickly! I prefer TrueCrypt because it is open source, cross platform,
and free (both in freedom and cost). TrueCrypt also functions and
performs better then any other solution including commercial products
like GuardianEdge or PGP both recently acquired by Symantec.

All security and encryption software should remain open sourced and peer
reviewed to prevent harmful tampering. Commercial software, written in a
black-box vacuum, prevents customers from viewing its code and
procedures. We cannot trust software for security when we cannot view
its source code.

You should follow me on twitter
`here <https://twitter.com/russellbal>`_

.. |onion| image:: /uploads/2011/04/onion.png
