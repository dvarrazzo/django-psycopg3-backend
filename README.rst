A Django backend for PostgreSQL using psycopg > 2
=================================================

The backend passes the entire Django test suite, but it needs a few
modifications to Django and its test suite. These changes will be proposed to
the Django project in a series of merge requests. The modifications are
available in the https://github.com/dvarrazzo/django/tree/psycopg3-support
Django branch.


Approximative instructions
--------------------------

Create and activate a virtualenv any way you like::

    python3 -m venv .venv
    source .venv/bin/activate

Install django, from a branch supporting Psycopg 3. Clone the repos to get the
test suite too. Example::

    git clone -b psycopg3-support https://github.com/dvarrazzo/django.git
    pip install ./django

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
