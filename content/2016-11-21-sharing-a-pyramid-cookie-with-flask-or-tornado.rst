Sharing a Pyramid cookie with Flask or Tornado
################################################################

:author: Russell Ballestrini
:slug: sharing-a-pyramid-cookie-with-flask-or-tornado
:date: 2016-11-21 18:35
:tags: Code
:status: published

Do you have a Pyramid application which authenticates users and uses a signed cookie as a session?
Do you want to build a microservice using another framework and allow it to use the same cookie and session? Me too!

First we will review a bit of Pyramid code which describes the cookie session.

Setup Pyramid Signed Cookie Session
====================================

At the top of your `__init__.py` you will have the following import:

.. code-block:: python

 # cookie only session, not encrypted but signed to prevent tampering!
 from pyramid.session import SignedCookieSessionFactory

In the `main()` function of `__init__.py` you will create a `Configurator`:

.. code-block:: python

 def main(global_config, **settings):
     """ This function returns a Pyramid WSGI application."""
 
     # setup session factory to use unencrypted but signed cookies.
     session_factory = SignedCookieSessionFactory(
         secret = 'test-secret' 
     )
 
     # build app config object from ini.
     config = Configurator(
         settings = settings,
         session_factory = session_factory,
     )

As you can see for this test example the `secret` is hardcoded. A real application would define the secret in the .ini and access it using the `settings` object.

Now all new requests will have a `request.session` attribute.

You use it like a dictionary, for example:

.. code-block:: python

  # set some data into the cookie. for me, this logs the user in.
  request.session['authenticated_user_id'] = 8

  # get some data from the cookie. for me this gets the user_id or None.
  authenticated_user_id = request.session.get('authenticated_user_id', None)

  # delete a key / value from cookie. for me this will log out the user.
  request.session['authenticated_user_id'] = None

Reference: `SignedCookieSessionFactory <http://docs.pylonsproject.org/projects/pyramid/en/latest/api/session.html#pyramid.session.SignedCookieSessionFactory>`_



Teach Tornado how to read Pyramid cookies
================================================

In this section I'll show you how to access and deserialize the Pyramid cookie from a Tornado application.

To do this, I'm going to extend the Tornado `Hello, world` application:

.. code-block:: python

 import tornado.ioloop
 import tornado.web
 
 class MainHandler(tornado.web.RequestHandler):
     def get(self):
         self.write("Hello, world")
 
 def make_app():
     return tornado.web.Application([
         (r"/", MainHandler),
     ])
 
 if __name__ == "__main__":
     app = make_app()
     app.listen(8888)
     tornado.ioloop.IOLoop.current().start()

This is a simple application which listens to port 8888 and serves the text `Hello, world` when `/` is requested.

Add the following imports:

.. code-block:: python

  # accessing Pyramid cookies.
  from webob.cookies import SignedSerializer
  from pyramid.session import PickleSerializer
  from pyramid.compat import bytes_

Adjust the `get` method in the `MainHandler` to look like this:

.. code-block:: python

    def get(self):
        raw_cookie = self.get_cookie('session')
        session_data = serializer.loads(bytes_(raw_cookie))
        self.write("Hello, world")
        self.write(str(session_data))

The complete program follows:

.. code-block:: python

 import tornado.ioloop
 import tornado.web
 
 # accessing Pyramid cookies.
 from webob.cookies import SignedSerializer
 from pyramid.compat import bytes_
 
 # http://docs.webob.org/en/stable/api/cookies.html#webob.cookies.SignedSerializer
 serializer = SignedSerializer(secret='test-secret')
 
 class MainHandler(tornado.web.RequestHandler):
     def get(self):
         raw_cookie = self.get_cookie('session')
         session_data = serializer.loads(bytes_(raw_cookie))
         self.write("Hello, world")
         self.write(str(session_data))
 
 def make_app():
     return tornado.web.Application([
         (r"/", MainHandler),
     ])
 
 if __name__ == "__main__":
     app = make_app()
     app.listen(8888)
     tornado.ioloop.IOLoop.current().start()

Again, we are hardcoding the same `secret`. If you set everything up properly, loading http://127.0.0.1:8888 in a web browser should print the cookie session_data in plain-text.
