from django.shortcuts import render
from drf_spectacular.utils import extend_schema

from core.bases import BaseModelViewSet
from portfolio.models import Portfolio
from portfolio.serializers import PortfolioModelSerializer


# Create your views here.



@extend_schema(tags=['Portfolio'])
class PortfolioModelViewSet(BaseModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioModelSerializer
