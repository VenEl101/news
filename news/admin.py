from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import News

@admin.register(News)
class NewsAdmin(TranslatableAdmin):
    list_display = ('get_title', 'image_preview')  # Fields to display in list view
    search_fields = ('translations__title', 'translations__desc')  # Searchable fields

    def get_title(self, obj):
        return obj.safe_translation_getter('title', any_language=True)
    get_title.short_description = 'Title'  # Column header

    def image_preview(self, obj):
        if obj.image:
            from django.utils.html import format_html
            return format_html('<img src="{}" height="50" />', obj.image.url)
        return "-"
    image_preview.short_description = 'Preview'


