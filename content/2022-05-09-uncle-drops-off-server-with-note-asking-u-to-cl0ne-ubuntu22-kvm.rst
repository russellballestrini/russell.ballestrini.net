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
 * hostname
 * network
 * dns

& you remembered you would promise to try to document the steps needed so that the next time you clone the image you will have a checklist to follow so no steps get missed!



