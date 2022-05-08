from django.db import models

from core.models import TimestampBaseModel


class Product(TimestampBaseModel):
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

    SEVEN_ELEVEN = "seven_eleven"
    CU = "cu"
    EMART24 = "emart24"
    MINISTOP = "ministop"
    GS25 = "gs25"

    STORE_CHOICES = (
        (SEVEN_ELEVEN, SEVEN_ELEVEN),
        (CU, CU),
        (EMART24, EMART24),
        (MINISTOP, MINISTOP),
        (GS25, GS25),
    )

    year = models.PositiveSmallIntegerField(db_index=True, help_text="행사 년")
    month = models.PositiveSmallIntegerField(db_index=True, help_text="행사 월")
    store = models.CharField(max_length=30, choices=STORE_CHOICES, db_index=True, help_text="편의점 종류")
    title = models.CharField(max_length=50, db_index=True, help_text="상품 이름")
    price = models.PositiveIntegerField(default=0, db_index=True, help_text="상품 가격")
    category = models.CharField(max_length=20, db_index=True, null=True, blank=True, default=None, help_text="상품 종류")
    sale_type = models.CharField(max_length=15, choices=SALE_TYPE_CHOICES, db_index=True, help_text="할인 타입")
    image = models.CharField(max_length=300, null=True, blank=True, default=None, help_text="상품 이미지")
    sale_off = models.BooleanField(default=False, db_index=True, help_text="행사 종료 날짜")

    def __str(self):
        return f'{self.title} - {self.price}'
