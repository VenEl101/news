from django.shortcuts import render
from drf_spectacular.utils import extend_schema

from category.models import Category, SubCategory
from category.serializers import CategoryModelSerializer, SubCategoryModelSerializer
from core.bases import BaseModelViewSet



@extend_schema(tags=['Categories'])
class CategoryModelViewSet(BaseModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


@extend_schema(tags=['SubCategories'])
class SubCategoryModelViewSet(BaseModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategoryModelSerializer



