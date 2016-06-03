Reasons why some Internet entities might want secure communication
##################################################################
:date: 2012-02-08 18:23
:author: Russell Ballestrini
:tags: Security
:slug: reasons-why-some-internet-entities-might-want-secure-communication
:status: published
:summary:

Internet entities often desire to communicate securely, some reasons include:

#. **Web Servers:** Communication on the Internet, or any network for that
   matter, should be encrypted before transmitting sensitive data. This
   will help prevent snooping from unauthorized parties. Most often SSL or
   HTTPS may be used to create a secure communication “tunnel” between a
   web server and a web client (browser).

#. **Server Administration:** 
   Operators should always use a secure protocal when working on a server or remote computer.
   SSH (Secure Shell) wins the popularity contest with server admins.

#. **DNS Servers:**
   Using DNSSEC could help prevent DNS poisoning and certifies DNS data.
   DNS was first conceived as a distributed and highly scalable address lookup system.
   Security was not its top priority.
   Since then we have new DNSSEC extensions which allow for origin authentication of DNS data,
   authenticated denial of existence, and data integrity.
   DNSSEC does not attempt to solve availability and confidentiality.
