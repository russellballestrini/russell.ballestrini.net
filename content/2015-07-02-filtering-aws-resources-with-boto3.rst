Filtering AWS resources with Boto3
##################################
:date: 2015-07-02 17:03
:author: Russell Ballestrini
:tags: Code, DevOps
:slug: filtering-aws-resources-with-boto3
:status: published
:summary:
  References to take you from filtering novice to expert.

This post will be updated frequently when as I learn more about how to
filter AWS resources using Boto3 library.

**Filtering VPCs by tags**

In this example we want to filter a particular VPC by the "Name" tag
with the value of 'webapp01'.

::

    >>> import boto3
    >>> boto3.setup_default_session(profile_name='project1')
    >>> ec2 = boto3.resource('ec2', region_name='us-west-2')
    >>> filters = [{'Name':'tag:Name', 'Values':['webapp01']}]
    >>> webapp01 = list(ec2.vpcs.filter(Filters=filters))[0]
    >>> webapp01.vpc_id
    'vpc-11111111'

You can also filter on the value of the 'tag-key' or the 'tag-value'
like so:

::

    >>> taco_key_filter = [{'Name':'tag-key', 'Values':['taco']}]
    >>> nacho_value_filter = [{'Name':'tag-value', 'Values':['nacho']}]

You can also filter on multiple 'Values'. In this example want 2 VPCs
named 'webapp01' and 'webapp02':

::

    >>> filters = [{'Name':'tag:Name', 'Values':['webapp01','webapp02']}]
    >>> list(ec2.vpcs.filter(Filters=filters))
    [ec2.Vpc(id='vpc-11111111'), ec2.Vpc(id='vpc-22222222')]

You can also use the '\*' wildcard to glob up results in your filter. In
this example we want all 3 VPCs named 'webapp01', 'webapp02' and
'webapp03':

::

    >>> filters = [{'Name':'tag:Name', 'Values':['webapp*']}]
    >>> list(ec2.vpcs.filter(Filters=filters))
    [ec2.Vpc(id='vpc-11111111'), ec2.Vpc(id='vpc-22222222'), ec2.Vpc(id='vpc-33333333')]

Thats all for now!

You should read my other Boto related posts for tricks to impress your friends.  : )

* `Setting region programmatically in Boto3 </setting-region-programmatically-in-boto3/>`_
* `Working with botocores AWS config </working-with-botocores-awsconfig/>`_


