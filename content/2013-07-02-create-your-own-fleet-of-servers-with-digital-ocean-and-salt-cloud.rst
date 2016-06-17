Create your own fleet of servers with Digital Ocean and salt-cloud
##################################################################
:date: 2013-07-02 22:20
:author: Russell Ballestrini
:tags: DevOps, Guide
:slug: create-your-own-fleet-of-servers-with-digital-ocean-and-salt-cloud
:status: published

Have you heard about Digital Ocean?
They offer a polished user interface, KVM guests with SSD storage, and an API to interact with a cloud of hypervisors.
API integration got you down?
Don't worry, salt-cloud has already integrated Digital Ocean among it's list of providers!
The rest of this post illustrates the steps I took to configure salt-cloud to work with Digital Ocean.

This guide assumes you already have a: 

* salt-master
* `Digital Ocean <https://www.digitalocean.com/?refcode=27e015299dc7%20>`__ account.

**Step one,** install the most recent version of salt-cloud.

On the salt-master:

::

    sudo apt-get install salt-cloud

    # or if you prefer ...
    pip install salt-cloud==2015.5.0

    # last verify it was successfully installed
    salt-cloud --version


**Step two,** configure salt-cloud.

Salt-cloud uses the following files YAML files for configuration:

/etc/salt/cloud.conf.d/main.conf:
 This is the main configuration file. I have the following statements:

::

    minion:
        master: master.foxhop.net
        append_domain: foxhop.net

/etc/salt/cloud.providers/do.conf:
  This is a provider configuration file for Digital Ocean (do).
  Collect your client\_key and personal\_access\_token (api\_key) from the Digital Ocean user dashboard.
  Also create an SSH key and add the public key using the dashboard:

::

    # For Digital Ocean
    do:
      provider: digital_ocean
      client_key: MyClientKeyLiftedFromDashboard
      personal_access_token: MyAPIKeyLiftedFromDashboard
      ssh_key_file: /keys/digital-ocean-salt-cloud
      ssh_key_name: digital-ocean-salt-cloud.pub

/etc/salt/cloud.profiles/do.conf:
  This is the Digital Ocean profiles configuration file.
  We will create just two profiles for now, but you can create unlimited named combinations.

::

    ubuntu-12-04-do-512:
      provider: do
      image: ubuntu-12-04-x64
      size: 512mb
      location: nyc1

    ubuntu-14-04-do-512:
      provider: do
      image: ubuntu-14-04-x64
      size: 512mb
      location: nyc1

ssh\_key\_file:
 This is your private SSH key located on your salt-master

ssh\_key\_name:
 This is the name of the public key you added in your Digital Ocean dashboard

size:
 The size or plan you would like to provision, 512mb is the smallest plan

location:
 The geographical region, location, and/or data center

image:
 The operating system image

After you configure the do provider in /etc/salt/cloud.providers you
gain access to the following commands::

    salt-cloud --list-sizes do
    salt-cloud --list-locations do
    salt-cloud --list-images do
    salt-cloud --help


**Lets provision a new cloud server!**

::

    salt-cloud --profile ubuntu-14-04-do-512 deejay

If all goes well you should have a newly provisioned server bootstrapped with salt-minion.
The new minion's keys are already added to the salt-master.
Now you just need to run highstate!
