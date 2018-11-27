r8168 driver issues after Ubuntu 11.10 upgrade kernel linux 3.0
###############################################################
:date: 2011-10-15 11:15
:author: Russell Ballestrini
:tags: Guide
:tags: guide
:slug: r8168-driver-issues-after-ubuntu-11-10-upgrade-kernel-linux-3-0
:status: published

**I had network issues after upgrading to Ubuntu 11.10 which has the
linux 3.0 kernel.**

I used `this guide <https://www.foxhop.net/realtek-dropping-packets-on-linux-ubuntu-and-fedora>`__
to compile the r8168 driver however, I needed to alter the Makefile to support for linux 3.0 kernel.

Edit *src/Makefile*:

.. code-block:: bash

    #KEXT  := $(shell echo $(KVER) | sed -ne 's/^2\.[567]\..*/k/p')o
    KEXT := $(shell echo $(KVER) | sed -ne 's/^[23]\.[1-9]\..*/k/p')o-

**Now you should follow the rest of the guide.**
