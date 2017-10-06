russell.ballestrini.net
#######################

This is the source code for my blog. My blog is a static web site with just HTML!
This project uses Pelican (a static site generator) to produce HTML from ``.rst`` or ``.md`` files.

Pelican is written in Python and uses Jinja2 template engine by default.

development
===============================

In development I use a ``make`` file to hold common build and test commands::

  make clean && make html && make serve


production release process
===============================

I use `Jenkins to build this site and Salt Stack to release it <http://russell.ballestrini.net/securely-publish-jenkins-build-artifacts-on-salt-master/>`_


