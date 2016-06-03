High load and CPU usage craftbukkit compared to vanilla minecraft
#################################################################
:date: 2013-06-20 23:35
:author: Russell Ballestrini
:tags: Opinion, Project
:slug: high-load-and-cpu-usage-craftbukkit-compared-to-vanilla-minecraft
:status: published

I started researching the best ways to use `salt to provision minecraft
servers <http://bobbylikeslinux.net/salt-minecraft-fun.html>`__. I wrote
a salt state formula for the vanilla minecraft server deployment. The
deployment worked out great so I decided to try my luck with plugins.

In order to use plugins and mods we need to use a customized server
package. I decided to try provisioning a craftbukkit server and quickly
noticed something was very wrong. Vanilla Craftbukkit (with no plugins)
produces very high load and CPU usage.

Here is a chart for proof. The spike is when I stopped the vanilla
minecraft server and started the craftbukkit minecraft server:

|minecraft-vs-craftbukkit|

.. |minecraft-vs-craftbukkit| image:: /uploads/2013/06/minecraft-vs-craftbukkit.png
   :target: /uploads/2013/06/minecraft-vs-craftbukkit.png
