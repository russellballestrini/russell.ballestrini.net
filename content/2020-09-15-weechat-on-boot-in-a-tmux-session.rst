WeeChat on-boot in a tmux session
################################################################

:author: Russell Ballestrini
:slug: weechat-on-boot-in-a-tmux-session
:date: 2020-09-15 13:32
:tags: automation
:status: published

Chronicles of a washed up systems administrator.

In the basement, M. Bison (``mbision.foxhop.net.``), a T430 with a cracked screen runs queitly with his lid closed, acting as a SmartOS hypervisor to 3 Solaris derived zones and 4 KVM ubuntu guests.

One of these guests is the oldest of the bunch and his name is Akuma (``akuma.foxhop.net.``).

Akuma and I go way back, over 13 years now. At one point Akuma was a physical machine, who ran ubuntu and had it's own guest operating systems.

Akuma has been "home base" for as long as I remember. A place a "jump box" where shit got done. A place to perform operations. It make sense that Akuma would evolve into the private internal DNS Nameserver for ``foxhop.net.`` and other domains, and also take on Salt Master resposibilities.

Akuma uses ``tmux`` with default settings to enable "remote shell" vibe.

This lets me connect to my session running on Akuma from anywhere in the world.

Only problem is, Akuma reboots weekly when M. Bison `triggers a complete backup of all guests </backup-all-virtual-machines-on-a-smartos-hypervisor-with-smart-back-sh/>`_ (snapshots are stored in-the-raw [uncompressed] on Guile, the FreeNAS server).

Since Akuma reboots so frequently, to continue to function as my "home base" I needed a way to create a tmux sessions on boot, and I did so using SaltStack:

.. code-block:: yaml

 create-tmux-session-on-boot:
   cron.present:
     - comment: "create a new tmux session on system boot"
     - name: /bin/bash /home/fox/new-tmux
     - identifier: "create-tmux-session-on-boot"
     - special: "@reboot"
     - user: fox
     - require:
       - user: fox
 
This salt state results in the following ``crontab -l`` entry:

.. code-block:: bash

 # create a new tmux session on system boot SALT_CRON_IDENTIFIER:create-tmux-session-on-boot
 @reboot /bin/bash /home/fox/new-tmux


And of course I what tutorial wouldn't be complete without a script! (``/home/fox/new-tmux``) :

.. code-block:: bash

  #!/bin/bash
  # The -A flag makes new-session behave like attach-session if session-name
  # already exists; in this case, -D behaves like -d to attach-session.
  tmux new-session -d -A -s "remote-shell" "weechat-curses"
  # also create a couple windows to use as "remote shells".
  tmux new-window
  tmux new-window
  # finally attach to the new session!
  tmux a -t "remote-shell"

Thanks for joining me on this escape into the world of computers.

Please feel free to comment below if you have suggestions for this post.
