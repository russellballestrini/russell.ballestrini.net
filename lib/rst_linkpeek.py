# -*- coding: utf-8 -*-
"""
Use LinkPeek via reStructuredText
=================================
This plugin allows you to use LinkPeek images from within reST documents. 
"""

from __future__ import unicode_literals
from docutils import nodes
from docutils.parsers.rst import (
  directives,
  Directive,
)

from collections import defaultdict

#from .liblinkpeek import api_v1
from liblinkpeek import api_v1

class LinkPeek(Directive):
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    has_content = True

    apikey = None
    secret = None

    params = defaultdict(str)

    def api_call(self):
        return api_v1(self.params['uri'], self.apikey, self.secret, self.params['size'])

    def _get_params(self):
        """
        turn [u'uri = linkpeek.com', u'size = 200x200']
        into {u'uri': u'linkpeek.com', u'size': u'200x200'}
        """
        params = defaultdict(str)
        for c in self.content:
            # split on = and then remove leading/trailing whitespace.
            key, value = c.split('=')
            key = key.strip()
            value = value.strip()
            params[key] = value
        self.params = params
        return params

    @property
    def action_registry(self):
        """return an registry (dictionary) or action methods."""
        return {
            'image' : self.html_image,
            'link-image' : self.html_link_image,
        }

    def get_action(self, action_name):
        """get action method from action registry or use default."""
        return self.action_registry.get(action_name, self.api_call)

    def html_image(self):
        """return html image markup."""
        html = '<img src="{}" title="{}" style="{}" class="{}" />'
        return html.format(self.api_call(), self.params['title'], self.params['style'], self.params['class'])

    def html_link_image(self):
        """return html link image markup."""
        html = '<a href="{}" target="_blank">{}</a>'
        return html.format(self.params['uri'], self.html_image())

    def run(self):
        """this method is fired when rendering."""
        self._get_params()

        action =  self.get_action(self.params['action'])

        output = action()

        return [nodes.raw('', output, format='html')]

    @classmethod
    def register(cls):
        """register this directive/class with docutils."""
        # this allows us to modify apikey and secret attributes before registering.
        directives.register_directive('linkpeek', cls)


