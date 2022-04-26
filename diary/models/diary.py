from django.db import models

from core.models import TimestampBaseModel


class Diary(TimestampBaseModel):
    content = models.CharField(max_length=500)
    emotion = models.PositiveIntegerField(default=1)
