A system administrators guide to installing and maintaining multiple python environments
########################################################################################

:date: 2011-09-08 19:28
:author: Russell Ballestrini
:tags: DevOps, Guide
:slug: a-system-administrators-guide-to-installing-and-maintaining-multiple-python-environments
:status: published

.. contents::

Some operating systems depend on a specific version of python to
function properly. For example, Yum on Redhat Enterprise Linux 5 (RHEL5)
depends on python 2.4.3. This version of python lacks support from many
utilities and 3rd party libraries. This guide will cover installing an
alternative python instance while leaving the system's python alone.

*This guide supports the following operating systems: Redhat, CentOS,
and Fedora. As of this publication the latest Python version was 2.7.8;
You might want to determine if a newer version exists.*

Install Python 2.7
==================

I found two methods which work for installing Python 2.7 side-by-side with the system's Python.

* compile from source
* install package via the *scl* repo

Choose which ever strategy you find easier.

Compile from source
-------------------

#. Gather the dependencies::

    yum install gcc zlib-devel python-setuptools readline-devel

   - **gcc** is a compiler used to build python 
   - **zlib-devel** allows the python zlib module to be built
   - **python-setuptools** provides the easy_install application
   - **readline-devel** arrows readline and history handling in python shell

#. Download and untar the python sourcecode::

    wget http://www.python.org/ftp/python/2.7.8/Python-2.7.8.tgz
    tar -xzvf Python-2.7.8.tgz
    cd Python-2.7.8


#. Compile the sourcecode::

    ./configure
    make altinstall

#. Test new alternative python::

    python2.7 --version

#. Document path to new python2.7, you will need it if you plan to use a virtualenv::

    which python2.7

#. Now we can install third party libraries into our alternative python::

    python2.7 -m easy_install

Install package from scl
------------------------

#. install centos-release-scl repolists::

    sudo yum install centos-release-scl

#. install python27::

    sudo yum install python27

#. enable python27 via scl::

    scl enable python27 bash

#. Document path to new python2.7, you will need it if you plan to use a virtualenv::

    which python2.7


virtualenv
==========

Optionally we can create a virtualenv (for development) based on the
python 2.7 install. Virtual environments appear useful for testing
packages and libraries without installing them to the system owned
python site-packages directory.

#. Install pip using easy\_install::

    sudo easy_install pip

#. Install virtualenv using pip::

    sudo pip install virtualenv

#. Create a new virtual python environment named virtpy::

    cd ~
    virtualenv -p /usr/local/bin/python2.7 virtpy

   This will create a virtual python 2.7.2 environment named virtpy in your present working directory.

   To invoke this environment run source virtpy/bin/activate and your prompt should change to reflect the active virtualenv.

   Now you can run easy_install to install packages into virtpy/lib/python2.7/site-packages.

**Thanks for reading, that's all for now.**
