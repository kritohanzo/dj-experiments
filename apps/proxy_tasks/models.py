from django.db import models

from apps.tasks.models import Task


class ProxyTask(Task):
    class Meta:
        verbose_name = 'Прокси задача'
        verbose_name_plural = 'Прокси задачи'
        proxy = True
