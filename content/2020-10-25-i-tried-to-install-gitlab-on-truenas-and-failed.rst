I tried to install GitLab on TrueNAS and failed
################################################################

:author: Russell Ballestrini
:slug: i-tried-to-install-gitlab-on-truenas-and-failed
:date: 2020-10-25 14:28
:tags: Code, DevOps
:status: published

Ok, so a month ago I changed employment and the new company uses GitLab exclusively for centralized code version control system.

This is my first time using GitLab and my first projects was integrating a ``dou/cloudmapper`` with a GitLab runner on a schedule.

After a couple weeks I've learned how GitLab runners work and wrote a wrapper to run cloudmapper concurrently so that each accounts is collected in parallel (the basic logic is running docker exec on a custom entrypoint and then backgrounds the task in a bash loop over each account configured in cloudmapper's config file)

GitLab runners are awesome.

I've used CircleCI for the better part of 3 years, having lifted the better part of 60 code bases from an internal app called conveyor to CircleCI 1.0 and performing CircleCI 2.0 conversions at Remind.

CircleCI 2.0 is awesome...

But GitLab runners are not black box which makes them so powerful.

Granted not all organizations need or even want this much power, but I'm a nerd and I want it, so I decided I also want to run GitLab at home.

My first thought was to try to just run GitLab on a VM on my ``SmartOS`` host called ``mbison``, but that's a bit janky of a setup since it's an ``T420 ThinkPad`` after all. Also I learned the recommended minimum memory footprint of ``GitLab`` is ``4G`` so a ``4 of 16G`` allocation without even discussing a separate KVM for the runner. It feels weird that a single rails application would need _that_ much memory.

Anyways, I have a FreeNAS ``FreeNAS-11.3-U5`` host at my house with ``46G`` of memory and a bunch of idle cores, So I wondered if they have a plug-in for GitLab... I'm sure they do by now.

After a bit of research I found that ``iXsystems`` renamed the ``FreeNAS`` codebase to ``TrueNAS`` and version ``TrueNAS-12.0-RELEASE`` has a GitLab plugin! Sweet!

Thankfully I remembered that back in 2019 I replaced my FreeNAS USB boot device with an SSD so it should be a safe operation to attempt a TrueNAS upgrade on a Saturday morning since I'd have the weekend to try to recover if things went sour. Fun side story, I ran into trouble last year trying to upgrade FreeNAS train because I didn't have room for the upgrade because I was using a USB drive as the boot disk and it had like 5 previous version on the 8G file system.

The kind people in the freenode ``#FreeNAS`` channel helped me switch back to an older version using SSH and told me I should not boot from a USB drive which was a thing I picked up from back in the FreeNAS 6 or 7 days. Boy were they correct, I moved the OS to an SSD and the server boots _WAY_ faster now, plus I have more capacity to try new versions.

Anyways, here is a fun command to determine when a ZFS pool was created, I used this to get the exact date and time I moved from USB to SSD for this blog post:

.. code-block:: bash

 root@guile[~]# zpool history -i freenas-boot | grep "create pool"

 2019-11-12.13:00:30 [txg:5] create pool version 28; software version 5000/5; uts  11.2-STABLE 1102500 amd64

So weilding this confidence, I switched FreeNAS trains in the UI and clicked upgrade, following the prompts to create a backup of my NAS config.
After the server rebooted, FreeNAS was now TrueNAS. I logged into the web UI to look around and make sure my data was still there.

Everything seemed fine, so I went to the plug-in tab and attempted to install GitLab. That failed with an error.

So I decided oh well, I'll try spinning up an Ubuntu VM on the ``TrueNAS`` box, apparently ``FreeBSD`` uses ``bhyve`` for that.

Attempting to start the VM does nothing in the UI, it appears like it will start but then the page refreshes and the VM is stopped.

I did eventually find the error message, by running 

.. code-block:: bash

 tail -f /var/log/libvirt/*/*

.. code-block:: bash

 /usr/sbin/bhyve -c cpus=1,sockets=1,cores=1,threads=1 -m 4096 -A -w -H -s 0:0,hostbridge -l bootrom,/usr/local/share/uefi-firmware/BHYVE_UEFI.fd -s 3:0,ahci,cd:/mnt/downloads/iso/ubuntu-20.04.1-live-server-amd64.iso -s 30:0,xhci,tablet -s 2:0,ahci -s 5:0,virtio-net,tap1,mac=00:a0:98:4f:98:13 -s 4:0,virtio-blk,/dev/zvol/downloads/gitlab-vcrg2z -s 31,lpc -l com1,/dev/nmdm1A -s 29,fbuf,vncserver,tcp=0.0.0.0:48009,w=1024,h=768 1_gitlab
 25/10/2020 17:49:58 Listening for VNC connections on TCP port 48009
 25/10/2020 17:49:58 Listening for VNC connections on TCP6 port 48009
 ROM boot failed: unrestricted guest capability not available
 fbuf frame buffer base: 0x941e00000 [sz 16777216]  

The important part is:

.. code-block:: text

 ROM boot failed: unrestricted guest capability not available


It seems if you ask ``bhyve`` to use the UEFI bootloader it will require UG support in the Intel CPU : (

I attempted to switch to the grub bootloader but in that case I get the following error message:

.. code-block:: text

  File "/usr/local/lib/python3.8/site-packages/middlewared/plugins/vm.py", line 1414, in do_update
    raise verrors
  middlewared.service_exception.ValidationErrors: [EINVAL] vm_update.devices.3.dtype: VNC only works with UEFI bootloader.


and the ``TrueNAS`` UI does not let you disable VNC on VMs at this point...

Another limitation of a missing UG CPU flag is ``bhyve`` may only allocate 1 core, and 1 vcpu to a VM.

Anyways I'm out of luck, I can't use the plugin which uses jails due to a strange error and no other hints as to the issue and ``byhve`` / ``TrueNAS`` not supporting VMs for my CPU...

**UPDATE** I recently upgraded my TrueNAS server hardware to an old ``Dell PowerEdge R720 R720xd`` with two Intel(R) Xeon(R) CPU E5-2670 @ 2.60GHz each with 8 Physical Cores and 128G of ECC Memory! Booyah!

I was able to flash the included Dell H710 Mini RAID card into IT mode for ZFS support using the awesome guides and tools found here: https://fohdeesha.com/docs/perc/

I now have GitLab running on a ``byhve`` instance and also a dedicated runner instance. It's working great and really fun to have this extremely powerful gear in my home lab!
