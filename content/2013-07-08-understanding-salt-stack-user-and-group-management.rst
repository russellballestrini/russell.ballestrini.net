Understanding Salt Stack user and group management
##################################################
:date: 2013-07-08 13:51
:author: Russell Ballestrini
:tags: DevOps, Guide
:slug: understanding-salt-stack-user-and-group-management
:status: published

This state will create a user:

::

    russell:
      user: 
        - present

This state will create a user and a group. This also makes the user part
of the group, and handles creating the group first:

::

    russell:
      group:
        - present
      user: 
        - present
        - groups:
          - russell 
        - require:
          - group: russell

This state handles user and group generation along with password and
ssh-key maintenance. This is all done securely using pillar to
parameterize arguments:

::

    # This state will create users accounts 
    #
    # This state requires a pillar named 'users' with data formatted like:
    # 
    # users:
    #
    #  tusername:
    #    fullname: Test Username
    #    uid: 1007
    #    gid: 1007
    #    groups:
    #      - sudo
    #      - ops
    #    crypt: $password-hash-sha512-prefered
    #    pub_ssh_keys:
    #      - ssh-rsa list-of-public-keys tusername-sm
    #
    #  anotheruser: ... snipped ...

    # loop over all users presented by pillar:
    # create user's group, create user, then add pub keys
    {% for username, details in pillar.get('users', {}).items() %}
    {{ username }}:

      group:
        - present
        - name: {{ username }}
        - gid: {{ details.get('gid', '') }}

      user:
        - present
        - fullname: {{ details.get('fullname','') }}
        - name: {{ username }}
        - shell: /bin/bash
        - home: /home/{{ username }}
        - uid: {{ details.get('uid', '') }}
        - gid: {{ details.get('gid', '') }}
        - crypt: {{ details.get('crypt','') }}
        {% if 'groups' in details %}
        - groups:
          {% for group in details.get('groups', []) %}
          - {{ group }}
          {% endfor %}
        - require:
          {% for group in details.get('groups', []) %}
          - group: {{ group }}
          {% endfor %}
        {% endif %}

      {% if 'pub_ssh_keys' in details %}
      ssh_auth:
        - present
        - user: {{ username }}
        - names:
        {% for pub_ssh_key in details.get('pub_ssh_keys', []) %}
          - {{ pub_ssh_key }}
        {% endfor %}
        - require:
          - user: {{ username }}
      {% endif %}

    {% endfor %}

