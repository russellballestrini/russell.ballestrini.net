Set DNS resolver options
=========================================================

:author: Russell Ballestrini
:slug: set-dns-resolver-options
:date: 2015-12-16 10:17
:tags: Operations
:status: published

I desire the following options in `/etc/resolv.conf`:

.. code-block:: bash

 rotate timeout:1 attempts:1

Ubuntu or Debian
----------------

For Ubuntu or Debian based systems, place the options in
`/etc/resolvconf/resolv.conf.d/base`:

.. code-block:: bash

 rotate timeout:1 attempts:1

These options merge with the options from DHCP and end up in `/etc/resolv.conf`.

Then restart the host, or at least networking.

Redhat or Centos or Fedora
--------------------------

For Redhat, Centos or Fedora, add the following to `/etc/sysconfig/network`:

.. code-block:: bash

 RES_OPTIONS="rotate timeout:1 attempts:1"

Then restart the host, or at least networking.
