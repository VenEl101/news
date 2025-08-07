from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class Partners(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=255)
    )
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True)
