from django.db import models

from core.models import TimestampBaseModel


class Store(TimestampBaseModel):
    title = models.CharField(max_length=30, db_index=True)

    def __str__(self):
        return self.title