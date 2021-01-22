from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_success(self):
        """ Test creating a new user with an email is successful"""

        email = 'raajrajnish@gmail.com'
        password = 'testpass_123'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normailzed(self):
        """Test new email of a user is normalized"""

        email = 'raajrajnish@GMAIL.COM'
        password = 'testpass_123'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email.lower())
        self.assertTrue(user.check_password(password))

    def test_new_user_invalid_email(self):
        """Test creating user with no email raise error"""

        email = None
        password = 'testpass_123'

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=email,
                password=password
            )

    def test_create_new_superuser(self):
        """Test creating a new super user"""

        email = 'raajrajnish@gmail.com'
        password = 'admin'

        user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_new_superuser_invalid_email(self):
        """Test creating superuser with no email raise error"""

        email = None
        password = 'admin'

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=email,
                password=password
            )
