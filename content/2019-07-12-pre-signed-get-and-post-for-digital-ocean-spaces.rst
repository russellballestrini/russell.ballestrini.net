Pre-signed GET and POST for Digital Ocean Spaces
################################################################

:author: Russell Ballestrini
:slug: pre-signed-get-and-post-for-digital-ocean-spaces
:date: 2019-07-12 16:01
:tags: Code, DevOps
:status: published

A pre-signed request grants a semi-trusted user temporary access to a private resource.

Let's unpack that statement ...

Pre-signed means, we bless a specific action on a specific private resource
for a short duration of time.

Semi-trusted means, we have authenticated the user, but we don't trust them
to have full access to our private resources.

That still seems a bit generic ...

No worries, our next example will appear more concrete:

Today we will pre-sign HTTP ``POST`` and ``GET`` requests to grant a
semi-trusted user temporary access to objects in a private Digital Ocean Space.

Pre-signing allows the client to perform specific actions on specific private
objects while still protecting us from link sharing and replay attacks.

The following examples use Python (Boto3), and Curl.

Before we start, you should reference the official `Boto3 Presigned Urls <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-presigned-urls.html>`_ documentation.

Pre-signed GET or Download
=================================

Allow a semi-trusted user the ability to download a specific file named ``my-object.zip``
from a private Digital Ocean Space named ``example-bucket`` for a short duration of ``30`` seconds.

Save this code into a file named ``pre_sign_get_test.py`` and run it with ``python pre_sign_get_test.py``.

The result will be a URL that you may redirect a user to. For testing you should be able to load the URL into a web browser and download the file.

.. code-block:: python

 import boto3
 from botocore.client import Config
 
 # Initialize an S3 session/client to talk to DigitalOcean Spaces.
 session = boto3.session.Session()
 client = session.client(
     "s3",
     # configure the region you created the space in.
     region_name="nyc3",
     # configure the region you created the space in.
     endpoint_url="https://nyc3.digitaloceanspaces.com",
     # configure your access key (generate this on the dashboard).
     aws_access_key_id="DOXXXXXXXXXXXXXXXXXX",
     # configure your secret key (generate this on the dashboard).
     aws_secret_access_key="DOO/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
 )
 
 signed_get_object_url = client.generate_presigned_url(
     ClientMethod='get_object',
     Params={
         'Bucket': 'example-bucket',
         'Key': 'my-object.zip',
     },
     ExpiresIn=30
 )
 
 # print the pre-signed GET request URL for downloading the object.
 # You may redirect the user to this URL when they click a "download" button.
 print(signed_get_object_url)

Pre-signed POST or Upload
================================

Allow a semi-trusted user the ability to upload a specific file named ``my-object2.zip``
into a private Digital Ocean Space named ``example-bucket`` for a short duration of ``60`` seconds.

Save this code into a file named ``pre_sign_post_test.py`` and run it with ``python pre_sign_get_test.py``.

The result will be a ``cURL`` command that you may run on your console for testing.

In a real situation, you would want to pass these parameters to the client and let it perform the authenticated upload.
The file never hits your server and is uploaded directly to the private Space.

**IMPORTANT:** parameter order matters! The ``file`` parameter must be last.

.. code-block:: python

 import boto3
 from botocore.client import Config

 # Initialize an S3 session/client to talk to DigitalOcean Spaces.
 session = boto3.session.Session()
 client = session.client(
     "s3",
     # configure the region you created the space in.
     region_name="nyc3",
     # configure the region you created the space in.
     endpoint_url="https://nyc3.digitaloceanspaces.com",
     # configure your access key (generate this on the dashboard).
     aws_access_key_id="DOXXXXXXXXXXXXXXXXXX",
     # configure your secret key (generate this on the dashboard).
     aws_secret_access_key="DOO/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
 )

 signed_post = client.generate_presigned_post(
     Bucket="example-bucket",
     Key="my-object2.zip",
     ExpiresIn=60,
 )
 
 params = []
 for key, value in signed_post["fields"].items():
     params.append('--form "{}={}"'.format(key, value))
 
 print("curl " + " ".join(params) + ' --form "file=@production-namespaces.txt;filename=production-namespaces.txt" ' + signed_post["url"])
 
