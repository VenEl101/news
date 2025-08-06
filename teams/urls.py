from django.urls import include, path
from rest_framework.routers import DefaultRouter

from teams.views import TeamsModelViewSet

router = DefaultRouter()

router.register('teams', TeamsModelViewSet, basename='teams')

urlpatterns = [
    path('', include(router.urls)),

]