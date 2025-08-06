from django.contrib import admin
from django.contrib.admin import register
from modeltranslation.admin import TranslationAdmin
from modeltranslation.translator import TranslationOptions
from parler.admin import TranslatableAdmin

from category.models import Category, SubCategory




@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    pass
