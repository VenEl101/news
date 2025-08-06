from django.db import models
from django.db.models import CharField, TextField, ImageField, FileField, Model, DateTimeField




class Teams(Model):
    name = CharField(max_length=255)
    exp = DateTimeField(auto_now_add=True)
    position = CharField(max_length=255)
    avatar_img = ImageField(null=True, blank=True)


    def __str__(self):
        return self.name


