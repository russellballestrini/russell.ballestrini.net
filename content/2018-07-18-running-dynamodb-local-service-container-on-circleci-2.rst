Running DynamoDB Local service container on CircleCI 2.0
################################################################

:author: Russell Ballestrini
:slug: running-dynamodb-local-service-container-on-circleci-2
:date: 2018-07-18 11:56
:tags: Code, DevOps
:status: published

**tl;dr** use a custom entrypoint in your CircleCI 2.0 config to limit Java memory to 1G.

The new CircleCI 2.0 docker configuration supports a "primary image" (listed first) which runs all the "steps" as well as zero or many "service images" (listed subsequently). The "service images", although not running in the same container as the primary present as if local to the primary.

It sort of feels like mixing many docker containers together.

Enough talk, in this example, I show how easy it is to run `DynamoDB Local <https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html>`_ in a separate container but at the same time present it to the primary as ``127.0.0.1:8000``:

.. code-block:: yaml

  version: 2
  workflows:
    version: 2
    tests:
      jobs:
        - test
  
  jobs:
  
    test:
  
      working_directory: /go/src/github.com/remind101/r101-myapp
  
      docker:
  
        # Primary container image where all the steps run.
        - image: circleci/golang:1.8
  
        # Service container image made available to the primary container at `host: localhost`
        - image: dwmkerr/dynamodb:41
          # custom entrypoint to limit RAM to 1G to prevent OOM on CircleCI 2.0.
          # https://circleci.com/docs/2.0/configuration-reference/#docker--machine--macosexecutor
          entrypoint: ["java", "-Xmx1G", "-jar", "DynamoDBLocal.jar"]
  
      steps:
        - checkout
        - run: make test_verbose
  


Troubleshooting
=====================

When I first tried to use this image, any test which tried to reach out to DynamoDB via ``127.0.0.1:8000`` had the following exception:

.. code-block:: bash

  Test Panicked
  Error creating table group_associations: RequestError: send request failed
  caused by: Post http://127.0.0.1:8000/: dial tcp 127.0.0.1:8000: getsockopt: connection refused
  /usr/local/go/src/runtime/panic.go:489

It seems the docker-dynamodb (DynamoDB Local) container failed to start and exited like this:

.. code-block:: bash

  Initializing DynamoDB Local with the following configuration:
  Port:	8000
  InMemory:	false
  DbPath:	null
  SharedDb:	false
  shouldDelayTransientStatuses:	false
  CorsParams:	*
  
  
  Exited with code 137

Apparently ``Exit code 137`` is a classic Docker + Java error code caused by an OOM (out of memory).

By default, projects on CircleCI build in virtual environments with 4GB of RAM but this is shared and Java acts greedy when inside a container so it needs a limit by adding ``-Xmx1G`` to the ``entrypoint``!

References:

* https://circleci.com/blog/how-to-handle-java-oom-errors/
* https://circleci.com/docs/2.0/postgres-config/
