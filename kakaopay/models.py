# from django.db import models
#
#
# class KakaoPay(models.Model):
#     cid = models.CharField(max_length=10, default='TC0ONETIME', help_text="가맹점 코드")
#     cid_secret = models.CharField(max_length=24, null=True, blank=True, help_text="가맹점 코드 인증키")
#     partner_order_id = models.CharField(max_length=100, default='10007', help_text="가맹점 주문번호")
#     partner_user_id = models.CharField(max_length=100, default='taxijjang', help_text="가맹점 회원 id")
#     item_name = models.CharField(max_length=100, help_text="상품명")
#     item_code = models.CharField(max_length=100, null=True, default=True, help_text="상품코드")
#     quantity = models.PositiveIntegerField(help_text="상품 수량")
#     total_amount = models.PositiveIntegerField(help_text="상품 총액")
#     tax_free_amount
#
#
