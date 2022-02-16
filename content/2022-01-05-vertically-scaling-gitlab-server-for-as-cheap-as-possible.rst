Vertically Scaling GitLab Server For As Cheap As Possible
################################################################

:author: Russell Ballestrini
:slug: vertically-scaling-gitlab-server-for-as-cheap-as-possible
:date: 2022-01-05 19:13
:tags: Code, DevOps
:status: published

Today's essay acts as a power-up love story for the underdog.

A living document & quickstart for:

* bootstrappers
* small business under 99 employees
* solo ops or devs
* entrepreneurs
* hackers
* tinkerers

You also deserve a quick start to a GitLab Server power house!

Regardless of my intended audience, this strategy should scale to
500-1,000 concurrent engineers on the smallest of the instance classes
which satisfy the current GitLab Server "minimum requirements".

* https://docs.gitlab.com/ee/install/requirements.html



Why GitLab Server?
====================

* GitLab is open source (not black box)
* GitLab CI is a game changer
* GitLab CI is extendable to any workflow
* GitLab Server wants 4G of memory



Expected Results
=====================

This guide prescribes the following setup:

* A Physical or Virtual Machine with at least 4G of RAM
* Docker installed
* Docker container started via docker-compose to manage
  a monolithic Omnibus installation of GitLab Server
* A Cronjob to backup GitLab Server to ``/tmp``
* A Cronjob to collect Gitlab Server backup tarball & ``/etc/gitlab/gitlab-secrets.json``
* A strong recommendation to test the complete backup and recovery process
  at least once to prepare for when times get rough.



GitLab Server Omnibus In Docker
===================================

The installation & configuration is documented using SaltStack to make it easy
to spin up GitLab Servers.

To install SaltStack on the new host dedicated for GitLab Server, Run the following:

.. code-block:: bash

 wget -O - https://bootstrap.saltstack.com | sudo sh -s -- stable;
 echo "master: salt.example.com" >> /etc/salt/minion.d/custom.conf;
 sudo service salt-minion restart

On the instance designated as salt-master, accept the new salt-minion key:

.. code-block:: bash

 sudo salt-key -a git2.unturf.com
 The following keys are going to be accepted:
 Unaccepted Keys:
 Git2.unturf.com
 Proceed? [n/Y] y

and make sure communication is established:

.. code-block:: bash

 sudo salt "git2*" test.ping
 git2.unturf.com:
     True

and run a highstate to configure that new host instance:

.. code-block:: bash

 sudo salt "git2*" state.highstate

Once the command returns, assuming we had no errors or failures we
have docker installed and an Omnibus Gitlab Server booted inside a container.

.. code-block:: bash

 Summary for git2.unturf.com
 --------------
 Succeeded: 104 (changed=69)
 Failed:      0
 --------------
 Total states run:     104
 Total run time:   194.431 s

The GitLab Server's internal services take over 3 minutes to come online.


Disaster Recovery
=====================

Prepare for real disaster by practicing the entire backup and restore process.

As extra homework, it is high advisable to spin up a 2nd host for GitLab Server
in order to test the backup and restore process from start to finish:

https://docs.gitlab.com/ee/raketasks/backup_restore.html#restore-gitlab



GitLab CI is a game changer.
 Gitlab is like Circle CI 2.0 only not black box.

GitLab CI is extendable to any workflow
 but you should keep it simple, learn to use the tool as intended,
 and rethink legacy workflows rather than port.
