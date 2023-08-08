from django.test import TestCase
from django.urls import reverse

from app_auth.models import User

def create_test_user_of_user_type(user_type: User.user_type):
    user = User.objects.create(username='Test', user_type=user_type)
    user.set_password('Test')
    user.save()
    return user

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

class StandardPageLoginTests(TestCase):
    def setUp(self):
        self.user = create_test_user_of_user_type(User.UserType.STANDARD)
        self.client.force_login(self.user)

    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

class AdminPageLoginTests(TestCase):
    def setUp(self):
        self.user = create_test_user_of_user_type(User.UserType.ADMIN)
        self.client.force_login(self.user)

    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)


class LoginTests(TestCase):
    def test_login_view_status_code(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

class LogoutTests(TestCase):
    def test_logout_view_status_code(self):
        url = reverse('logout')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)