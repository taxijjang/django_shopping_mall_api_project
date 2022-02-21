import json
from unittest import mock
from urllib.parse import urlencode

import requests

from django.test import Client
from django.test import TestCase
from django.urls import reverse
from django.urls import resolve

from user.models import User
from products.models import Product

kakaopay_ready_mock_data = dict(
    next_redirect_pc_url="https://mockup-pg-web.kakao.com/v1/xxxxxxxxxx/info"
)


class KakaoReadyViewTestCase(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            name='test_user',
            email='test@email.com',
            password='test'
        )
        self.product = Product.objects.create(
            title='test product',
            price=10000
        )
        self.client = Client()

    @mock.patch('kakaopay.payment.requests.post')
    def test_ready_view(self, mock_post):
        self.client.post(
            path=reverse('users:login'),
            data=dict(
                email=self.user.email,
                password=self.user.password
            )
        )
        data = dict(
            product_pk=self.product.pk,
            quantity=1
        )
        response_mock = mock_post.return_value
        response_mock.status_code = 200
        response_mock.json.return_value = dict(
            next_redirect_pc_url="https://mockup-pg-web.kakao.com/v1/xxxxxxxxxx/info"
        )
        response = self.client.post(
            path=reverse('purchases:kakaopay_ready'),
            data=urlencode(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.content)
