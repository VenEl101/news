from rest_framework.serializers import ModelSerializer

from portfolio.models import Portfolio


class PortfolioModelSerializer(ModelSerializer):

    class Meta:
        model = Portfolio
        fields = ['id', 'url_link', 'image', 'title', 'desc']
