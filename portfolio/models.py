from django.db import models
from django.db.models import URLField, Model, ImageField, CharField, TextField


# Create your models here.
class Portfolio(Model):
    url_link = URLField()
    image = ImageField(null=True, blank=True)
    title = CharField(max_length=255)
    desc = TextField()

    def __str__(self):
        return self.title