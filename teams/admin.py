from django.contrib import admin
from django.utils.html import format_html
from parler.admin import TranslatableAdmin

from teams.models import Teams

@admin.register(Teams)
class TeamsAdmin(TranslatableAdmin):
    list_display = ('__str__', 'position_display', 'exp', 'avatar_preview')
    search_fields = ('translations__name', 'translations__position')

    def position_display(self, obj):
        return obj.safe_translation_getter('position', any_language=True)

    position_display.short_description = "Position"

    def avatar_preview(self, obj):
        if obj.avatar_img:
            return format_html('<img src="{}" style="max-height: 50px;" />', obj.avatar_img.url)
        return "-"
    avatar_preview.short_description = "Avatar"