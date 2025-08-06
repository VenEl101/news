from django.urls import path, include
from rest_framework.routers import DefaultRouter

from partners.views import PartnersModelViewSet

router = DefaultRouter()


router.register('partners', PartnersModelViewSet, basename='partners')


urlpatterns = [
    path('', include(router.urls)),
]