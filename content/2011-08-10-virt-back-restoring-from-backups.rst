virt-back: restoring from backups
#################################
:date: 2011-08-10 23:20
:author: Russell Ballestrini
:tags: Code, DevOps, Guide, Project
:slug: virt-back-restoring-from-backups
:status: published

**In a perfect world we should create backups but never need them.**
Although this statement holds truth, creating guest backups provides
many more benefits.

The most common reasons system administrators restore from a virt-back
guest backup:

-  recovering from data corruption
-  recovering deleted files
-  recovering from a virus infection
-  recovering from a compromised server
-  backing out a failed change
-  rolling back to a previous state
-  testing disaster recovery plans
-  cloning a server
-  building test environments

During this article we will cover how to restore a system from a
virt-back guest backup. This article will not cover how to restore a VM
host server.

**Virt-back guest restore procedure**

In this guide our guest mbison has failed with a major corruption and we
would like to restore from our backups. We have our running production
guest images in /KVMROOT and our virt-back guest backups in /KVMBACK. We
will be restoring the backup on the same hypervisor.

**Overview:**

#. Ensure the guest is shut off.
#. move the bad image file out of the way
#. untar the virt-back backup into place
#. power up the guest

**Detailed Procedure:**

#. Verify the guest is shut off by running:

   ::

       virt-back --info-all
           

#. We noticed that mbison was still running so we invoked:

   ::

       virt-back --shutdown mbison
           

#. Move the corrupted image file out of the way:

   ::

       mv /KVMROOT/mbison.img /KVMROOT/mbison.img.NFG
           

#. Unzip and unarchive the backup using the following command:

   ::

       sudo tar -xzvf /KVMBACK/mbison.tar.gz -C /KVMROOT --strip 1
           

#. When the untar completes, start the guest:

   ::

       virt-back --create mbison
           

#. Connect to the guest over SSH and verify that all required services
   and applications start. Determine if the restore was successful.

| 

**Restore guest backup on new hypervisor:**

| 

The details in this section were adapted from a tutorial given by 
`Fabian Rodriguez <http://fabianrodriguez.com/>`_.

| 

#. Re-create any bridge network interfaces on new hypervisor
   (/etc/network/interfaces for Debian)

#. Adjust mbison.xml if needed (for example if you are changing paths)

::

    sudo mkdir /KVMROOT
    sudo tar -xvzf mbison.tar.gz -C /KVMROOT --strip 1
    virsh create /KVMROOT/mbison.xml

**Note:** We use virsh create instead of virt-back create. While both
commands start guest DOMs, virsh create will also register the DOM into
the hypervisor.

| 
