from django.test import RequestFactory
from django.urls import reverse
from aboutus.views import our_story

class TestAboutUsView:

    #test if product page loads with valid id
    def test_about_us_view(self):
        path = reverse('aboutus')
        request = RequestFactory().get(path)
        response = our_story(request)
        assert response.status_code == 200