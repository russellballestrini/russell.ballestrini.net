four2go!: A new spin on an old classic
######################################
:date: 2010-12-31 20:33
:author: Russell Ballestrini
:tags: Project
:tags: four2go!, gumyum, programming, python
:slug: four2go-a-new-spin-on-an-old-classic
:status: published

|four2go! logo|

**For the past two months** I have feverishly worked on my side project.
Initially I set out to work on this application for submission to the
Hacker News, lets make November "Launch an App Month".

The whole project took longer than expected but I was please with my
progress so I continued development. Today, a month later, I have added
the finishing touches to the app. It gives me great pleasure to announce
the official launch of `four2go! <http://four2go.gumyum.com>`__

**A new spin ...**

`four2go! <http://four2go.gumyum.com>`__ brings a new spin to the
classic "four in a row" genre.

Instead of weighted tokens, `four2go! <http://four2go.gumyum.com>`__
uses balloons which float up rather than down. This new game mechanic
requires players to retrain their brains and can easily throw off a
novice player.

Another new spin, rather than playing on a coffee table, users play
using a computer over the internet. The four2go! web application
requires a simple account registration but does not require any download
or installation!

Users can play with anyone, at anytime, anywhere in the world. The game
sessions are persistent meaning the board will not disappear. This
persistence allows players to check their games much like they would
check their email.

|gumyum logo|

**The gumyum framework**

The game itself was completed after the first weekend of coding.
Programming the game was fun and exciting and originally four2go! was a
command prompt application with a text-based gui. That version was not
accessible and in order for people to play we needed to move to a
different medium. So I set out to code a web front end.

After another weekend of coding I had the game working in the browser.
It was very clunky (It didn't refresh after player moves) and didn't
have any authentication, anyone could play any game.

    **Coding the game was simple, the framework was the difficult
    part...**

*Enter Stage Left:* The gumyum framework. I needed a way to
authentication users and a way to store and retrieve game sessions. I
also needed a way to track user statistics and player history. Most
importantly I needed a user interface that would be intuitive and fun to
use! The remainder of the project set out to solve each of those needs.
I needed the gumyum framework to make four2go! popular. I spent the rest
of the time (1.5 months) working on gumyum and I feel safe claiming that
the framework appears complete.

The great part about having a framework is the code reusability, I
should be able to "plug" new games or new mechanics behind the gumyum
framework with little trouble. My labor and efforts should pay off if I
ever decide to build another game.

**Artwork and graphic design**

I was very fortunate to work with my brother `Joey
Ballestrini <http://joey.ballestrini.net>`__ on some of the concept and
game art. We designed the `four2go! <http://four2go.gumyum.com>`__ logo,
the `gumyum <http://gumyum.com>`__ logo, and the balloons. Joey designed
each of the "create" game icons. The clouds, the grass, and the dirt
were created for another game and I decided they were a good fit so they
were re-purposed. We both use gimp when creating graphical computer art.

**LETS PLAY!**

I have attached a video of the game, but I
urge you to try `four2go! <http://four2go.gumyum.com>`__ out for
yourself!

.. raw:: html

   <p>
   <center>
   <iframe title="YouTube video player" width="480" height="338" src="http://www.youtube.com/embed/wmB9PeKBAlA" frameborder="0">
   </iframe>
   </center>
   </p>


.. |four2go! logo| image:: /uploads/2010/12/four2go.png

.. |gumyum logo| image:: /uploads/2010/12/gumyumgameslogo.png
