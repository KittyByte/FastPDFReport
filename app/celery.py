import time
from celery import Celery

from app.settings import settings



celery_app = Celery(__name__)
celery_app.conf.broker_url = settings.celery_broker_url
# celery_app.conf.result_backend = settings.celery_result_backend



@celery_app.task(name="debug_task")
def debug_task(time_to_sleep):
    time.sleep(time_to_sleep * 10)
    return True
