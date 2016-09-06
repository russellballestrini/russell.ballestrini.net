Set static hostname for RHEL Centos 7 on AWS
################################################################

:author: Russell Ballestrini
:slug: set-static-hostname-for-rhel-centos-7-on-aws
:date: 2016-09-06 11:18
:tags: Code, DevOps
:status: published

This took me about 2 hours to figure out, hopefully it saves you time.

/etc/sysconfig/network::

 HOSTNAME=desired-hostname.example.com

/etc/hostname::

 desired-hostname.example.com

/etc/cloud/cloud.cfg::

 preserve_hostname: true

