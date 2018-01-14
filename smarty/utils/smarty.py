from __future__ import unicode_literals

import re

from smartypants import _tags_to_skip_regex, _tokenize, smartypants as _smartypants

from .. import settings


def _wrap_caps(matchobj):
    return '<span class="%s">%s</span>' % (settings.SMARTY_CAPS_CLASS, matchobj.group(0))


def smartycaps(text):
    tokens = _tokenize(text)
    result = []
    in_pre = False
    tags_to_skip_regex = _tags_to_skip_regex()
    caps_re = re.compile(r'[0-9]*([A-Z][0-9\/\-.+&]?){1,}[A-Z][0-9]*\.?')
    for cur_token in tokens:
        if not cur_token[0] == 'tag':
            t = cur_token[1]
            if not in_pre:
                t = re.sub(caps_re, _wrap_caps, t)
            result.append(t)
    return ''.join(result)


def smartypants(value):
    return _smartypants(value)
