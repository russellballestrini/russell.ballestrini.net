Custom Rundeck HipChat notification templates
#############################################
:date: 2014-12-03 01:37
:author: Russell Ballestrini
:tags: Code, DevOps
:slug: custom-rundeck-hipchat-notification-templates
:status: published

Today I built a GUI and workflow around Ansible using Rundeck. Tonight I
started diving into sending HipChat notifications and after a bit of
research, I managed to create a custom notification template for each
Rundeck project.

Modify your project's configuration file, on Ubuntu it was in
``/var/rundeck/projects/pname/etc/project.properties``, and add the
following line to the bottom:

    ::

        framework.plugin.Notification.HipChatNotification.messageTemplateLocation=/var/rundeck/projects/pname/etc/custom-hipchat-template.ftl

    Note: replace ``pname`` with your project name.

I ended up producing a single line chat notification template.
I uploaded it here to act as an example:

`Custom Rundeck HipChat Notification Template <http://pad.yohdah.com/311/rundeck-hipchat-custom-notification-template>`__

The template syntax and renderer is called FreeMarker. Rundeck and the
HipChat plugin pass many different context Map hash objects to
FreeMarker for use in the templates. In this case I display "VPC name"
selected by the user when starting the job.

References:

.. raw:: html

   <ul>
   <li>

`Rundeck HipChat Notification
Plugin <http://rundeck.org/plugins/2013/06/24/hipchat-notification.html>`__

.. raw:: html

   </li>
   <li>

`Rundeck HipChat Notification
Plugin <https://github.com/hbakkum/rundeck-hipchat-plugin>`__ (User
Guide and Default Template)

.. raw:: html

   </li>
