from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet

from core.bases import BaseModelViewSet
from teams.models import Teams
from teams.serializers import TeamsSerializer


# Create your views here.


@extend_schema(tags=['Teams'])
class TeamsModelViewSet(ModelViewSet):
    queryset = Teams.objects.all()
    serializer_class = TeamsSerializer
