Monoalphabetic Cipher and Inverse Written in Python 
####################################################
:date: 2012-02-13 22:39
:author: Russell Ballestrini
:tags: Code, Security
:slug: monoalphabetic-cipher-and-inverse-written-in-python
:status: published

.. contents::

introduction and background
===============================

A monoalphabetic cipher uses fixed substitution over the entire message.

You can build a monoalphabetic cipher using a Python dictionary, like so:

.. code-block:: python

    monoalpha_cipher = {
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

We can create an inverse of this cipher dictionary by switching the key and value places:

.. code-block:: python

    inverse_monoalpha_cipher = {}
    for key, value in monoalpha_cipher.iteritems():
        inverse_monoalpha_cipher[value] = key

Now that we have both the cipher and the inverse_cipher, we may encrypt a message.

**Encryption example:**

.. code-block:: python

    message = "This is an easy problem"
    encrypted_message = []
    for letter in message:
        encrypted_message.append(monoalpha_cipher.get(letter, letter))
        
    print(''.join(encrypted_message))

Result:
  ``Tasi si mj cmiw lokngch``

Using the inverse_cipher, We may *decrypt* a message.

**Decryption example:**

.. code-block:: python

    encrypted_message = "rmij'u uamu xyj?"
    decrypted_message = []
    for letter in encrypted_message:
         decrypted_message.append( inverse_monoalpha_cipher.get(letter, letter))
         
    print(''.join( decrypted_message ))

Result:
  ``wasn't that fun?``


monoalphabetic_cipher.py
=============================

Here is a toy library I wrote to make the process repeatable -

``monoalphabetic_cipher.py``:

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

 def inverse_monoalpha_cipher(monoalpha_cipher):
     """Given a Monoalphabetic Cipher (dictionary) return the inverse."""
     inverse_monoalpha = {}
     for key, value in monoalpha_cipher.iteritems():
         inverse_monoalpha[value] = key
     return inverse_monoalpha

 def encrypt_with_monoalpha(message, monoalpha_cipher):
     encrypted_message = []
     for letter in message:
         encrypted_message.append(monoalpha_cipher.get(letter, letter))
     return ''.join(encrypted_message)

 def decrypt_with_monoalpha(encrypted_message, monoalpha_cipher):
     return encrypt_with_monoalpha(
                encrypted_message,
                inverse_monoalpha_cipher(monoalpha_cipher)
            )

     
monoalphabetic_cipher.py example usage
==========================================

Here I show how to use the library:

.. code-block:: python

 >>> # load the module / library as 'mc'.
 >>> import monoalphabetic_cipher as mc


 >>> # generate a random cipher (only if needed).
 >>> cipher = mc.random_monoalpha_cipher()

 >>> # output the cipher (store for safe keeping).
 >>> print(cipher)

 >>> # encrypt a message with the cipher.
 >>> mc.encrypt_with_monoalpha('Hello all you hackers out there!', cipher)
 'sXGGt SGG Nt0 HSrLXFC t0U UHXFX!'

 >>> # decrypt a message with the cipher. 
 >>> mc.decrypt_with_monoalpha('sXGGt SGG Nt0 HSrLXFC t0U UHXFX!', cipher)
 'Hello all you hackers out there!'
