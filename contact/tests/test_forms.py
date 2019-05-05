from django.test import TestCase
from django.forms import ValidationError
from contact.forms import ContactForm

valid_data = {'firstName':'Ali','lastName':'Hussam','email':'alihussam.cs@gmail.com','subject':'Test Message','message':"This is a test message"}
invalid_data = {'firstName':'Ali','lastName':'Hussam','email':'alihussam.cs','subject':'Test Message','message':"This is a test message"}


class TestContactForm(TestCase):

    #Check if form accepts valid data or not
    def test_true_validity(self):
        form = ContactForm(data=valid_data)
        self.assertTrue(form.is_valid)

    #check if form accepts invalid data
    def test_false_validity(self):
        form = ContactForm(data=invalid_data)
        if not form.has_error :
            raise ValidationError('CONTACT FORM ACCEPTED INVALID EMAIL')
        invalid_data["email"]=None
        form = ContactForm(data=invalid_data)
        if not form.has_error :
            raise ValidationError('CONTACT FORM ACCEPTED Null EMAIL')
        invalid_data["email"]="hussam.cs@gmail.com"
        invalid_data["firstName"]=None
        form = ContactForm(data=invalid_data)
        if not form.has_error :
            raise ValidationError('CONTACT FORM ACCEPTED Null NAME')