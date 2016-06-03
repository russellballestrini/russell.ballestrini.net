sensu-salt 
###########
:date: 2013-12-17 11:35
:author: Russell Ballestrini
:tags: DevOps, Guide
:slug: sensu-salt
:status: published

A while back I explained how to `Create your own fleet of servers with
Digital Ocean and
salt-cloud <http://russell.ballestrini.net/create-your-own-fleet-of-servers-with-digital-ocean-and-salt-cloud/>`__.
Today I will extend that post and show how I deployed a test environment
for `Sensu, an open source monitoring
framework <http://sensuapp.org/>`__.

Before I test out new infrastructure software, I always attempt to write
deployment manifests. I subject myself to this exercise for the
following reasons:

-  to get better at configuration management (self growth)
-  to enable quick setup and tear down of test environments (save money)
-  to make sure the new software may be deployed and maintained in
   configuration management (a must)
-  to document the install process and leave comments (my notes double
   as automation scripts!)
-  to allow knowledge transfer (sharing is caring, you're welcome!)

The state formulas in this post were tested on Ubuntu 12.04.3 x64bit.

**Clone or fork the Salt-State tree**

https://github.com/sensu/sensu-salt

::

    git clone https://github.com/sensu/sensu-salt.git

.. raw:: html

   </p>

**Declare deployment targets**

Before deployment, we must declare some targets in the top.sls file:

::

      '*':
        - git

      'sensu-client*':
        - sensu.client

      'sensu-server*':
        - rabbitmq.server
        - redis.server
        - sensu.server
        - sensu.client

.. raw:: html

   </p>

**Stand up Sensu test environment**

I used the following ``salt-cloud`` command to create the sensu monitor
server:

::

    salt-cloud --profile ubuntu_do sensu-server && salt 'sensu-server' state.highstate

.. raw:: html

   </p>

Once the sensu-server was live, I altered the ``client-config.json`` and
modified the RabbitMQ host with the new ``sensu-server``'s IP or DNS
record.

I then spun up 4 sensu-clients using the following command:

::

    salt-cloud -P --profile ubuntu_do sensu-client1 sensu-client2 sensu-client3 sensu-client4 && salt 'sensu-client*' state.highstate

.. raw:: html

   </p>

This caused 4 cloud servers to be spawned in parallel, and when the
provisioning finished, they instantly appeared in the
``sensu-dashboard`` which runs on the ``sensu-server``.

**Tear down Sensu test environment**

Later when I was done messing with writing checks, I used the following
``salt-cloud`` commands to destroy the sensu server and clients:

::

    salt-cloud --destroy sensu-server
    salt-cloud --destroy sensu-client1 sensu-client2 sensu-client3 sensu-client4

.. raw:: html

   </p>
