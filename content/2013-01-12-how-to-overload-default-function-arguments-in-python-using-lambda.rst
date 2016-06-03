How to overload default function arguments in python using lambda
#################################################################
:date: 2013-01-12 11:22
:author: Russell Ballestrini
:tags: Code, Greatest Hits, Guide
:slug: how-to-overload-default-function-arguments-in-python-using-lambda
:status: published

Python Lambda functions are very powerful but I often forget how they
work or the fun things they do. This post will document how to use a
lambda to provide different default arguments to a function.

We will use the `human function found in
ago.py <https://bitbucket.org/russellballestrini/ago/overview>`__ as an
example - because I'm the module author and I really like it. Lets use
the interactive python interpreter to run help on the human function.

::

    >>> from ago import human
    >>> help( human )

    Help on function human in module ago:

    human(dt, precision=2, past_tense='{} ago', future_tense='in {}')
        Accept a datetime or timedelta, return a human readable delta string

.. raw:: html

   </p>

Shown above the human function accepts 1 argument and 3 named keyword
arguments. The dt argument must be a datetime or timedelta object, the
precision must be an integer, and the other two must be strings. If we
didn't like the default arguments, we would need to specify (or pass in)
new values each time we invoked the function.

Example: ``human(dt, 3, 'this happened {} ago!', 'in {} from now!')``.
If we know we will always want different default arguments we can create
a lambda function to shorten the invocation length.

::

    >>> h = lambda dt : human(dt, 3, 'this happened {} ago!', 'in {} from now!')
    >>> print h( dt ) # h is much shorter then human, and still reusable!

| Above creates a new function h who only accepts one argument dt. This
  function calls human with our default arguments.
|  This lambda is equivalent to this regular python function:

::

    >>> def h( dt ):
    ...    return human(d, 3, 'this happened {} ago!', 'in {} from now!')
    >>> print h( dt ) # h is much shorter then human, and still reusable!

Here is a working example to show the new lambda function h in action:

::

    >>> from datetime import datetime
    >>> from datetime import timedelta
    >>> from ago import human
    >>> 
    >>> h = lambda dt : human(dt, 3, 'this happened {} ago!', 'in {} from now!')
    >>> 
    >>> present = datetime.now()
    >>> 
    >>> for i in range( 1, 15 ):
    ...     if i % 2 == 0:
    ...         new_date = present - timedelta( i, i * i, i * i * i )
    ...     else:
    ...         new_date = present + timedelta( i, i * i, i * i * i )
    ...     h( new_date )
    ... 
    'in 22 hours, 9 minutes, 30 seconds from now!'
    'this happened 2 days, 1 hour, 50 minutes ago!'
    'in 2 days, 22 hours, 9 minutes from now!'
    'this happened 4 days, 1 hour, 50 minutes ago!'
    'in 4 days, 22 hours, 9 minutes from now!'
    'this happened 6 days, 1 hour, 51 minutes ago!'
    'in 6 days, 22 hours, 10 minutes from now!'
    'this happened 8 days, 1 hour, 51 minutes ago!'
    'in 8 days, 22 hours, 10 minutes from now!'
    'this happened 10 days, 1 hour, 52 minutes ago!'
    'in 10 days, 22 hours, 11 minutes from now!'
    'this happened 12 days, 1 hour, 52 minutes ago!'
    'in 12 days, 22 hours, 12 minutes from now!'
    'this happened 14 days, 1 hour, 53 minutes ago!'

