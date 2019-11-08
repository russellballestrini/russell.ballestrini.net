Unity collab not working on Fedora because of invalid CA certificate path
##########################################################################

:author: Russell Ballestrini
:slug: unity-collab-not-working-on-fedora-because-of-invalid-ca-certificate-path
:date: 2019-11-08 12:19
:tags: Code, Games
:status: published

.. image:: /uploads/2019/unity-collab-fedora-ca-certificate-error-no-link.png
   :align: center
   :alt: An image showing that Unity Collab is not linked

This issue blocked me for about two days and prevented me from collaborating with another engineer at `gumyum` games studio.

He was on Windows and he was able to interact with collab and our shared project owned by our shared org while I was on Fedora 30.

.. image:: /uploads/2019/unity-collab-fedora-ca-certificate-error-curl.png
   :align: center
   :alt: An image showing that Unity is looking for the CA Certificates in the wrong location

Apparently Unity naively assumes that a Linux system's copy of the root CA certificates is located `/etc/ssl/certs/ca-certificates.crt`. This is the default location on Debian and Ubuntu based systems but not Fedora or Redhat, which uses the `/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem` file.

The work around is simple, we create a soft link between the paths::
 
 sudo ln -s /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem /etc/ssl/certs/ca-certificates.crt

.. image:: /uploads/2019/unity-collab-fedora-ca-certificate-error-fixed.png
   :align: center
   :alt: An image showing that Unity Collab is working again!


