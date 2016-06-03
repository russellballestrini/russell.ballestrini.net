Dealing with pagination in Python
#################################
:date: 2014-11-13 21:06
:author: Russell Ballestrini
:tags: Code, DevOps
:slug: dealing-with-pagination-in-python
:status: published

So I'm working with an API (AWS ElastiCache) that offers mandatory
pagination of results. I need to get all results, so I took some time to
work out this logic.

::

    def combine_results(function, key, marker=0, **kwargs):
        """deal with manditory pagination of AWS result descriptions"""
        results = []
        while marker != None:
            result = function(marker = marker, **kwargs)
            marker = nested_lookup('Marker', result)[0]
            results += nested_lookup(key, result)
        return results

.. raw:: html

   </p>

| Not only is the AWS ElastiCache API paginated but it also appears
  deeply nested in lists and dicts.
|  I use this to burn it with fire:

::


    def nested_lookup(key, dictionary):
        """Lookup a key in a nested dictionary, return a list of values"""
        return list(_nested_lookup(key, dictionary))

    def _nested_lookup(key, dictionary):
        """ 
        Lookup a key in a nested dictionary, return value

        Authors: Dougles Miranda and Russell Ballestrini
        """
        if isinstance(dictionary, list):
            for d in dictionary:
                for result in _nested_lookup(key, d): 
                    yield result

        if isinstance(dictionary, dict):
            for k, v in dictionary.iteritems():
                if k == key:
                    yield v
                elif isinstance(v, dict):
                    for result in _nested_lookup(key, v): 
                        yield result
                elif isinstance(v, list):
                    for d in v:
                        for result in _nested_lookup(key, d): 
                            yield result

The end result is we have access to paginated and deeply nested data
with a simple to use function:

::

    >>> from lib import combine_results, nested_lookup
    >>> d = elasticache_connection.describe_cache_clusters()
    >>> nested_lookup('CacheClusterId', d)
    [u'demo04-a-redis', u'demo04-b-redis', u'demo06-a-redis', u'demo06-b-redis', u'test-a-memcached', u'test-b-redis', u'ops01-redis', u'qa01-redis', u'ops02-redis', u'qa02-redis', u'int01-a-redis', u'int01-b-redis', u'ops03-redis', u'ops04-redis']

Here are some unit tests to prove these functions work like expected:

::

    from unittest import TestCase

    from lib.util import (
      combine_results,
      nested_lookup,
      _nested_lookup,
    )

    def my_func_that_paginates(max_results=3, marker=0):
        """this function sort of mocks the paginated AWS description results"""
        data = [
          {'desired_key' : 0},
          {'desired_key' : 1},
          {'desired_key' : 2},
          {'desired_key' : 3},
          {'desired_key' : 4},
          {'desired_key' : 5},
          {'desired_key' : 6},
          {'desired_key' : 7},
          {'desired_key' : 8},
          {'desired_key' : 9},
        ]
        new_marker = marker + max_results
        if new_marker > len(data):
            # last page!
            page = data[marker:]
            return {'results' : page, 'Marker' : None}
        page = data[marker:new_marker]
        return {'results' : page, 'Marker' : new_marker}

    class TestCombineResults(TestCase):

        def test_combine_results_returns_all_results(self):
            expected_set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
            f = my_func_that_paginates
            result_set = set(combine_results(f, 'desired_key'))
            self.assertSetEqual(expected_set, result_set)

    class TestNestedLookup(TestCase):

        def setUp(self):
            self.subject_dict = {'a':1,'b':{'d':100},'c':{'d':200}}

        def test_nested_lookup(self):
            results = nested_lookup('d', self.subject_dict)
            self.assertEqual(2, len(results))
            self.assertIn(100, results)
            self.assertIn(200, results)
            self.assertSetEqual({100,200}, set(results))

        def test_nested_lookup_wrapped_in_list(self):
            results = nested_lookup('d', [{}, self.subject_dict, {}])
            self.assertEqual(2, len(results))
            self.assertIn(100, results)
            self.assertIn(200, results)
            self.assertSetEqual({100,200}, set(results))

        def test_nested_lookup_wrapped_in_list_in_dict_in_list(self):
            results = nested_lookup('d', [{}, {'H' : [self.subject_dict]} ])
            self.assertEqual(2, len(results))
            self.assertIn(100, results)
            self.assertIn(200, results)
            self.assertSetEqual({100,200}, set(results))

        def test_nested_lookup_wrapped_in_list_in_list(self):
            results = nested_lookup('d', [ {}, [self.subject_dict, {}] ])
            self.assertEqual(2, len(results))
            self.assertIn(100, results)
            self.assertIn(200, results)
            self.assertSetEqual({100,200}, set(results))

With this test, the steps of the algorithm looks like this:

::

    {'Marker': 3, 'results': [{'desired_key': 0}, {'desired_key': 1}, {'desired_key': 2}]}
    3
    [0, 1, 2]
    [0, 1, 2]
    {'Marker': 6, 'results': [{'desired_key': 3}, {'desired_key': 4}, {'desired_key': 5}]}
    6
    [3, 4, 5]
    [0, 1, 2, 3, 4, 5]
    {'Marker': 9, 'results': [{'desired_key': 6}, {'desired_key': 7}, {'desired_key': 8}]}
    9
    [6, 7, 8]
    [0, 1, 2, 3, 4, 5, 6, 7, 8]
    {'Marker': None, 'results': [{'desired_key': 9}]}
    None
    [9]
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ok
