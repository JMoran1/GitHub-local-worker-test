from django.test import TestCase
from django.urls import reverse

# Create your tests here.
# Write a test to make sure that the home page returns a 200 HTTP status code.
class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)