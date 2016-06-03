SmartOS Ubuntu guest, apt-get not working because IPv6
######################################################
:date: 2015-05-09 20:29
:author: Russell Ballestrini
:tags: Guide
:slug: smartos-ubuntu-guest-apt-get-not-working-because-ipv6
:status: published
:summary: My brutal yet simple work around.

Turns out I don't have IPv6 setup properly in my network so when apt
attempts to connect to the Internet it tries IPv6 and fails.

To disable IPv6 on the ubuntu guest, add this to end of /etc/sysctl.conf
and restart the guest:

sudo vim /etc/sysctl.conf:

::

    net.ipv6.conf.all.disable_ipv6 = 1
    net.ipv6.conf.default.disable_ipv6 = 1
    net.ipv6.conf.lo.disable_ipv6 = 1

.. raw:: html

   </p>

This was a hacky work around mostly because although I desire to have
IPv6 working, I desire to get this VM running more...

Thanks for reading, leave comments please.
