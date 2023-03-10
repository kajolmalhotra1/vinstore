import os

# from dotenv import load_dotenv

# load_dotenv()

timezone = 'Asia/Kolkata'
enable_utc = False
broker_transport_options = {'region': 'ap-south-1', 'visibility_timeout': 43200, 'polling_interval': 0.3,
                            'wait_time_seconds': 20}
mongodb_backend_settings = {
    "taskmeta_collection": os.getenv('CELERY_TASKMETA_COLLECTION')
}
broker_url = os.getenv('CELERY_BROKER_URL')
result_backend = os.getenv('CELERY_BACKEND_URL')
task_default_queue = os.getenv('CELERY_DEFAULT_QUEUE')
task_time_limit = 7200
task_soft_time_limit = 3600
result_backend_always_retry = True

# this ensures that the worker acks the task after it’s completed. If the worker crashes, it will just restart.
task_acks_late = True

# this ensures that the worker process can reserve at most one un-acked task at a time. If this is used with
# ACKS_LATE=False (the default), the worker will reserve a task as soon as it starts processing the first one.
worker_prefetch_multiplier = 1

# If you have it set to True, whenever you call delay or apply_async it will just run the task synchronously instead
# of delegating it to a worker. This simplifies debugging in your local environment and facilitates automated testing.
task_always_eager = False