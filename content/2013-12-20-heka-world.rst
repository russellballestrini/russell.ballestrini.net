Heka, World!
############
:date: 2013-12-20 18:25
:author: Russell Ballestrini
:tags: DevOps, Guide
:slug: heka-world
:status: published

This post serves as a "Hello World" for the `data collection and
processing software called
Heka <https://github.com/mozilla-services/heka>`__. Heka is written in
Go and was open sourced by Mozilla, the same fabulous group that brings
us Firefox!

I intend to use Heka to replace Logstash agents by sending logs directly
to ElasticSearch and continuing to use Kibana3 for visualizations. Also
I aim to start collecting metrics and sending to a central Whisper
back-end to fuel Graphite charts. All that we need to make Heka take on
these responsibilities is one binary and some custom configuration.

**Heka:** Hello, World!

This mostly contrived example will show how to use Heka to watch
``/tmp/input.log`` and write to ``/tmp/output.log``.

**Step 1:** install Heka

Compile from source or install the `Heka
package <https://github.com/mozilla-services/heka/releases>`__ for your
operating system.

**Step 2:** create a Heka TOML configuration file

``/tmp/hello-heka.conf:``

::

    [hello_heka_input_log]
    type = "LogstreamerInput"
    log_directory = "/tmp"
    file_match = 'input\.log'

    [hello_heka_output_log]
    type = "FileOutput"
    message_matcher = "TRUE"
    path = "/tmp/output.log"
    perm = "664"
    encoder = "hello_heka_output_encoder"

    [hello_heka_output_encoder]
    type = "PayloadEncoder"
    append_newlines = false

.. raw:: html

   </p>

**Step 3:** start Hekad and test!

#. in terminal 1:

   ::

       sudo hekad -config=/tmp/hello-heka.conf

#. in terminal 2:

   ::

       tail -f /tmp/output.log

#. in terminal 3:

   ::

       echo 'Heka, World!' >> /tmp/input.log

Like magic the data appended to ``input.log`` will appear in
``output.log``

Heka also has great docs and a number of input and output plugins, but
don't take my word for it, try it yourself!
