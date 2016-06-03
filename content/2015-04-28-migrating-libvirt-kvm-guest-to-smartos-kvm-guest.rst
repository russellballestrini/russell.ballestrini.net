Migrating libvirt KVM guest to SmartOS KVM guest
################################################
:date: 2015-04-28 22:17
:author: Russell Ballestrini
:tags: DevOps, Guide
:slug: migrating-libvirt-kvm-guest-to-smartos-kvm-guest
:status: published
:summary:
  Stop worrying and replace your Linux hypervisor with SmartOS.

The following tutorial documents how to migrate a libvirt/KVM guest from
Ubuntu to SmartOS.

| akuma:
|  Ubuntu Hypervisor

| guy:
|  SmartOS Hypervisor

| sagat:
|  guest to migrate

These commands were run on akuma:

::

    WORKDIR=/KVMROOT/migrate
    sudo mkdir $WORKDIR
    cd $WORKDIR

    # this tool simply stops and tarballs up the qcow and xml for libvirt KVM guest.
    sudo /usr/local/bin/virt-back --path=$WORKDIR --backup sagat

    sudo tar -xzvf sagat.tar.gz

    sudo qemu-img convert -O raw sagat.qcow2 sagat.raw
    sudo qemu-img convert -O raw sagat-var.qcow2 sagat-var.raw

    scp sagat*.raw root@guy:/opt/tmp

These commands were run on guy:

Create the following file on guy - setup-ubuntu-sagat.json:

::

    {
      "brand": "kvm",
      "resolvers": [
        "192.168.1.22",
        "8.8.4.4"
      ],
      "ram": "4096",
      "vcpus": "4",
      "alias": "sagat",
      "hostname": "sagat",
      "nics": [
        {
          "nic_tag": "admin",
          "ip": "192.168.1.50",
          "netmask": "255.255.255.0",
          "gateway": "192.168.1.254",
          "model": "virtio",
          "primary": true
        }
      ],
      "disks": [
        {
          "boot": true,
          "model": "virtio",
          "size": 10240
        },
        {
          "model": "virtio",
          "size": 20480
        }
      ]
    }

We then create a new KVM guest on guy:

::

    [root@guy /opt/setup-jsons]# vmadm create -f setup-ubuntu-sagat.json 
    Successfully created VM aa0f603c-9572-4cb0-b96f-4c79eb431223

List out the virtual block devices on the new KVM guest:

::

    [root@guy /opt/setup-jsons]# vmadm info aa0f603c-9572-4cb0-b96f-4c79eb431223 block
    {
      "block": [
        {
          "device": "virtio0",
          "locked": false,
          "removable": false,
          "inserted": {
            "ro": false,
            "drv": "raw",
            "encrypted": false,
            "file": "/dev/zvol/rdsk/zones/aa0f603c-9572-4cb0-b96f-4c79eb431223-disk0"
          },
          "type": "hd"
        },
        {
          "device": "virtio1",
          "locked": false,
          "removable": false,
          "inserted": {
            "ro": false,
            "drv": "raw",
            "encrypted": false,
            "file": "/dev/zvol/rdsk/zones/aa0f603c-9572-4cb0-b96f-4c79eb431223-disk1"
          },
          "type": "hd"
        }
      ]
    }

Stop the new guest, it needs to be off for the restore.

::

    [root@guy /opt/setup-jsons]# vmadm stop aa0f603c-9572-4cb0-b96f-4c79eb431223
    Successfully completed stop for VM aa0f603c-9572-4cb0-b96f-4c79eb431223

.. raw:: html

   </p>

Use dd to:

-  write sagat.raw to disk0
-  write sagat-var.raw to disk1

::

    dd if=sagat.raw of=/dev/zvol/rdsk/zones/aa0f603c-9572-4cb0-b96f-4c79eb431223-disk0 bs=1M
    dd if=sagat-var.raw of=/dev/zvol/rdsk/zones/aa0f603c-9572-4cb0-b96f-4c79eb431223-disk1 bs=1M

Lastly start the new guest up, and check it out:

::

    vmadm start aa0f603c-9572-4cb0-b96f-4c79eb431223
