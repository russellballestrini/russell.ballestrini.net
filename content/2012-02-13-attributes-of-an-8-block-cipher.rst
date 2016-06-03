Attributes of an 8-block cipher
###############################
:date: 2012-02-13 00:50
:author: Russell Ballestrini
:tags: Security
:slug: attributes-of-an-8-block-cipher
:status: published

**Consider an 8-block cipher and answer the following:**

How many possible input blocks does this cipher have?

How many possible mappings are there?

If we view each mapping as a key, then how many possible keys does this cipher have?

To find the input blocks of this cipher we raise 2 to the 8th power. 2^8 = 256 possible inputs.

To find the number of possible mappings we take the 256 input blocks and
find it's factorial. There are 256! possible mappings.

We can view each of these mappings as a key, so this cipher has 256! keys.
