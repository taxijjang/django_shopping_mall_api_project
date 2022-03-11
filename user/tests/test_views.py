import json

from django.test import TestCase
from django.urls import reverse

from ..models import User


class UserSignUpViewTestCase(TestCase):
    def test_user_signup_기본(self):
        new_user_data = dict(
            name='new_user',
            email='new_user@email.com',
            password='1234'
        )

        url = reverse('users:signup')
        response = self.client.post(
            path=url,
            data=new_user_data,
        )
        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.content)
        self.assertTrue(User.objects.get(email=response_data.get('email')))
