Hackathon 2013 Virtualization
#############################
:date: 2013-12-13 20:56
:author: Russell Ballestrini
:tags: Project
:slug: hackathon-2013-virtualization
:status: published

As a warning before we dive into things, this post is less of a formal
publication and more of a stream of conscience.

My employer `newcars.com <http://newcars.com/jobs/>`__ has allowed the
technical staff to host hackathon! Over the past couple weeks I have had
quite a few ideas tumbling around in my head:

-  Standup a central logging server
-  Standup Sensu for monitoring
-  Bake-off and document some KVM virtualization hypervisors (Ubuntu or
   SmartOS)
-  Test Docker and document findings

Ultimately I have chosen to dedicate my time to testing out
virtualization on the new Cisco UCS Blade servers. I plan to test Ubuntu
KVM first.

**KVM (Ubuntu 12.04)**

I decided to use a Salt-stack configuration management formulas to
document how I transformed ``kvmtest02`` (a regular Ubuntu 12.04 server)
into a KVM hypervisor. I use ``kvmtest0a`` and ``kvmtest02b`` when
refering to the virtual machines living on the hypervisor. Here is the
formula:

**kvm/init.sls:**

::

    # https://help.ubuntu.com/community/KVM
    # Ubuntu server a KVM - Kernel Virtual Machine hypervisor

    # the official ubuntu document suggests we install the following
    kvm-hypervisor:
      pkg.installed:
        - names:
          - qemu-kvm
          - libvirt-bin
          - ubuntu-vm-builder
          - bridge-utils

    # we need to make all of our ops people part of the libvirtd group
    # so that they may create and manipulate guests. we skip this for now
    # and assume all virtual machines will be owned by root.

    # these are optional packages which gives us a GUI for the hypervisor
    virt-manager-and-viewer:
      pkg.installed:
        - names:
          - virt-manager 
          - virt-viewer 
        - require:
          - pkg: kvm-hypervisor

    # create a directory to hold virtual machine image files
    kvm-image-dir:
      file.directory:
        - name: /cars/vms
        - user: root
        - group: root
        - mode: 775

.. raw:: html

   </p>

I used the following to install the formula to the test hypervisor:

::

    salt 'kvmtest02.example.com' state.highstate

.. raw:: html

   </p>

The salt highstate reported everything was good (green), so I moved on
to setting up the bridge networking interface. At this point I don't
want to figure out the logistics setting up the network bridge in
configuration management, so I simply manually edited
``/etc/network/interfaces`` to look like this (substitute your own
network values):

::


    # The loopback network interface
    auto lo
    iface lo inet loopback

    # The primary network interface
    #auto eth0
    #iface eth0 inet manual

    # https://help.ubuntu.com/community/KVM/Networking
    # create a bridge so guest VMs may have their own identities
    auto br0
    iface br0 inet static
        address XXX.XX.89.42
        netmask 255.255.255.0
        network XXX.XX.89.0
        broadcast XXX.XX.89.255
        gateway XXX.XX.89.1

        # dns-* options are implemented by the resolvconf package
        dns-nameservers XXX.XX.254.225 XXX.XX.254.225
        dns-search example.com

        # bridge_* options are implemented by bridge-utils package
        bridge_ports eth0
        bridge_stp off
        bridge_fd 0
        bridge_maxwait 0

Then, I crossed my fingers and reloaded the network stack using this
command:

::

    /etc/init.d/networking restart

I also used this to "bounce" the bridge network interface:

::

    ifdown br0 && ifup br0

I verified with ``ifconfig``.

I'm ready to create my first VM. There are many different ways to boot
the VM and install the operating system. KVM is fully virtualized so
nearly any operating system may be install on the VM.

If you have not already, please get familiarized with the following two
commands:

#. virsh
#. virt-install

The ``virsh`` command is an unified tool / API for working with
hypervisors that support the libvirt library. Currently ``virsh``
supports Xen, QEmu, KVM, LXC, OpenVZ, VirtualBox and VMware ESX. For
more information run ``virsh help``.

The ``virt-install`` command line tool is used to create new KVM, Xen,
or Linux container guests using the "libvirt" hypervisor management
library. For more information run ``man virt-install``.

    Woah, virsh and virt-install both support LXC?

We have decided to only support Ubuntu 12.04 at this time, so obviously
we will choose that for our guest's OS. Now we need to decide on an
installation strategy. We may use the following techniques to perform an
install:

-  boot from local CD-rom
-  boot from local ISO
-  boot from PXE server on our local vLAN
-  boot from netboot image from anywhere in the world

We will choose the PXE boot strategy because our vLAN environment
already uses that for physical hosts.

We will use the ``virt-install`` helper tool to create the virtual
machine's "hardware" with various flags. Lets document the creation of
this guest in a simple bash script so we may reference it again in the
future.

/tmp/create-kvmtest02-a.sh:

::

    HOSTNAME=kvmtest02-a
    DOMAIN=example.com

    sudo virt-install \
      --connect qemu:///system \
      --virt-type kvm \
      --name $HOSTNAME \
      --vcpu 2 \
      --ram 4096 \
      --disk /cars/vms/$HOSTNAME.qcow2,size=20 \
      --os-type linux \
      --graphics vnc \
      --network bridge=br0,mac=RANDOM \
      --autostart \
      --pxe

.. raw:: html

   </p>

This was not used, but shows the flags to perform a netboot from
Internet:

::

    --location=http://archive.ubuntu.com/ubuntu/dists/raring/main/installer-amd64/ \
    --extra-args="auto=true priority=critical keymap=us locale=en_US hostname=$HOSTNAME domain=$DOMAIN url=http://192.168.1.22/my-debconf-preseed.txt"

.. raw:: html

   </p>

I created the vm:

::

    bash /tmp/create-kvmtest02-a.sh

.. raw:: html

   </p>

``virt-install`` drops you into the "console" of the VM, but this will
not work yet, so we use ctrl+] to break out and get back to our
hypervisor. Use ``virsh list`` to list all the currently running VMs.

Lets use ``virt-viewer`` to view the VMs display. For this we need to
SSH to the hypervisor and forward our display to our workstation, we do
this with the ``-X`` flag. For example:

::

      
    ssh -X kvmtest02

Now we can launch ``virt-viewer`` on the remote hypervisor, and the GUI
will be drawn on our local X display!

::

      
    virt-viewer kvmtest02-a

Once I got that to work, I also tested ``virt-manager`` which gives a
GUI to control all guests on the remote hypervisor.

::

      
    virt-manager

.. raw:: html

   </p>

Now we need to determine the auto-generated MAC Address of the new
virtual machine.

::

    virsh dumpxml kvmtest02-a | grep -i "mac "
      mac address='52:54:00:47:86:8e'

We need to add this MAC address to our PXE server's DHCP configuration
to allocate the IP and tell it where to PXE-boot from.

During a real deployment we would get an IP address allocated and an A
record and PTR setup for new servers. This is a test and I will be
destroying all traces of this virtual machine after presenting during
the hackathon, so for now I'm going to skip the DNS entries and "steal"
an IP address. I must be VERY careful not to use an IP address already
in production. First use dig to find an IP without a record, then
attempt to ping and use NMAP on the IP.

::

    dig -x XXX.XX.89.240 +short
    ping XXX.XX.89.240
    nmap XXX.XX.89.240 -PN

The IP address checked out, it didn't have a PTR, it didn't respond to
pings, and using nmap proved there were no open ports. I'm very
confident this IP address is not in use.

I added a record to our DHCP / PXE server for this Virtual Machine. I
attempted multiple times to pxe boot the VM, but the network stack was
never automatically configured... The DHCP server was discovering the
new VMs MAC and offering the proper IP address, as noted by these log
lines:

::

    Dec 13 07:57:43 pxeserver60 dhcpd: DHCPDISCOVER from 52:54:00:47:86:8e via eth0
    Dec 13 07:57:43 pxeserver60 dhcpd: DHCPOFFER on xxx.xx.89.240 to 52:54:00:47:86:8e via eth0
    Dec 13 07:57:44 pxeserver60 dhcpd: DHCPDISCOVER from 52:54:00:47:86:8e via eth0
    Dec 13 07:57:44 pxeserver60 dhcpd: DHCPOFFER on xxx.xx.89.240 to 52:54:00:47:86:8e via eth0
    Dec 13 07:57:48 pxeserver60 dhcpd: DHCPDISCOVER from 52:54:00:47:86:8e via eth0
    Dec 13 07:57:48 pxeserver60 dhcpd: DHCPOFFER on xxx.xx.89.240 to 52:54:00:47:86:8e via eth0

I wasted about 4 hours attempting to troubleshoot and diagnose why the
VM wouldn't work with DHCP. I ended the night without any guests
online...

**The Next DAY!**

So today I decided to stop trying to get DHCP and PXE working. I
downloaded an Ubuntu server ISO to the hypervisor, and used
``virt-manager`` to mount the ISO on the guest and booted for a manual
operating system install.

This did two things, it proved that the hypervisor's network bridge
``br0`` worked for static network assigned settings and that something
between the DHCP server and the hypervisor was preventing the
``DHCPOFFER`` answer from getting back to the VM. I looked into iptables
firewall, removed apparmor, removed SELINUX and reviewed countless logs
looking for hints... then moved on...

I was able to get salt-minion installed on the vm using our
post-install-salt-minion.sh script, which I manually downloaded from the
salt master. But to keep this test self contained, I pointed the VM's
salt-minion to ``kvmtest02`` which we already had setup as a test
salt-master.

The salt-master saw the salt-minion's key right away, so I decided to
target an install. This what I applied to the VM:

salt/top.sls:

::

      'kvmtest02.example.com':
        - kvm

      'kvmtest02b.example.com':
        - virtualenv
        - python-ldap
        - nginx
        - the-gateway

salt-pillar/top.sls

::

      # kvmtest02b gateway in a VM experiment
      'kvmtest02b.example.com':
        - nginx
        - the-gateway.alpha
        - deployment-keys.the-gateway-alpha

.. raw:: html

   </p>

The stack was successfully deployed to the VM and proved that virtual
machines are a viable solution for stage or production. It also gave me
the change to test out this particular deployment again and found a few
gotchas we need to create maintenance tickets for.

Without configuration management, it would have taken weeks to deploy
this custom application stack. The install with configuration management
took less then 10 minutes!

One of the KVM related snags I ran into was that Nginx does some fun
calculations with cpu cache to determine hash table sizes. As a
temporary work around, until I can devote more research time, I raised
up the following three hash table directives in the http section of
nginx.conf:

::

        server_names_hash_bucket_size 512;
        types_hash_bucket_size 512;
        types_hash_max_size 4096;

.. raw:: html

   </p>

**SmartOS**

**snippet from /etc/dhcp/dhcpd.conf**

::

    # SmartOS hypervisor group to boot image
    group "smartos-hypervisors" {
      next-server xxx.xx.89.71;

       host smrtest01-eth0 {
            hardware ethernet 00:25:B5:02:07:DF;
            option host-name "ncstest01";
            fixed-address smrtest01.example.com;

            if exists user-class and option user-class = "iPXE" {
               filename = "smartos/menu.ipxe";
            } else {
               filename = "smartos/undionly.kpxe";
            }
        }

    }

::

    mkdir /cars/tftp/smartos
    cd /cars/tftp/smartos
    wget http://boot.ipxe.org/undionly.kpxe
    wget https://download.joyent.com/pub/iso/platform-latest.tgz
    tar -xzvf platform-latest.tgz
    mv platform-20130629T040542Z 20130629T040542Z
    mkdir platform
    mv i86pc/ platform/

create boot menu that we referenced,
``vim /cars/tftp/smartos/menu.ipxe``

::

    #!ipxe

    kernel /smartos/20130629T040542Z/platform/i86pc/kernel/amd64/unix
    initrd /smartos/20130629T040542Z/platform/i86pc/amd64/boot_archive
    boot

Make sure to replace platform version with current.

I was able to get the blade server to PXE boot the image, but it seems
SmartOS doesn't really support the SANs. SmartOS really expects to see
local disks, and to build a ZFS pool on top of that. Basically SmartOS
could be used to build a SAN, so they didn't put much effort in
supporting SANs. After I figured this out I abandoned this test. We
could revist this again, using one of the Dell servers, or use it to
stand up a really powerful Alpha server environment.

**LXC**

Run /usr/bin/httpd in a linux container guest (LXC). Resource usage is
capped at 512 MB of ram and 2 host cpus:

::

    virt-install \
    --connect lxc:/// \
    --name lxctest02-a \
    --ram 512 \
    --vcpus 2 \
    --init /usr/bin/httpd

.. raw:: html

   </p>

**Discussion points**

-  Why doesn't DHCP work on bridge?
-  If we use virtualization, we need to come up with a plan for IP
   addresses, like possibly allocate ~5 IP addresses to a hypervisor
   host
-  We need to come up with a naming convention for guests, in testing I
   appended a letter to the hypervisor name ``kvmtest02`` so the guests
   names were ``kvmtest02a`` and ``kvmtest02b``, is this plausible going
   forward?

**If I had more time ...**

.. raw:: html

   <ul>
   <li>

I would have liked to test out LXC

.. raw:: html

   </li>
   <li>

I would have liked to test out Docker

.. raw:: html

   </li>
   <li>

I would have liked to test out physical to virtual migrations

.. raw:: html

   </li>
   </p>
