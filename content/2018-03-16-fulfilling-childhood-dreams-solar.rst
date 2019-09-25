Fulfilling Childhood Dreams: Solar
################################################################

:author: Russell Ballestrini
:slug: fulfilling-childhood-dreams-solar
:date: 2018-03-16 08:03
:tags: Solar, Project
:status: published

Ever since I was an 8 year old boy I have wanted solar. I remember reading about the environment and alternative energy sources in a monthly "socal studies" flyer my school subscribed our classroom to. I questioned, even at my young age, why the world wasn't actively switching over to solar, water, and wind!

25 years later I have finally fulfilled one of my childhood dreams: I installed a 11.375kWh solar system on my roof.

This post will act as an overview of the stuff I learned about solar, I hope you learn something too!

.. contents::

*Disclosure: This post contains affiliate links.* See `full disclosure page here </disclosures-and-terms/>`_.

.. image:: /uploads/2018/panasonic-325watt-panels-front.jpg
  :alt: 325 watt panasonic solar Panels on front of house

.. image:: /uploads/2018/panasonic-325watt-panels-back.jpg
  :alt: 325 watt panasonic solar Panels on back of house

Solar Monitoring
=====================

The system is composed 35 x Panasonic 325 watt panels (VBHN325SA16). The panels are isolated into 3 arrays ("strings") of 8, 13, and 14.

.. code-block:: python

  >>> # 35 panels x 325 watts ~= 11.375kWh 
  >>> 35 * .325
  11.375

Each panel has an "optimizer" which communicates to the centralized SolarEdge inverter installed in my basement near the breaker box. The optimizers allow each array to work efficently even when a panel is shaded or broken.

Here is the layout of the panels on my house:

.. image:: /uploads/2018/11kWh-solar-panel-layout.png
   :alt: My 11.375kWh Solar Panel Layout

Additionally the optimizers emit energy production metrics to the inverter, which in turn forwards this data to "the cloud" (aka SolarEdge Monitoring System). From there, I can watch daily playbacks of the whole system.

For example, this playback from March 19th, 2018 was a good "solar day" as my family calls:

.. image:: /uploads/2018/solar-playback-2018-03-19.gif
   :alt: My 11.375kWh Solar Playback of March 19th, 2018

You can see how the sun rises to cover the 8 panels on the front of the house and then later moves to cover the panels on the back of the house.

.. image:: /uploads/2018/solaredge-10k-central-inverter.jpg
  :alt: 325 watt panasonic solar Panels on back of house

SolarEdge Monitoring Dashboard also keeps track of various high level metrics. For example, I input my electricity rates with date ranges and the dashboard calculates the "lifetime revenue" of my solar system. I plan to track my ROI on this number!

.. image:: /uploads/2018/2018-03-16-solar-overview.png

Home Energy Monitoring
=============================

Most of my key insights into home energy actually come from another device I had installed called `Curb Home Energy Monitor <https://www.amazon.com/gp/product/B015IY0Z3E/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B015IY0Z3E&linkCode=as2&tag=russellball0b-20&linkId=727da547a2b0a22fa53016191c2cf313>`_. Curb uses a bunch of non-invasive CT clamps on each breaker circut to gather consumption. Metrics are gathered and sent to "the cloud" and power some really cool realtime dashboards.

For example, this chart shows solar production versus consumption in dollars for the last 15 days:

.. image:: /uploads/2018/solar-15-day-production-consumption-in-dollars.png
   :alt: 15 day solar production versus household breaker consumption

As you can see, about **50% of my solar production is being consumed by heating hot water** for a family of 5! 

This feels absurd... 

**Update:** I switched to a `Hybrid Water Heater </hybrid-hot-water-heater-saves-69-percent-on-energy-consumption/>`_ and wrote a post to show how I now use 69% less electricity when heating water!

Anyways, here is a short video showing the Curb user interface.

.. raw:: html

 <center>
 <video src="/uploads/2018/curb-user-interface.webm" width="620px" controls>
 Sorry, your browser doesn't support embedded videos,
 but don't worry, you can <a href="/uploads/2018/curb-user-interface.webm">download it</a>
 and watch it with your favorite video player!
 </video>
 </center>

The `Curb <https://www.amazon.com/gp/product/B015IY0Z3E/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B015IY0Z3E&linkCode=as2&tag=russellball0b-20 &linkId=727da547a2b0a22fa53016191c2cf313>`_ is likely the most accurate home energy monitor on the market. The draw back is the cost of parts and labor; I used my solar installer's electrician and the total cost was $800.

The competition has less accuracy but I could have likely installed a Sense myself and saved on the labor cost.

Here are the two other brands I was looking at, for reference:

* `Sense Home Energy Monitor <https://www.amazon.com/gp/product/B075K6PHJ9/ref=as_li_tl?ie=UTF8&tag=russellball0b-20 &camp=1789&creative=9325&linkCode=as2&creativeASIN=B075K6PHJ9&linkId=cc8e52d403b4b24da1f7b6a27a96ff74>`_
* `Neurio Home Electricity Monitor <https://www.amazon.com/gp/product/B0149EE5KS/ref=as_li_tl?ie=UTF8&tag=russellball0b-20 &camp=1789&creative=9325&linkCode=as2&creativeASIN=B0149EE5KS&linkId=7e3e5d1063e980892649ea98351034bd>`_ 

Solar Financing
=========================

When talking with Tesla, I fully expected to pay for my solar system in full with cash savings. It wasn't until I reached out to `SunLight Solar <http://sunlightsolar.com>`_ did I change my strategy. SunLight urged me to take advantage of the ".99% CT Green Bank" finance option. I took out a loan for the whole project and dumped my cash savings into my home mortgage as a bulk payment to the principle.

Additionally, the CT Green Bank granted me $3,600 toward my project and the US federal government will grant 30% or $8,400 on my next tax return.

After all the incentives, the parts and labor of my system came in just under $20,000:

.. code-block:: math

 $32,000 - $3,600 - 8,400 = $20,000

Putting solar on my house actually opened up my financial options and diversified my portfolio!

I now have:

* a power plant on my roof with an expected 9-10 year ROI; after 10 years I'll be generating wealth, capital, and positive "cash flow" in the form of energy
* paid down my 4.125% house mortgage by $35,000; saving tens of thousands over the life of the loan
* increased the value of my house by $20-30,000; this is an asset I can sell with or without my house
* shielded or insulated myself from electricity rate hikes; who knows what electricity will cost in 5 to 10 years

Contact me
=========================

As always, please feel free to leave comments below. I live in New England so you may also `contact me </contact/>`_ to setup a time to tour my setup and ask questions. I look forward to meeting you!
