from django.db import models
from django.db.models import Model, CharField, ForeignKey, CASCADE



class Category(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


    class Meta:
        ordering = ['name']



class SubCategory(Model):
    name = CharField(max_length=255)
    category = ForeignKey('Category', on_delete=CASCADE, related_name='category')

    def __str__(self):
        return self.name


    class Meta:
        ordering = ['name']