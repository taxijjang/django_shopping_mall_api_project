from django.db import models

from core.models import TimestampBaseModel


class Product(TimestampBaseModel):
    ONE_PLUS_ONE = "1+1"
    TWO_PLUS_ONE = "2+1"
    THREE_PLUS_ONE = "3+1"
    SALE_PRODUCT = "sale_product"
    PRESENT_PRODUCT = 'present_product'

    SALE_TYPE_CHOICES = (
        (ONE_PLUS_ONE, ONE_PLUS_ONE),
        (TWO_PLUS_ONE, TWO_PLUS_ONE),
        (THREE_PLUS_ONE, THREE_PLUS_ONE),
        (SALE_PRODUCT, SALE_PRODUCT),
        (PRESENT_PRODUCT, PRESENT_PRODUCT),
    )

    SEVEN_ELEVEN = "seven_eleven"
    CU = "cu"

    conveniences_store = models.CharField(max_length=30, db_index=True)
    title = models.CharField(max_length=50, db_index=True)
    price = models.PositiveIntegerField(default=0, db_index=True)
    category = models.CharField(max_length=20, db_index=True, null=True, blank=True, default=None)
    sale_type = models.CharField(max_length=15, choices=SALE_TYPE_CHOICES, db_index=True)
    image = models.CharField(max_length=300, null=True, blank=True, default=None)

    def __str(self):
        return f'{self.title} - {self.price}'
