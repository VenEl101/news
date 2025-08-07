from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Teams



@admin.register(Teams)
class TeamsAdmin(TranslatableAdmin):
    list_display = ('name', 'position', 'exp')