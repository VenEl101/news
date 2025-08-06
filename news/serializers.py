from rest_framework.serializers import ModelSerializer

from news.models import News


class NewsModelSerializer(ModelSerializer):

    class Meta:
        model = News
        fields = ['id', 'title', 'desc', 'image', 'content', 'content_img', 'content_video']

