Guido name dropped tornado python tulip and pep-3156 
#####################################################
:date: 2013-03-22 22:07
:author: Russell Ballestrini
:tags: Uncategorized
:slug: guido-name-dropped-tornado-python-tulip-and-pep-3156
:status: published

Pycon 2013 was excellent, in fact it was my first one I have attended.

I found it odd that django and Pyramid had plenty of talks but nobody
mentioned tornado.

The only person that brought up tornado was Guido himself, who has been
researching and developing async python since December 12th, 2012. Guido
wants to add async API libraries to python core, and has been comparing
his work to twisted and more importantly tornado. He is leveraging the
existing solutions to stay on the correct track.

Async API's in Python core! This news was extra exciting for me, because
I have already learned the power of async by messing around with
tornado. Since the talk many people have approached me and asked for
more information about async API's.

My favorite use for async is long polling for web applications. Here is
a diagram that shows how great tornado is:

|2013-03-22-tornado-callback-long-polling-event-loop-scaled|

This type of polling can support thousands of concurrent users, all
connected and waiting for a callback event to occur. I used tornado to
build `four2go <http://four2go.gumyum.com>`__, a real-time and
multi-player browser-based-game.

.. |2013-03-22-tornado-callback-long-polling-event-loop-scaled| image:: /uploads/2013/03/2013-03-22-tornado-callback-long-polling-event-loop-scaled.png
   :target: /uploads/2013/03/2013-03-22-tornado-callback-long-polling-event-loop-scaled.png
