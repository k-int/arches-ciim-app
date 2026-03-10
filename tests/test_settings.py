import os

from arches_ciim_app.settings import *
from arches.settings import *

PACKAGE_NAME = "arches_ciim_app"
APP_NAME = "arches_ciim_app"

APP_ROOT = os.path.dirname(__file__)
TEST_ROOT = os.path.normpath(os.path.join(ROOT_DIR, "..", "tests"))

ROOT_URLCONF = "arches_ciim_app.arches_ciim_app.urls"

MEDIA_ROOT = os.path.join(TEST_ROOT, "fixtures", "data")

BUSINESS_DATA_FILES = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

DATABASES = {
    "default": {
        "ATOMIC_REQUESTS": False,
        "AUTOCOMMIT": True,
        "CONN_MAX_AGE": 0,
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "HOST": "localhost",
        "NAME": "arches_ciim_app",
        "OPTIONS": {
            "options": "-c cursor_tuple_fraction=1",
        },
        "PASSWORD": "postgis",
        "PORT": "5432",
        "POSTGIS_TEMPLATE": "template_postgis",
        "TEST": {"CHARSET": None, "COLLATION": None, "MIRROR": None, "NAME": None},
        "TIME_ZONE": None,
        "USER": "postgres",
    }
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    },
    "user_permission": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
        "LOCATION": "user_permission_cache",
    },
}

LOGGING["loggers"]["arches"]["level"] = "ERROR"

ELASTICSEARCH_PREFIX = "test"

# TEST_RUNNER = "arches.test.runner.ArchesTestRunner"

TEST_RUNNER = "tests.base_test.ArchesTestRunner"

SILENCED_SYSTEM_CHECKS.append(
    # "arches.W001",  # Cache backend does not support rate-limiting
    "arches.E001",  # Ussing dummy cache in production
)

ELASTICSEARCH_HOSTS = [
    {"scheme": "http", "host": "localhost", "port": ELASTICSEARCH_HTTP_PORT}
]

print("In the test settings")