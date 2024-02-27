from django.urls import re_path, include
from rest_framework.routers import DefaultRouter
from pilotlog import views

router = DefaultRouter()

router.register(r'pilotlogs', views.PilotLogAPIViewSet, basename='pilotlogs')

urlpatterns = [
    re_path(r'^api/v1/', include(router.urls)),
]

# Path: pilotlog/urls.py