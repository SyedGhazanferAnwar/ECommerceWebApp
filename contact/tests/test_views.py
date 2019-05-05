from django.test import RequestFactory
from django.urls import reverse
from contact.views import contactForm

class TestContactView:

    def test_contact_view(self):
        path = reverse('contact')
        request = RequestFactory().get(path)
        response = contactForm(request)
        assert response.status_code == 200