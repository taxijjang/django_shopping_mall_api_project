from django.test import TestCase

from ..serializers import UserSignupSZ


class UserSignupSZTestCase(TestCase):
    def setUp(self) -> None:
        pass

    def test_user_serializer_기본(self):
        user_data = dict(
            name='test_user',
            email='test_uset@email.com',
            password='1234'
        )
        serializer = UserSignupSZ(data=user_data)
        self.assertTrue(serializer.is_valid())
        test_user = serializer.save()

        self.assertEqual(user_data.get('name'), test_user.name)
        self.assertEqual(user_data.get('email'), test_user.email)
