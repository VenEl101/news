from parler_rest.serializers import TranslatableModelSerializer
from rest_framework import serializers
from .models import Category, SubCategory


class CategorySerializer(TranslatableModelSerializer):
    class TranslatedFields:
        name = serializers.CharField()

    class Meta:
        model = Category
        fields = ['id', 'name']


class SubCategorySerializer(TranslatableModelSerializer):
    class TranslatedFields:
        name = serializers.CharField()

    category = CategorySerializer(read_only=True)

    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'category']