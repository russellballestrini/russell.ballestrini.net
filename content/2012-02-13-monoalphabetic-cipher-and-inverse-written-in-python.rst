Monoalphabetic Cipher and Inverse Written in Python 
####################################################
:date: 2012-02-13 22:39
:author: Russell Ballestrini
:tags: Code, Security
:slug: monoalphabetic-cipher-and-inverse-written-in-python
:status: published

| 
|  **Here is my implementation of a Monoalphabetic Cipher written with a
  python dictionary:**

.. code-block:: python

    monoalpha = {
        'a': 'm',
        'b': 'n',
        'c': 'b',
        'd': 'v',
        'e': 'c',
        'f': 'x',
        'g': 'z',
        'h': 'a',
        'i': 's',
        'j': 'd',
        'k': 'f',
        'l': 'g',
        'm': 'h',
        'n': 'j',
        'o': 'k',
        'p': 'l',
        'q': 'p',
        'r': 'o',
        's': 'i',
        't': 'u',
        'u': 'y',
        'v': 't',
        'w': 'r',
        'x': 'e',
        'y': 'w',
        'z': 'q',
        ' ': ' ',
    }

    inverse_monoalpha = {}
    for key, value in monoalpha.iteritems():
        inverse_monoalpha[value] = key

    message = "This is an easy problem"
    encrypted_message = []
    for letter in message:
        encrypted_message.append( monoalpha[letter.lower()] )

    print ''.join( encrypted_message )

**The encrypted output:** ``uasi si mj cmiw lokngch``

**Now we may use the inverse cipher to decrypt a message, "rmij'u uamu
xyj"**

.. code-block:: python

    encrypted_message = "rmij'u uamu xyj"
    decrypted_message = []
    for letter in encrypted_message:
        try:
            decrypted_message.append( inverse_monoalpha[letter] )
        except KeyError:
            decrypted_message.append( letter )

    print ''.join( decrypted_message )

**Decrypted message:** ``wasn't that fun``

Random Cipher
===============

This is a function to generate a random Monoalphabetic cipher:

.. code-block:: python

 from string import letters, digits
 from random import shuffle

 def random_monoalpha_cipher(pool=None):
     """Generate a Monoalphabetic Cipher"""
     if pool is None:
         pool = letters + digits
     original_pool = list(pool)
     shuffled_pool = list(pool)
     shuffle(shuffled_pool)
     return dict(zip(original_pool, shuffled_pool))

