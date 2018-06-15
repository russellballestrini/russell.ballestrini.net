Pyramid SQLAlchemy bootstrap console script with transaction.manager
#########################################################################

:author: Russell Ballestrini
:slug: pyramid-sqlalchemy-bootstrap-console-script-with-transaction-manager
:date: 2018-06-15 10:54
:tags: Code
:status: published

So I've struggled for a while with the best way to properly setup a console script for my SQLAlchemy Pyramid apps.

I use the `Pyramid Cookiecutter Alchemy <https://github.com/Pylons/pyramid-cookiecutter-alchemy>`_ to setup my projects and as such, I do not have a global and thus importable DBSession object. Instead my database session is attached to the request on creation.

Anyways, here is my recipe:

.. code-block:: python
    
    import argparse

    from pyramid.paster import bootstrap, setup_logging
    
    from remarkbox.models import invalidate_all_node_cache_objects
    
    
    def get_arg_parser():
        parser = argparse.ArgumentParser(
            description="Invalidate all NodeCache objs to force recomputation."
        )
        parser.add_argument("-c", "--config", default="development.ini")
        return parser
    
    
    def main():
        parser = get_arg_parser()
        args = parser.parse_args()
        setup_logging(args.config)
    
        # use bootstrap context manager to prepare app and request,
        # next use the resulting request's transaction manager!
        with bootstrap(args.config) as env, env["request"].tm:
            request = env["request"]
            invalidate_all_node_cache_objects(request.dbsession)
      
      
This pattern should help you solve this error:

.. code-block:: python

 NoTransaction error when using bootstrap in script
