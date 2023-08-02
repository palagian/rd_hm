import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_HW.settings')

app = Celery('Django_HW')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

