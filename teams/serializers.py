from rest_framework.serializers import ModelSerializer

from teams.models import Teams


class TeamsModelSerializer(ModelSerializer):
    class Meta:
        model = Teams
        fields = ['id', 'name', 'exp', 'position', 'avatar_img']

