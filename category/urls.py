from django.urls import path, include
from rest_framework.routers import DefaultRouter

from category.views import CategoryModelViewSet, SubCategoryModelViewSet

router = DefaultRouter()


router.register('category', CategoryModelViewSet, basename='category')
router.register('subcategory', SubCategoryModelViewSet, basename='subcategory')


urlpatterns = [
    path('', include(router.urls)),

]