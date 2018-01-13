Django Smarty
*************

|PyPI version|_

.. |PyPI version| image::
   https://badge.fury.io/py/django-smarty.svg
.. _PyPI version: https://pypi.python.org/pypi/django-smarty

**Django Smarty** is a `Django <https://www.djangoproject.com/>`_ `template filter <https://docs.djangoproject.com/en/2.0/howto/custom-template-tags/>`_ application to convert ASCII punctuation characters into smart typographic punctuation HTML entities with `SmartyPants <https://daringfireball.net/projects/smartypants/>`_. Uses the `Python smartypants <https://pypi.python.org/pypi/smartypants>`_ package.

* `Package distribution <https://pypi.python.org/pypi/django-smarty>`_
* `Code repository <https://github.com/richardcornish/django-smarty>`_

Install
=======

.. code-block:: bash

   $ pipenv install django-smarty

Add to ``settings.py``.

.. code-block:: python

   INSTALLED_APPS = [
       # ...
       'smarty',
   ]

Usage
=====

.. code-block:: django

   {% load smarty_tags %}

   {{ post.body|smarty }}

Result:

.. code-block:: html

   &#8220;Hello&#8212;world!&#8221;

Settings
========

``smarty`` is a filter composed of several smaller filters:

- ``smartypants`` is the original SmartyPants
- ``smartycaps`` wraps capital letters in ``<span class="initialism"></span>``

One can apply any filter individually. For example, if one preferred the original SmartyPants, write ``{{ post.body|smartypants }}``.

One can customize the application and order of ``smarty`` filters with the ``SMARTY_FILTERS`` setting. By default, the ``SMARTY_FILTERS`` setting is:

.. code-block:: python

   SMARTY_FILTERS = [
       'smartypants',
       'smartycaps',
   ]

One can also customize the HTML class of ``smartycaps`` with the ``SMARTY_CAPS_CLASS`` setting. By default, the ``SMARTY_CAPS_CLASS`` setting is:

.. code-block:: python

   SMARTY_CAPS_CLASS = 'initialism'
