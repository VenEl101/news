
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField
from .models import News


class NewsSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=News, write_only=True)


    class Meta:
        model = News
        fields = [
            'id',
            'title',
            'desc',
            'content',
            'translations',
            'image',
            'content_img',
            'content_video'
        ]
