Voice Over IP with TeamSpeak
############################

:date: 2011-04-03 12:11
:author: Russell Ballestrini
:tags: Guide
:slug: voice-over-ip-with-teamspeak
:status: published

**This article will cover running a Voice Over IP service like TeamSpeak
on a VPS.**

Voice Over IP allows users to communicate using audio over the Internet.

When planning for this article I originally was going to cover ventrilo,
but their download link was obfuscated behind a heinous php session
script. Ventrilo also does not have a Linux client although they have
been promising one for quite some time.

Instead we will cover how to install and configure
`TeamSpeak <http://www.TeamSpeak.com>`__.

**Installing a teamspeak server on your VPS**

Create a user to run teamspeak.

::

    sudo adduser teamspeak

*follow the prompts*

Personally I don't want the teamspeak user to have ssh access so I added
the following to /etc/ssh/sshd\_config:

::

    DenyUsers teamspeak

Then reload ssh server config:

::

    sudo service ssh reload

Setup the installation environment.

The following 4 commands will create a directory to hold your
installation, change the ownership of the directory to the teamspeak
user, change the working directory to the new folder and then become the
teamspeak user:

::

    sudo mkdir /opt/teamspeak
    sudo chown teamspeak:teamspeak /opt/teamspeak
    cd /opt/teamspeak
    sudo su teamspeak

Download and extract TeamSpeak server software.

Find the proper package for your VPS and download it, in my case I ran:

::

    wget http://teamspeak.gameserver.gamed.de/ts3/releases/beta-30/teamspeak3-server_linux-amd64-3.0.0-beta30.tar.gz

*For best results download the latest version of teamspeak.*

A teamspeak tarball should now exist in your present working directory.
We can extract the files from the tarball by issuing the following
command:

::

    tar xvf teamspeak3-server_linux-amd64-3.0.0-beta30.tar.gz --strip-components=1

*No you don't have to type that file name out! The bash shell has tab
completion, type 'tar xvf teamsp' and then press tab. : )*

Install the TeamSpeak server software.

I had success running:

::

    ./ts3server_startscript.sh start

Write down the auto generated serveradmin password.

Configure TeamSpeak to start at system bootup.

Create a cronjob under the teamspeak user:

::

    crontab -e

Place the following into teamspeak's crontab:

::

    @reboot /opt/teamspeak/ts3server_startscript.sh start
