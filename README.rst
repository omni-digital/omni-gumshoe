=============================
Omni Gumshoe
=============================

.. image:: https://badge.fury.io/py/omni_gumshoe.svg
    :target: https://badge.fury.io/py/omni_gumshoe

.. image:: https://travis-ci.org/NoLogo/omni_gumshoe.svg?branch=master
    :target: https://travis-ci.org/NoLogo/omni_gumshoe

.. image:: https://codecov.io/gh/NoLogo/omni_gumshoe/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/NoLogo/omni_gumshoe

Django middleware for tracking superuser logins.

Documentation
-------------

The full documentation is at https://omni_gumshoe.readthedocs.io.

Quickstart
----------

Install Omni Gumshoe::

    pip install omni_gumshoe

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'omni_gumshoe.apps.OmniGumshoeConfig',
        ...
    )

Add Omni Gumshoe's URL patterns:

.. code-block:: python

    from omni_gumshoe import urls as omni_gumshoe_urls


    urlpatterns = [
        ...
        url(r'^', include(omni_gumshoe_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
