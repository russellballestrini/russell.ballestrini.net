Control a MongoDB collection in configuration management
########################################################
:date: 2013-10-14 21:39
:author: Russell Ballestrini
:tags: DevOps, Guide
:slug: control-a-mongodb-collection-in-configuration-management
:status: published

This post explains how to use configuration management (Salt Stack) to
completely control a MongoDB collection. In our example we want to
control a store's collection of plans.

First we create a JSON representation of the collection.

**mongodb/plan.json:**

::

    { 
      "_id" : { "$oid" : "4ef8b9e2be329f491d98f74b" },
      "cost" : 20, "description" : "development",
      "name" : "good", "count" : 6000
    }
    { 
      "_id" : { "$oid" : "4ef8b9e8be329f491d98f74c" },
      "cost" : 60, "description" : "freelancers",
      "name" : "better", "count" : 36000 
    }
    { 
      "_id" : { "$oid" : "4ef8b9f0be329f491d98f74d" },
      "cost" : 180, "description" : "production",
      "name" : "best", "count" : 162000
    }

.. raw:: html

   </p>

Next we configure a salt state formula to manage the JSON file and watch
it for changes.

**mongodb/init.sls:**

::

    # install mongodb server
    mongodb-server:
      pkg:
        - installed

    # manage the store's plan.json
    /tmp/plan.json:
      file.managed:
        - source: salt://mongodb/plan.json
        - user: root
        - group: root
        - mode: 644

    # import the plan collection if it changes
    import-plan-collection:
        cmd.wait:
          - name: mongoimport --db=store --collection=plan --upsert /tmp/plan.json
          - require:
            - pkg: mongodb-server
          - watch:
            - file: /tmp/plan.json

.. raw:: html

   </p>

*Now whenever plan.json is altered in configuration management, the file
on the minion will update which will trigger a mongoimport with upsert
to occur.*

Optionally, we could replace ``--upsert`` with ``--drop`` which will
drop the collection before re-importing thus removing stale records.

We now have a version controlled JSON file in configuration management
and the power of MongoDB Document Objects in our application code!
