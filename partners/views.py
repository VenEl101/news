from django.shortcuts import render
from drf_spectacular.utils import extend_schema

from core.bases import BaseModelViewSet
from partners.models import Partners
from partners.serializers import PartnersSerializer



@extend_schema(tags=['Partners'])
class PartnersModelViewSet(BaseModelViewSet):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer




