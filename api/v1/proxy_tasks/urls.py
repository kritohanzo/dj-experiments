from rest_framework.routers import SimpleRouter

from api.v1.proxy_tasks import views

router = SimpleRouter()

router.register('', views.ProxyTaskViewSet)

urlpatterns = router.urls
