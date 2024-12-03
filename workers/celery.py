from celery import Celery
from kombu import Queue
from workers.shared_tasks import high_priority_task, default_task, low_priority_task, add
from workers.scheduled_tasks import scheduled_tasks

app = Celery(
    'tasks',
    broker='redis://redis:6379/0',
    backend='redis://redis:6379/0',
)



# Define queues
app.conf.task_queues = (
    Queue('high_priority'),
    Queue('default'),
    Queue('low_priority'),
)

app.conf.beat_schedule = scheduled_tasks

app.conf.timezone = 'UTC'





