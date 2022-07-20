from django_celery_beat.models import IntervalSchedule
from django_celery_beat.models import PeriodicTask
from host.tasks import periodic_tasks


for taskrunner in periodic_tasks:

    interval, created = IntervalSchedule.objects.get_or_create(
        every=taskrunner.task_frequency_seconds, period=IntervalSchedule.SECONDS
    )

    PeriodicTask.objects.create(
        interval=interval,
        name=taskrunner._task_name(),
        task=taskrunner.task_function_name,
    )

