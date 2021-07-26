A Django backend for PostgreSQL using psycopg > 2
=================================================

The backend passes the entire Django test suite, but it needs a few
modifications of Django and the test suite. These changes will be proposed to
the Django project in a series of merge requests. The modifications are
available in the repository at https://github.com/dvarrazzo/django/, where the
backend has been developed (as the 'django.db.backends.postgresql_psycopg3'
module).

Approximative instructions
--------------------------

Create and activate a virtualenv any way you like::

    python3 -m venv .venv
    source .venv/bin/activate

Install django, from a branch supporting Psycopg 3. Clone the repos to get the
test suite too. Example::

    git clone -b psycopg3-external https://github.com/dvarrazzo/django.git
    pip install ./django

Install Psycopg 3 from the master branch::

    git clone https://github.com/psycopg/psycopg.git
    pip install -e ./psycopg/psycopg

Install the backend (this project)::

        pip install -e .

Customise the test config module if necessary::

    vim dtests/test_psycopg3.py
    # hack hack
    :wq

Run the django test suite::

    python django/tests/runtests.py --settings=dtests.test_psycopg3 -v2 --parallel=1 --noinput
