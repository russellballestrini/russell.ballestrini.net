You can hack on FreeNAS 9
#########################
:date: 2014-05-15 01:06
:author: Russell Ballestrini
:tags: Code
:slug: you-can-hack-on-freenas-9
:status: published

This post analyses the FreeNAS 9 code base and discusses the various
places users may feel confident to hack on.

FreeNAS uses the following software stack:

Django
    A Python Web Application Framework which complies with WSGI

Nginx
    A very fast web server which may act as a reverse proxy server for
    HTTP, HTTPS, SMTP, POP3, and IMAP protocols, as well as a load
    balancer and HTTP cache.

Dojo Toolkit
    The Javascript toolkit used to create widgets and handle client side
    processing.

FreeBSD
    FreeBSD is an advanced computer operating system used to power
    modern servers.

Want to hack on the frontend web application?
    Start here if you enjoy Python, or if you really enjoy coding on
    Django applications:
    
    https://github.com/freenas/freenas/tree/master/gui

Want to hack on the GUI?
    Start here if you are a front end developer and enjoy writing HTML,
    CSS, and working with Javascript:

    https://github.com/freenas/freenas/tree/master/gui/templates

Want to change Nginx?
    Take a look here if you would like to review, change, or tune Nginx
    on FreeNAS:

    https://github.com/freenas/freenas/tree/master/nanobsd/Files/usr/local/etc/nginx
    This directory holds the nginx "vhost" config files and CGI parameters.

Want to hack on the OS?
    Start here, if you know about ``FreeBSD`` or operating systems in general:

    https://github.com/freenas/freenas/tree/master/nanobsd
    This directory seems like a customized and completely version controlled nanoBSD install!
