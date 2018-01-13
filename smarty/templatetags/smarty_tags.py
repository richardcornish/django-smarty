from __future__ import unicode_literals

from django import template
from django.utils.safestring import mark_safe

from ..utils.smarty import smartypants as _smartypants, smartycaps as _smartycaps
from .. import settings

register = template.Library()


@register.filter
def smartycaps(value):
    return mark_safe(_smartycaps(value))


@register.filter
def smartypants(value):
    return mark_safe(_smartypants(value))


@register.filter
def smarty(value, filters=settings.SMARTY_FILTERS):
    filters_dict = {
        'smartypants': _smartypants,
        'smartycaps': _smartycaps,
    }
    for key in filters_dict:
        for item in filters:
            if key == item:
                value = filters_dict[key](value)
    return mark_safe(value)
