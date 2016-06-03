autofs /net automount stopped working
#####################################
:date: 2014-12-21 22:38
:author: Russell Ballestrini
:tags: DevOps
:slug: autofs-net-automount-stopped-working
:status: published

So autofs randomly stopped working on one of my Ubuntu hosts (this issue
has been found on Arch as well so its most likely a change upstream). I
found this error in the logs:

::

    attempting to mount entry /net/freenas.example.net
    get_exports: lookup(hosts): exports lookup failed for freenas.example.net
    key "freenas.example.net" not found in map source(s).
    failed to mount /net/freenas.example.net

.. raw:: html

   </p>

The fix was to replace the following line in /etc/auto.master from

::

    /net   -hosts

.. raw:: html

   </p>

to this

::

    /net /etc/auto.net --timeout=60

.. raw:: html

   </p>

and then restart autofs (sudo service autofs restart).
