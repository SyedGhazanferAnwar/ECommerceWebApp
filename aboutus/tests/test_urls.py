from django.test import Client
from unittest import TestCase

#These tests checks if the navigation and redirects are working properly or not

class TestAboutUsView(TestCase):

    def setUp(self):
        self.client = Client()

    #Valid/invalid page requests
    def test_ourstory_invalid(self):
        response = self.client.get('http://localhost:8000/about/our-stor')
        self.assertEqual(response.status_code, 404)
    def test_ourstory_navigation(self):
        response = self.client.get('http://localhost:8000/about/our-story')
        self.assertEqual(response.status_code,200)
    #Tests to check redirects
    def test_ourstory_nav_redirect(self):
        response = self.client.get('https://localhost:8000/about/our-story/')
        self.assertEqual(response.url,'/about/our-story')
    def test_ourstory_about_redirect(self):
        response = self.client.get('https://localhost:8000/about/')
        self.assertEqual(response.url,'/about/our-story')
    def test_ourstory_about_slashdirect(self):
        response = self.client.get('https://localhost:8000/about')
        self.assertEqual(response.url,'/about/')
    