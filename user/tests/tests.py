from django.test import TestCase
from ..models import User


class UserTestCase(TestCase):
    def setUp(self) -> None:
        User.objects.create_user(
            name='test user',
            email='test@test.com',
            password='test password',
        )

    def test_user_model_기본(self):
        self.assertEqual(True, True)