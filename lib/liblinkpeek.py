#!/usr/bin/python
from hashlib import md5
import urllib.parse

# signup for an APIKEY here: https://linkpeek.com/signup
APIKEY = ""
SECRET = ""

def api_v1(uri, apikey=APIKEY, secret=SECRET, size="336", viewport="1024"):
    """LinkPeek.com API v1 helper function"""
    token = md5(
        secret.encode("utf-8") +
        uri.encode("utf-8") +
        size.encode("utf-8")
    ).hexdigest()
    return "https://linkpeek.com/api/v1?uri={}&apikey={}&token={}&size={}&viewport={}".format(
        urllib.parse.quote(uri), apikey, token, size, viewport
    )


if __name__ == "__main__":
    """TESTS"""
    print(api_v1("remarkbox.com"))
    print(api_v1("https://www.remarkbox.com", size="200x400"))
    print(api_v1("https://www.remarkbox.com", size="400x200"))
