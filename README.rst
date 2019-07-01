russell.ballestrini.net
#######################

This is the source code for `my blog <https://russell.ballestrini.net>`_. My blog is a static web site with just HTML!
This project uses Pelican (a static site generator) to produce HTML from ``.rst`` or ``.md`` files.

Pelican is written in Python and uses Jinja2 template engine by default.

development
===============================

Clone this repo, then in the ``pelican-themes`` directory clone this repo:

.. code-block:: bash

 cd pelican-themes
 git clone git@github.com:russellballestrini/pelican-svbhack.git
 cd ..

Next clone the `pelican-plugins` repo (I use ``random_article``)

.. code-block:: bash

 git clone git@github.com:getpelican/pelican-plugins.git

In development I use a ``make`` file to hold common build and test commands::

  make clean && make html && make serve

I also manage my resume using ``.rst`` and I use the ``rst2pdf`` tool to turn it into a ``.pdf``::

  make clean && make html && make resume

production release process
===============================

I use `Jenkins to build this site and Salt Stack to release it <http://russell.ballestrini.net/securely-publish-jenkins-build-artifacts-on-salt-master/>`_

Any web server may be used to host an HTML site. I choose nginx in production because it is known to be very fast at serving static files.

I use environment variables in my ``pelicanconf.py`` to store secrets.

For example:  `LinkPeek screenshots <https://linkpeek.com>`_ or `Remarkbox comments <https://www.remarkbox.com>`_.
