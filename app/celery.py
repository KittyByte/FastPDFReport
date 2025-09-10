import time
from celery import Celery

from app.settings import settings



celery_app = Celery(__name__, broker=settings.CELERY_BROKER_URL, backend=settings.CELERY_RESULT_BACKEND)


@celery_app.task(name="debug_task")
def debug_task(time_to_sleep):
    time.sleep(time_to_sleep)
    return True
