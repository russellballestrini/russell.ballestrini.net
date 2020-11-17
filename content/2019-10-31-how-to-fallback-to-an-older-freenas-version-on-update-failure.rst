How to fallback to an older FreeNAS version on update failure
################################################################

:author: Russell Ballestrini
:slug: how-to-fallback-to-an-older-freenas-version-on-update-failure
:date: 2019-10-31 17:06
:tags: Code, DevOps
:status: published

try to log in as root locally, I needed to press ``ctrl-alt-f7`` to get to a log in prompt.

Once logged in as root, I used the ``beadm`` command.

For example, ``beadm list`` and ``beadm activate <old-version>``.

Finally ``reboot``.

I followed this process and then got my FreeNAS server to boot again.

From the GUI I was able to create myself a config backup.

I then burned a new FreeNAS CD and used that to install a fresh new install on my USB drive and then once that booted I used the GUI to restore my config.
