How to capture HTTPS SSL TLS packets with wireshark
###################################################
:date: 2012-02-29 19:14
:author: Russell Ballestrini
:tags: Guide, Security
:slug: how-to-capture-https-ssl-tls-packets-with-wireshark
:status: published

This article will explain how to use wireshark to capture TCP/IP
packets. Specifically I will show how to capture encrypted (HTTPS)
packets and attempt to document the "dance" a client and server do to
build an SSL tunnel.

**What is Wireshark?**

Wireshark is a network protocol analyzer for Windows, OSX, and Linux. It
lets you capture and interactively browse the traffic running on a
computer network. Similar software includes tcpdump on Linux.

**Install Wireshark**

First step, acquire Wireshark for your operating system.

*Ubuntu Linux:* ``sudo apt-get install wireshark``

*Windows or Mac OSX:* search for wireshark and download the binary.

**How to capture packets**

This is Wireshark's main menu:

|image0|

To start a capture, click the following icon:

|image1|

A new dialog box should have appeared. Click start on your preferred
interface:

|image2|

You are now capturing packets. The packet information is displayed in
the table below the main menu:

|image3|

Now browse to an HTTPS website with your browser. I went to
https://linkpeek.com and after the page completely loaded, I stopped the
Wireshark capture:

|image4|

Depending on your network, you could have just captured MANY packets. To
limit our view to only interesting packets you may apply a filter.
Filter the captured packets by ssl and hit Apply:

|image5|

Now we should be only looking at SSL packets.

**Next we will analyze the SSL packets and answer a few questions**

**1.** For each of the first 8 Ethernet frames, specify the source of
the frame (client or server), determine the number of SSL records that
are included in the frame, and list the SSL record types that are
included in the frame. Draw a timing diagram between client and server,
with one arrow for each SSL record.

| Frame 1 client \| 1 record \| Arrival Time: Feb 15, 2012
  15:38:55.601588000
|  Frame 2 server \| 1 record \| Arrival Time: Feb 15, 2012
  15:38:55.688170000
|  Frame 3 server \| 2 record \| Arrival Time: Feb 15, 2012
  15:38:55.688628000
|  Frame 4 client \| 3 record \| Arrival Time: Feb 15, 2012
  15:38:55.697705000
|  frame 5 server \| 2 record \| Arrival Time: Feb 15, 2012
  15:38:55.713139000
|  frame 6 client \| 1 record \| Arrival Time: Feb 15, 2012
  15:38:55.713347000
|  frame 7 server \| 0 record \| Arrival Time: Feb 15, 2012
  15:38:55.713753000
|  frame 8 server \| 1 record \| Arrival Time: Feb 15, 2012
  15:38:55.715003000

**2.** Each of the SSL records begins with the same three fields (with
possibly different values). One of these fields is “content type” and
has length of one byte. List all three fields and their lengths.

| Each hexadecimal digit (also called a "nibble") represents four binary
  digits (bits) so each pair of hexadecimal digits equals 1 byte.

| a. Destination mac address \| 6 btyes \| 00 21 9b 31 99 51
|  b. Source mac address \| 6 bytes \| 00 10 db ff 20
|  c. Type: IP \| 2 byte \| 08 00

**ClientHello Records**

| **3.**\ Expand the ClientHello record. (If your trace contains
  multiple ClientHello
|  records, expand the frame that contains the first one.) What is the
  value of the
|  content type?
| hex: 16 (16+6=22) Handshake

| **4.** Does the ClientHello record advertise the cipher suites it
  supports? If so, in the first listed suite, what are the public-key
  algorithm, the symmetric-key algorithm, and the hash algorithm?
|  MD5, SHA, RSA, DSS, DES, AES

**ServertHello Records**

| **5.** Look to the ServerHello packet. What cipher suite does it
  choose?
|  Cipher Suite: TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA (0x002f)

| **6.** Does this record include a nonce? If so, how long is it? What
  is the purpose of the
|  client and server nonces in SSL?
|  Yes, 28 bytes. The ClientHello packet also generated a nonces. They
  are used to make the session communication between the two nodes
  unique. It "salts" the communication to prevent replay attacks. A
  replay attack happens when data from old communications is used to
  "crack" a current communication.

| **7.**\ Does this record include a session ID? What is the purpose of
  the session ID?
|  Yes, This is to make things efficient, in case the client has any
  plans of closing the current connection and reconnect in the near
  future.

| **8.**\ How many frames does the SSL certificate take to send?
|  In this case it took 4 frames

.. |image0| image:: /uploads/2012/02/wireshark.png
.. |image1| image:: /uploads/2012/02/wireshark-start-capture.png
.. |image2| image:: /uploads/2012/02/wireshark-sniff.png
.. |image3| image:: /uploads/2012/02/wireshark-packets.png
.. |image4| image:: /uploads/2012/02/wireshark-stop-capture.png
.. |image5| image:: /uploads/2012/02/wireshark-filter.png
