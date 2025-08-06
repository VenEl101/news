from django.contrib import admin
from parler.admin import TranslatableAdmin

from portfolio.models import Portfolio

# Register your models here.


@admin.register(Portfolio)
class PortfolioAdmin(TranslatableAdmin):
    list_display = ('__str__', 'url_link', 'image')
