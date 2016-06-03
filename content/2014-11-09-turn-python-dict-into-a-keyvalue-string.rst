Turn python dict into a key=value string and back again
#######################################################
:date: 2014-11-09 22:02
:author: Russell Ballestrini
:tags: Code, DevOps
:slug: turn-python-dict-into-a-keyvalue-string
:status: published

I'm currently refactoring a script that tags AWS resources and I came up
with this one liner to generate pretty output. It basically turns
``{'tag1':'value1','tag2':'value2'}`` into ``tag1=value1, tag2=value2``.
Here is the code:

::

    ', '.join(['='.join(key_value) for key_value in {'a':'1','b':'2'}.items() ])

.. raw:: html

   </p>

Oh and here is a function if you love this!

::

    def dict_to_key_value(data, sep='=', pair_sep=', '):
        """turns {'tag1':'value1','tag2':'value2'} into tag1=value1, tag2=value2"""
        return pair_sep.join([sep.join(key_value) for key_value in data.items()])

.. raw:: html

   </p>

Careful, this might blow up on dictionaries that nest other objects.
Also here is a test:

::

    def test_dict_to_key_value():
        data = {'tag1':'value1','tag2':'value2'}
        pretty_str = dict_to_key_value(data)
        assert('tag1=value1' in pretty_str)
        assert('tag2=value2' in pretty_str)
        assert('tag1=value1, tag2=value2' in pretty_str)
        not_as_pretty = dict_to_key_value(data,'x','x')
        assert('tag1xvalue1xtag2xvalue2' in not_as_pretty)

.. raw:: html

   </p>

Here is the inverse, taking a list of key\_value strings and returning a
dictionary of the data:

::

    def key_value_to_dict(key_value_list, sep='=', pair_sep=',' ):
        """ 
        Accept a key_value_list, like::

          key_value_list = ['a=1,b=2', 'c=3, d=4', 'e=5']

        Return a dict, like::

          {'a':'1', 'b':'2', 'c':'3', 'd':'4', 'e':'5'}
        """
        d = {}
        for speclist in key_value_list:
            for spec in speclist.strip().split(','):
                key, value = spec.strip().split('=')
                d[key] = value
        return d

.. raw:: html

   </p>

And of course a test to prove it works how we expect:

::

    def test_key_value_to_dict():
        key_value_list = ['a=1,b=2', 'c=3, d=4', 'e=5']
        desired_result = {'a':'1', 'b':'2', 'c':'3', 'd':'4', 'e':'5'}
        assert(key_value_to_dict(key_value_list) == desired_result)

.. raw:: html

   </p>
