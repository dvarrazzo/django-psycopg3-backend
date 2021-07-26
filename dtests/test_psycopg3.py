# A django settings module to run the Django test suite using Psycopg 3.

DATABASES = {
    'default': {
        'ENGINE': 'django_psycopg3',
        'NAME': 'piro',
        'USER': 'piro',
    },
    'other': {
        'ENGINE': 'django_psycopg3',
        'NAME': 'dj_other',
        'USER': 'piro',
    }
}

INSTALLED_APPS = [
    'django.contrib.postgres'
]

SECRET_KEY = "django_tests_secret_key"

# Use a fast hasher to speed up tests.
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
