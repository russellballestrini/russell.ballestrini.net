Trouble mounting filesystem on KVM guest after reboot
#####################################################
:date: 2012-03-27 12:04
:author: Russell Ballestrini
:tags: DevOps
:slug: trouble-mounting-filesystem-on-kvm-guest-after-reboot
:status: published

**Just found this out the hard way...**

It looks like the attachment of ``/KVMROOT/guest-dev-app.img`` on
guest-dev did not persist when the KVM host rebooted for patching.

As it appears the ``virsh attach-disk`` command works a lot like the
``mount`` command.

In order to have a disk attachment persist after a reboot, I think we still need to do a ``virsh edit``.

the ``virsh attach-disk`` command is useful because it allows us to
attach disk images to guests without restarting.

**tldr;**

| ``virsh attach-disk`` is to ``mount`` as
|  ``virsh edit`` is to ``vim /etc/fstab``
