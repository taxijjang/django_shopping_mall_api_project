import json
from unittest import mock
from urllib.parse import urlencode

import requests

from django.test import TestCase
from django.urls import reverse

from products.models import Product

kakaopay_ready_mock_data = dict(
    next_redirect_pc_url="https://mockup-pg-web.kakao.com/v1/xxxxxxxxxx/info"
)


class KakaoReadyViewTestCase(TestCase):
    def setUp(self) -> None:
        self.product = Product.objects.create(
            title='test product',
            price=10000
        )

    @mock.patch('purchases.views.ready.kakaopay.ready', return_value=kakaopay_ready_mock_data)
    def test_ready_view(self):
        data = dict(
            product_pk=self.product.pk,
            quantity=1
        )
        response = requests.post(
            path=reverse('purchases:kakaopay_ready'),
            data=urlencode(data),
            content_type='application/x-www-form-urlencoded'
        )
        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.content)
