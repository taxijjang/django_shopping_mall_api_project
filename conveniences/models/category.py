from django.db import models

from core.models import TimestampBaseModel


class Category(TimestampBaseModel):
    title = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.title
