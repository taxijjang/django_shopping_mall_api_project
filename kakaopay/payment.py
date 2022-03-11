import os

import requests

from django.shortcuts import resolve_url
from django.conf import settings
from django.utils import timezone
from django.db import transaction

from user.models import User
from products.models import Product
from purchases.models import Purchase
from purchases.models import PurchaseApprovalResult

BASE_URL = 'http://127.0.0.1:8000' if settings.DEBUG else 'http://218.48.14.96'

READY_URL = 'https://kapi.kakao.com/v1/payment/ready'
APPROVE_URL = 'https://kapi.kakao.com/v1/payment/approve'
STATUS_URL = 'https://kapi.kakao.com/v1/payment/order'


class KakaoPayClient:

    def __init__(self, cid='TC0ONETIME', partner_order_id='taxijjang', partner_user_id='0710', pg_token=None, tid=None):
        self.cid = cid
        self.partner_order_id = partner_order_id
        self.partner_user_id = partner_user_id
        self.pg_token = pg_token
        self.tid = tid
        self.headers = {
            'Authorization': f'KakaoAK {os.environ.get("KAKAO_APP_ADMIN_KEY")}',
            'Content-type': 'application/x-www-form-urlencoded;charset=utf-8',
        }

    @transaction.atomic
    def ready(self, user: User, product: Product, quantity: int) -> str:
        purchase = Purchase.objects.create(
            user=User.objects.get(pk=4),
            product=product,
            quantity=int(quantity),
        )
        params = dict(
            cid=self.cid,
            partner_order_id=self.partner_order_id,
            partner_user_id=self.partner_user_id,
            item_name=product.title,
            quantity=int(quantity),
            total_amount=int(product.price),
            tax_free_amount=0,
            approval_url=f'{BASE_URL}{resolve_url("purchases:kakaopay_approve", purchase_pk=purchase.pk)}',
            cancel_url=BASE_URL,
            fail_url=BASE_URL
        )

        res = requests.post(READY_URL, headers=self.headers, params=params)
        res_data = res.json()

        purchase.tid = res_data.get('tid')
        purchase.ready = timezone.now()
        purchase.save()

        data = dict(
            next_redirect_pc_url=res_data.get('next_redirect_pc_url')
        )
        return data

    @transaction.atomic
    def approve(self, user: User, pg_token: str, purchase_pk: int):
        purchase = Purchase.objects.get(pk=purchase_pk, user=User)
        params = dict(
            cid=self.cid,
            tid=purchase.tid,
            partner_order_id=self.partner_order_id,
            partner_user_id=self.partner_user_id,
            pg_token=pg_token
        )

        res = requests.post(APPROVE_URL, headers=self.headers, params=params)
        res_data = res.json()

        PurchaseApprovalResult.objects.create(
            purchase=purchase,
            aid=res_data.get('aid'),
            payment_type=res_data.get('payment_method_type'),
            total_amount=res_data.get('amount').get('total'),
            tax_free_amount=res_data.get('amount').get('tax_free'),
            vat_amount=res_data.get('amount').get('vat'),
            ready_at=res_data.get('created_at'),
            approved_at=res_data.get('approved_at'),
            item_name=res_data.get('item_name')
        )
        purchase.approve = timezone.now()
        purchase.save()
