from django.db import models

from apps.tasks.choices import TaskProrityType


class Task(models.Model):
    name = models.CharField(
        verbose_name='Наименование',
        max_length=64,
    )

    description = models.CharField(
        verbose_name='Описание',
        max_length=255,
        blank=True,
    )

    priority = models.CharField(
        verbose_name='Приоритет',
        choices=TaskProrityType.choices,
        max_length=6,
    )

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
