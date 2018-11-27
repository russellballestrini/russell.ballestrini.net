Simplify deployments with Upstart and uWSGI
###########################################
:date: 2013-10-19 22:35
:author: Russell Ballestrini
:tags: DevOps, Opinion
:slug: simplify-deployments-with-upstart-and-uwsgi
:status: published

As you know from my previous post, I recently `deleted
LinkPeek.com <https://russell.ballestrini.net/honey-i-just-deleted-linkpeek-com/>`__
and after struggling to get it back online, I vowed to start utilizing
configuration management. During this exercise, I noticed that the
architecture I use in production seems overly complicated.

**The current production deployment stack:**

-  Nginx listen on 80/443 proxy upstream 9901/9902
-  Upstart => Supervisord => Cherrypy/Paste listen on 9901/9902

*Each of these services and processes have their own configuration files
which must work together. Upstart needs to know the location of
Supervisord's configuration files. Supervisord needs to know the
location of Cherrypy/PasteDeploy's configuration files. Supervisord also
must bring up a specified number of worker processes who listen on a
pool of ports. Nginx needs to proxy upstream to that pool of worker
ports.*

This architecture seems difficult to automate because of the numerous
places errors may sneak in. I started researching an alternative
architecture and stumbled upon Nicholas Piel's `Benchmark of Python Web
Servers <https://nichol.as/benchmark-of-python-web-servers>`__. The
graphs Nicholas compiled allowed me to narrow down a list of potential
replacements.

I chose to review uWSGI first because it was a top contender on every
chart. After briefly testing uWSGI, I halted my explorations and
selected it as the winner. I know you probably feel that was a premature
decision but uWSGI fit what I was looking for.

**The new simplified stack:**

-  Nginx listen on 80/443 proxy upstream 5200
-  Upstart => uWSGI listen on 5200

The uWSGI server possesses great performance out-of-the-box but also
presents many options for fine tuning. These options may be specified
either directly in the Upstart script using flags or in a configuration
file (like a Pyramid .ini). Either way, the stack uses less files, less
processes, and less complexity then the original architecture. For
`LinkPeek <https://linkpeek.com>`__ deployments I decided to place all
uWSGI related configuration directly in the Upstart script which I
embedded below:

**linkpeek/weblinkpeek.conf \| Upstart for starting uWSGI**

::

    description "Start the uWSGI master for the LinkPeek WEB"

    start on runlevel [2345]
    stop on runlevel [!2345]

    respawn

    # run service as linkpeek user
    setuid linkpeek
    setgid linkpeek

    # uWSGI command to execute and treat as a daemon
    exec /path/to/linkpeek/web/env/bin/uwsgi --master --processes=4 --http=127.0.0.1:5200 --die-on-term --logto2=/path/to/linkpeek/web/uwsgi.log --virtualenv=/path/to/linkpeek/web/env --ini-paste=/path/to/linkpeek/web/linkpeek/production.ini

.. raw:: html

   </p>

The web application is now daemonized and listening on port 5200 with 4
workers. I leave implementing the Nginx front end to the reader.
