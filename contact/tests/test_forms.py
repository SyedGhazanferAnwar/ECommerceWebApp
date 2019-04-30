from django.test import TestCase
from django.forms import ValidationError
from contact.forms import ContactForm

class FormTest(TestCase):
    def test_true_validity(self):
        data = {'firstName':'Ali','lastName':'Hussam','email':'alihussam.cs@gmail.com','subject':'Test Message','message':"This is a test message"}
        form = ContactForm(data=data)
        self.assertTrue(form.is_valid)
    #check if form accepts invalid emails
    def test_false_validity(self):
        data = {'firstName':'Ali','lastName':'Hussam','email':'alihussam.cs','subject':'Test Message','message':"This is a test message"}
        form = ContactForm(data=data)
        if not form.has_error :
            raise ValidationError('NEWSLETTER FORM ACCEPTED INVALID EMAIL')
    #check if form accepts null emails        
    def test_accept_null_data(self):
        data = {'firstName':'','lastName':'Hussam','email':'alihussam.cs@gmail.com','subject':None,'message':"This is a test message"}
        form = ContactForm(data=data)
        if not form.has_error:
            raise ValidationError('NEWSLETTER FORM ACCEPTED NULL/BLANK CONTACT VALUES')