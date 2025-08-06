from rest_framework.serializers import ModelSerializer

from category.models import Category, SubCategory


class CategoryModelSerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']



class SubCategoryModelSerializer(ModelSerializer):
    category = CategoryModelSerializer(read_only=True)

    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'category']