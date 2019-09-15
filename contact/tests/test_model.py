from django.shortcuts import get_object_or_404
from django.test import TestCase
from contact.models import Message
from datetime import datetime, timedelta, timezone, date
import pytest

@pytest.mark.django_db
class TestContactModel(TestCase):
    def setUp(self):
        Message.objects.create(firstName='User',lastName='SurName',email='email@gmail.com',
        subject='Subject of Message',message='This is a valid test message')


    def test_title_string_representation(self):
        newMsg = Message.objects.get(pk=1)
        self.assertEqual(str(newMsg),newMsg.subject)
    #Check for blank/null email
    def test_blank_first_name(self):
        newMsg = Message.objects.get(pk=1)
        self.assertNotEqual(newMsg.firstName,None)
        self.assertNotEqual(newMsg.firstName,'')
    def test_blank_last_name(self):
        newMsg = Message.objects.get(pk=1)
        self.assertNotEqual(newMsg.lastName,None)
        self.assertNotEqual(newMsg.lastName,'')
    def test_blank_email(self):
        newMsg = Message.objects.get(pk=1)
        self.assertNotEqual(newMsg.email,None)
        self.assertNotEqual(newMsg.email,'')
    def test_blank_subject(self):
        newMsg = Message.objects.get(pk=1)
        self.assertNotEqual(newMsg.subject,None)
        self.assertNotEqual(newMsg.subject,'')
    def test_blank_message(self):
        newMsg = Message.objects.get(pk=1)
        self.assertNotEqual(newMsg.message,None)
        self.assertNotEqual(newMsg.message,'')
    def test_if_storing_right_date(self):
        newMsg = Message.objects.get(pk=1)
        now = datetime.now(timezone.utc)
        self.assertAlmostEqual(newMsg.date_added,now,delta=timedelta(seconds=1))