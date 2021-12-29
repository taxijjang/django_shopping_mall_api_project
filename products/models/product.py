from django.db import models

from core.models import TimestampBaseModel


class Product(TimestampBaseModel):
    title = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=0)
    image = models.ImageField(null=True, blank=True)
