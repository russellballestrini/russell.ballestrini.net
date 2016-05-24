#!/usr/bin/python
from hashlib import md5
from urllib import quote

# signup for an APIKEY here: https://linkpeek.com/signup
APIKEY = ''
SECRET = ''

def api_v1( uri, apikey=APIKEY, secret=SECRET, size='336' ):
    """LinkPeek.com API v1 helper function"""
    token = md5( secret + uri + size ).hexdigest()
    uri = quote( uri )
    return "http://linkpeek.com/api/v1?uri=%s&apikey=%s&token=%s&size=%s" % (
    uri, apikey, token, size)


if __name__ == '__main__':
    """TESTS"""
    print api_v1( 'lostquery.com' )
    print api_v1( 'http://lostquery.com', size='200x400' )
    print api_v1( 'https://lostquery.com', size='400x200' )
