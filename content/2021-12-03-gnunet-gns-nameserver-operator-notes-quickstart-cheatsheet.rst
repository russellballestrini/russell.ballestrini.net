GNUnet GNS Nameserver Operator Notes, Quickstart, & Cheatsheet
################################################################

:author: Russell Ballestrini
:slug: gnunet-gns-nameserver-operator-notes-quickstart-cheatsheet
:date: 2021-12-03 18:21
:tags: Code, DevOps
:status: published

.. contents::

We GROW with Truth, Freedom, Love.

| "You have an ally".

We scroll through the official GNUnet handbook, everything is covered in details, sections have examples. Seems verbose at first glance but also familiar .

Freedom of speech is under attack.

I AM not scared, we understand the technology we have and the technology we need. We will rescue ourselves and GROW together.

GNS right NOW!

Why?

Our Collective's Internet Nameservice (DNS) is UNDER ACTIVE ATTACK by groups of governments.
Multitiple reports of DNS Name registrars breaking registrants Internet Domains on the behalf of NON-HUMAN ENTITIES.

To avoid any erosion of our Freedom of speech, we will use GNS to make sure our web domains continue to map to our resources for people looking for us.

I AM a seasoned 17 year Bind9 DNS administrator. I had my start on FreeBSD 5.0, virtualized over the years, now on Ubuntu VMs running on "the cloud" & local hypervisors hosting on broken laptops.

We know how to scale DNS, it sort of just works once you figure out the config files.

So let's figure out GNS and GROW a new Internet Culture, eh?

---

We pull down the source code using git:

.. code-block:: bash

 git clone https://git.gnunet.org/gnunet.git

We see a lot of C code, interesting choice.

.. code-block:: bash

 cd gnunet
 [fox@blanka gnunet]$ ls -hal src/dns/
 total 144K
 drwxrwxr-x. 1 fox fox  362 Dec  3 18:09 .
 drwxrwxr-x. 1 fox fox  834 Dec  3 18:09 ..
 -rw-rw-r--. 1 fox fox 9.3K Dec  3 18:09 dns_api.c
 -rw-rw-r--. 1 fox fox 1.3K Dec  3 18:09 dns.conf.in
 -rw-rw-r--. 1 fox fox 2.2K Dec  3 18:09 dns.h
 -rw-rw-r--. 1 fox fox  126 Dec  3 18:09 .gitignore
 -rw-rw-r--. 1 fox fox  11K Dec  3 18:09 gnunet-dns-monitor.c
 -rw-rw-r--. 1 fox fox 7.1K Dec  3 18:09 gnunet-dns-redirector.c
 -rw-rw-r--. 1 fox fox  32K Dec  3 18:09 gnunet-helper-dns.c
 -rw-rw-r--. 1 fox fox  35K Dec  3 18:09 gnunet-service-dns.c
 -rw-rw-r--. 1 fox fox  14K Dec  3 18:09 gnunet-zonewalk.c
 -rw-rw-r--. 1 fox fox 2.2K Dec  3 18:09 Makefile.am
 -rw-rw-r--. 1 fox fox 7.5K Dec  3 18:09 plugin_block_dns.c
 -rwxrwxr-x. 1 fox fox 1.6K Dec  3 18:09 test_gnunet_dns.sh

GNUnet 0.15.0 released: https://www.gnunet.org/en/news/2021-08-0.15.0.html

GNS First-come-first-served GNUnet top-level domain ".pin" zone key and website updated 

Register now: https://fcfs.gnunet.org/

Wow, Ok - We want to reserve our favorite names, right?

How do we generate our ``zone key```?

A section in the GNUnet handbook which seems to cover zones and keys:

 * https://docs.gnunet.org/handbook/gnunet.html#First-steps-_002d-Using-the-GNU-Name-System

To register a top-level domain of the ``.pin`` we need to generate a public/private keypair for each zone.

But before we do that we need to install GNUnet and configure the tool.

Ok, I would prefer some up-to-date binaries than the source tree.

Fedora package looks old and abandoned, same with Ubuntu, & Alpine... 

I AM dreaming of a lightweight Alpine docker container to pass around the nets with with GNUnet prebaked in. Maybe a project for another day.

It seems like the NixOS package manager has an uptodate version 0.15.3!

To install GNUnet binaries, we must first learn how to install ``nix`` package manager.

Installing nix package manager, run the following:

.. code-block:: bash

 # reference: https://nixos.org/download.html
 curl -L https://nixos.org/nix/install | sh

Once installed try to install GNUnet, like this:

.. code-block:: bash

 nix-env -iA nixpkgs.gnunet

Errors complaining about certificates might be an easy fix:

.. code-block:: bash

 source /home/fox/.nix-profile/etc/profile.d/nix.sh

For example the install script placed the following into my ``~/.bash_profile``:

.. code-block:: bash

 if [ -e /home/fox/.nix-profile/etc/profile.d/nix.sh ]; then . /home/fox/.nix-profile/etc/profile.d/nix.sh; fi # added by Nix installer

Once you get all that sorted you should have installed GNUnet!

To verify try to interact with ``~/.nix-profile/bin/gnunet-config``.


Battleship Operational, A Carrier Has Arrived.

.. code-block:: bash

 [fox@blanka russell.ballestrini.net]$ gnunet-config --version
 gnunet-config v0.15.3 release


Alright now we must somehow configure zones and public/private keypairs with this tool.

The handbook gives us this as an example, and we break down the anatomy of the command and outputs.

.. code-block:: bash

 gnunet-config -s gns -o .myfriend -V PUBLIC_KEY 

Let's try passing ``--help``

.. code-block:: bash

 [fox@blanka russell.ballestrini.net]$ gnunet-config --help
 
 gnunet-config [OPTIONS]
 Manipulate GNUnet configuration files
 Arguments mandatory for long options are also mandatory for short options.
   -b, --supported-backend=BACKEND
                              test if the current installation supports the
                                specified BACKEND
   -c, --config=FILENAME      use configuration file FILENAME
   -d, --diagnostics          output extra diagnostics
   -F, --full                 write the full configuration file, including
                                default values
   -f, --filename             interpret option value as a filename (with
                                $-expansion)
   -h, --help                 print this help
   -L, --log=LOGLEVEL         configure logging to use LOGLEVEL
   -l, --logfile=FILENAME     configure logging to write logs to FILENAME
   -o, --option=OPTION        name of the option to access
   -r, --rewrite              rewrite the configuration file, even if nothing
                                changed
   -S, --list-sections        print available configuration sections
   -s, --section=SECTION      name of the section to access
   -V, --value=VALUE          value to set
   -v, --version              print the version number
 Report bugs to gnunet-developers@gnu.org.
 Home page: http://www.gnu.org/s/gnunet/
 General help using GNU software: http://www.gnu.org/gethelp/

Ok so it seems like this command simply edits config files for GNUnet.

Ok but where are these enigmatic config files?

This is a living document we will continue the story toward a resolution and simple quickstart guide!

Leave comments below!
