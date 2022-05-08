from django.db import models

from core.models import TimestampBaseModel


class SaleType(TimestampBaseModel):
    ONE_PLUS_ONE = "1+1"
    TWO_PLUS_ONE = "2+1"
    THREE_PLUS_ONE = "3+1"
    FOUR_PLUS_ONE = "4+1"
    SALE_PRODUCT = "할인상품"
    PRESENT_PRODUCT = '증정상품'

    SALE_TYPE_CHOICES = (
        (ONE_PLUS_ONE, ONE_PLUS_ONE),
        (TWO_PLUS_ONE, TWO_PLUS_ONE),
        (THREE_PLUS_ONE, THREE_PLUS_ONE),
        (FOUR_PLUS_ONE, FOUR_PLUS_ONE),
        (SALE_PRODUCT, SALE_PRODUCT),
        (PRESENT_PRODUCT, PRESENT_PRODUCT),
    )

    sale_type = models.CharField(max_length=15, choices=SALE_TYPE_CHOICES, db_index=True)

    def __str__(self):
        return self.sale_type
