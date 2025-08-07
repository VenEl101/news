from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet

from portfolio.models import Portfolio
from portfolio.serializers import PortfolioSerializer


# Create your views here.



@extend_schema(tags=['Portfolio'])
class PortfolioModelViewSet(ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
