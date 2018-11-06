"""
Django production settings for webvirtcloud project.
"""
try:
    from .base import *
except ImportError:
    pass

DEBUG = False
ADMIN_ENABLED = True

try:
    from .local import *
except ImportError:
    pass
