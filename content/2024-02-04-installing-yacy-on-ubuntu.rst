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

Securing YaCy Portal and admin access with SSL/TLS
---------------------------------------------------

In the early days of YaCy, encryption was not as prevalent as it is today. However, securing your YaCy instance with SSL/TLS is essential for modern web safety standards. Here's how to enable SSL/TLS encryption for your YaCy server:

1. Generate a keystore using the ``keytool`` command:

   .. code-block:: bash

       keytool -keystore mySrvKeystore -genkey -keyalg RSA -alias yacy.foxhop.net

   This command creates a keystore file named ``mySrvKeystore``.

2. Move the ``mySrvKeystore`` file to the ``DATA/SETTINGS/`` directory in your YaCy installation:

   .. code-block:: bash

       mv mySrvKeystore /path/to/YaCy/DATA/SETTINGS/

3. Edit the ``yacy.conf`` file to configure YaCy to use the new keystore:

   .. code-block:: bash

       vim /path/to/YaCy/DATA/SETTINGS/yacy.conf

   Add or modify the following lines:

   .. code-block:: none

       keyStore=DATA/SETTINGS/mySrvKeystore
       keyStorePassword=YourKeystorePassword

   Replace ``YourKeystorePassword`` with the password you chose when you created the keystore with the ``keytool`` command.

4. Restart YaCy to apply the SSL/TLS settings:

   .. code-block:: bash

       /path/to/YaCy/stopYACY.sh
       /path/to/YaCy/startYACY.sh

Now, you can access the YaCy admin interface securely via ``https://localhost:8443``. By default, YaCy listens on port ``8443`` for HTTPS, but this can be changed in the admin console, as was done in this case to use port ``8091`` so that ``https://localhost:8091`` works instead. Ensure that HTTP remains on port ``8090`` for DHT network access by peers.

What's next?
------------

With SSL/TLS enabled, it's time to start a local crawl and consider sharing the results with the YaCy network. To do this, you may need to open port ``8090`` on your router and forward it to your YaCy host. Before making changes to your network configuration, verify your peer mode status in the YaCy admin interface to understand your node's role in the network.

Sharing your crawl index with the network allows for a distributed scraping effort, meaning that the data you collect can benefit all users of YaCy, not just your local instance. This is the essence of the Distributed Hash Table (DHT) that underpins YaCy's decentralized architecture.

Continue to explore the capabilities of your YaCy server, and remember to update your documentation to assist others in their journey toward a more open and collaborative internet.`
