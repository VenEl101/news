from django.db import models
from django.db.models import Model, CharField, ForeignKey, CASCADE
from parler.models import TranslatableModel, TranslatedFields


class Category(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=255)
    )

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True)



#
class SubCategory(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=255)
    )
    category = ForeignKey('Category', on_delete=CASCADE, related_name='category')
