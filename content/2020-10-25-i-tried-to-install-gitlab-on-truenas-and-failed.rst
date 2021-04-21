I tried to install GitLab on TrueNAS and failed
################################################################

:author: Russell Ballestrini
:slug: i-tried-to-install-gitlab-on-truenas-and-failed
:date: 2020-10-25 14:28
:tags: Code, DevOps
:status: published

Ok, so a month ago I changed employment and the new company uses GitLab exclusively for it's centralized code version control system.

This is my first time using GitLab but my first projects was integrating a dou/cloudmapper with GitLab runners on a schedule.

Two weeks later I learned how GitLab runners work and wrote some wrapper logic to run cloudmapper concurrently so that all accounts are collected in parallel (basic logic is running docker exec on a custom entrypoint and then backgrounding the task in a bash loop over the accounts configured in the cloudmapper's config)

Anyways GitLab runners are awesome. I've been using CircleCI for the better part of 3 years, having lifted the better part of 50 code bases from an internal app called conveyor to CircleCI 1.0 and 2.0 conversions at Remind.

CircleCI 2.0 is awesome, but GitLab runners are just more powerful since they are not black box. Not all organizations need are even want this power. But I'm a nerd and I want it, so I decided I also want to run GitLab at home.

I could just run this on a VM on my SmartOS host called mbison, but that's a bit janky of a setup, it's an T420 ThinkPad after all. Also I learned the recommended minimum memory footprint of GitLab is 4G! That's 4/16G allocation without even discussing the separate KVM for the runner. This might be my only option if I want to go down this path, but it feels weird that a single application would need that much memory.

Anyways, I do have a FreeNAS `FreeNAS-11.3-U5` host at my house with 46G of memory and a bunch of idle cores, I wonder if they have a plug-in for GitLab, I'm sure they do by now.

Ok it seems like iXsystems renamed the FreeNAS codebase to TrueNAS and version `TrueNAS-12.0-RELEASE` has a GitLab plugin! Sweet!

Thankfully I remembered that back in 2019 I replaced the FreeNAS USB boot device with an SSD so it was likely a safe operation to attempt a TrueNAS upgrade on a Saturday morning since I'd have to weekend to try to recover.

Fun side story, I ran into trouble last year trying to upgrade FreeNAS train, and I didn't have room for the upgrade because I was using a USB drive as the boot disk and it had like 5 previous version on the 8G file system.

The kind people in the freenode #FreeNAS channel helped me switch back to an older version using SSH and told me I should not boot from a USB drive which was a think I picked up from back in the FreeNAS 6 or 7 days. Boy were they correct, I moved boot to an SSD and the thing really boots faster, plus it's a lot bigger.

Anyways, here is a fun command to determine when a ZFS pool was created, I used this to get the exact date and time I moved from USB to SSD for this blog post:

.. code-block:: bash

 root@guile[~]# zpool history -i freenas-boot | grep "create pool"
 2019-11-12.13:00:30 [txg:5] create pool version 28; software version 5000/5; uts  11.2-STABLE 1102500 amd64


So with confidence in my mind, I clicked upgrade from the FreeNAS UI by changing trains. I followed the prompts to create a backup of my config on my laptop and after a reboot, FreeNAS was now TrueNAS. I logged into the web UI and had a look around.

Everything seemed fine, so I went to the plug-in tab and attempted to install GitLab. That failed with this error:

<screenshot here>

So I decided oh well, I'll try spinning up an Ubuntu VM on the FreeNAS box, apparently FreeBSD uses bhyve for that.

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


It seems if you ask bhyve to use the UEFI bootloader it will require UG support in the Intel CPU : (

I attempted to switch to the grub bootloader but in that case I get the following error message:

.. code-block:: text

  File "/usr/local/lib/python3.8/site-packages/middlewared/plugins/vm.py", line 1414, in do_update
    raise verrors
 middlewared.service_exception.ValidationErrors: [EINVAL] vm_update.devices.3.dtype: VNC only works with UEFI bootloader.


FreeNAS does not let you disable VNC at this point...

Another limitation of a missing UG CPU flag is bhyve may only allocate 1 core, and 1 vcpu to a VM.

Anyways I'm out of luck, I can't use the plugin which uses jails due to a strange error and no other hints as to the issue and byhve / TrueNAS not supporting VMs for my CPU...

Maybe I try running GitLab with like 2G on mbison the Thinkpad t430 after all, still feels janky though, I would have liked to use the extra power.
