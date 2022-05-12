Uncle Drops off server with note asking u to cl0ne ubuntu22 kvm
################################################################

:author: Russell Ballestrini
:slug: uncle-drops-off-server-with-note-asking-u-to-cl0ne-ubuntu22-kvm
:date: 2022-05-09 13:14
:tags: Code, DevOps
:status: published

Imagine your uncle just dropped off a TrueNAS Core server with root credentials, & a preconfigured IP Address in the subnet space of 192.168.1.1/24.

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
           routes:
             - to: default
               via: 192.168.1.1
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

---------------------------------------------

Ok, so the next day you wake up & decide to try out SaltStack configuration management, so that means 
you will want to clone ubuntu22 kvm into a guest named ``master`` (short for salt-master, ``salt`` consistently crashes [me shrugs]).

Anyways, you do the tricks above to configure netplan (networking & DNS) & then go about installing ``salt-master`` service. The ``-M`` flag signals to install both ``salt-minion`` & ``salt-master``:

.. code-block:: bash

  wget -O - https://bootstrap.saltstack.com | sudo sh -s -- stable -M;

Of course this doesn't always work if for example you are on a very new Ubuntu LTS (which you are) no fear,
you remembered uncle documented a similar snag in a `github comment <https://github.com/saltstack/salt-bootstrap/issues/1821#issuecomment-1113868737>`_ that said you adapted to also install the ``salt-master`` daemon, since this is the salt master vm.

.. code-block:: bash

 git clone https://github.com/saltstack/salt-bootstrap.git
 cd salt-bootstrap
 bash salt-bootstrap.sh -M

By now you are watching the growing list of hosts using ubuntu22's SSH host key...

* [ ] https://blog.g3rt.nl/regenerate-ssh-host-keys.html

You do this to fix salt host & start to consider ways to deal with this in the future, should likely be one of the first steps or maybe we could run this on ubuntu22? You decide to write this down as a (rabbit)(hole) for another day.

---

Dual booting Ubuntu 22.04 LTS?

Did you know grub 2 OS Prober was recently disabled by default?

If plan to dual boot with windows or any other OS, try these settings:

* [x] https://www.solaris-cookbook.eu/linux/linux-ubuntu/ubuntu-22-04-fix-grub-dual-boot-with-windows/


.. code-block:: bash

 sudo vi /etc/default/grub
 
 GRUB_CMDLINE_LINUX=""
 GRUB_DISABLE_OS_PROBER=false

applied but it didn't seem to work...

---

While doing this work you remember you needed to back up your gpg keys (and verify the restore process!):

* [] https://www.jwillikers.com/backup-and-restore-a-gpg-key

& also make sure you can access pass from multiple machines, using git!

* [] https://www.passwordstore.org/

and get multiple machines pushing & pulling from the same remote origin this way it is safer to loose a node on the "cluster",

for full transparency, this is what I did to look around & export / import

.. code-block:: bash

 [fox@blanka ~]$ gpg --list-secret-keys --keyid-format LONG

 /home/fox/.gnupg/pubring.gpg
 ----------------------------
 sec   rsa2048/23CDA6102BFB3D7D 2014-06-23 [SC]
       4ABE744F1FDAF12C78E2E5D923CDA6102BFB3D7D
 uid                 [ultimate] Russell Ballestrini (Personal) <russell@ballestrini.net>
 ssb   rsa2048/1E6F09A2613E8133 2014-06-23 [E]
 
 [fox@blanka ~]$ gpg -o russell-at-ballestrini-dot-net.gpg --export-options backup --export-secret-keys russell@ballestrini.net

 [fox@blanka ~]$ ll russell-at-ballestrini-dot-net.gpg 
 -rw-------. 1 fox fox 2645 May 11 18:59 russell-at-ballestrini-dot-net.gpg

 [fox@blanka ~]$ file russell-at-ballestrini-dot-net.gpg
 russell-at-ballestrini-dot-net.gpg: OpenPGP Secret Key Version 4, Created Mon Jun 23 01:44:34 2014, RSA (Encrypt or Sign, 2048 bits)

 [fox@blanka ~]$ scp russell-at-ballestrini-dot-net.gpg fox@akuma.foxhop.net:/home/fox/russell-at-ballestrini-dot-net.gpg
 russell-at-ballestrini-dot-net.gpg    


you think this will allow you to copy the private key file around to various computers via SSH and import the key using this:

.. code-block:: bash
 
 gpg --import-options restore --import russell-at-ballestrini-dot-net.gpg

you admit whenever working with pgp or gpg makes you feel squeemish, but a key is a key right? ...

should not treat any differently than a private SSH key.

You will however want to trust this key completely with your whole heart & soul & sole so you modify the newly imported key to trust it completely and ultimately which just so happens to be a 5 in this tool's universe!

so you follow these prompts:

gpg --edit-key  russell@ballestrini.net

gpg> trust

and choose 5!

gpg> quit
