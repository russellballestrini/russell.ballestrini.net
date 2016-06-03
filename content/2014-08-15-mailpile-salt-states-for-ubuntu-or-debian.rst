Mailpile Salt States for Ubuntu or Debian
#########################################
:date: 2014-08-15 20:32
:author: Russell Ballestrini
:tags: DevOps
:slug: mailpile-salt-states-for-ubuntu-or-debian
:status: published

I wrote these Salt States to install Mailpile on an Ubuntu host. Fun
fact, it took me 20 minutes to write these states and they worked the
first time I ran them. Disclaimer - I used a throw away server and
wasn't concerned that buckets of packages were installed to the system
instead of using a virtualenv.

::

    cd /opt/Mailpile
    ./mp --set sys.http_host=0.0.0.0
    ./mp

.. raw:: html

   </p>

Then open a web browser the IP address of the host running the mp
command and follow the prompts to setup the server/client/app.

**mailpile/init.sls:**

::

    # Clone the source repository
    mailpile-git-latest:
      git.latest:
        - name: https://github.com/pagekite/Mailpile.git
        - target: /opt/Mailpile

    # install the system requirements
    mailpile-system-packages:
      pkg.installed:
        - names:
          - make
          - python-imaging
          - python-lxml
          - python-jinja2
          - pep8
          - ruby-dev
          - yui-compressor
          - python-nose
          - spambayes
          - phantomjs
          - python-pip
          - python-mock
          - python-pexpect
          {% if grains['lsb_distrib_release']|float >= 14.04 %}
          - rubygems-integration
          {% else %}
          - rubygems
          {% endif %}

    # install some python requirements with pip
    mailpile-pip-packages:
      pip.installed:
        - names:
          - pgpdump
          - selenium >= 2.40.0
        - require:
          - pkg: mailpile-system-packages

    # install some ruby requirements with gem
    mailpile-gem-packages:
      gem.installed:
        - names:
          - therubyracer
          - less
        - require:
          - pkg: mailpile-system-packages

.. raw:: html

   </p>
