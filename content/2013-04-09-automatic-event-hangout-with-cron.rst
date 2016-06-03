Automatic event hangout with cron
#################################
:date: 2013-04-09 09:17
:author: Russell Ballestrini
:tags: Guide
:slug: automatic-event-hangout-with-cron
:status: published

**Create an online only, hangout event**

Create a new event with a date far into the future, like the year 2015.
Go to the event's options > advanced and enable 'this event is online
only' which will create a unique Hangout URI.

**Create a cronjob**

Create a cronjob on each device to open the web browser Monday-Friday at
12:49pm and open the unique Hangout URI.

Firefox cron example:

::

    # Run Firefox at 12:49 EST each weekday and open hangout URI
    49 12 * * 1-5 export DISPLAY=:0 && /usr/bin/firefox 'hangout-uri'

.. raw:: html

   </p>

Chromium-browser cron example:

::

    # Run Chromium-browser at 12:49 EST each weekday and open hangout URI
    49 12 * * 1-5 export DISPLAY=:0 && /usr/bin/chromium-browser 'hangout-uri'

.. raw:: html

   </p>
