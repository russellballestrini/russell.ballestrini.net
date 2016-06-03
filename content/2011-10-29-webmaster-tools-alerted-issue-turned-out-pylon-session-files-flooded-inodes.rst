Webmaster tools alerted issue turned out Pylon session files flooded inodes
###########################################################################
:date: 2011-10-29 15:30
:author: Russell Ballestrini
:tags: DevOps, Opinion
:slug: webmaster-tools-alerted-issue-turned-out-pylon-session-files-flooded-inodes
:status: published
:summary:

**This graph could happen to you if you ever forget to configure munin
email alerting:**

|image0|

It only took approximately 1 hour to diagnoses and resolve this issue
however most of my web applications hosted on this server were down for
about 11 hours. I was lucky that this outage fell on a weekend otherwise
I would not have known about the problem till around 6:30pm!

|image1|

**Diagnosis:**

Two of my pylons apps had session files that slowly ran away on me. The
session files don't consume much capacity however the shear quantity of
them caused my inode usage to hit 100%.

Had I properly configured Munin's email alerting this issue would have
been identified well before it was a problem.

Want to know what alerted me to the problem? G Webmaster's tools claimed
it could not read my robots.txt on a few of my sites... After
investigating I learned the site was down. Checking the Apache error
logs pointed me to disk space issues. ``df -ha`` reported everything was
fine, however ``df -hi`` reported 100% inode usage! At this point I
started looking to cache and log locations to find lots of files, which
lead me to my pylons web applications data/sessions directories.

**Resolution:**

Delete the session cache tree directories and allow the applications to
rebuild them.

Todo: move /www off the root disk partition. This issue could have been
much worse if I was unable to boot or login to remedy. Moving /www off
root should prevent the web server from effecting the systems ability to
boot.

.. |image0| image:: /uploads/2011/10/df_inode-year.png
.. |image1| image:: /uploads/2011/10/df_inode-day.png
