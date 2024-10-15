from rest_framework.serializers import ModelSerializer

from apps.proxy_tasks.models import ProxyTask


class ProxyTaskSerializer(ModelSerializer):
    class Meta:
        model = ProxyTask
        fields = (
            'id',
            'name',
            'description',
            'priority',
        )
