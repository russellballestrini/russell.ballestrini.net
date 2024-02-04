Installing YaCy on Ubuntu
#########################

:author: Russell Ballestrini
:slug: installing-yacy-on-ubuntu
:date: 2024-02-04 11:02
:tags: Code, DevOps
:status: published


This guide will walk you through installing YaCy on Ubuntu.

By default YaCy is configured to bind to ``0.0.0.0`` but it's admin interface is only accessible by default to a white list which includes ``localhost`` and ``127.0.0.1``, since my install is headless on a remote Ubuntu server, I access the admin interface remotely via an SSH tunnel.

Installing YaCy
---------------

run this script in a terminal, ``install_yacy.sh``:

.. code-block:: bash

    #!/bin/bash

    # Update package lists
    sudo apt-get update

    # Install Java Development Kit (JDK)
    sudo apt-get install -y openjdk-21-jdk

    # Check if Java is correctly installed
    java -version

    # Download YaCy
    wget https://download.yacy.net/yacy_v1.924_20210209_10069.tar.gz

    # Extract the downloaded file
    tar xfz yacy_v1.924_20210209_10069.tar.gz

    # Change to the extracted directory
    cd yacy

    # Start YaCy
    ./startYACY.sh

Accessing the Admin Interface Remotely via an SSH Tunnel
-----------------------------------------------------------

You can create an SSH tunnel to your remote YaCy server, for example ``yacy.foxhop.net`` so that when you access ``localhost:8090``, it tunnels to the remote host.

Open a terminal on your local machine and run the following command:

.. code-block:: bash

    ssh -L 8090:localhost:8090 user@yacy.foxhop.net

Replace `user` with your username on the remote host. Now, when you access `localhost:8090` on your local machine, it will be tunneled to the remote host.

What's next?
----------------

you can kick off a local crawl and depending on your peer mode status you can share the results the to network, I'm still working on figuring out how to find my peer mode status, but my guess is I'll need to open port ``8090`` in my NAT on the router and forward it to the new host.  That said I'd rather be able to see my state before and after and also the reason for wanting to share the crawl index with the nextwork is the scrape can be done once and then shared with any computer using YaCy, instead of the query only working for local host.

At least that's the theory behind DHT.

I'll keep tinkering and hopefully keep this section updated with my findings.
