from django.urls import include, path
from rest_framework.routers import DefaultRouter

from portfolio.views import PortfolioModelViewSet

router = DefaultRouter()

router.register('portfolio', PortfolioModelViewSet, basename='portfolio')



urlpatterns = [
    path('', include(router.urls)),
]