Set Root Password SmartOS Percona MySQL Zone
############################################
:date: 2014-10-11 00:12
:author: Russell Ballestrini
:tags: DevOps, Guide
:slug: set-root-password-smartos-percona-mysql-zone
:status: published

I used project-fifo to launch the ``percona (14.2.0)`` MySQL dataset. I
couldn't get into the MySQL instance so I reached out on IRC.
Johngrasty, a friendly guy in the ``#smartos`` IRC channel, provided a
command to display the randomly generated MySQL password emitted to the
zone-init log:

::

    cat /var/svc/log/system-zoneinit\:default.log | grep MYSQL_PW

I used this initial password to get into the ``mysql>`` shell and
changed it with this SQL statement:

::

    mysql> SET PASSWORD = PASSWORD('clear-text-password');

Johngrasty also supplied a snippet of JSON which shows how to declare
root MySQL password:

::

    {
      ... truncated ...
      "customer_metadata": {
        "salt-master": "10.0.0.101",
        "salt-id": "mysql1"
      },
      "internal_metadata": {
        "mysql_pw": "mypassword"
      }
    }

I looked for help in the #project-fifo channel as to why the GUI does
not work for assigning initial MySQL password. MerlinDMC, the author and
operator of `datasets.at <https://datasets.at>`__, gave me the following
command to run in the Global Zone to look at a particular zone's
metadata:

::

    cat /zones/uuid-of-zone-goes-here/config/metadata.json

Turns out the GUI is placing the ``"mysql_pw"`` parameter into
``"customer_metadata"`` instead of ``"internal_metadata"`` which is
invalid.
