from django.test import Client
from unittest import TestCase

class TestAboutUsView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_ourstory_navigation(self):
        response = self.client.get('http://localhost:8000/about/our-story')
        self.assertEqual(response.status_code,200)
    def test_ourstory_nav_redirect(self):
        response = self.client.get('https://localhost:8000/about/our-story/')
        self.assertEqual(response.url,'/about/our-story')
    def test_ourstory_about_redirect(self):
        response = self.client.get('https://localhost:8000/about/')
        self.assertEqual(response.url,'/about/our-story')
    def test_ourstory_about_slashdirect(self):
        response = self.client.get('https://localhost:8000/about')
        self.assertEqual(response.url,'/about/')
    