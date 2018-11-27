Output all instance identifiers of an AWS VPC to JSON
=====================================================

:author: Russell Ballestrini
:slug: output-all-instance-identifiers-of-an-aws-vpc-to-json
:date: 2016-06-21 10:25
:tags: Code, DevOps
:status: published

At work today I needed an easy way to collect private IP addresses of every instance in one of our production VPCs.

I ended up adding a tool to https://botoform.com to perform this task.

.. code-block:: bash

  bf --profile <aws_profile> dump <vpc_name_tag> instances --output-format json

For example:

.. code-block:: bash

  bf --profile customer3 dump prd instances --output-format json > ~/customer3-prd-instances.json

Checkout the `Botoform Quickstart <https://botoform.readthedocs.io/en/latest/guides/quickstart.html>`_
for installation instructions.

