import os
from .settings import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB", "testdb"),
        "USER": os.getenv("POSTGRES_USER", "testuser"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", "testpassword"),
        "HOST": os.getenv("POSTGRES_HOST", "localhost"),
        "PORT": os.getenv("POSTGRES_PORT", "5432"),
    }
}
