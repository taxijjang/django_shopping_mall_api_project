import os

import requests

from django.utils import timezone

from user.models import User
from products.models import Product
from purchases.models import Purchase

BASE_URL = 'http://127.0.0.1:8000'

READY_URL = 'https://kapi.kakao.com/v1/payment/ready'
APPROVE_URL = 'https://kapi.kakao.com/v1/payment/approve'
STATUS_URL = 'https://kapi.kakao.com/v1/payment/order'


class KakaoPayClient:

    def __int__(self, partner_order_id='taxijjang', partner_user_id='0710'):
        self.cid = "TC0ONETIME"
        self.partner_order_id = partner_order_id
        self.partner_user_id = partner_user_id
        self.headers = {
            'Authorization': f'KakaoAK {os.environ.get("KAKAO_APP_ADMIN_KEY")}',
            'Content-type': 'application/x-www-form-urlencoded;charset=utf-8',
        }

    def ready(self, user: User, product: Product, quantity: int):
        purchase = Purchase.objects.create(
            user=user,
            product=product,
            quantity=quantity,
            ready=timezone.now()
        )
        params = dict(
            cid=self.cid,
            partner_order_id=self.partner_user_id,
            partner_user_id=self.partner_user_id,
            item_name=product.title,
            quantity=purchase.quantity,
            total_amount=purchase.total_amount,
            tax_free_amount=0,
            approval_url=APPROVE_URL,
            cancel_url=BASE_URL,
            fail_url=BASE_URL
        )
        response = requests.post(READY_URL, header=self.headers, params=params)

        if response.status_code != 200:
            purchase.finish = timezone.now()
            purchase.save()
            return BASE_URL

        response_data = response.json()
        purchase.tid = response_data.get('tid')
        purchase.save()

        return response_data.get('next_redirect_pc_url')

    def approve(self, pg_token):
        pass

    def order(self):
        pass
