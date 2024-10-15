from django.urls import include, path

urlpatterns = [
    path('tasks/', include('api.v1.tasks.urls')),
    path('proxy-tasks/', include('api.v1.proxy_tasks.urls')),
]
