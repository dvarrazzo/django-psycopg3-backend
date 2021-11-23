# A django settings module to run the Django test suite using psycopg2.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'piro2',
        'USER': 'piro',
    },
    'other': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dj_other2',
        'USER': 'piro',
    }
}

SECRET_KEY = "django_tests_secret_key"

# Use a fast hasher to speed up tests.
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
USE_TZ = False
