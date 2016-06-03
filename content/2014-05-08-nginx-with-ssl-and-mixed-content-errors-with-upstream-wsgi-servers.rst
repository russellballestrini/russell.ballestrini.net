Nginx with SSL and mixed content errors with upstream WSGI servers
##################################################################
:date: 2014-05-08 16:28
:author: Russell Ballestrini
:tags: Code, Guide
:slug: nginx-with-ssl-and-mixed-content-errors-with-upstream-wsgi-servers
:status: published

Mixed content errors occur because Nginx (the front-end server)
communicates to the upstream WSGI server using http. WSGI does not know
(or care) about the SSL session between Nginx and the user. The WSGI
server will naively generate URIs and serve assets as http.

To fix mixed content errors, we need to communicate the inbound request
scheme or configure the WSGI server to always use https.

**waitress**

| Waitress is meant to be a production-quality pure-Python WSGI server
  with very acceptable performance.
|  It commonly powers Pyramid and Substance D deployments.

To configure waitress to always use https in code:

::

    from waitress import serve
    serve(wsgiapp, host='0.0.0.0', port=8080, url_scheme='https')

.. raw:: html

   </p>

configure waitress to always use https in paste deploy compatible
configuration file:

::

    [server:main]
    host = 127.0.0.1
    port = 6543
    url_scheme = https

.. raw:: html

   </p>
