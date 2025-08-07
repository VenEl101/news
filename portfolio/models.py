from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class Portfolio(TranslatableModel):
    url_link = models.URLField()
    image = models.ImageField(null=True, blank=True)

    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        desc=models.TextField()
    )

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)
