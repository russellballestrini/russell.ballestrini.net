Securely publish Jenkins build artifacts on Salt Master
#######################################################
:date: 2015-02-22 12:39
:author: Russell Ballestrini
:tags: DevOps, Guide
:slug: securely-publish-jenkins-build-artifacts-on-salt-master
:status: published
:summary:
  Your project deserves an asset pipeline.

Do you want a secure setup for publishing and staging build artifacts
from a Jenkins build server to a Salt Master? This guide describes my
fully automated pipeline to transport binaries using Salt's encrypted
"bus".

We start off with some Salt States to stand up a Jenkins build server
"client":

**jenkins/client.sls:**

::

    # https://russell.ballestrini.net/securely-publish-jenkins-build-artifacts-on-salt-master/
    # manage jenkins user, home dir, and Jenkins "master" public SSH key.
    jenkins:
      user.present:
        - fullname: jenkins butler
        - shell: /bin/bash
        - home: /home/jenkins

      file.directory:
        - name: /home/jenkins
        - user: jenkins
        - group: jenkins
        - require:
          - user: jenkins

      ssh_auth.present:
        - user: jenkins
        - name: {{ pillar.get('jenkins-public-key') }}
        - require:
          - user: jenkins

    # Manage a script to push artifacts to Salt Master.
    # Note: jenkins user should _not_ have ability to change this file.
    /opt/salt-call-put-artifacts-onto-salt-master.sh:
      file.managed:
        - user: root
        - group: jenkins
        - mode: 755
        - contents: |
            #!/bin/bash
            set -x
            salt-call cp.push_dir "$PWD" glob='*.tar.gz'
            salt-call cp.push "$PWD/commit-hash.txt"
        - require:
          - file: jenkins

    # Allow jenkins to run push script as root via sudo.
    jenkins-sudoers:
      file.append:
        - name: /etc/sudoers
        - text:
          - "jenkins    ALL = NOPASSWD: /opt/salt-call-put-artifacts-onto-salt-master.sh"

.. raw:: html

   </p>

On the Salt Master we must enable MinionFS and restart Salt Master
process:

::

    fileserver_backend:
      - roots
      - minion

    file_recv: True

.. raw:: html

   </p>

We then use this command as the last build task in every Jenkins build
job:

::

    sudo /home/jenkins/salt-call-put-artifacts-onto-salt-master.sh

This causes the file to be staged on the Salt Master on a successful
build.

The Salt States to deploy the software to production, look something
like this:

::

    # extract tarball from Salt Master using MinionFS.
    extract-tarball-for-mysite:
      archive.extracted:
        - name: /www/mysite
        - archive_format: tar
        - source: salt://ubuntu-jenkins.foxhop.net/home/jenkins/workspace/job-name/env.tar.gz
        - user: uwsgi
        - group: uwsgi
        # I want to always extract, not sure a better way.
        - if_missing: /dev/taco
        - require:
          - service: make-mysite-dead-for-release

.. raw:: html

   </p>

I also have build triggers which monitor remote git/hg repos for
changes. Pushing code triggers a build which tests my code base and
securely publishes to my Salt Master. When the time comes to perform a
release, all I have to do is run highstate, because the pipeline did all
the other work for me!

**Update**

Special thanks to an `anonymous commentor <#efbc6dc7-02e3-11e9-b440-040140774501>`_ regarding how to increase security. I have updated the scripts accordingly.
