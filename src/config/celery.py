import os

import django
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

# Add settings to Celery
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

# Set settings to Celery
app = Celery("config")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


from app.internal.models.hub import Hub
from app.internal.parser import start_parser


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    for hub in Hub.objects.all():
        sender.add_periodic_task(
            crontab(minute=f"*/{hub.crawl_period}"),
            start_parser.s(hub.id),
            name="start parser every hub.crawl_period minutes",
        )
