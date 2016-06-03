Postfix Salt State Formula
##########################
:date: 2013-10-17 21:28
:author: Russell Ballestrini
:tags: DevOps, Guide
:slug: postfix-salt-state-formula
:status: published
:summary:

|postfix-config-management|

The following formula was tested on Ubuntu and Debian however it would
not take much work to test on other operating systems.

This state formula will install postfix and mutt. The postfix service
will watch various configuration files for changes and restart
accordingly.

This formula will also manage and watch the /etc/aliases file and invoke
the *newaliases* command to initialize or re-initialize the alias
database. This formula will also manage and watch the
/etc/postfix/virtual file and invoke the *postmap* command to create or
update a managed Postfix lookup table.

**postfix/init.sls:**

::

    # Install mutt and postfix mutt packages.
    #
    # This formula supports setting an optional:
    #
    #  * 'aliases' file 
    #  * 'virtual' map file
    #
    # Both aliases and virtual use a pillar data schema
    # which takes the following form: 
    # 
    # postfix:
    #   aliases: |
    #       postmaster: root
    #       root: testuser
    #       testuser: russell@example.com
    #   virtual: |
    #       example.com             this is a comment
    #       test1@example.com       me@example.com
    #       test2@example.com       me@example.com
    #       

    # install mutt
    mutt:
      pkg:
        - installed

    # install postfix have service watch main.cf
    postfix:
      pkg:
        - installed
      service:
        - running
        - enable: True
        - watch:
          - pkg: postfix
          - file: /etc/postfix/main.cf

    # postfix main configuration file
    /etc/postfix/main.cf:
      file.managed:
        - source: salt://postfix/main.cf
        - user: root
        - group: root
        - mode: 644
        - template: jinja
        - require:
          - pkg: postfix

    # manage /etc/aliases if data found in pillar
    {% if 'aliases' in pillar.get('postfix', '') %}
    /etc/aliases:
      file.managed:
        - source: salt://postfix/aliases
        - user: root
        - group: root
        - mode: 644
        - template: jinja
        - require:
          - pkg: postfix

    run-newaliases:
      cmd.wait:
        - name: newaliases
        - cwd: /
        - watch:
          - file: /etc/aliases
    {% endif %}

    # manage /etc/postfix/virtual if data found in pillar
    {% if 'virtual' in pillar.get('postfix', '') %}
    /etc/postfix/virtual:
      file.managed:
        - source: salt://postfix/virtual
        - user: root
        - group: root
        - mode: 644
        - template: jinja
        - require:
          - pkg: postfix

    run-postmap:
      cmd.wait:
        - name: /usr/sbin/postmap /etc/postfix/virtual
        - cwd: /
        - watch:
          - file: /etc/postfix/virtual
    {% endif %}
     

**postfix/aliases:**

::

    # Managed by config management
    # See man 5 aliases for format
    {{pillar['postfix']['aliases']}}

**postfix/virtual:**

::

    # Managed by config management
    {{pillar['postfix']['virtual']}}

**postfix/main.cf:**

::

    # Managed by config management
    # See /usr/share/postfix/main.cf.dist for a commented, more complete version

    # Debian specific:  Specifying a file name will cause the first
    # line of that file to be used as the name.  The Debian default
    # is /etc/mailname.
    #myorigin = /etc/mailname

    smtpd_banner = $myhostname ESMTP $mail_name
    biff = no

    # appending .domain is the MUA's job.
    append_dot_mydomain = no

    # Uncomment the next line to generate "delayed mail" warnings
    #delay_warning_time = 4h

    readme_directory = no

    # TLS parameters
    smtpd_tls_cert_file=/etc/ssl/certs/ssl-cert-snakeoil.pem
    smtpd_tls_key_file=/etc/ssl/private/ssl-cert-snakeoil.key
    smtpd_use_tls=yes
    smtpd_tls_session_cache_database = btree:${data_directory}/smtpd_scache
    smtp_tls_session_cache_database = btree:${data_directory}/smtp_scache

    # See /usr/share/doc/postfix/TLS_README.gz in the postfix-doc package for
    # information on enabling SSL in the smtp client.

    myhostname = {{ grains['fqdn'] }}
    alias_maps = hash:/etc/aliases   
    alias_database = hash:/etc/aliases
    mydestination = {{ grains['fqdn'] }}, localhost
    relayhost = 
    mynetworks = 127.0.0.0/8 [::ffff:127.0.0.0]/104 [::1]/128
    mailbox_size_limit = 0
    recipient_delimiter = +
    inet_interfaces = all

    {% if 'virtual' in pillar.get('postfix','') %}
    virtual_alias_maps = hash:/etc/postfix/virtual
    {% endif %}

.. |postfix-config-management| image:: /uploads/2013/10/mysza.gif
