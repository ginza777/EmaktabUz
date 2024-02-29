import os

import environ
from celery import Celery

from django.conf import settings

env = environ.Env()
env.read_env(f"{os.getcwd()}/.env")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "EmaktabUz.settings")

app = Celery("EmaktabUz")

app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
app.autodiscover_tasks(packages=settings.INSTALLED_APPS)
