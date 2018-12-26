Yuletide Trains and Homegrown Video Games
################################################################

:author: Russell Ballestrini
:slug: yuletide-trains-and-homegrown-video-games
:date: 2018-12-25 17:15
:tags: Code, Games
:status: published

.. contents::

.. image:: /uploads/2018/pixel-art-bomb.gif
   :align: right

Each holiday season I find myself drawn to a side passion of mine. While some build model trains and others create Christmas light shows with synchronized music you'll find me on my sofa where I build, explore, and tinker on my own video game engine.

Maybe the sound of wrapping paper tearing acts as a trigger, but I only prioritize time on my game engine during the holiday season.

Looking at my commit history, the first iteration of my current game engine was saved on Jan 01, 2014 (there were other engines before it). I had a few commits until Jan 19, 2014, at which point nothing until Dec 25, 2014 (Christmas itself). My sprint lasted until Jan 10, 2015.

The next year, I must have hacked on something else, with no changes until Oct 09, 2016 where I had two commits.

Like clockwork on Dec 25, 2016 (Christmas) I tried to fix a regression in the engine's collision and intersection code, and left myself some breadcrumb comments to help me debug in the future...

Nothing in 2017.

Today is Christmas 2018 and finally I have a `work around for the regression`_ I was looking into from Christmas 2016!


    Why am I working on Christmas every year, am I a work-a-holic?

Why do I and so many others absorb ourselves into seasonal hobbies? Are we escaping? Are we simply making use of the flexible time we normally don't have to work on things we wish we could during the rest of the year?

For me, building my game on Christmas is fun, not *work*. Similar to how fishing while camping is fun, not *work*. 

What is fun for one person might be work for another. It is relative and depends on context.

    What is the last activity a commercial fisherman would do "for fun" on Christmas?
    Fishing.

Accounts of a tipping point when an activity switches from fun to work has long been documented.

For an average person, I think this moment occurs when the answer to the following question changes:

* Do you rely on the activity for the majority of your income?

  * if yes, the activity will often feel like work
  * if no, the activity will often going to feel like fun

Now that's not to say you cannot have fun while at work, and vice versa. In fact, finding the perfect mix, the right balance for each individual task might be the secret to having a happy life.

My situation seems a bit more complex. I use the computer "professionally" for 7-10 hours each work day. If I was in the games industry, I doubt I would find fun in building a video game on Christmas. But I'm not in the games industry and I have more fun building games than playing games. That is to say, building a game is fun, while playing a game is work.

Crazy right?

Even though there are huge overlaps between the activities of my "day job" and the activities involved with building my game, there are enough differences which make one feel like work while the other feel like fun.

I'm not making an excuse for working during Christmas; I honestly have a blast coding and tinkering on my game. I love getting stumped and learning. I love showing the games to my boys and seeing their eyes light up. I love to see how fast I can implement a small suggestion one of them have. I love how there are no rules, only my own skills and understanding can block me. While the family is occupied with their new holiday gifts, I use my free time to explore creative ideas on a non-stressful personal project where the stakes are low and the pleasure is high.

This year, I modified my game engine to: 

* save the game state to a `json` file
* load the game state from a `json` file
* added a few algorithms for auto-generating maps
* refactored some common code (so I'm not reapeating myself)
* implemented an action charge / recharge system

Here is a short video of the current state of the engine. Let me know what you think in the comments on this page.

(video here)

I also took the time to learn how to make pixel art using `GIMP`, something that could be useful for making game assets.

Check those out here:

.. image:: /uploads/2018/mario-hat-big.png
    :width: 200px

.. image:: /uploads/2018/pixel-art-bomb.png



Research for this post
===========================

While doing some research for this post, I reached out to a number of indie game developers. I had a solid conversation with `Maverick Peppers <https://github.com/TheMaverickProgrammer>`_ a developer who runs a `software company called ProtoComplete <https://protocomplete.com/>`_ 

He was working during Christmas on his income generating game (while making pudding and drinking white russians [recipe in the foot notes]). We quickly arrived at the conclusion that I was working from a passion-oriented mindset while he was from a goal-oriented mindset. For him, building games is a goal-oriented process because he relies on the income. For me, building games is a passion-oreiented process, I use it to unwind and I don't rely on the income.

We talked about how people can approach activities with either:

* type-a (goal-oriented mindset)
* type-b (passion-oriented mindset)

The fun part is most people are both, depending on the activity or project.

Let me know in the comments, do you have a specific hobby that you do most holiday seasons?



Porting SFML Rect from C++ to Python
========================================

This work around ports the `Rect` intersection logic from `SFML` from C++ to pure Python and avoids the following error message:

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
==============================

* 1/4 cup distilled водка
* 1/4 cup Kahlua coffee rum
* 1/2 cup cream

Hard Apple Cider Recipe
==============================

* No recipe, but I made a video of one of my hard cider brews here: https://www.youtube.com/watch?v=0hnfhlurS90

