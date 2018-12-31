Yuletide Trains and Homegrown Video Games
################################################################

:author: Russell Ballestrini
:slug: yuletide-trains-and-homegrown-video-games
:date: 2018-12-25 17:15
:tags: Code, Games
:status: published

.. image:: /uploads/2018/pixel-art-gift.png
    :align: right

Each holiday season I find myself drawn to a side passion of mine.

While some build model trains and others create Christmas light shows with synchronized music you'll find me on my sofa where I build, explore, and tinker on my own video game engine.

Maybe the sound of wrapping paper tearing acts as a trigger, but I only prioritize time on my game engine during the holiday season.

Do you have a specific hobby that you do during the holiday season but not during other parts of the year?

    Why am I working on Christmas every year - Am I a work-a-holic?


Work or Play.
=============================================

.. image:: /uploads/2018/pixel-art-santa-hat.png
    :align: right

Why do I absorb myself into this seasonal hobby? Am I escaping? Or am I making use of down time to work on a project that I am too occupied to even think about during the rest of the year?

For me, building my game on Christmas is fun, not *work*. Similar to how fishing while camping is fun, not *work*. 

    What is the last activity a commercial fisherman would do "for fun" on Christmas?
    Fishing.

What is fun for one person might be work for another. It is relative and depends on context.

I suspect that most people experience a tipping point, when an activity switches from fun to work.

I think, for an average person, this moment occurs when the answer to the following question changes:

* Do you rely on the activity for the majority of your income?

  * if yes, the activity often feels like work
  * if no, the activity often feels like fun


Work and Play?
=============================================

.. image:: /uploads/2018/pixel-art-bomb.gif
   :align: right

Now that's not to say you cannot find fun while at work, and vice versa. Personally, I aim to land a perfect balance between the two with anything I do. 

In my situation, I use the computer "professionally" each work day, for 7-10 hours.

If I was in the games industry, I doubt I would find much fun in building a video game on Christmas. But I'm not in the games industry and I have more fun building games than playing games.

That is to say, for me building a game feels fun while playing a game feels like work. Crazy right?

Even though the activities of my "day job" overlap with the activities involved with building my game, there are enough differences. These differences make one feel like work while the other feel like fun.

I'm not making an excuse for working during Christmas; I honestly have a blast coding and tinkering on my game.

I love getting stumped and learning. I love showing different ideas to my boys and seeing their eyes light up. I love to see how fast I can implement a small suggestion one of them have. I love how there are no rules and only my own skills and understanding can block me.

While my family is occupied with their new holiday gifts, I use my free time to explore creative ideas on a non-stressful personal project. A project where the stakes are low and the pleasure is high.




Show me the game already!
==============================

This years game engine modifications: 

* ability to save the game state to a `json` file
* ability to load the game state from a `json` file
* added a few algorithms for auto-generating maps
* refactored some common code (so I'm not reapeating myself)
* implemented an action charge / recharge system

Here is a short video of the current state of the engine. Let me know what you think in the comments.

.. raw:: html

 <iframe width="560" height="315" src="https://www.youtube.com/embed/qeMPV6aXKzk" frameborder="0" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

I also took the time to learn how to make pixel art using `GIMP`, a useful skill for making game assets.


Who else makes games during Christmas?
==========================================

I reached out to a number of indie game developers while formulating this blog post and I had a solid conversation with `Maverick Peppers <https://github.com/TheMaverickProgrammer>`_ a developer who runs a `software company called ProtoComplete <https://protocomplete.com/>`_ 

He was working during Christmas on his game while making pudding and drinking white russians (`recipe in the foot notes </yuletide-trains-and-homegrown-video-games/#white-russian-recipe>`_). He arrived at the conclusion that I was working from a passion-oriented mindset while he was from a goal-oriented mindset.

Maverick doesn't rely on the income from his games, so I asked "why are you 'working' on Christmas?" He explained that because he often has a `type-a` or "goal mindset" and because of this, he has trouble relaxing until he finishes whatever he is working on. In a sense, he was working Christmas *so that he could* relax.

As for myself, building games is a passion-oreiented process, I don't rely on the income and I use it to unwind.

We talked about how people can approach activities with either:

* `type-a` (goal-oriented mindset)
* `type-b` (passion-oriented mindset)

The fun part is people are often both, depending on the activity or project. For example Maverick has a passion mindset when making music and DJing, but always takes a goal mindset when it comes to business.



Footnotes
====================


Unwrapping My Christmas Commit History
------------------------------------------


Looking at my commit history, the first iteration of my current game engine was saved on Jan 01, 2014 with a few commits until Jan 19, 2014, at which point nothing until Dec 25, 2014 (Christmas itself) when I sprinted until Jan 10, 2015.

The next year, I must have hacked on something else, with no changes until Oct 09, 2016 where I had two commits.

Like clockwork on Dec 25, 2016 (Christmas) I tried to fix a regression in the engine's collision and intersection code. I left myself some breadcrumb comments to help me debug in the future... Nothing in 2017.

Today is Christmas 2018 and finally I have a work around for the regression I was looking into from Christmas 2016!


Porting SFML Rect from C++ to Python
------------------------------------------

This work around ports the `Rect` intersection logic of `SFML` from C++ to pure Python and avoids the following error message:

   `terminated by signal SIGSEGV (Address boundary error)`


.. code-block:: python

 def get_rect_intersection(r1, r2):
     """
     Accept two sfml.graphics.Rect objects.
     Return a new sfml.graphics.Rect of the overlap or None.
     """
 
     # We allow Rects with negative dimensions, so handle them correctly.
 
     # Compute the min and max of the first Rect (r1).
     r1_min_x = min(r1.left, r1.left + r1.width)
     r1_max_x = max(r1.left, r1.left + r1.width)
     r1_min_y = min(r1.top, r1.top + r1.height)
     r1_max_y = max(r1.top, r1.top + r1.height)
 
     # Compute the min and max of the second Rect (r2).
     r2_min_x = min(r2.left, r2.left + r2.width)
     r2_max_x = max(r2.left, r2.left + r2.width)
     r2_min_y = min(r2.top, r2.top + r2.height)
     r2_max_y = max(r2.top, r2.top + r2.height)
 
     # compute the intersection boundaries.
     i_left   = max(r1_min_x, r2_min_x)
     i_top    = max(r1_min_y, r2_min_y)
     i_right  = min(r1_max_x, r2_max_x)
     i_bottom = min(r1_max_y, r2_max_y)
 
     # if the intersection is valid (positive non zero area),
     # then there is an intersection.
     if i_left < i_right and i_top < i_bottom:
         return sfml.graphics.Rect((i_left, i_top), (i_right - i_left, i_bottom - i_top))
 

White Russian Recipe
----------------------------

* 1/4 cup distilled водка
* 1/4 cup Kahlua coffee rum
* 1/2 cup cream


Older versions of the game engine
-----------------------------------

Some `videos of older versions <https://russell.ballestrini.net/test-game-engine-with-python-and-sfml/>`_ of this game engine.

.. contents:: index



