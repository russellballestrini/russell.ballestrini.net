nosslsearch cname is a bad idea and solution
############################################
:date: 2012-03-26 11:51
:author: Russell Ballestrini
:tags: Opinion, Security
:slug: nosslsearch-cname-is-a-bad-idea-and-solution
:status: published

| 
|  **Google SafeSearch and SSL Search for Schools suggests implementing
  the following changes to the network:**

    To utilize the no SSL option for your network, configure the DNS
    entry for www.google.com to be a CNAME for nosslsearch.google.com.

| 
|  **
   Here are the reasons why this is a bad idea and solution:**

-  In order to create a CNAME record for www.google.com we need to
   become an authoritative master of that zone.
-  If you become an authoritative master you need to host all of
   Google's DNS resource records for the domain.
-  Google is asking us to DNS poison it's flag ship product on our
   networks.
-  If other companies follow suit the internet will quickly become
   unmanageable. DNS was not ment to work this way.
-  Not all networks have a local DNS server

| 
|  This is a bad idea. Please change your stance on this matter.

| 
|  Reference:
  http://support.google.com/websearch/bin/answer.py?hl=en&answer=186669
