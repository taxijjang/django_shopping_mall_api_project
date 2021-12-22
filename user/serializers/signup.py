from rest_framework import serializers

from ..models import User


class UserSignupSZ(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password')
        read_only_fields = ('id',)
