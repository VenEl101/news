from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField
from .models import Portfolio


class PortfolioSerializer(TranslatableModelSerializer):
    class TranslatedFields:
        title = serializers.CharField()
        desc = serializers.CharField()

    class Meta:
        model = Portfolio
        fields = ['id', 'url_link', 'image', 'title', 'desc']