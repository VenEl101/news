from django.shortcuts import render
from drf_spectacular.utils import extend_schema

from core.bases import BaseModelViewSet
from teams.models import Teams
from teams.serializers import TeamsModelSerializer


# Create your views here.


@extend_schema(tags=['Teams'])
class TeamsModelViewSet(BaseModelViewSet):
    queryset = Teams.objects.all()
    serializer_class = TeamsModelSerializer
