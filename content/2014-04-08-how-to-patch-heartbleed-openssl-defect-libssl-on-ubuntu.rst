How to patch Heartbleed OpenSSL defect (libssl) on Ubuntu 
##########################################################
:date: 2014-04-08 22:42
:author: Russell Ballestrini
:tags: Guide, Security
:slug: how-to-patch-heartbleed-openssl-defect-libssl-on-ubuntu
:status: published

Lots of people claim that you need to upgrade openssl package, but this
will not fix the issue.

| The issue is not the openssl package, it is one of the libraries that
  the package relies on (libssl).
|  https://www.ubuntu.com/usn/usn-2165-1/

The output of ``openssl version -a`` command should have a ``built on``
date older then ``Mon Apr  7 20:33:29 UTC 2014``. After patching openssl
we still see the vulnerable date:

::

    openssl version -a | egrep "OpenSSL|built"
    OpenSSL 1.0.1 14 Mar 2012
    built on: Tue Aug 21 05:18:48 UTC 2012

Now we patch ``libssl1.0.0``:

::

    sudo apt-get update
    sudo apt-get install libssl1.0.0

Notice the patched ``built on`` date:

::

    openssl version -a | egrep "OpenSSL|built"
    OpenSSL 1.0.1 14 Mar 2012
    built on: Mon Apr  7 20:33:29 UTC 2014

In my case I used a Salt remote execution to patch, verify, and restart
nginx on all of my 14 hosts:

::

    sudo salt '*' cmd.run 'apt-get update'

::

    sudo salt '*' cmd.run 'apt-get -y install libssl1.0.0'

::

    sudo salt '*' cmd.run 'openssl version -a | egrep "OpenSSL|built"'

::

    sudo salt '*' service.restart nginx

.. raw:: html

   <p>
   <center>

| 
|  |image0|
|  xkcd 1353

.. raw:: html

   </center>
   </p>

.. |image0| image:: https://imgs.xkcd.com/comics/heartbleed.png
