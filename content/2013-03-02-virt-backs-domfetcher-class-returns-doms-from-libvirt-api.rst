virt-back's Domfetcher class returns doms from libvirt API
##########################################################
:date: 2013-03-02 15:04
:author: Russell Ballestrini
:tags: Code, DevOps
:slug: virt-backs-domfetcher-class-returns-doms-from-libvirt-api
:status: published
:summary:

|2013-03-02-scale-virt-back-domfetcher-scaled|

**I'm hooked...**

I attended SCaLE 11x, my first technical conference, and had an amazing
time. My favorite talk was Michael Day's "`Advancements with Open
Virtualization &
KVM <http://code.ncultra.org/2013/02/scale-11x-open-virtualization/>`__\ "
(link to slides). Michael's presentation inspired me to continue my work
on virt-back.

During my trip home I used the in-flight wifi to push this
`commit <https://bitbucket.org/russellballestrini/virt-back/commits/d6dff27323650bf784cc284f676299ffe07953cb>`__
into the cloud from the clouds! This particular commit re-factored the
dom object list generation into a simple-to-use class called Domfetcher.
Domfetcher abstracts the libvirt API and grants access to the following
helper methods:

| **get\_all\_doms( )**
|  Return a list of all dom objects

| **get\_doms\_by\_names( guest\_names=[] )**
|  Accept a list of guest\_names, return a list of related dom objects

| **get\_running\_doms( )**
|  Return a list of running dom objects

| **get\_shutoff\_doms( )**
|  Return a list of shutoff but defined dom objects

**This is an example of how to use Domfetcher:**

::

    import virtback

    # optionally supply hypervisor uri
    domfetcher = virtback.Domfetcher()

    doms = domfetcher.get_running_doms()

    for dom in doms:
        print dom.name()

    for dom in doms:
        print dom.info()

    for dom in doms:
        print dom.shutdown()

.. raw:: html

   </p>

As always thanks for reading!

.. |2013-03-02-scale-virt-back-domfetcher-scaled| image:: /uploads/2013/03/2013-03-02-scale-virt-back-domfetcher-scaled.png
   :target: /uploads/2013/03/2013-03-02-scale-virt-back-domfetcher-scaled.png
