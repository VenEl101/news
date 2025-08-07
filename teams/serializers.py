from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField
from .models import  Teams





class TeamsSerializer(TranslatableModelSerializer):
    class TranslatedFields:
        name = serializers.CharField()
        position = serializers.CharField()

    class Meta:
        model = Teams
        fields = ['id', 'avatar_img', 'exp', 'name', 'position']
