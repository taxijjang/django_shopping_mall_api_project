import uuid

from django.db import models
from django.conf import settings
from core.models import TimestampBaseModel

from products.models import Product


class Purchase(TimestampBaseModel):
    uuid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField()
    tid = models.CharField(max_length=20, null=True, blank=True, default=None)
    ready = models.DateTimeField(null=True, blank=True, default=None)
    approve = models.DateTimeField(null=True, blank=True, default=None)

    def __str__(self):
        return self.uuid

    @property
    def total_amount(self):
        return self.product.price * self.quantity
