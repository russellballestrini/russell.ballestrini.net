Honey!  I just DELETED LinkPeek.com
###################################
:date: 2013-05-26 13:19
:author: Russell Ballestrini
:tags: DevOps, LinkPeek, Opinion
:slug: honey-i-just-deleted-linkpeek-com
:status: published

During the day I am an ops sys-admin. During the night I am a husband,
father of two, and a CEO of a bootstrapped start-up. After launch, my
first project was to schedule regular backups of user data and archive
off-site. My goal was to `create backups but never need
them <http://russell.ballestrini.net/virt-back-restoring-from-backups/>`__.
Boy was I lucky ...

Yes, leave it to me to inadvertently delete the VPS root disk. One of
the major cloud providers places the "rename" and "remove" disk buttons
right next to each other and I learned a nasty habit of clearing pop-ups
without reading them (thanks Windows).

    "Honey! I just deleted LinkPeek.com"

The horror... My stomach felt like I took a tumble in a roller-coaster.
Instantly I tossed off my developer hat and put on my operations hat. I
checked the off-site backups. I had nightly dumps of MongoDB and weekly
tar backups of the /etc partition. The user data was in MongoDB and most
of the system configuration information was in the tar. I used the tar
to recover 2 upstart scripts, 2 supervisord scripts, 2 complex nginx
confs, an ssl cert, and the pyramid production.ini.

I set out to stand up a new server, re-install the needed packages,
recover the user data, and restore the service. After 1.5 hours of
feverish typing, https://linkpeek.com/ was back online.

**What I learned and my plan going forward**

If you are a small team or a start-up, you must have somebody dedicated
to operations. Without backups I would not have been able to gracefully
recover. Most likely I would have reimbursed the existing members and
shuttered the doors.

This experience was eye-opening. In my next couple of posts I will
explain how I `create and maintain backups </automatic-backups/>`__ and
my next project will implement a configuration management and
provisioning system.

This system will allow me to:

#. take out the human element of recovery
#. significantly reduce the time-to-recover from a catastrophic failure
#. test disaster recovery procedures before needing them
#. provision development and production environments without effort
#. have a reproducible blueprint of "how to build a LinkPeek server"
