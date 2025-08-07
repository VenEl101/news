from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from category.models import Category, SubCategory
from category.serializers import CategorySerializer, SubCategorySerializer


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class SubCategoryModelViewSet(ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer