from celery import Celery

from app.settings import settings
from kombu import Exchange, Queue



celery_app = Celery(
    __name__,
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND
)

celery_app.autodiscover_tasks(["app.tasks.tasks"])

celery_app.conf.task_queues = [
    Queue('celery', Exchange('celery'), routing_key='celery'),
    Queue('send-request', Exchange('send-request'), routing_key='send-request'),

]

celery_app.conf.task_routes = {
    'app.tasks.tasks.create_and_send_report': {'queue': 'send-request'}
}

