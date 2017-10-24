webwords: a minimal viable web app with docker in as many languages as possible
#################################################################################

:author: Russell Ballestrini
:slug: webwords-is-a-minimal-viable-web-app-with-docker-in-as-many-languages-as-possible
:date: 2017-10-24 12:11
:tags: Code, DevOps
:status: published

The companion `webwords git repo <https://github.com/russellballestrini/webwords>`_ lives here.

This project shows how to code the same minimal web app called ``webwords`` in as many different programming languages as possible.
It also provides a guides for building and running ``webwords`` as a docker image.

.. contents::

what is webwords
================

A simple web application whose spec accepts the following two query parameters —

keyword:
 The ``keyword`` you want to search for.

target:
 The URI ``target`` that you want to search.

The application always returns an ``HTTP 200`` response and the string ``true`` or ``false`` depending on if the keyword is found in the ``target`` web page body.

Once you have the application running inside docker, run this command to get the exposed port:

.. code-block:: bash

 docker ps

To see if a ``keyword`` exists on a ``target`` web page, put the follwing in a browser:

.. code-block:: txt

 http://127.0.0.1:32779/?keyword=potato&target=https://www.remarkbox.com

In this example we check if the keyword ``potato`` is on the web page https://www.remarkbox.com (spoiler, it is)

Note: You will need to replace the port of ``32779`` with the port from the ``docker ps`` output.



go
========

To build the docker image:

.. code-block:: bash

 cd go
 docker build -t webwords-go .

To run a test container from the new image:

.. code-block:: bash

 docker run -d -p 8888 webwords-go

python
========

To build the docker image:

.. code-block:: bash

 cd python
 docker build -t webwords-python .

To run a test container from the new image:

.. code-block:: bash

 docker run -d -p 8888 webwords-python


debugging
=========

If you're anything like me, your programs rarely compile or work properly on the first try.
Just like with programming, a docker image will rarely build correct the first time so you will need to learn how to debug.

To debug, get the failed docker container's id:

.. code-block:: bash

 docker ps --all

Once you have the id, you can run the following to see the error:

.. code-block:: bash

 docker logs <container-id>

Debug the issue, fix your ``Dockerfile``, and retry the build process until you have it working.

You can delete old attempts by running:

.. code-block:: bash

 docker rm <container-id>
