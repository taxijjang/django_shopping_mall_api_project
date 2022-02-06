from django.test import TestCase
from ..models import User
from django.contrib.auth import get_user_model


class UserModelTestCase(TestCase):
    def setUp(self) -> None:
        pass

    def test_user_model_기본_유저_생성(self):
        user_data = dict(
            name='test_basic_user',
            email='test_basic@email.com',
            password='1234'
        )
        basic_user = User.objects.create_user(**user_data)

        self.assertEqual(user_data.get('name'), basic_user.name)
        self.assertEqual(user_data.get('email'), basic_user.email)
        self.assertEqual(True, basic_user.is_active)
        self.assertEqual(False, basic_user.is_staff)
        self.assertEqual(False, basic_user.is_superuser)
        self.assertEqual(False, basic_user.is_admin)

        self.assertEqual(user_data.get('name'), basic_user.__str__())
        self.assertEqual(basic_user.has_perm(), basic_user.is_admin)
        self.assertEqual(basic_user.has_module_perms(), basic_user.is_admin)

    def test_user_model_슈퍼_유저_생성(self):
        user_data = dict(
            name='test_super_user',
            email='test_super@email.com',
            password='1234'
        )
        super_user = User.objects.create_superuser(**user_data)

        self.assertEqual(user_data.get('name'), super_user.name)
        self.assertEqual(user_data.get('email'), super_user.email)
        self.assertTrue(super_user.is_active)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_admin)

        self.assertEqual(user_data.get('name'), super_user.__str__())
        self.assertEqual(super_user.has_perm(), super_user.is_admin)
        self.assertEqual(super_user.has_module_perms(), super_user.is_admin)
