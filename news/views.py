from django.shortcuts import render
from drf_spectacular.utils import extend_schema

from core.bases import BaseModelViewSet
from news.models import News
from news.serializers import NewsModelSerializer


# Create your views here.


@extend_schema(tags=['News'])
class NewsModelViewSet(BaseModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsModelSerializer
