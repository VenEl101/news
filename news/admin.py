from django.contrib import admin
from parler.admin import TranslatableAdmin

from news.models import News




@admin.register(News)
class NewsAdmin(TranslatableAdmin):
    list_display = ('__str__',)
    search_fields = ('translations__title', 'translations__desc', 'translations__content')
