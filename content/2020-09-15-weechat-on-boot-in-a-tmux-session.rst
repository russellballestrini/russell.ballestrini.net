WeeChat on-boot in a tmux session
################################################################

:author: Russell Ballestrini
:slug: weechat-on-boot-in-a-tmux-session
:date: 2020-09-15 13:32
:tags: automation
:status: published

Chronicles of a washed up systems administrator.

In the basement, M. Bison (`mbision.foxhop.net.`), a T430 with a cracked screen runs queitly with his lid closed, acting as a SmartOS hypervisor to 3 Solaris derived zones and 4 KVM ubuntu guests.

One of these guests is the oldest of the bunch and his name is Akuma (`akuma.foxhop.net.`). Akuma and I go way back, over 15 years now. At one point akuma was a physical machine, which ran ubuntu and had it's own guest operating systems. Akuma has been "home base" for a long time, a place to SSH jump from and a place to perform operations. This server is the Salt Master and also a private internal DNS server running Bind9.

To use Akuma as a "remote shell", one which I can connect and disconnect to from anywhere in the world, I use `tmux` (previously `screen`) with defaults settings.

Akuma reboots weekly to perform a complete system backup (stored without compression on Guile, a FreeNAS server running on an HP G6 180 [link to that blog post])

Since Akuma reboots so frequently, it creates a tmux session on boot, configured using SaltStack:

.. code-block:: yaml

 create-tmux-session-on-boot:
   cron.present:
     - comment: "create a new tmux session on system boot"
     - name: /home/fox/new-tmux
     - identifier: "create-tmux-session-on-boot"
     - special: "@reboot"
     - user: fox
     - require:
       - user: fox
 
This salt state results in the following `crontab -l` entry:

.. code-block:: bash

 # create a new tmux session on system boot SALT_CRON_IDENTIFIER:create-tmux-session-on-boot
 @reboot /home/fox/new-tmux


And of course I would be terrible if I didn't share with you the contents of `/home/fox/new-tmux`:

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
