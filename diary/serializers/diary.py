from rest_framework import serializers

from ..models import Diary
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.utils import OpenApiTypes


class DiarySerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()

    class Meta:
        model = Diary
        fields = ["id", "content", "emotion", "date", ]
        extra_kwargs = {
            "id": {"read_only": True},
            "date": {"read_only": True},
        }

    @extend_schema_field(OpenApiTypes.INT)
    def get_date(self, obj):
        return int(obj.date.utcnow().timestamp() * 1e3)
