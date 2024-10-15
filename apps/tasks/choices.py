from django.db.models import TextChoices


class TaskProrityType(TextChoices):
    HIGH = 'HIGN', 'Высокий'
    MEDIUM = 'MEDIUM', 'Средний'
    LOW = 'LOW', 'Низкий'
