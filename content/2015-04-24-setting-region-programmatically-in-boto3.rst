Setting region programmatically in Boto3
########################################
:date: 2015-04-24 14:07
:author: Russell Ballestrini
:tags: Code, DevOps
:slug: setting-region-programmatically-in-boto3
:status: published
:summary:

At work I'm looking into the possibility of porting parts of our AWS
automation codebase from Boto2 to Boto3. We desire to perform this port
because Boto2's record and result pagination appears defective.

I started to familiarize myself with Boto3 by using the Interactive Python interpreter.

Here I show myself trying to connect to the RDS AWS endpoint following the docs:

.. code-block:: python

    >>> import boto3
    >>> rds = boto3.client('rds')
    Traceback (most recent call last):
    ...
    NoRegionError: You must specify a region.

What, No region? OK - how do I set a region?

Well it turns out the docs want you to configure a region in a config file.
This will not work for me, I need to set the region programatically...

So after stumbling around in the botocore source code I found the
following solutions.

**Solution 1 - Set region\_name when creating client:**

.. code-block:: python

    >>> import boto3
    >>> rds = boto3.client('rds', region_name='us-west-2')


**Solution 2 - Set default region\_name on the session:**

.. code-block:: python

    >>> import boto3
    >>> rds = boto3.setup_default_session(region_name='us-west-2')
    >>> rds = boto3.client('rds')

It seems Boto3 has two types of interfaces, clients and resources.

Clients:
 return description objects and appear lower level.
 Description objects seem like AWS XML responses transformed into Python Dicts/Lists.

Resources:
  return higher level Python objects and like Instances with stop/start methods.


At a quick glance, both clients and resources seem to properly implement
pagination automatically!


.. code-block:: python

    >>> # client interface.
    >>> ec2 = boto3.client('ec2', region_name='us-west-2')
    >>> idesc = ec2.describe_instances()
    >>> len(idesc['Reservations'])
    273
    >>> idesc['ResponseMetadata']
    {'HTTPStatusCode': 200, 'RequestId': '7e431ff7-xxxx-xxxx-xxxx-xxxxxxxxxxxxx'}

    >>> # resource interface.
    >>> ec2 = boto3.resource('ec2', region_name='us-west-2')
    >>> for instance in ec2.instances.all():
    >>>     print instance, instance.tags

That all for now! 

You should read my other Boto related posts for tricks to impress your friends.  : )

* `Filtering AWS resources with Boto3 </filtering-aws-resources-with-boto3/>`_
* `Working with botocores AWS config </working-with-botocores-awsconfig/>`_
