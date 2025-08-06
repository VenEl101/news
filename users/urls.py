from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import UserLoginGenericAPIView, UserModelViewSet

router = DefaultRouter()


router.register('users', UserModelViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', UserLoginGenericAPIView.as_view(), name='login'),
]