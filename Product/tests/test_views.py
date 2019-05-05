from django.test import RequestFactory
from django.urls import reverse
from Product.views import product
from mixer.backend.django import mixer
import pytest

@pytest.mark.django_db
class TestProductView:

    #test if product page loads with valid id
    def test_product_detail_view_by_valid_id(self):
        mixer.blend('Product.Product')
        path = reverse('product', kwargs={'id':1})
        request = RequestFactory().get(path)
        response = product(request, id=1)
        assert response.status_code == 200

        #test if product page loads with invalid id
    def test_product_detail_view_by_valid_id(self):
        path = reverse('product', kwargs={'id':1})
        request = RequestFactory().get(path)
        try:
            response = product(request, id=1)
        except:
            return 
        assert response.status_code == 404