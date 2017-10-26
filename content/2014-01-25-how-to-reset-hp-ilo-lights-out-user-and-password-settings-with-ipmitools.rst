How to reset HP iLO Lights-Out User and Password Settings with IPMItool
#######################################################################
:date: 2014-01-25 09:18
:author: Russell Ballestrini
:tags: Guide
:slug: how-to-reset-hp-ilo-lights-out-user-and-password-settings-with-ipmitools
:status: published

Warning:
 Do NOT follow guides that suggest to make a DOS boot disk, this is over complicated.

Use the ``ipmitool`` which ships with most Unix based operating systems.
I tested on SmartOS and Ubuntu Linux. Use a live boot disk if you must.

#. Run ``ipmitool user list`` to list all users installed on the iLO.
#. Choose a user ID from the list and run ``ipmitool user set password [ID]``.
#. Last, make sure the user is enabled with ``ipmitool user enable [ID]``.

**Here is a complete set of commands I used to reset user ID 6:**

::

    [root@1c-c1-de-f0-ad-36 /opt]# ipmitool user list
    ID  Name             Callin  Link Auth  IPMI Msg   Channel Priv Limit
    2   ROUSER           true    false      false      Unknown (0x00)
    3   USERID           true    false      false      Unknown (0x00)
    4   OEM              true    false      false      Unknown (0x00)
    5   Operator         true    false      false      Unknown (0x00)
    6   admin            true    false      false      Unknown (0x00)
    ... truncated ...
    15  admin            true    false      false      Unknown (0x00)
    16  OEM              true    false      false      Unknown (0x00)

    [root@1c-c1-de-f0-ad-36 /opt]# ipmitool user set password 6 mynew-password

    [root@1c-c1-de-f0-ad-36 /opt]# ipmitool user enable 6

Next I logged into the web GUI and cleaned up this crazy list of users.
You may also need to change the privileges on a user ID to grant admin
level access. Run ``ipmitool user`` for a list of possible sub-commands.

After I finished poking around with the web GUI, I decided to learn a
bit more about IPMI and the ``ipmitool`` command.

I figured out how to get sensor information over the LAN using this
command:

::

    sudo ipmitool -I lan -H guy-ilo.foxhop.net -U admin sensor


I was even able to log into the server OS via Serial-over-LAN (SOL)
using this command:

::

    sudo ipmitool -I lanplus -H guy-ilo.foxhop.net -U admin sol activate

Serial-over-LAN completely resolves the need for a complicated JAVA/KVM
(keyboard video mouse) setup, I was able to reboot the server and watch
the machine POST over the serial connection! Now you don't need to shell
out $229+ on an Advanced 1 yr single server Licence for HP Lights-Out 100i (LO100i)!

I uploaded a video showing
`Serial-Over-LAN with IPMItools to an HP Proliant DL160 G6 running
SmartOS <http://www.youtube.com/watch?v=xAFjbKAzB4s>`__.


**Update:** 

Documenting a few other useful commands for myself here.

Power on and off the server chassis:

::

  sudo ipmitool -I lan -H guy-ilo.foxhop.net -U admin chassis power status
  sudo ipmitool -I lan -H guy-ilo.foxhop.net -U admin chassis power on 
  sudo ipmitool -I lan -H guy-ilo.foxhop.net -U admin chassis power soft
  sudo ipmitool -I lan -H guy-ilo.foxhop.net -U admin chassis power off
  sudo ipmitool -I lan -H guy-ilo.foxhop.net -U admin chassis power cycle


**Update:** 

Apparently after you know the ILO username and password you may
also use SSH to connect and manage the server:

::

        ssh admin@guy-ilo.foxhop.net
        admin@guile-ilo.foxhop.net's password: 

        Lights-Out 100 Management
        Copyright 2005-2007 ServerEngines Corporation
        Copyright 2006-2007 Hewlett-Packard Development Company, L.P.

        /./-> help
        Root Directory

        /./-> show
            /./
            Targets
                system1
                map1
                
            Properties
                
            Verbs
                cd
                version
                exit
                show
                help

        /./-> cd system1
        /./system1/-> show
            /./system1/
            Targets
                oemhp_sensors
                oemhp_frus
                console1
                led1
                
            Properties
                name=DL180(Aspen)    _R
                enabledstate=enabled
                
            Verbs
                cd
                version
                exit
                show
                reset
                start
                stop
                help

You can even trigger the server OS to stop change run levels or mess
with chassis power for more extreme measures.

::

        /./system1/-> stop
        System1 stopped.



**Update:**

I run FreeNAS on an HP DL180 G6 and just replaced my p410 controller with an LSI SAS9220-8i (IBM M1015) flashed to IT mode. The stock cables are long enough. I did not have issues with fans running at high RPM.

(I did the same replacement on an [HP DL160 G6 running SmartOS](/how-i-added-two-seagate-240g-ssds-as-smartos-l2arc/) and it didn't have a high fan RPM issues either) 
