from django.db.models import Model, DateTimeField
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from core.permissions import IsAdminOrReadOnly




class TimeBaseModel(Model):
    created_at = DateTimeField(auto_now=True)
    updated_at = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True



class BaseModelViewSet(ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)

