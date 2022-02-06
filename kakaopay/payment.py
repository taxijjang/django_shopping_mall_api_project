import os

import requests


class KakaoPayClient:
    BASE_URL = 'http://127.0.0.1:8000'
    ADMIN_KEY = os.environ.get('KAKAO_APP_ADMIN_KEY')

    READY_URL = 'https://kapi.kakao.com/v1/payment/ready'
    APPROVE_URL = 'https://kapi.kakao.com/v1/payment/approve'
    STATUS_URL = 'https://kapi.kakao.com/v1/payment/order'

    # only user test
    cid = "TC0ONETIME"

    headers = {
        'Authorization': f'KakaoAK {ADMIN_KEY}',
        'Content-type': 'application/x-www-form-urlencoded;charset=utf-8',
    }

    def ready(self, user, product):
        pass

    def approve(self, pg_token):
        pass

    def order(self):
        pass
