DATABASES = {
    'default': {
        'ENGINE': 'psycopg3_django',
        'NAME': 'piro',
        'USER': 'piro',
    },
    'other': {
        'ENGINE': 'psycopg3_django',
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
