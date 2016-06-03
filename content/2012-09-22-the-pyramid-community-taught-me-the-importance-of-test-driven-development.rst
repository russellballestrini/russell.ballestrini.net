The Pyramid community taught me the importance of test driven development
#########################################################################
:date: 2012-09-22 14:03
:author: Russell Ballestrini
:tags: Opinion
:slug: the-pyramid-community-taught-me-the-importance-of-test-driven-development
:status: published

`Sontek's patch <https://github.com/Pylons/pyramid/commit/72561a213ccc456738582551e85fab0f0c8d09ab>`__

I greeted the UPS man in the middle of the street to sign for my new
Lenovo ThinkPad T430. Because this was My first *brand-new* laptop
purchase I rationalized the time I spent tracking the package from the
factory in China to my hands in Connecticut. Once inside, I opened the
box and started installing Fedora 17. I couldn't help but to take in the
new-electronics smell.

I've been without a laptop for more than a month so I was eager to get
my development environment configured. Most of my tools ship with
vanilla Linux, vim, python, hg mercurial, chromium browser, etc. My
first goal was to get a development copy of linkpeek.com running
locally. This took about 5 minutes and it seemed to be working fine
until I noticed a few pages had errors. The errors seemed to be caused
by a difference between Pyramid 1.3 and 1.4a1. But what was failing?

I posted a short message in #pyramid about the bug and minutes later I
had multiple developers prodding for hints. "Could you post the whole
traceback?", "What does your view look like?". I answered quickly and
attempted to explain what I thought was going on. Turns out I was close
but before I could finish explaining the problem, sontek had a working
one-character-fix and was in the process finishing the tests to prove
the patch. He also explained what I should do in the interim to patch
locally.

In the next 4 hours a pull request was submitted to the upstream master
and the patch was peer reviewed, accepted, and integrate by mcdonc. That
impressed me, a lot. All Pylon Projects have strict policies about test
coverage and now I understand why. Tests not only help produce better
bug-free software but also act as a powerful tool when proving the
validity of a patch. I plan to devote the next couple weeks to making
test-driven-development a habit.
