Why does a Hash provide better message integrity then an Internet checksum?
###########################################################################
:date: 2012-02-13 19:19
:author: Russell Ballestrini
:tags: Code, Security
:slug: why-does-a-hash-provide-better-message-integrity-then-an-internet-checksum
:status: published

**Why does a Hash provide better message integrity then an Internet
checksum?**

Hash function and checksum function both return a value which cannot be
reversed.

| An Internet checksum (TCP checksum or IP checksum) is designed to
  detect common errors quickly and efficiently. An Internet checksum
  does not attempt to prevent collisions.
|  *Man cksum for more info.*

A Hash provides better message integrity because it has less collisions
then an Internet checksum. A collision means there is more then one way
to produce the same sum. A great hash function aims to reduce the
occurrence of collisions. *Man md5 and sha for more info.*

**What is a collision**

| Let H() be a hash function. Let x and y be two differing messages.
|  *H(x) = H(y)* would be a collision.

**I like to use python to show examples of hash functions**

In this example I pass a message into the MD5 hash function to produce a
resulting hash of the message. You can think of this hashed output as a
finger print of the message.

::

    import hashlib as h
    message = "This message will be placed into an MD5 hash function to authenticate its integrity."
    print h.md5(message).hexdigest()

.. raw:: html

   </p>

| *Hash Output:*

::

    18f189f94b245ad8566206c199b4f60a

.. raw:: html

   </p>

Now If I passed that message to you along with its MD5 hash hex
representation, you could put the message into your own MD5 hash
function and compare the resulting hash. This method is used to validate
the message or verify data integrity.

**Can you "decrypt" a hash of a message to get the original message**

No! A hash may *not* be reversed, which means it cannot be decrypted.

.. raw:: html

   </p>

By design a hash algorithm has no inverse, there is no way to get the
original message from the hash. This is good news, turns out we have
some really great applications for this type of function. We can
validate messages, we can securely store passwords, and we can quickly
determine if a message or file has been tampered with.

When using a publicly known hash function for storing password hashes,
make sure to always use a salt or shared secret. Failure to do so will
make your storage scheme susceptible to a rainbow table attack. A
rainbow table allows a cracker to quickly match a list of hashes with a
table of previously computed hash values and correlated passwords.

**What is salt or a shared secret?**

You can use salt or a shared secret to add extra data to a message
before hashing with a publicly known algorithm. Below I will document
how to properly add salt to a message before generating a SHA256 hash.

::

    import hashlib as h
    message = "This message and some salt will be hashed with SHA 256."
    salt = "This is some secret salt data"
    print h.sha256(message+salt).hexdigest()

.. raw:: html

   </p>

| *Hash Output:*

::

    5e8d86bab9604620f19cfbc5f836f47feb9e8c9e74264fff1f4938bdaab1eeaa

.. raw:: html

   </p>

Adding a salt to the message allows us to use a publicly know algorithm
in a more protected manner.

**Can you spot the error in the python code below?**

::

    import hashlib as h
    message = "This message and some salt will be hashed with SHA 256."
    salt = "This is some secret salt data"
    print h.sha256(message).hexdigest()+salt

.. raw:: html

   </p>

If you guessed that the message and salt BOTH need to be hashed together
then you are correct!

The above code would have produced the following invalid hash:

| *Hash Output:*

::

    79cd4bfa1bcb71a7a1b5bfd5e8cfc8368a6cc6cb836d24bf04f2ef2bd0e81261This is some secret salt data

.. raw:: html

   </p>

**You should follow me on twitter
`here <https://twitter.com/#!/RussellBal>`__.**
