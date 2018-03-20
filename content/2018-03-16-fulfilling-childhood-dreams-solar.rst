Fulfilling Childhood Dreams: Solar
################################################################

:author: Russell Ballestrini
:slug: fulfilling-childhood-dreams-solar
:date: 2018-03-16 08:03
:tags: Solar, Project
:status: published

Ever since I was an 8 year old boy I have wanted solar. I remember reading about the environment and alternative energy sources in a monthly "socal studies" flyer my school subscribed our classroom to. I questioned, even at my young age, why the world wasn't actively switching over to solar, water, and wind!

25 years later I have finally fulfilled one of my childhood dreams. I have installed a 11.375kWh solar system on my roof. The system is composed of three arrays ("strings") of 8, 13, and 14 panels for a total of ``35``. The panels are the Panasonic ``VBHN325SA16`` which are ``325 watts``.

.. code-block:: python

  >>> # 35 panels x 325 watts ~= 11.375kWh 
  >>> 35 * .325
  11.375

Each panel has an "optimizer" which communicates to the centralized SolarEdge inverter installed in my basement near the breaker box. The optimizers allow each array to work efficently even when a panel is shaded or broken.

.. image:: /uploads/2018/11kWh-solar-panel-layout.png
   :alt: My 11.375kWh Solar Panel Layout

Additionally the optimizers report metrics regarding energy production to the inverter, which in turn sends this data to "the cloud" (aka SolarEdge Monitoring System) and I can watch daily playbacks of the whole system. For example, this was a good "solar day" as my family calls it back on Feburary 28th, 2018.

.. image:: /uploads/2018/solar-playback-2018-03-19.gif
   :alt: My 11.375kWh Solar Playback of March 19th, 2018

You can see how the sun rises to cover the 8 panels on the front of the house and then later moves to cover the panels on the back of the house.

The SolarEdge also keeps track of various high level metrics. If you insert the date ranges and electricity prices into SolarEdge dashboard, it will do the math to Calculate the "lifetime revenue" of the system. Having this number makes it really easy to calculate the ROI of the system as a whole!

.. image:: /uploads/2018/2018-03-16-solar-overview.png


Most of my key insights into home energy actually come from the other device I had installed called "Curb". How Curb works is a bunch of non-invasive CT clamps are installed on each breaker circut in a homes breaker box. Metrics are gathered about energy usage and sent to "the cloud".

The tool lets you see charts like this, which is the Solar Production and consumption in dollars for the last 15 days:

.. image:: /uploads/2018/solar-15-day-production-consumption-in-dollars.png
   :alt: 15 day solar production versus household breaker consumption

As you can see from this chart, about **50% of my solar production is being consumed by heating hot water** for a family of 5! This feels absurd, I wish there was a startup working in the hot water heating space.

Here is a short video showing the Curb user interface.

.. raw:: html

 <center>
 <video src="/uploads/2018/curb-user-interface.webm" width="620px" controls>
 Sorry, your browser doesn't support embedded videos,
 but don't worry, you can <a href="/uploads/2018/curb-user-interface.webm">download it</a>
 and watch it with your favorite video player!
 </video>
 </center>

