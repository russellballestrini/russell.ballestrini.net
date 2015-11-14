#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Russell Ballestrini'
SITENAME = u'Russell Ballestrini'
SITEURL = ''

THEME='pelican-themes/svbhack'
#THEME='pelican-themes/svbtle'
#THEME='pelican-themes/medius'
#THEME='pelican-themes/mediumfox'
#THEME='pelican-themes/pure'

PATH = 'content'

STATIC_PATHS = ['uploads']

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
  ('LinkPeek', 'https://linkpeek.com/'),
  ('RemarkBox', 'http://remarkbox.com/'),
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

# teach pelican to use directory/index.html files
ARTICLE_URL = '{slug}/'
PAGE_URL = '{slug}/'
CATEGORY_URL = 'category/{slug}/'
TAG_URL = 'tags/{slug}/'
AUTHOR_URL = 'author/{slug}/'

# Adjust save location.
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_SAVE_AS = '{slug}/index.html'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_SAVE_AS = 'tags/{slug}/index.html'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
