from __future__ import unicode_literals

from django.conf import settings


SMARTY_FILTERS = getattr(settings, 'SMARTY_FILTERS', [
    'smartypants',
    'smartycaps',
])

SMARTY_CAPS_CLASS = getattr(settings, 'SMARTY_CAPS_CLASS', 'initialism')
