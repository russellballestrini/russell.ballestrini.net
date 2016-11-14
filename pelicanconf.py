#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from os import environ

DEFAULTS = {
  'AUTHOR'    : u'Russell Ballestrini',
  'SITENAME'  : u'Russell Ballestrini',
  'SITEURL'   : 'http://127.0.0.1:8000',
  #'THEME'    : 'pelican-themes/svbhack',
  'THEME'     : 'pelican-themes/pelican-svbhack',
  'GOOGLE_ANALYTICS' : '',
  'REMARKBOX' : True,
  'LINKPEEK_APIKEY' : None,
  'LINKPEEK_SECRET' : None,
}

def get_environ_or_default(key):
    return environ.get(key, DEFAULTS[key])

AUTHOR   = get_environ_or_default('AUTHOR')
SITENAME = get_environ_or_default('SITENAME')
SITEURL  = get_environ_or_default('SITEURL')

THEME    = get_environ_or_default('THEME')

GOOGLE_ANALYTICS = get_environ_or_default('GOOGLE_ANALYTICS')

REMARKBOX = get_environ_or_default('REMARKBOX')

LINKPEEK_APIKEY = get_environ_or_default('LINKPEEK_APIKEY')
LINKPEEK_SECRET = get_environ_or_default('LINKPEEK_SECRET')

# Theme specific
USER_LOGO_URL = 'https://lh3.googleusercontent.com/-uAPZy7NmmP0/AAAAAAAAAAI/AAAAAAAAAnI/iG2P43gCL2U/s125-c/photo.jpg'
TAGLINE = '<a href="/about" class="tagline">Builds Products</a>'

PATH = 'content'

STATIC_PATHS = ['uploads']

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Atom all feed.
FEED_ALL_ATOM = 'feeds/all.atom.xml'

# Feed generation is usually not desired when developing
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
  ('Remarkbox', 'http://remarkbox.com/'),
  ('LinkPeek', 'https://linkpeek.com/'),
  ('unturf', 'https://unturf.com/'),
)

# Social widget
SOCIAL = (
  ('@russellbal', 'https://twitter.com/russellbal'),
  ('github', 'https://github.com/russellballestrini'),
  ('bitbucket', 'https://bitbucket.org/russellballestrini'),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU = False

# teach pelican to use directory/index.html files
ARTICLE_URL = '{slug}/'
PAGE_URL = '{slug}/'
CATEGORY_URL = 'category/{slug}/'
TAG_URL = 'tags/{slug}/'
AUTHOR_URL = 'author/{slug}/'

RANDOM = 'random.html'

# Adjust save location.
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_SAVE_AS = '{slug}/index.html'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_SAVE_AS = 'tags/{slug}/index.html'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'

# Setup filters and plugins.

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['random_article']

# register filters.
#JINJA_FILTERS = {'linkpeek':linkpeek}

# register linkpeek docutils directive.
import sys
sys.path.append('lib')
import rst_linkpeek
linkpeek = rst_linkpeek.LinkPeek
linkpeek.apikey = LINKPEEK_APIKEY
linkpeek.secret = LINKPEEK_SECRET
linkpeek.register()

