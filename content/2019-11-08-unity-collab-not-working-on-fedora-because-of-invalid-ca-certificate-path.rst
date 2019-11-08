Unity Collab not working on Fedora because of an invalid CA certificate path
#############################################################################

:author: Russell Ballestrini
:slug: unity-collab-not-working-on-fedora-because-of-invalid-ca-certificate-path
:date: 2019-11-08 12:19
:tags: Code, Games, gumyum
:status: published

This issue blocked me for about two days and prevented me from collaborating with another engineer at `gumyum co-operative video game studio <https://www.gumyum.com>`_.

.. image:: /uploads/2019/unity-collab-fedora-ca-certificate-error-no-link.png
   :align: center
   :alt: An image showing that Unity Collab is not linked


The other engineer's environment was Windows and he was able to interact with collab and our shared project owned by our shared org. My environment was Fedora 30 and was not working with collab, however I was able to download the project files.

.. image:: /uploads/2019/unity-collab-fedora-ca-certificate-error-curl.png
   :align: center
   :alt: An image showing that Unity is looking for the CA Certificates in the wrong location

The issue?

Apparently Unity naively assumes that a Linux system's copy of the root CA certificates is located `/etc/ssl/certs/ca-certificates.crt`. This is the default location on Debian and Ubuntu based systems but not Fedora or Redhat, which uses the `/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem` file.

The work around is simple, create a soft link between the paths::
 
 sudo ln -s /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem /etc/ssl/certs/ca-certificates.crt

.. image:: /uploads/2019/unity-collab-fedora-ca-certificate-error-fixed.png
   :align: center
   :alt: An image showing that Unity Collab is working again!


Please come back again soon to learn more about the games we are building over here at `gumyum`!
