from rest_framework.viewsets import ModelViewSet

from api.v1.proxy_tasks.serializers import ProxyTaskSerializer
from apps.proxy_tasks.models import ProxyTask


class ProxyTaskViewSet(ModelViewSet):
    queryset = ProxyTask.objects.all()
    serializer_class = ProxyTaskSerializer
