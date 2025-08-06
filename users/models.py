


from django.contrib.auth.models import AbstractUser
from django.db import models
from users.manager import CustomUserManager


class User(AbstractUser):

    class Roles(models.TextChoices):
        ADMIN = 'ADMIN', 'admin'
        USER = 'USER', 'user'


    role = models.CharField(max_length=25, choices=Roles, default=Roles.USER)
    status = models.BooleanField(default=False)

    objects = CustomUserManager()

    def __str__(self):
        return self.email