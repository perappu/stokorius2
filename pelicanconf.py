#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'stokori'
SITENAME = 'stokori.us'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = [('Twitter', 'http://twitter.com/stokori')]

# Social widget
SOCIAL = [('Twitter', 'http://twitter.com/stokori')]

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['extract_toc','summary','clean_summary','thumbnailer']
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

ARTICLE_URL = "{category}/{slug}/"
ARTICLE_SAVE_AS = "{category}/{slug}/index.html"

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

CATEGORY_URL = "category/{slug}/"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

ARCHIVES_URL = "archives/"
ARCHIVES_SAVE_AS = 'archives/index.html'

IMAGE_PATH = 'images'
THUMBNAIL_DIR = 'thumbs'
THUMBNAIL_KEEP_NAME = True
THUMBNAIL_SIZES = {
    'vertical': '200x?',
    'horizontal': '?x300',
    'square': '200x200'
}

# Theme Configuration
THEME = 'theme/'