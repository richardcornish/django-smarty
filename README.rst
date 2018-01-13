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
