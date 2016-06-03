mysql-back
##########
:date: 2014-02-07 16:39
:author: Russell Ballestrini
:tags: Code, DevOps
:slug: mysql-back
:status: published

``mysql-back``\ is a backup utility script to dump (backup) and gzip
every MySQL database on a host.

I use ``mysql-back`` in combination with cron to perform regular
database dumps of MySQL servers to the ``/archive/db`` partition on
localhost. I then have a central long term storage server that collects
the ``/archive`` partition from every host.

**mysql-back:**

::

    #!/bin/bash

    USER="root"
    PASSWORD=""
    TODAY=`date +%Y-%m-%d`
    OUTPUTDIR="/archive/db/$TODAY"
    MYSQLDUMP=`which mysqldump`
    MYSQL=`which mysql`
    GZIP=`which gzip`

    mkdir $OUTPUTDIR

    # get a list of databases
    databases=`$MYSQL --user=$USER --password=$PASSWORD \
     -e "SHOW DATABASES;" | tr -d "| " | grep -v Database`

    # dump each database in turn
    for db in $databases; do
        $MYSQLDUMP --force --opt --user=$USER --password=$PASSWORD \
        --databases $db > "$OUTPUTDIR/$db.sql"
    done

    # compress all of the files
    $GZIP $OUTPUTDIR/*

    # clean up all dumps 30 days old
    find /archive/db -ctime +30 -type d | xargs rm -rf

.. raw:: html

   </p>

If you ever need to restore, like in my case when I moved all my
databases over to a brand new Percona MySQL SmartOS zone, I used the
following command:

::

    zcat *sql.gz | mysql -u root -p

.. raw:: html

   </p>
