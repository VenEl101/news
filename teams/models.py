from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class Teams(TranslatableModel):
    avatar_img = models.ImageField(null=True, blank=True)
    exp = models.DateTimeField(auto_now_add=True)

    translations = TranslatedFields(
        name=models.CharField(max_length=255),
        position=models.CharField(max_length=255),
    )

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True)


