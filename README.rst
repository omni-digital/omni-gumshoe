=============================
Omni Gumshoe
=============================

.. image:: https://badge.fury.io/py/omni_gumshoe.svg
    :target: https://badge.fury.io/py/omni_gumshoe

.. image:: https://travis-ci.org/omni-digital/omni-gumshoe.svg?branch=master
    :target: https://travis-ci.org/omni-digital/omni-gumshoe

.. image:: https://codecov.io/gh/omni-digital/omni-gumshoe/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/omni-digital/omni-gumshoe

Simple logging for superuser logins.

Quickstart
----------

Install Omni Gumshoe::

    pip install omni_gumshoe

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'omni_gumshoe',
        ...
    )

Features
--------

* Adds a `LogEvent` every time a super user logs in.
* Adds a `LogEvent` every time a staff user logs in.

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Recommended With
----------------
We would recommend using Logentry Admin, Omni Gumshoe adds slightly more visibility to Logentry Admin.

Install django-logentry-admin::

    pip install django-logentry-admin

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django-logentry-admin',
        ...
    )

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
