from rest_framework.serializers import ModelSerializer

from ..models import User


class ProfileSZ(ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'name', 'password',)
