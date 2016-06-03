Add a custom header to all Salt managed files using pillar and jinja templates
##############################################################################
:date: 2013-07-01 14:11
:author: Russell Ballestrini
:tags: DevOps, Guide
:slug: add-a-custom-header-to-all-salt-managed-files-using-pillar-and-jinja-templates
:status: published

Salt-stack (salt) provides a solution for centralized configuration
management and remote execution. One of the most basic things Salt
provides is the ability to manage the contents of a file or a directory
of files. Using Salt we can dictate the state of our minions and as a
result we also gain auto-healing of configuration files.

Salt will clobber local changes to managed files and force the state to
reflect the version in configuration management. In an effort to avoid
confusing the uninformed, I place a header on each managed file which
announces "THIS FILE IS MANAGED BY SALT".

To avoid repeating myself in each managed file, I came up with the
following centralized solution -

First, I give all minions access to the headers pillar tree in top.sls:

::

    base:
      '*':
        - headers

Next, I create a couple headers in in headers/init.sls:

::

    headers:
      salt:
        file: |
            ################################
            # THIS FILE IS MANAGED BY SALT #
            ################################
        directory: |
            #####################################
            # THIS DIRECTORY IS MANAGED BY SALT #
            #####################################

Then, I parse each managed file in the state tree with jinja, for
example hosts/init.sls:

::

    /etc/hosts:
      file.managed:
        source: salt://hosts/hosts
        user: root
        group: group
        mode: 644
        template: jinja

Finally, in each file served by salt I add the jinja header
substitution, for example hosts/hosts:

::

    {{pillar['headers']['salt']['file']}}
    127.0.0.1       localhost.localdomain localhost
    ::1     localhost6.localdomain6 localhost6

I use this same technique to declare most configuration options as
parameters, like hostnames, IP addresses, ports, and more.
