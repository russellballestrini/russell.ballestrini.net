Always attempt to scale vertically first
########################################
:date: 2012-06-10 21:52
:author: Russell Ballestrini
:tags: DevOps, LinkPeek
:slug: always-attempt-to-scale-vertically-first
:status: published

I spent the weekend fretting because one of my servers was basically
being DOS'd by paying customers. During the outage I started thinking
about the best way to scale and how I could make the code-base more
efficient.

Linux top reported high load, in the 20's. Eventually I figured out that
the server was having IO performance issues.

I wasted a bunch of time attempting to fight fires. After about an hour
of that I decided to scale my VPS vertically by giving it an extra 256mb
of memory and a larger swap file (256mb to 1024mb).

These two changes were surprisingly effective and the IO issues
resolved. Apparently the server was starving for memory which caused the
host to swap which brought things to a crawl waiting for IO.

Crisis averted for the moment. Now I am free to think clearly and
engineer a proper solution instead of attempting to put out fires.

If you ever encounter a similar situation, attempt the simplest fix.
There is no shame in throwing more money at a problem if it will buy you
time. In this case, an extra $10.00 a month relieved the performance
issues and bought myself some time, for the moment.

|image0|

.. |image0| image:: /uploads/2012/06/vertical-scale-marked.png
   :target: https://russell.ballestrini.net/always-attempt-to-scale-vertically-first/vertical-scale-marked/
