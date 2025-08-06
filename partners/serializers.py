from rest_framework.serializers import ModelSerializer

from partners.models import Partners


class PartnersModelSerializer(ModelSerializer):

    class Meta:
        model = Partners
        fields = ['id', 'name', 'image']