#Test if urls work fine
from django.urls import reverse, resolve
# from django.test import TestCase

class TestProductUrl:
    
    def test_product_detail_url(self):
        path = reverse('product',kwargs={'id':1})
        assert resolve(path).view_name == 'product'