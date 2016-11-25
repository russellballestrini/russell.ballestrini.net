How to Incorporate Custom Configuration in a Pyramid Application
################################################################
:date: 2011-11-30 22:47
:author: Russell Ballestrini
:tags: Code, Guide
:slug: how-to-incorporate-custom-configuration-in-a-pyramid-application
:status: published


**Note:** This post shows an old way to modify the request object.
I discuss a new way in my `Pyramid add_request_method </register-super-powers-with-pyramid-add-request-method/>`_ post.


Imagine that you have just built a wiki, blog, or cms web application
that will be deployed multiple times by different people. You would like
to provide the ability to configure some aspects of the program without
the end user altering your python or template code. This guide explains
how to incorporate custom configuration from the project's .ini file
with the rest of the application.

To explain this process we will add a customizable Google Analytics key
to our project.

#. Make a configuration key/value pair for Google Analytics
#. Add the Google Analytics javascript code to the template

**Make a configuration key/value pair for Google Analytics**

Inside production.ini place the following in the ``[app:main]`` section::

    #google_analytics_key = UA-55555555-1
    google_analytics_key =

**Add the Google Analytics javascript code to the template**

In this case I will show an example in mako. Other template solutions
should look similar.

::
 
  <%def name="google\_analytics()">
  % if request.registry.settings['google_analytics_key']:


   <script type="text/javascript"></p>
   <p>var _gaq = _gaq || [];<br />
             _gaq.push(['_setAccount', "${request.registry.settings['google_analytics_key']}"]);<br />
             _gaq.push(['_trackPageview']);</p>
   <p>(function() {<br />
             var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;<br />
             ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';<br />
             var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);<br />
             })();</p>
   <p></script>

  % endif
  
  

Then in the head section call the function::

    ${ google_analytics() }

That was easy because the configuration string just needed to be
substituted into the JavaScript in the template. What if you needed to
do something with the provided key/value before using it? Next I will
show you a method for building renderer globals again showing a
different way to configure Google Analytics:

**Make an inject\_renderer\_globals subscriber**

Define ``inject_renderer_globals(event)`` function in the project's
``__init__.py`` file.

I normally place it at the bottom of the file and it looks like this::

    def inject_renderer_globals(event):
        """Inject some renderer globals before passing to template"""

        request = event['request']
       
        # Build ${google_analytics_key} from the configuration file  
        event['google_analytics_key'] = request.registry.settings[ 'google_analytics_key' ]

Import BeforeRender at the top of the ``__init__.py``::

    from pyramid.events import BeforeRender

In the main function, add the ``inject_renderer_globals`` to the
subscribers::

    config.add_subscriber(inject_renderer_globals, BeforeRender)

Now you can use ``${google_analytics_key}`` anywhere in your template.

**Thank you for reading, and feel free to leave comments**
