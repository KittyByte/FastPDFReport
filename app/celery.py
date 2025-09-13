from celery import Celery

from app.settings import settings



celery_app = Celery(
    __name__,
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND
)
celery_app.autodiscover_tasks(["app.tasks.tasks"])
