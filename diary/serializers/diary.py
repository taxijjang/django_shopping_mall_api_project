from rest_framework import serializers

from ..models import Diary


class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = ["id", "content", "emotion", "created_at", ]
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
        }
