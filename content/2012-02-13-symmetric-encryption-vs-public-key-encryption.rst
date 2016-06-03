Symmetric Encryption vs Public Key Encryption
#############################################
:date: 2012-02-13 17:25
:author: Russell Ballestrini
:tags: Security
:slug: symmetric-encryption-vs-public-key-encryption
:status: published

**How many keys are involved for symmetric key encryption? How about
public key encryption?**

Suppose you have N people who want to communicate with each other using
symmetric keys. All communication between any two people, i and j, is
visible to group N. Only person i and person j can decrypt each others
messages.

**How many keys would Symmetric Encryption require to protect group N?**

I solved this with the following python function:

::

    def count_symmetric_keys( N=2 ):
        """Provide the number of entities in group N.
        return the number of symmetric keys needed for this group"""
        keys = 0
        for i in range( 0, N ): keys += i
        return keys

A reader suggested the following optimized formula:

::

    def calc_symmetric_keys( N=2 ):
        """Provide the number of entities in group N.
        return the number of symmetric keys needed for this group"""
        return N*(N-1)/2

.. raw:: html

   </p>

If group N had 10 members, it would need to generate and maintain 45
Symmetric Keys.

If group N had 50 members, it would need to generate and maintain 1225
Symmetric Keys.

Symmetric keys are also susceptible to man-in-the-middle attacks. This
attack occurs when an entity poses as a trusted entity. Let i and j be
trusted entities. Let k be an untrusted attacker. If k determined the
Symmetric key it could send or receive messages posing as i or j.

**How many keys would Public-key Encryption require to protect group
N?**

Public Key Encryption requires 2n keys or two keys per person in group
N. Public key encryption also does not require 'pre sharing' the secret
key before communication may start. Each member would need 1 public key
and 1 private key.

If group N had 10 members, it would need to generate and maintain 20
Public/Private Keys.

If group N had 50 members, it would need to generate and maintain 100
Public/Private Keys.
