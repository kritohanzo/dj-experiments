from rest_framework.viewsets import ModelViewSet

from api.v1.tasks.serializers import TaskSerializer
from apps.tasks.models import Task


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
