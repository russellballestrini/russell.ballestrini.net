Copying files between cloud object stores like S3 GCP and Spaces using Boto3
############################################################################

:author: Russell Ballestrini
:slug: copying-files-between-cloud-object-stores-like-s3-gcp-and-spaces-using-boto3
:date: 2021-05-12 18:50
:tags: Code, DevOps
:status: published

tl;dr if you just want something like `aws s3 cp` cli, try `gsutil rsync`. 

At work one key item team's sprint is properly utilizing and securing Google Cloud Platform (GCP).

For one of my projects, I'm learning GCP's Object Store called Google Cloud Storage (GCS).

I have prior experience using AWS S3 and Digital Ocean Spaces via ``aws s3`` CLI and ``boto3`` and I've even blogged in the past about some pretty advanced topics, like `Pre-signed GET and POST requests </pre-signed-get-and-post-for-digital-ocean-spaces/>`_. Pre-signing allows the client to perform specific actions on specific private objects, which is great for short time-to-live link downloads or direct browser uploads into the object store, all without compromising data security (hampering link sharing and preventing replay attacks)

At work, learning how to utilize and secure the GCS object store is critical to our teams interopability between clouds. We want to be able to store security artifacts into a single GCS bucket and sync all data to our main AWS S3 bucket as a long term archive.


Working with GCS using Boto3
============================

Given my prior experience with ``boto3`` I decided to test interoperability between it's ``s3`` client and GCS.

For this test I created the following via the GCP Console:

* `IAM Service Account <https://console.cloud.google.com/iam-admin/iam>`_ (with GCS Editor and GCS Viewer roles)
* `GCS Bucket <https://console.cloud.google.com/storage/browser>`_
* `Service Account HMAC <https://console.cloud.google.com/storage/settings;tab=interoperabily>`_ (linked to the new IAM Service Account)
   I also set the default GCP project which is important because by default boto3 is not configured to pass the ``x-amz-project-id`` HTTP header.

At this point I have an access key and secret key (``hmac``) which in theory I may pass to my existing code to communicate with GCP in a similar way to how I communicate with S3 or Spaces. 

Armed with this information I ran the following test and it worked: 


.. code-block:: python

 # Reference:
 # https://cloud.google.com/storage/docs/migrating#storage-list-objects-s3-python

 import boto3
 
 def list_gcs_objects(google_access_key_id, google_access_key_secret, bucket_name):
     """Lists GCS objects using boto3 SDK"""
     # Create a new client and do the following:
     # 1. Change the endpoint URL to use the
     #    Google Cloud Storage XML API endpoint.
     # 2. Use Cloud Storage HMAC Credentials.
 
     client = boto3.client(
         "s3",
         region_name="auto",
         endpoint_url="https://storage.googleapis.com",
         aws_access_key_id=google_access_key_id,
         aws_secret_access_key=google_access_key_secret,
     )
 
     # Call GCS to list objects in bucket_name
     response = client.list_objects(Bucket=bucket_name)
 
     # Print object names
     print("Objects:")
     for blob in response["Contents"]:
         print(blob["Key"])

If you are working with many GCP projects, you'll want to figure out how to configure ``boto3`` to pass the ``x-amz-project-id``. I found a good example reference but have not put it to practice: https://github.com/boto/boto3/issues/2251

The TL;DR is AWS doesn't have a concept of projects or default projects so this header is something GCP introduced for interopability.


GCP IAM first impressions
=========================

From a surface level look GCP IAM appears less complicated than AWS IAM but also less granular. I'm not sure how I feel at this point but I'm excited to see what the rest of my team uncovers when it comes to permissions, roles, and best practices.


Working with GCS using a CLI
============================

Now that we covered ``boto3`` (Python) interoperability between object stores, I started looking at some other simple CLI workflows which typically utilize ``aws s3``. In the case of GCP the prefered CLI is ``gsutil``.

The subcommand `gsutil rsync <https://cloud.google.com/storage/docs/gsutil/commands/rsync>`_ in particular caught my eye as a simple way to setup a cross cloud object store synchronization!

For example:

.. code-block:: bash

   gsutil rsync -d -r gs://my-gs-bucket s3://my-s3-bucket

For my next test, I'd like to try to setup a cronjob style automation to trigger ``gsutil rsync`` to copy and sync data from GCP GCS into AWS S3 for our long term security and governance artifacts, likely using a Gitlab CI Pipeline on a schedule.

.. contents::
