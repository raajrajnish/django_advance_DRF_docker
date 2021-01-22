from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        """Special type of function which helps in setting some resource which are
            required inorder to pass our test"""

        # call the client and create a admin user
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="raajrajnish@gmail.com",
            password="admin"
        )
        # login with admin user
        self.client.force_login(self.admin_user)

        # create a test user
        self.user = get_user_model().objects.create_user(
            email="testraajrajnish@gmail.com",
            password="test",
            name="Test User Full Name"
        )

    def test_user_listed(self):
        """Test to get all the users listed on user page"""

        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
