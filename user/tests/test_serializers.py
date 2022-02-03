from django.test import TestCase

from ..serializers import UserSignupSZ


class UserSignupSZTestCase(TestCase):
    def setUp(self) -> None:
        pass

    def test_user_serializer_기본(self):
        user_data = dict(
            name='test_user',
            email='test_user@email.com',
            password='1234'
        )
        serializer = UserSignupSZ(data=user_data)
        self.assertTrue(serializer.is_valid())
        test_user = serializer.save()

        self.assertEqual(user_data.get('name'), test_user.name)
        self.assertEqual(user_data.get('email'), test_user.email)

    def test_user_serializer_이메일_양식_올바르지_않음(self):
        user_data = dict(
            name='test_user',
            email='test_useremail.com',
            password='1234'
        )
        serializer = UserSignupSZ(data=user_data)
        self.assertFalse(serializer.is_valid())
