from django.db import models
from django.db.models import CharField, ImageField, Model
# Create your models here.


class Partners(Model):
    name = CharField(max_length=255)
    image = ImageField(null=True, blank=True)

    def __str__(self):
        return self.name