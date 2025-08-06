from django.db.models import Q
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer, Serializer

from users.models import User


class UserModelSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'role', 'is_active')
        extra_kwargs = {'password': {"write_only": True}}


    def create(self, validated_data):
        return User.objects.create_user(**validated_data)




class UserLoginSerializer(Serializer):
    username_or_email = CharField()
    password = CharField()

    def validate(self, attrs):
        identifier = attrs.get('username_or_email')
        password = attrs.get('password')

        user = User.objects.filter(Q(email=identifier) | Q(username=identifier)).first()

        print(user.check_password(password))

        if not user:
            raise ValidationError("User not found.")

        if not user.check_password(password):
            raise ValidationError("Incorrect password.")

        if not user.is_active:
            raise ValidationError("User is inactive.")

        attrs['user'] = user
        return attrs



