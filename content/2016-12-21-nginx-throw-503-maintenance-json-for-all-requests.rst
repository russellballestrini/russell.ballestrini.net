Nginx throw HTTP 503 maintenance JSON for all requests
################################################################

:author: Russell Ballestrini
:slug: nginx-throw-503-maintenance-json-for-all-requests
:date: 2016-12-21 15:09
:tags: Code, DevOps
:status: published

I found this technique after stumbling on Aaron Parecki's blog.  You can read his post here:

* `Setting a custom json 503 error page in nginx with proper http and content-type headers <https://aaronparecki.com/2014/09/03/28/custom-json-503-error-page-nginx-http-content-type-headers>`_

Lets pretend you have an API and you need to turn on maintenance for a major change.
All your client's (phones, web frontends) know what to do when they get an HTTP 503 Error code with JSON body.

Now you want to cause all requests to get the following JSON -

``/opt/maint/maint.json``:

.. code-block:: json

 {
  "errorCode": "maintenance",
  "errorDesc": "We are currently performing scheduled maintenance. Please try again later."
 }

The nginx configuration looks like this -

``maint.conf``:

.. code-block:: nginx

 server {
     listen          80 default;
     listen          [::]:80 default_server;
     server_name     _;

     root /opt/maint;

     add_header Retry-After 30 always;

     error_page 503 /maint.json;
 
     location / {
         # all API calls will miss try_files on purpose and return custom 503.
         try_files $uri =503;
     }

 }
 
All API calls will miss ``try_files`` on purpose and return our custom 503 ``maint.json``.

Proof that this method rocks, it supports ``GET``, ``POST``, ``PUT``, ``UPDATE``, and ``DELETE``.

It also serve proper headers like ``Content-Type: application/json`` -

.. code-block:: curl

 curl -v -X POST --data "param1=value1&param2=value2" http://127.0.0.1:80/my-very-favorite-api-call

 > POST /my-very-favorite-api-call HTTP/1.1
 > User-Agent: curl/7.29.0
 > Host: 127.0.0.1
 > Accept: */*
 > Content-Length: 27
 > Content-Type: application/x-www-form-urlencoded
 >
 * upload completely sent off: 27 out of 27 bytes
 < HTTP/1.1 503 Service Temporarily Unavailable
 < Server: nginx/1.10.2
 < Date: Wed, 21 Dec 2016 20:32:44 GMT
 < Content-Type: application/json
 < Content-Length: 150
 < Connection: keep-alive
 < ETag: "585addfe-96"
 < Retry-After: 30
 <
 {
   "errorCode": "maintenance",
   "errorDesc": "The server is undergoing scheduled maintenance and will be back up shortly. Please try again later"
 }

Need to make sure you always set a custom header? Don't forget the ``always`` directive::

      add_header Retry-After 30 always;

Leave a comment if this helps you!
