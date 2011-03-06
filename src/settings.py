# -*- coding: utf-8 -*-

import os


DEBUG = True
TEMPLATE_DEBUG = DEBUG


ROOT_PATH = os.path.dirname(__file__)
ROOT_URLCONF = 'urls'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.doc.XViewMiddleware',
)

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.sites',
)

TEMPLATE_DIRS = (
    os.path.join(ROOT_PATH, 'templates'),
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.debug",
    "django.core.context_processors.media",

    "misc.context_processors.user",
    "misc.context_processors.statics",
)
APPEND_SLASH = True
