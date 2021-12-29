from rest_framework.serializers import ModelSerializer

from ..models import User


class ProfileSZ(ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'email', 'name',)
        read_only_fields = ('pk', 'email',)


class PatchProfileSZ(ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'email', 'name',)
        read_only_fields = ('pk', 'email',)

    def update(self, instance, validated_data):
        return super(ProfileSZ, self).update(instance, validated_data)
