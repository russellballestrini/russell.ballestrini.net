Add a Breadcrumb Subscriber to a Pyramid project using 4 simple steps
#####################################################################
:date: 2011-07-02 17:25
:author: Russell Ballestrini
:tags: Code, Guide
:slug: add-a-breadcrumb-subscriber-to-a-pyramid-project-using-4-simple-steps
:status: published
:summary:

**This article will explain how to add a breadcrumb subscriber to a
Pyramid project using 4 simple steps.**

While programming http://school.yohdah.com/ I needed the ability to easily create
breadcrumb links from the current url. You may view the `bread.py source
code
here <https://bitbucket.org/russellballestrini/bread/src/tip/bread.py>`__.
The following guide describes the process I took to add this
functionality.

1. Download and include
`bread.py <https://bitbucket.org/russellballestrini/bread/raw/tip/bread.py>`__
at the top of your Pyramid project's \_\_init\_\_.py file:

::

        from yourproject.bread import Bread
        from pyramid.events import subscriber, NewRequest

2. At the bottom of the projects \_\_init\_\_.py file create the
following subscriber function as follows:

::

        def bread_subscriber( event ):
            """ Build Bread object and add to request """
            event.request.bread = Bread( event.request.url )

3. Now we can add our new subscriber to our Pyramid config inside
main and above the routes:

::

        config.add_subscriber( base_subscriber, NewRequest )

4. You are done! Now you should have the ability to use the bread
object from your template. Below I have provided a mako template
snippet:

::

        % for link in request.bread.links:
          ${ link | n } /
        % endfor
