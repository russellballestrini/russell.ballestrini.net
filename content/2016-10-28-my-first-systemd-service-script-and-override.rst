My first Systemd Service Script and Override
##############################################

:author: Russell Ballestrini
:slug: my-first-systemd-service-script-and-override
:date: 2016-10-28 15:54
:tags: Code, DevOps
:status: published

At work we mostly run Centos and I have some NodeJS services to deploy.
I feel most familiar with Ubuntu / Upstart so this post serves as my notes.

In this contrived example, we define a service for our `taco-api` application.
The `taco-api` source code lives in `/opt/taco-api`.

We manage a static `.service` file using a package or config management.

`/lib/systemd/system/taco-api.service`:

.. code-block:: ini

 [Unit]
 Description=Node.js service for taco API

 [Service]

 Environment=NODE_ENV=development

 ExecStart=/usr/bin/node /opt/taco-api/app.js

 # Restart service after all crashes but wait 10 seconds between restarts.
 Restart=always
 RestartSec=10

 # output stdout and stderr to syslog. (/var/log/messages) 
 StandardOutput=syslog
 StandardError=syslog
 SyslogIdentifier=taco-api

 # define the user and group to own the process.
 #User=node
 #Group=node

 # change directory before running ExecStart command.
 WorkingDirectory=/opt/taco-api

 [Install]
 WantedBy=multi-user.target

We also manage a static `override.conf` file using config management.
In this file, we customize the environment variables present.

`/etc/systemd/system/forcare-api.service.d/override.conf`:

.. code-block:: ini

 [Service]
 Environment=NODE_ENV=production

This allows us to only override and keep track of the deltas.

You can test, like this:

.. code-block:: bash

 # emit the status of the service.
 service taco-api status

 # start the service.
 service taco-api start

 # look at the process list, note that node is running.
 ps aux | grep node

 # emit the status of the service.
 service taco-api status

 # start the service.
 service taco-api stop

 # look at the process list, note that node is not running.
 ps aux | grep node

Thank you!

