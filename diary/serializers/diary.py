from rest_framework import serializers

from ..models import Diary


class DiarySerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()

    class Meta:
        model = Diary
        fields = ["id", "content", "emotion", "date", ]
        extra_kwargs = {
            "id": {"read_only": True},
            "date": {"read_only": True},
        }

    def get_date(self, obj):
        return int(obj.date.utcnow().timestamp() * 1e3)
