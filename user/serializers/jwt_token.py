from rest_framework import serializers


class TokenObtainPairResponseSerializer(serializers.Serializer):
    access = serializers.CharField(help_text='access token 만료시간 999day')
    refresh = serializers.CharField(help_text='refresh token 만료시간 999day')

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()


class TokenRefreshResponseSerializer(serializers.Serializer):
    access = serializers.CharField(help_text='access token 만료시간 999day')

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()
