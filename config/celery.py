from __future__ import absolute_import, unicode_literals
import os
import time

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')

app = Celery('config')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


@app.task(bind=True)
def do_calc_total(self):
    n = 100
    total = 0
    for i in range(n):
        time.sleep(1)
        total += i
    return total