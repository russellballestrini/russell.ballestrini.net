Configuration Management vs Remote Execution
############################################
:date: 2013-07-11 23:15
:author: Russell Ballestrini
:tags: DevOps, Greatest Hits, Opinion
:slug: configuration-management-vs-remote-execution
:status: published
:summary:
  It's about time to learn the difference.

|config-mangement-vs-remote-execution|

| 

**What is configuration management?**

In a perfect world configuration management provides a centralized,
revision controlled, self-documented, change management location for
manifests and formulas which both define how to build a complete system
and organize a means of knowledge transfer. An infrastructure perfectly
described in configuration management allows any single part of the
system to be created, reproduced, multiplied, self-healed or even
re-purposed.

**When should I use configuration management?**

Use configuration management whenever you intend to permanently alter
system state or infrastructure data.

*System state - the current state of the system:*

-  operating system (distro,kernel,patches,hot-fixes)
-  software installed (base,role-specific)
-  services running (base,role-specific)
-  user access
-  etc

*Infrastructure data - the information that describes the
infrastructure:*

-  asset information (models,specs,IP,DNS,rack-elevation,etc)
-  roles (app,web,db,proxy,load-balancer,etc)
-  current allocations (allocated,unallocated,number of servers in each
   role,etc)
-  etc

**What is remote execution?**

Remote execution is the act of issuing commands to one or more remote
systems. The most popular remote execution system in use today is SSH.
SSH is great for maintaining a small group of dissimilar systems. Once
the system count grows and similar roles present themselves, start
looking at something like Fabric. Fabric is a python framework which
builds on top of the SSH protocol and makes it possible to invoke the
same command on hundreds of servers sequentially. Once the fleet count
reaches thousands of servers and commands must run in parallel, look at
Salt-stack's remote execution layer written with python and ZeroMQ.

**When should I use remote execution?**

Only use remote execution for ad hoc reports, data collection, or for
temporary tests which have no expectation of persistence after research
is complete. Frequent data collection jobs work best when implemented in
a metrics collection or monitoring system. (I'll save that for another
post)

**When should I not use remote execution?**

Do not use remote execution to change the state of the system or the
data which describes the infrastructure! If a remote execution job
changes either state or data it should be placed into the configuration
management for the reasons mentioned above.

.. |config-mangement-vs-remote-execution| image:: /uploads/2013/07/config-mangement-vs-remote-execution.png
