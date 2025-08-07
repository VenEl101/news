from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class News(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        desc=models.TextField(),
        content=models.TextField(),
    )
    image = models.ImageField(null=True, blank=True)
    content_img = models.ImageField(null=True, blank=True)
    content_video = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)

    class Meta:
        ordering = ['translations__title']
