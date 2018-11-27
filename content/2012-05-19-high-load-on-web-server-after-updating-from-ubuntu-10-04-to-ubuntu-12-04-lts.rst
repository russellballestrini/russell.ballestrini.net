High load on web server after updating from Ubuntu 10.04 to Ubuntu 12.04 LTS
############################################################################
:date: 2012-05-19 18:40
:author: Russell Ballestrini
:tags: DevOps
:slug: high-load-on-web-server-after-updating-from-ubuntu-10-04-to-ubuntu-12-04-lts
:status: published
:summary:
  Charts that show the load difference.

| 
|  **High load on web server after updating from Ubuntu 10.04 to Ubuntu
  12.04 LTS**
|  Check out charts which lineup to when I upgraded:

| |image0|
|  I couldn't determine the cause of the load average increase...

**Update:** The issue might be memory bound. Check out this graph that
show much higher swap.

|image1|

**After much research this appears to be a load calculation and display
problem with the newer Linux kernels. The community has found Commit-ID:
c308b56b5398779cd3da0f62ab26b0453494c3d4 to be the problem. The commit
causes incorrect high reported load averages can be reported under
conditions of light load and high enter/exit idle frequency conditions
(greater then 25 hertz).**

A nice fellow named Doug from smythies.com researched
the topic between `tick and tickless linux kernels and the effect they
have on load averages <http://www.smythies.com/~doug/network/load_average/new.html>`. You should check it out.

.. |image0| image:: /uploads/2012/05/high-load-after-updating-ubuntu-from-10.04-LTS-to-12.04-LTS.png
   :target: https://russell.ballestrini.net/high-load-on-web-server-after-updating-from-ubuntu-10-04-to-ubuntu-12-04-lts/high-load-after-updating-ubuntu-from-10-04-lts-to-12-04-lts/
.. |image1| image:: /uploads/2012/05/ubuntu.12.04.swap_.year_.png
   :target: https://russell.ballestrini.net/high-load-on-web-server-after-updating-from-ubuntu-10-04-to-ubuntu-12-04-lts/ubuntu-12-04-swap-year/
