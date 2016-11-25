Register Super Powers with Pyramid add_request_method
#####################################################

:author: Russell Ballestrini
:slug: register-super-powers-with-pyramid-add-request-method
:date: 2016-11-24 15:30
:tags: Code, DevOps
:status: published

The Pyramid web application framework uses a request object to hold state regarding an inbound HTTP connection.
A view must accept a request object as the first argument which makes it always available to our views and templates.

This behavior rocks, but Pyramid makes it even better by allowing us to enrich the request object!

As an example, lets pretend we want to randomly generate an integer from 1 to 999 and attach it to each request:

.. code-block:: python

 from pyramid.config import Configurator

 from random import randint

 def main(global_config, **settings):
     """ This function returns a Pyramid WSGI application."""

     # build app config object from ini.
     config = Configurator(
         settings = settings,
     )

    def add_random_number(request):
        """return a random number."""
        return randint(1, 1000)

    # register request methods.
    # each request instance will run these functions.
    # the result attaches to the request as an attribute.
    # cache the result with `reify=True` to prevent multiple computations.
    config.add_request_method(add_random_number, 'random_number', reify=True)

Now we have access to this attribute in our views and templates:

.. code-block:: python

 request.random_number

This strategy has a number of uses. For example, I use it to:

* attach configuration settings and secrets like API keys
* attach a user object, by querying the database for the user_id sourced from the cookie session
* analyze requests for misuse like spam or flooding

What super powers do you register to your request? You should let the world know in the comments.

Another Pyramid related post: `Sharing a Pyramid cookie with Flask or Tornado </sharing-a-pyramid-cookie-with-flask-or-tornado/>`_
