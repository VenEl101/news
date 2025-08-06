from django.contrib import admin
from django.utils.html import format_html
from parler.admin import TranslatableAdmin

from partners.models import Partners

@admin.register(Partners)
class PartnersAdmin(TranslatableAdmin):
    list_display = ('__str__', 'image_preview')
    search_fields = ('translations__name',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 50px;" />', obj.image.url)
        return "-"
    image_preview.short_description = "Image"