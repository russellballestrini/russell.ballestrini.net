Capability driven Presentation
################################################################

:author: Russell Ballestrini
:slug: capability-driven-presentation
:date: 2016-12-18 18:21
:tags: Code
:status: published

A web page does not need to look the same on every browser or device.
We cannot control the capabilities of a user's browser or device.
As web designers, we have the duty to give the viewer the best experience possible.
A user will come with what they have and we should do our best to accommodate.

TL;DR: Capability drives presentation.

Resilient Web Design
========================

A resilient web page should:

* have a single canonical URI
* serve the same content, regardless of a viewer's capibilities
* use the viewer's capibilities to gracefully enhance and/or downgrade the presentation of the content 

For more background and history please read this free online book: https://resilientwebdesign.com/

Techniques
========================

.. contents::
   :local:

The js-only class
------------------------

Purpose: hide HTML elements when Javascript does not work.

In this technique we:

#. use a ``<noscript>`` tag to nest a class named ``js-only``
#. declare ``display: none`` in the ``js-only`` class to hide elements
#. apply the ``js-only`` class to any element which should hide without js

   Note: The ``js-only`` class will only exists when Javascript does not work.

.. code-block:: html

 <noscript>
   <style>
   .js-only {display: none;}
   </style>
 </noscript> 

Now, suppose we have a notification message which clears when a user clicks 'x'.
To clear the notification, we must use a Javascript ``onclick`` event handler.

Without the Javascript capability the notification cannot clear.
Therefore, to prevent confusion we should remove the 'x' from the presentation.

For example, with Javascript the notification will look like this:

  .. image:: /uploads/2016/12/notification-with-javascript.png
     :alt: notification with javascript has an x


But without Javascript the 'x' is removed and the notification will look this:

  .. image:: /uploads/2016/12/notification-without-javascript.png
     :alt: notification without javascript does not have an x

To do this we assign the ``js-only`` class to our label holding 'x':

.. code-block:: html

 <div id="alerts">
 {%- for message, level in request.session.pop_flash() %}
 <div class="alert alert-{{level}}" onclick="this.style.display='none'" name="alert">
   <p>
     <label class="close js-only" alt="dismiss" title="dismiss">x</label>
     {{message}}
   </p>
 </div>
 {%- endfor %}
 </div>

The content is the same, but we hide the interface based on the user's capibility!
This small change has a huge impact on the overall user experience.

We no longer present a broken button to the user.
