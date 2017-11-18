#!/usr/bin/python
from hashlib import md5
from urllib import quote

# signup for an APIKEY here: https://linkpeek.com/signup
APIKEY = ''
SECRET = ''

def api_v1(uri, apikey=APIKEY, secret=SECRET, size='336', viewport='1024'):
    """LinkPeek.com API v1 helper function"""
    token = md5(secret + uri + size).hexdigest()
    return 'https://linkpeek.com/api/v1?uri={}&apikey={}&token={}&size={}&viewport={}'.format(
            quote(uri), apikey, token, size, viewport)


if __name__ == '__main__':
    """TESTS"""
    print api_v1('remarkbox.com')
    print api_v1('https://www.remarkbox.com', size='200x400')
    print api_v1('https://www.remarkbox.com', size='400x200')
