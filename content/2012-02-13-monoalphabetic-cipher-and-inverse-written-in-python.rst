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

::

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

::

    encrypted_message = "rmij'u uamu xyj"
    decrypted_message = []
    for letter in encrypted_message:
        try:
            decrypted_message.append( inverse_monoalpha[letter] )
        except KeyError:
            decrypted_message.append( letter )

    print ''.join( decrypted_message )

**Decrypted message:** ``wasn't that fun``
