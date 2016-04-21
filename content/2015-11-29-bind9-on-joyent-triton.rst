Bind9 on Joyent Triton 
======================

:author: Russell Ballestrini
:slug: bind9-on-joyent-triton
:date: 2015-11-29 18:47
:tags: Operations
:status: published
:summary:
 Tricks to reduce Bind9's large memory footprint on Joyent Triton.

I have a single DNS server running on a KVM at DigitalOcean for $5/mo. I might move to Joyent and use 2 x 128M Ubuntu containers for $2.23/mo each.

In my first test Bind9 (named RNDC) ended up using 111M of memory on a 256M Ubuntu Triton container.

The large 111M memory footprint correlated with the amount of worker threads running. Bind9 determines the number of worker threads to manage by the number of CPUs detected by the OS.

In my case, Ubuntu detected 48 CPUs because Joyent containers run on bare-metal.

We can see this by running the following commands:

.. code-block:: bash

 cat /proc/cpuinfo | grep processor | wc -l                                                  
 48  

.. code-block:: bash

 sudo rndc status    
 version: 9.9.5-3ubuntu0.5-Ubuntu <id:f9b8a50e>                           
 CPUs found: 48                                                           
 worker threads: 48                                                        
 UDP listeners per interface: 1                                           
 number of zones: 216                                                     
 debug level: 0                                                           
 xfers running: 0                                                         
 xfers deferred: 0                                                        
 soa queries in progress: 0                                               
 query logging is OFF                                                     
 recursive clients: 0/0/1000                                              
 tcp clients: 0/100                                                       
 server is up and running 

To fix this, at least on Ubuntu, we need to pass `-n 2` to limit the `worker threads` to 2.

For Ubuntu, edit `/etc/default/bind9`:

.. code-block:: bash

 OPTIONS="-u bind -n 2"

Then restart the `bind9` service and verify using `sudo rndc status` and `free -m`.

.. code-block:: bash

 sudo service bind9 restart
 sudo rndc status
 free -m

