from django.db import models

from core.models import TimestampBaseModel


class Diary(models.Model):
    content = models.CharField(max_length=500)
    emotion = models.PositiveIntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)