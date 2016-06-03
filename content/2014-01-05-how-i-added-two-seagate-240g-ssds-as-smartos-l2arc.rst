How I added two Seagate 240G SSDs as SmartOS L2ARC
##################################################
:date: 2014-01-05 14:56
:author: Russell Ballestrini
:tags: Guide
:slug: how-i-added-two-seagate-240g-ssds-as-smartos-l2arc
:status: published

**How I added two Seagate 240G SSDs as SmartOS L2ARC**

#. removed icepacks from two western digital velociraptors
#. installed ssds into icepacks
#. installed icepacks into HP hotswap trays
#. installed trays into HP prolaient g6 server

**How to list all drive installed in Solaris, Open Solaris, or SmartOS**

::

    iostat -eE

::

    format

.. raw:: html

   </p>

::

    AVAILABLE DISK SELECTIONS:
           0. c1t0d0 
              /pci@0,0/pci103c,330b@1f,2/disk@0,0
           1. c1t1d0 
              /pci@0,0/pci103c,330b@1f,2/disk@1,0
           2. c1t2d0 
              /pci@0,0/pci103c,330b@1f,2/disk@2,0
           3. c1t3d0 
              /pci@0,0/pci103c,330b@1f,2/disk@3,0

.. raw:: html

   </p>

**list zpools:**

::

    zpool list

::

    NAME    SIZE  ALLOC   FREE  EXPANDSZ    CAP  DEDUP  HEALTH  ALTROOT
    zones  1.81T  41.4G  1.77T         -     2%  1.00x  ONLINE  -

.. raw:: html

   </p>

**Add the two 240G SSDs as L2ARC devices:**

::

    zpool add zones cache c1t2d0 c1t3d0

.. raw:: html

   </p>

**Look at the iostats of the drives in the zpool**

::

    zpool iostat -v

::

                   capacity     operations    bandwidth
    pool        alloc   free   read  write   read  write
    ----------  -----  -----  -----  -----  -----  -----
    zones       41.4G  1.77T      5     46  78.7K   730K
      mirror    41.4G  1.77T      5     46  78.7K   730K
        c1t0d0      -      -      0     15  41.5K   733K
        c1t1d0      -      -      0     15  41.6K   733K
    cache           -      -      -      -      -      -
      c1t2d0    14.6M   224G      0      3  2.48K   273K
      c1t3d0    45.5M   224G      0      6  2.48K   852K
    ----------  -----  -----  -----  -----  -----  -----

.. raw:: html

   </p>

This machine is a test hypervisor and after reviewing the output from
``zpool iostat -v`` over the last couple days, I'm pretty sure adding
L2ARC to this box was not needed, but it was a great learning
experience.
