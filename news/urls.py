from django.urls import path, include
from rest_framework.routers import DefaultRouter

from news.views import NewsModelViewSet

router = DefaultRouter()


router.register('news', NewsModelViewSet, basename='news')


urlpatterns = [
    path('', include(router.urls)),

]