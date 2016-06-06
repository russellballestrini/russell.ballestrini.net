CSS frameworks not rendering properly on all browsers
#####################################################
:date: 2011-10-11 00:07
:author: Russell Ballestrini
:tags: Code, Guide
:slug: css-frameworks-not-rendering-properly-on-all-browsers
:status: published
:summary:
  Read on for the one line fix.

I ran into an issue when testing skeleton css framework and twitter
bootstrap where some browsers were not rendering the pages properly.
After some research I determined that I forgot the DOCTYPE declaration
tag.

The DOCTYPE tag tells the browser what "rules" or standards to use when
rendering markup.

The following code block displays the minimal approach to setting the
document type:

.. code-block:: html

  <!DOCTYPE html>

This doctype tag forces the broswer into standards mode which allows the pages to render properly.

Thanks!
