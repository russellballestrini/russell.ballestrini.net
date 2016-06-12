Boto3 get main route table
##########################
:date: 2015-10-16 12:15
:author: Russell Ballestrini
:tags: Code, DevOps
:slug: boto3-get-main-route-table
:status: published
:summary:
  Library work around.

While developing Botoform I ran into an issue with Boto3 where I
couldn't easily get the "main" route table of a VPC. I ended up adding a
`get\_main\_route\_table <https://github.com/russellballestrini/botoform/blob/master/botoform/enriched/vpc.py>`__
method to do the duty.

.. code-block:: python

 def get_main_route_table(self):
     """Return the main (default) route table for VPC."""
     main_route_table = []
     for route_table in list(self.route_tables.all()):
         for association in list(route_table.associations.all()):
             if association.main == True:
                 main_route_table.append(route_table)
     if len(main_route_table) != 1:
         raise Exception('cannot get main route table! {}'.format(main_route_table))
     return main_route_table[0]

That all for now!

You should read my other Boto related posts for tricks to impress your friends.  : )

* `Setting region programmatically in Boto3 </setting-region-programmatically-in-boto3/>`_
* `Filtering AWS resources with Boto3 </filtering-aws-resources-with-boto3/>`_

