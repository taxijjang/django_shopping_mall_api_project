from django.db import models

from core.models import TimestampBaseModel

PAY_TYPE_CHOICES = (
    (0, "CARD"),
    (1, "MONEY"),
)


class PurchaseApprovalResult(TimestampBaseModel):
    purchase = models.ForeignKey('Purchase', on_delete=models.PROTECT, verbose_name='주문번호')
    aid = models.CharField(max_length=50, verbose_name='요청 고유 변호')
    payment_type = models.CharField(db_index=True, max_length=5, verbose_name='결제 수단')
    # amount
    total_amount = models.IntegerField(verbose_name='결제총액')
    tax_free_amount = models.IntegerField(verbose_name='상품 비과세 금액')
    vat_amount = models.IntegerField(default=0, verbose_name='상품 부가세 금액')
    # card_info
    card_info = models.TextField(null=True, blank=True)
    item_name = models.CharField(max_length=100)

    ready_at = models.DateTimeField()
    approved_at = models.DateTimeField()
