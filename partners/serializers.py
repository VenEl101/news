from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer
from .models import Partners


class PartnersSerializer(TranslatableModelSerializer):
    class TranslatedFields:
        name = serializers.CharField()

    class Meta:
        model = Partners
        fields = ['id', 'image', 'name']
