Optimizing Memory Management for Plausible Docker on Ubuntu
################################################################

:author: Russell Ballestrini
:slug: optimizing-memory-management-for-plausible-docker-on-ubuntu
:date: 2024-02-05 17:40
:tags: Docker, Ubuntu
:status: published

Running Docker containers on a server with limited memory can lead to out-of-memory (OOM) issues, which can disrupt services and lead to downtime. This guide will show you how to increase swap space on an Ubuntu server to provide a buffer against OOM errors, using a real-world example from a server running multiple Docker containers.

Background
----------

Consider a typical scenario where an Ubuntu server is running several Docker containers:

.. code-block:: none

    fox@analytics:~$ sudo docker ps
    CONTAINER ID        IMAGE                                           PORTS                          NAMES
    7677a77e5606        plausible/analytics:v2.0                        0.0.0.0:8000->8000/tcp         plausible-plausible-1
    0ea79b7d0c03        clickhouse/clickhouse-server:23.3.7.5-alpine    8123/tcp, 9000/tcp, 9009/tcp   plausible-plausible_events_db-1
    33f6e8a30da4        postgres:14-alpine                              5432/tcp                       plausible-plausible_db-1
    40400c725d7c        bytemark/smtp                                   25/tcp                         plausible-mail-1

    fox@analytics:~$ free -m
                  total        used        free      shared  buff/cache   available
    Mem:            981         693          62          70         225          66
    Swap:             0           0           0

In this example, the server has less than 1 GB of RAM and no swap space configured. This configuration is prone to OOM errors, especially when the containers require more memory than what is available. In my case the service stayed online but the configuration management service ``salt-minion`` was unable to be reached to deploy new TLS certificates, the cert expired and prevented clients from sending metrics.

Creating and Enabling Swap Space
--------------------------------

To prevent OOM errors, we'll create a swap file. This script automates the process, ensuring that your system has additional virtual memory to handle peak loads.

Save the script as ``setup_swap.sh`` and execute it on your server:

.. code-block:: bash

    #!/bin/bash

    # Size of the swap file
    SWAP_SIZE=1G
    SWAP_FILE=/swapfile
    SWAPPINESS=10
    CACHE_PRESSURE=50

    # Create a swap file
    fallocate -l $SWAP_SIZE $SWAP_FILE || dd if=/dev/zero of=$SWAP_FILE bs=1024 count=1048576

    # Secure swap file permissions
    chmod 600 $SWAP_FILE

    # Set up a Linux swap area
    mkswap $SWAP_FILE

    # Enable the swap file
    swapon $SWAP_FILE

    # Make the swap file permanent
    echo "$SWAP_FILE none swap sw 0 0" | tee -a /etc/fstab

    # Set the swappiness value
    sysctl vm.swappiness=$SWAPPINESS
    echo "vm.swappiness=$SWAPPINESS" | tee -a /etc/sysctl.conf

    # Set the cache pressure value
    sysctl vm.vfs_cache_pressure=$CACHE_PRESSURE
    echo "vm.vfs_cache_pressure=$CACHE_PRESSURE" | tee -a /etc/sysctl.conf

    # Output the results
    echo "Swap file created and enabled:"
    swapon --show
    echo "Swappiness set to $SWAPPINESS and cache pressure set to $CACHE_PRESSURE."

This script will create a 1 GB swap file, configure the system to use it, and adjust kernel parameters to optimize memory usage.

Understanding Swappiness and Cache Pressure
------------------------------------------

The ``swappiness`` parameter influences how often the system uses swap space. A value of 10 encourages the system to keep processes in RAM, resorting to swap only when necessary.

The ``vfs_cache_pressure`` setting determines how aggressively the kernel reclaims memory from the cache. A value of 50 provides a balance between reclaiming memory and maintaining cache for quick file access.

Monitoring Your System
----------------------

After increasing the swap space, monitor your system's memory usage with:

.. code-block:: bash

    free -m

This will help you understand if the swap space is sufficient or if further adjustments are needed.

What's Next?
------------

By adding swap space and tuning kernel parameters, you've bolstered your server's ability to handle memory-intensive Docker containers. However, swap is not a replacement for physical RAM. If your server consistently uses a lot of swap, consider upgrading the RAM for better performance.

Stay proactive in managing your server's resources to ensure uninterrupted service for your Dockerized applications. Happy hosting!

