import os
import sys

from celery import Celery
from django.conf import settings

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("django-skeleton")

# Load Django settings
app.config_from_object("django.conf:settings", namespace="CELERY")


# Setup Custom queue (with or without kombu)
app.conf.task_queues = {}

app.conf.beat_schedule = {}
# Auto-discover tasks from installed apps
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
