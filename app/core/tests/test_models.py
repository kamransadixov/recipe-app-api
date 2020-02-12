from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        email = 'kamransadixov@mail.ru'
        password = 'kam125486'

        """
        get_user_model() returns the default user model.
        If it has to return custom usermodel, create a new model
        and in settings.py Set AUTH_USER_MODEL pointing to custom model
        """
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        email = 'tets@SADASD.com'
        user = get_user_model().objects.create_user(email, 'kam125486')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test email user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'kam125486')

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            'kamransadikhov@yandex.com',
            'kam125486'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
