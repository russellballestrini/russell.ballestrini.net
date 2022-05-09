Uncle Drops off server with note asking u to cl0ne ubuntu22 kvm
################################################################

:author: Russell Ballestrini
:slug: uncle-drops-off-server-with-note-asking-u-to-cl0ne-ubuntu22-kvm
:date: 2022-05-09 13:14
:tags: Code, DevOps
:status: published

Imagine your uncle just dropped off a TrueNAS Core server with root credentials, & a preconfigured IP Address in the netspace of 192.168.0.1/24.

The note also highly suggests you to create your desired arch with
KVM by making a cl0ne of ubuntu22, into separate VMs for different purposes.

Kind of open ended when to end a note, but whatever, you have nothing else to
do this __________ so you crack open the card board box & pull out an enormous 2u blade server! (this is like an FF8 Gunsword cutscene moment). We say enourmous not because it's any different in size than any other 2u, but this thing is extra heavy, I mean real heavy, 4 mechanical drives but fits up to 12!

The 4 hard drives, configured in ZFS mirrors, labeled "downloads" & "personal".

upon booting the The TrueNAS Core server graphical user interface is connected over HTTPS as a web application, available from the IP address on the sticky notes!

The UI seems to show the baremetal system has 128G of memory, most is free!
Additionally it has 2 x Intel(R) Xeon(R) CPU E5-2670 0 @ 2.60GHz with a 1% Avg Usage on 32 threads!

You clone a KVM guest from ubuntu22 & name it  ______________________________.

Now you will need to configure the new cloned guest via VNC in order to change the following list of configurations. The ubuntu22 base image is the vanilla defaults of Ubuntu 22.04 LTS server without any Snap (uncle likes flatpak if anything) so this means the server is "headless" there isn't a graphical user interface.

You'll need to configure:

 * hostname ``vim /etc/hostname``:

   .. code-block:: bash 

      cammy.foxhop.net

 * network  & dns ``vim /etc/netplan/00-installer-config.yaml``:

   .. code-block:: yaml

     # run this command after making changes!
     # sudo netplan --debug apply
     network:
       ethernets:
         enp0s4:
           addresses:
           - 192.168.1.64/24
           gateway4: 192.168.1.1
           nameservers:
             addresses:
               ### CloudFlare.
               #- 1.1.1.1
               ### Google DNS.
               #- 8.8.8.8
               #- 8.8.4.4
               ### OpenDNS.
               #- 208.67.220.220
               #- 208.67.222.222
               - 208.67.222.220
               ### Quad9.
               - 9.9.9.9
             search:
             - foxhop.net
       version: 2

.. code-block:: bash 


You remembered to try to document steps needed for next time a person needs to clone the image we will have a checklist to follow so no steps get missed!

What is that checklist for you?

Do you bootstrap configuration management next? Or maybe some in house remote execution? Do you outsource your admin hacker tooling?
