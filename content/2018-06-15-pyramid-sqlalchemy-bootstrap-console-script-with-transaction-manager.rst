Pyramid SQLAlchemy bootstrap console script with transaction.manager
#########################################################################

:author: Russell Ballestrini
:slug: pyramid-sqlalchemy-bootstrap-console-script-with-transaction-manager
:date: 2018-06-15 10:54
:tags: Code
:status: published

So I've struggled for a while with the best way to properly setup a console script for my SQLAlchemy Pyramid apps.

I use the cookie cutter to setup my projects and as such, I do not have a global (and the importable) DBSession object. Instead my database session is attached to the request when it is created.

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
        parser.add_argument("-d", "--debug", action="store_true", default=False)
        return parser
    
    
    def main():
        parser = get_arg_parser()
        args = parser.parse_args()
    
        if args.debug:
            setup_logging(args.config)
    
        # use bootstrap context manager to prepare app and request,
        # next use the resulting request's transaction manager!
        with bootstrap(args.config) as env, env["request"].tm:
            request = env["request"]
            invalidate_all_node_cache_objects(request.dbsession)
