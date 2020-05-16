#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     develop.py.py
   Description :   ''
   Author :        jocker
   Date：          2020/5/16 13:38
   Software:       PyCharm
-------------------------------------------------
   Change Activity:
                   2020/5/16: change des
-------------------------------------------------
"""

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}