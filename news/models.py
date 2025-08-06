from django.db import models
from django.db.models import CharField, TextField, ImageField, FileField, Model


class News(Model):
    title = CharField(max_length=255)
    desc = TextField()
    image = ImageField(null=True, blank=True)
    content = TextField()
    content_img = ImageField(null=True, blank=True)
    content_video = FileField(null=True, blank=True)


    def __str__(self):
        return self.title


    class Meta:
        ordering = ['title']