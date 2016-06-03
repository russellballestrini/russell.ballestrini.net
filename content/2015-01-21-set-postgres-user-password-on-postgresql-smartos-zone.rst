Set postgres user password on PostgreSQL SmartOS Zone
#####################################################
:date: 2015-01-21 22:28
:author: Russell Ballestrini
:tags: DevOps, Guide
:slug: set-postgres-user-password-on-postgresql-smartos-zone
:status: published
:summary:

Connect to zone and determine the auto generated password for postgres
user::

    cat /var/svc/log/system-zoneinit\:default.log | grep PGSQL_PW

document the result and log into postgres with the following command,
entering the password when prompted::

    [root@psql ~]# psql --user postgres

Alter the postgres role's password::

    postgres=# ALTER ROLE postgres UNENCRYPTED PASSWORD 'new-password';

Now exit (``\q``) then try to log in with the new password.

In my case I was setting up PostgreSQL for testing out Zabbix monitoring
system. So I did the following as the postgres user::

    postgres=# CREATE USER zab UNENCRYPTED PASSWORD 'zabby'
    postgres=# CREATE DATABASE zab OWNER zab;

