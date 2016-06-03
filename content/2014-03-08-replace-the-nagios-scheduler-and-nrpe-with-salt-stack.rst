Replace the Nagios Scheduler and NRPE with Salt Stack
#####################################################
:date: 2014-03-08 15:53
:author: Russell Ballestrini
:tags: Code, DevOps
:slug: replace-the-nagios-scheduler-and-nrpe-with-salt-stack
:status: published

Note: I will update this post as I progress.

So the idea is to use Salt Stack's remote execution to communicate with
all nodes and run the Nagios checks and collect the return output
instead of using the NRPE client/service protocol. This reduces the
number of agents running on each host and appears significantly more
secure. Salt Stack uses public/private crypto on top of the ZMQ
publisher/subscriber model. This means the communication transport is
very fast, very secure, and all nodes will run checks in parallel!

| First, we need to install the Nagios checks and plugins on each host
  or minion.
|  I used the following State Formula on my Ubuntu and Debian hosts:

**salt://nagios/plugins.sls**

    ::

        nagios-plugins:
          pkg:
            - installed

        nagios-plugins-extra:
          pkg:
            - installed

**salt://top.sls**

    ::

        base:
          '*'
            - nagios.plugins

I kicked off a highstate (``salt '*' state.highstate``) on all minions
and eventually they all returned in the affirmative. We now have all the
Nagios plugins and checks installed on each host.

This next part is FUN, We run a check on every host concurrently.

    This particular check counts the number of processes running on each
    host and warns at 150 and criticals at 200.

    ::

        salt '*' --out=json --static cmd.run_all '/usr/lib/nagios/plugins/check_procs -w 150 -c 200'

    .. raw:: html

       </p>

    Output static JSON - Wait for all minions to return and then
    generate a single JSON object.

    ::

        {
            "graphite.foxhop.net": {
                "pid": 24356, 
                "retcode": 0, 
                "stderr": "", 
                "stdout": "PROCS OK: 78 processes"
            }, 
            "akuma.foxhop.net": {
                "pid": 4610, 
                "retcode": 1, 
                "stderr": "", 
                "stdout": "PROCS WARNING: 158 processes"
            }, 
            "ken.foxhop.net": {
                "pid": 31254, 
                "retcode": 2, 
                "stderr": "", 
                "stdout": "PROCS CRITICAL: 392 processes"
            } 
        }

    .. raw:: html

       </p>

    Review the `Nagios Plugin
    API <http://nagios.sourceforge.net/docs/3_0/pluginapi.html>`__ for
    more information about return codes and STDOUT formats.

Last, we take this JSON data perform further processing or display it in
a meaningful way.

For example, we could generate an HTML/JavaScript dashboard from the raw
JSON objects. We could cut metrics out of the STDOUT and persist
historic values in a data store. We could push the data into another
system like Graphite or even send an email alerts.

This solution has all the perks of Nagios without ANY of the cons!

Returning the check output data to the CLI isn't super useful for
further processing, so I hacked in a way to return data back to the
master using the encrypted zeromq bus.

**\_returners/zeromq\_return.py**

::

    # -*- coding: utf-8 -*-
    '''
    The zeromq returner will send return data back to the Salt Master over the
    Encrypted 0MQ event bus with a custom tag for filtering on the other end. 

    Basically after the remote execution finishes, the ret data is "packaged" into
    a special "envelope" which triggers the local Salt Minion Daemon to
    forward the ret data to the Salt Master's event bus. 

    The "package" basically wraps the ret data and uses the tag 'fire_master'.

    For example, a ret data object from the execution of test.ping
    would be "packaged" like this::

      ret = {
        'graphite.foxhop.net': true
      }

      ret['tag'] = 'third-party'

      package = {
        'events': [ ret ],
        'tag': None,
        'pretag': None,
        'data': None
      }

    The Salt Minion Daemon will forward this package to the Salt Master
    where a 3rd party script may be filtering on the specified internal event tag.

    To use the zeromq returner, append '--return zeromq' to the salt command. ex::

      salt --return zeromq '*' test.ping 

    TODO:

     figure out a way for user to define custom tag for filtering ... 
     Most returners use the Salt Minion config file to supply returner
     details... that is not optimal, it would be ideal if the custom tag
     could be supplied on the CLI when the remote execution is run, like::

       --return=zeromq --tag=mytag

    '''

    # needed to log to log file
    import logging

    # needed for config to opts processing
    import os
    import salt.syspaths as syspaths
    from salt.config import minion_config

    # needed to send events over ZMQ
    import salt.utils.event

    log = logging.getLogger(__name__)

    # needed to define the module's virtual name
    __virtualname__ = 'zeromq'

    def __virtual__():
        return __virtualname__


    def returner(ret):
        '''
        Send the return data to the Salt Master over the encrypted
        0MQ bus with custom tag for 3rd party script filtering.
        '''

        # get opts from minion config file, supports minion.d drop dir!
        opts = minion_config(os.path.join(syspaths.CONFIG_DIR, 'minion'))

        # TODO: this needs to be customizable!
        tag = 'third-party'

        # add custom tag to return data for filtering
        ret['tag'] = tag

        # multi event example, supports a list of event ret objects.
        # single event does not currently expand/filter properly on Master side.
        package = {
          #'id': opts['id'],
          'events': [ ret ],
          'tag': None,
          'pretag': None,
          'data': None
        }

        # opts must contain valid minion ID else it binds to invalid 0MQ socket.
        event = salt.utils.event.SaltEvent('minion', **opts)

        # Fire event payload with 'fire_master' tag which triggers the
        # salt-minion daemon to forward payload to the master event bus!
        event.fire_event(package, 'fire_master')

.. raw:: html

   </p>

Next we run a third party application on the Salt Master which
subscribes to our events by filtering on the special tag
('third-party').

**listen\_to\_master\_bus.py**

::

    # event libary for events over ZMQ
    import salt.utils.event

    # create event object, attach to master socket ...
    event = salt.utils.event.MasterEvent('/var/run/salt/master')

    tag = 'third-party'

    print('Listening for events tagged \'{}\' on Salt Master bus.'.format(tag))

    # generator iterator yields events forever, we filter on tag
    for data in event.iter_events(tag=tag):
        print(data)

This small application just prints the incoming return data, but it
could easily be expanded to process the incoming return data and persist
it somewhere.

Open two terminals on the Salt Master host.

    ::

        # on terminal 1 run:
        python listen_to_master_bus.py

    ::

        # on terminal 2 run:
        salt '*' --return zeromq cmd.run_all '/usr/lib/nagios/plugins/check_procs -w 150 -c 200'

    Same remote execution check as before but now our new returner will
    make data appear in terminal 1!

This zeromq returner is more of a proof-of-concept. I think the salt
remote execution command line tool should allow end-users to provide a
``--tag`` so that data may be feed directly back to a third-party script
listening to the Salt Master's event bus which filters on the particular
tag. My next step is to look into what it would take to build in this
functionality.

In the future I want to rig up the Salt scheduler to invoke these remote
execution checks on a steady and predictable cadence. Nagios
historically runs checks every 5 minutes. The Salt scheduler will allow
us schedule different checks with different frequencies. For example, I
might want my load checks and metrics to be collected every 10 secs, but
my disk capacity usage checked every 2 minutes. This fine-grain control
is super powerful!
