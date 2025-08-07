from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Partners


@admin.register(Partners)
class PartnersAdmin(TranslatableAdmin):
    list_display = ('name',)
