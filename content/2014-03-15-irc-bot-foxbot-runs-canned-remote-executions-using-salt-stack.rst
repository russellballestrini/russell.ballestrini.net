IRC Bot (Foxbot) runs canned remote executions using Salt Stack
###############################################################
:date: 2014-03-15 16:33
:author: Russell Ballestrini
:tags: Code, DevOps
:slug: irc-bot-foxbot-runs-canned-remote-executions-using-salt-stack
:status: published

I extended my IRC Bot Foxbot today to allow it to run canned remote
executions on behalf of users in an IRC channel. This is only a
prototype or proof-of-concept. Be very careful not to allow users to
inject their own commands. Foxbot must be running on the Salt Master and
must be running as the same user that runs the salt-master daemon.

The code lives here:
`foxbot/plugins/checks.py <https://bitbucket.org/russellballestrini/foxbot/src/tip/plugins/checks.py>`__

Example usage:

.. code-block:: text

 16:18:25            * | russell checks uptime minion2.foxhop.net
 16:18:25       foxbot | minion2.foxhop.net:  16:18:25 up 496 days, 22:36, 17 users,  load average: 0.33, 0.70, 0.87

.. code-block:: text

 16:29:10            * | russell checks procs *
 16:29:17       foxbot | minion2.foxhop.net: PROCS WARNING: 165 processes
 16:29:17       foxbot | minion5.foxhop.net: PROCS CRITICAL: 309 processes

