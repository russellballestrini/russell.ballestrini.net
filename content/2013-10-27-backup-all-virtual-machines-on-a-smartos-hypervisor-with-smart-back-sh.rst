Backup all virtual machines on a SmartOS hypervisor with smart-back.sh
######################################################################
:date: 2013-10-27 20:45
:author: Russell Ballestrini
:tags: DevOps, Guide
:slug: backup-all-virtual-machines-on-a-smartos-hypervisor-with-smart-back-sh
:status: published

This post will explain how to create a cronjob to backup of every
virtual machine on a SmartOS hypervisor.

**Create** the following bash script in /opt/smart-back.sh:

::

    #!/usr/bin/bash

    # Backup all virtual machines on a SmartOS hypervisor
    # Author:  russell@ballestrini.net
    # Website: https://russell.ballestrini.net/

    # Backup directory without trailing slash
    backupdir=/opt/backups

    # temp dir where we ZFS send and gzip before moving to backupdir  
    tmpdir=/opt

    svcadm enable autofs

    for VM in `vmadm list -p -o alias,uuid`
      do
        # create an array called VM_PARTS splitting on ':'
        IFS=':' VM_PARTS=($VM)

        # create some helper varibles for alias and uuid
        alias=${VM_PARTS[0]}
        uuid=${VM_PARTS[1]}

        # echo "Backup started for $VM"
        vmadm send $uuid > $tmpdir/$alias

        # echo "Starting $VM"
        vmadm start $uuid

        pbzip2 $tmpdir/$alias

      done 
      
    mv $tmpdir/*.bz2 $backupdir

|

**Create** a cronjob entry to schedule the backups:

::

    crontab -e

::

    2 6 * * 0 /usr/bin/bash /opt/smart-back.sh

|

If I expand on this script much more, I plan to stick it into revision
control.

If you look closely, I have also added a hack to enable autofs 
(``svcadm enable autofs``) which allows me to automount an NFS
share on my remote FreeNAS by setting
``backupdir=/net/[ip-or-fqdn-of-freenas]/mnt/zfs-mirror/backup/vms``.

We have scheduled a backup of each virtual machine on your SmartOS
hypervisor!

If or when the time comes to restore a VM from a backup, use the
following:

::

    # decompress the backup file.
    pbzip2 -d backup-file.bz2
    
    # ingest the backup file into the hypervisor.
    vmadm receive -f /path/to/backup-file

Just make sure the VM doesn't currently exist on the hypervisor.

This strategy is great for complete backups of machines which could be
used during a manual migration, or if corruption happened to the VM and
we wanted to restore to a previous version.
