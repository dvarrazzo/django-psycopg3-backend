A Django backend for PostgreSQL using Psycopg > 2
=================================================

The backend passes the entire Django test suite, but it needs a few
modifications to Django and to its test suite. These changes will be proposed
to the Django project in a series of merge requests. `A writeup`__ explains
the changes in more details.

.. __: https://www.psycopg.org/articles/2021/08/02/psycopg3-django-driver/

The modifications required (targeting the main branch at the time of writing)
are available in the `psycopg3-4.1`__ Django branch. This is `the list of
changes`__.

.. __: https://github.com/dvarrazzo/django/tree/psycopg3-4.1
.. __: https://github.com/django/django/compare/8b020f2e64...dvarrazzo:psycopg3-4.1


Approximative instructions
--------------------------

Create and activate a virtualenv any way you like::

    python3 -m venv .venv
    source .venv/bin/activate

Install Django, from a branch supporting Psycopg 3. Clone the repos to get the
test suite too. Example::

    git clone -b psycopg3-4.1 https://github.com/dvarrazzo/django.git
    pip install -e ./django

Install Psycopg 3 from the master branch::

    git clone https://github.com/psycopg/psycopg.git
    pip install -e ./psycopg/psycopg

Install the backend (this project)::

        pip install -e .

Customise the test config module if necessary::

    vim configs/test_psycopg3.py
    # hack hack
    # :wq

Run the django test suite::

    python django/tests/runtests.py --settings=configs.test_psycopg3 -v2 --parallel=1 --noinput

A ``configs.test_psycopg2`` module is also available to run the same tests
with psycopg2 and check for regressions.
