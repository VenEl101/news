
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from category.views import SubCategoryModelViewSet, CategoryModelViewSet

router = DefaultRouter()

router.register('category', CategoryModelViewSet, basename='category')
router.register('sub-category', SubCategoryModelViewSet, basename='sub-category')

urlpatterns = [
    path('', include(router.urls)),

]