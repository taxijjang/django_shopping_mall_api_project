import os
import requests

from django.shortcuts import render
from django.shortcuts import redirect


def index(request):
    if request.method == 'POST':
        URL = 'https://kapi.kakao.com/v1/payment/ready'
        headers = {
            'Authorization': f'KakaoAK {os.environ.get("KAKAO_APP_ADMIN_KEY")}',
            'Content-type': 'application/x-www-form-urlencoded;charset=utf-8',
        }
        params = {
            "cid": "TC0ONETIME",  # 테스트용 코드
            "partner_order_id": "1",  # 주문번호
            "partner_user_id": "taxijjang",  # 유저 아이디
            "item_name": "택시짱",  # 구매 물품 이름
            "quantity": 1,  # 구매 물품 수량
            "total_amount": 12000,  # 구매 물품 가격
            "tax_free_amount": 0,  # 구매 물품 비과세
            "approval_url": "http://127.0.0.1:8000",
            "cancel_url": "http://127.0.0.1:8000",
            "fail_url": "http://127.0.0.1:8000",
        }
        res = requests.post(URL, headers=headers, params=params)
        request.session['tid'] = res.json()['tid']
        next_url = res.json()['next_redirect_pc_url']
        return redirect(next_url)
    return render(request, 'kakaopay/index.html')
