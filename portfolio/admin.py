from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Portfolio


@admin.register(Portfolio)
class PortfolioAdmin(TranslatableAdmin):
    list_display = ('title',)