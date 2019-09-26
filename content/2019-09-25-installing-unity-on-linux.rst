Installing Unity on Linux 
################################################################

:author: Russell Ballestrini
:slug: installing-unity-on-linux
:date: 2019-09-25 18:55
:tags: Code, Games, gumyum
:status: published

Russell, why are you installing Unity? I thought you were an open source developer and `homegrown video game engine builder </yuletide-trains-and-homegrown-video-games/>`_?!

|gumyum logo|

The TL;DR is I'm starting `a video game co-operative called gumyum <https://gumyum.com>`_. The basic idea is to build a large Video Game company owned completely by members. There will be no employees and most revenue after paying taxes, operational expenses, and marketing, will be divided among members.

We are actively looking for members, specifically engineers who want to build games. We already have a distributed team of 4 artists and 2 engineers meeting on Slack and working on two games.

Adopting Unity, at least for our first couple games, will lower the barrier of entry for other engineers when joining the team.

**Installing Unity On Linux**

To get started first we will create a Unity Account and install the ``Unity Hub``.
You need both in order to aquire a free licence for personal use.

The ``Unity Hub`` software will help you download various Unity versions, manage your licence, and manage game projects.

You should go to the Unity website and created an account.

I found the Linux `Unity Hub` installer in `this thread <https://forum.unity.com/threads/unity-hub-v-1-0-0-is-now-available.555547/>`_ and downloaded it to my `~/Downloads` directory.

Next I opened a terminal and made the file executable, and executed it.

.. code-block:: bash

 cd ~/Downloads
 chmod 755 UnityHub.AppImage
 ./UnityHub.AppImage

From there I needed to sign in and then request a licence. I chose the free option since this is a $0 hobby project at this point.

On the ``Installs`` tab in ``Unity Hub`` you may download various stable and LTS version of Unity. I definately suggest using stable. I accidentally grabbed a non-stable one and all I had was pink screens inside of Unity!

Anyways, now you may start a Unity project. ``Unity Hub`` seems to store files locally and also allows you to sync to the cloud. This enables easy collaboration on the same project.

Thats all for now, please check back for more posts about gumyum!

.. image:: /uploads/2019/09/unity-hub-gumyum.png

.. |gumyum logo| image:: /uploads/2010/12/gumyumgameslogo.png
