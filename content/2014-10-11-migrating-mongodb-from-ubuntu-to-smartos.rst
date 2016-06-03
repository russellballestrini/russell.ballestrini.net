Migrating MongoDB from Ubuntu to SmartOS
########################################
:date: 2014-10-11 20:52
:author: Russell Ballestrini
:tags: DevOps, Guide
:slug: migrating-mongodb-from-ubuntu-to-smartos
:status: published

I installed the mongodb 14.2.0
(``uuid a5775e36-2a02-11e4-942a-67ae7a242985``) dataset and launched a
new zone. The zone automatically creates a username and password for
admin and "quickbackup". You can find these passwords by running the
following command inside the zone:

::

    cat /var/svc/log/system-zoneinit\:default.log | grep -i mon

First thing I did was disable authentication by modifying
``/opt/local/etc/mongod.conf``:

::

    #auth = true
    noauth = true

Then I restarted MongoDB to re-read its configuration:

::

    svcadm restart mongodb

Next I attempted to restore the database BSON files, with the following
command:

::

    mongorestore --db=taco taco/taco.bson

But I got the following error:

::

    connected to: 127.0.0.1
    terminate called after throwing an instance of 'std::runtime_error'
      what():  locale::facet::_S_create_c_locale name not valid
    Abort (core dumped)

After some research I learned that I needed to export the following
variable before running the restore:

::

    export LC_ALL=C
