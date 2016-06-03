What are the differences between message confidentiality and message integrity
##############################################################################
:date: 2012-02-08 17:47
:author: Russell Ballestrini
:tags: Security
:slug: what-are-the-differences-between-message-confidentiality-and-message-integrity
:status: published
:summary:

| 

**What are the differences between message confidentiality and message
integrity? Can you have confidentiality without integrity? Can you have
integrity without confidentiality?**

| 

message confidentiality
    Two or more hosts communicate securely, typically using encryption.
    The communication cannot be monitored (sniffed) by untrusted hosts.
    The communication between trusted parties is confidential.

message integrity
    The message transported has not been tampered with or altered. A
    message has integrity when the payload sent is the same as the
    payload received.


Sending a message confidentially does not guarantee data integrity. Even
when two nodes have authenticated each other, the integrity of a message
could be compromised during the transmission of a message.

Yes, you can have integrity of a message without confidentiality. One
can take a hash or sum of the message on both sides to compare. Often we
share downloadable files and provide data integrity using md5 hash sums.
