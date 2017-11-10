virt-back: a python libvirt backup utility for kvm xen virtualbox
#################################################################
:date: 2011-03-20 11:32
:author: Russell Ballestrini
:tags: Code, DevOps, Greatest Hits, Guide, Project
:slug: virt-back-a-python-libvirt-backup-utility-for-kvm-xen-virtualbox
:status: published
:summary:
  backup your virtual maching guests.

|image0|

.. contents::

**Over the weekend I wrote virt-back, a backup utility for QEMU, KVM,
XEN, or Virtualbox guests.**

virt-back is a python application that uses the libvirt API to safely
shutdown, gzip, and restart guests.

The backup process logs to syslog for auditing and virt-back works great
with cron for scheduling outages. Virt-back is in active development so
feel free to give suggestions or branch the source.

virt-back has been placed in the public domain and the latest version
may be downloaded here:

* `https://bitbucket.org/russellballestrini/virt-back <https://bitbucket.org/russellballestrini/virt-back>`_

Installation
============

The fastest way to install virt-back is to use pip or setuptools.

Try `sudo pip install virt-back` or `sudo easy_install virt-back`

Otherwise you may manually install virt-back

::

    sudo wget https://bitbucket.org/russellballestrini/virt-back/raw/tip/virt-back \
    -O  /usr/local/bin/virt-back

::

    sudo chmod 755 /usr/local/bin/virt-back

Test installation
=================

::

    virt-back --help

Example cronjob
===============
::

    15  2  *  *  1  /usr/local/bin/virt-back --quiet --backup sagat
    15  23 *  *  5  /usr/local/bin/virt-back --quiet --backup mbison

Manual
======

::

    russell@host:~$ virt-back --help
    Usage: virt-back [options]
    Options:
      -h, --help            show this help message and exit
      -q, --quiet           prevent output to stdout
      -d, --date            append date to tar filename [default: no date]
      -g, --no-gzip         do not gzip or tar the resulting files
      -a amount, --retention=amount
                            backups to retain [default: 3]
      -p 'PATH', --path='PATH'
                            backup path [default: '/KVMBACK']
      -u 'URI', --uri='URI'
                            optional hypervisor uri

      Actions for info testing:
        These options display info or test a list of guests.

        -i, --info          info/test a list of guests (space delimited dom names)
        --info-all          attempt to show info on ALL guests

      Actions for a list of dom names:
        WARNING:  These options WILL bring down guests!

        -b, --backup        backup a list of guests (space delimited dom names)
        -r, --reboot        reboot a list of guests (space delimited dom names)
        -s, --shutdown      shutdown a list of guests (space delimited dom names)
        -c, --create        start a list of guests (space delimited dom names)

      Actions for all doms:
        WARNING:  These options WILL bring down ALL guests!

        --backup-all        attempt to shutdown, backup, and start ALL guests
        --reboot-all        attempt to shutdown and then start ALL guests
        --shutdown-all      attempt to shutdown ALL guests
        --create-all        attempt to start ALL guests

Restoring
=========

`virt-back: restoring from backups </virt-back-restoring-from-backups/>`_


.. |image0| image:: /uploads/2011/03/virt-back.png


