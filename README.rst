russell.ballestrini.net
#######################

This is the source code for my blog. My blog is a static web site with just HTML!
This project uses Pelican (a static site generator) to produce HTML from ``.rst`` or ``.md`` files.

Pelican is written in Python and uses Jinja2 template engine by default.

development
===============================

In development I use a ``make`` file to hold common build and test commands::

  make clean && make html && make serve

I also manage my resume using ``.rst`` and I use the ``rst2pdf`` tool to turn it into a ``.pdf``::

  make clean && make html && make resume

production release process
===============================

I use `Jenkins to build this site and Salt Stack to release it <http://russell.ballestrini.net/securely-publish-jenkins-build-artifacts-on-salt-master/>`_

Any web server may be used to host an HTML site.  I choose nginx in production because it is known to be very fast at serving static files.

I use environment variables in my ``pelicanconf.py`` to store secrets for things like  `LinkPeek (web page screenshots as a service) <https://linkpeek.com>`_ or `Remarkbox comments as a service <https://www.remarkbox.com>`_.
