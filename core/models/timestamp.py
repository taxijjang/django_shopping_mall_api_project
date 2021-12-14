from django.db import models


class TimestampBaseModel(models.Model):
    created_at = models.DateTimeField(auto_created=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
