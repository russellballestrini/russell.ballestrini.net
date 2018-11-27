Google Bot Attempts to Crawl Shortest Urls First
################################################
:date: 2011-06-25 09:37
:author: Russell Ballestrini
:tags: Code, Greatest Hits, Opinion, Project
:slug: google-bot-attempts-to-crawl-shortest-urls-first
:status: published
:summary:

**Recently I built https://school.yohdah.com a Python, Pyramid, and
mongoDB project during the last couple weekends.**

|image0|

The site features a directory style navigation of nearly every public
school in the US. We have 61 state pages, approximately 19,000 city
pages, and over 103,000 school pages.

It seems the Google Bots have noticed
`school.yohdah.com <https://school.yohdah.com>`__ and started crawling
the site. Since the initial crawl I started reviewing a sample of the
sites apache logs in an attempt to track the bot's activity. After a few
minutes of viewing the logs, I locked onto a pattern; Google Bot's
algorithm appears to crawl the short URLs first!

PersonalCompute (a user) attached a graph of the fetched URL lengths
here:

|school.yohdah.com.graph|\ 

I have attached a zip containing the apache google bot crawl logs
here:
`access-school.yohdah.log.zip </uploads/2011/06/access-school.yohdah.log_.zip>`_

I found the pattern by opening the file in vim and scrolling very
quickly down. You will notice the log lines will grow slowly to the
right, as the urls being fetched increase by one character.

**Why does Google do this? Does anyone have speculation as to what this
means?**

.. |image0| image:: /uploads/2011/06/us-public-schools1.png
   :target: https://school.yohdah.com
   :alt: school.yohdah.com
   :class: wordwrap-left

.. |school.yohdah.com.graph| image:: /uploads/2011/06/school.yohdah.com_.graph_.png
   :target: /uploads/2011/06/school.yohdah.com_.graph_.png
