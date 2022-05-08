from rest_framework import serializers


class ApproveSerializer(serializers.Serializer):
    data = serializers.CharField()