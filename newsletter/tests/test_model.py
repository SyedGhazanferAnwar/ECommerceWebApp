from django.shortcuts import get_object_or_404
from django.test import TestCase
from newsletter.models import NewsUser
from datetime import datetime, timedelta, timezone, date
class TestNewsletterModel(TestCase):
    def setUp(self):
        NewsUser.objects.create(email='email@gmail.com')

    #Check if email to be shown in admin is right
    def test_newsletter_string_representation(self):
        newUser = NewsUser.objects.get(pk=1)
        self.assertEqual(str(newUser),newUser.email)
    #Check for blank/null email
    def test_newsletter_blank_null_email(self):
        newUser = NewsUser.objects.get(pk=1)
        self.assertNotEqual(newUser.email,None)
        self.assertNotEqual(newUser.email,'')
    #Check if datetime is being stored at time of creation
    def test_if_storing_date(self):
        newUser = NewsUser.objects.get(pk=1)
        self.assertNotEqual(newUser.date_added,None)
    #check if datetime being stored is right
    def test_if_storing_right_date(self):
        newUser = NewsUser.objects.get(pk=1)
        now = datetime.now(timezone.utc)
        self.assertAlmostEqual(newUser.date_added,now,delta=timedelta(seconds=1))
        