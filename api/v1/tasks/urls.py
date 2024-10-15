from rest_framework.routers import SimpleRouter

from api.v1.tasks import views

router = SimpleRouter()

router.register('', views.TaskViewSet)

urlpatterns = router.urls
