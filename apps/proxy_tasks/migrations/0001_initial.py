# Generated by Django 5.1.2 on 2024-10-15 16:48

from django.db import migrations


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProxyTask',
            fields=[],
            options={
                'verbose_name': 'Прокси задача',
                'verbose_name_plural': 'Прокси задачи',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('tasks.task',),
        ),
    ]
