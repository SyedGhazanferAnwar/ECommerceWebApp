from django.test import TestCase
from Product.models import Product, Category
import pytest

class TestProductModel(TestCase):

    def setUp(self):
        Product.objects.create(name='Product',category=Category.objects.create(name='testcat',description='okay new cat'),rating=4.0,
        price=200,stock=100,profileImage=None,Description='THIS IS DDES',Discount=10)
    def test_product_gives_discount(self):
        product = Product.objects.get(pk=1)
        assert product.getDiscountedPrice != None
    def test_title_string_representation(self):
        name = Product.objects.get(pk=1)
        self.assertEqual(str(name),name.name)
    #Check for blank/null email
    def test_blank_name(self):
        newObj = Product.objects.get(pk=1)
        self.assertNotEqual(newObj.name,None)
        self.assertNotEqual(newObj.name,'')
    def test_blank_category(self):
        newObj = Product.objects.get(pk=1)
        self.assertNotEqual(newObj.category,None)
        self.assertNotEqual(newObj.category,'')
    def test_blank_rating(self):
        newObj = Product.objects.get(pk=1)
        self.assertNotEqual(newObj.rating,None)
    def test_blank_price(self):
        newObj = Product.objects.get(pk=1)
        self.assertNotEqual(newObj.price,None)
    def test_blank_stock(self):
        newObj = Product.objects.get(pk=1)
        self.assertNotEqual(newObj.stock,None)
    def test_blank_description(self):
        newObj = Product.objects.get(pk=1)
        self.assertNotEqual(newObj.Description,None)
        self.assertNotEqual(newObj.Description,'')

class TestCategoryModel(TestCase):
    def setUp(self):
        Category.objects.create(name='testcat',description='okay new cat')
    def test_title_string_representation(self):
        name = Category.objects.get(pk=1)
        self.assertEqual(str(name),name.name)
    def test_blank_name(self):
        newObj = Category.objects.get(pk=1)
        self.assertNotEqual(newObj.name,None)
        self.assertNotEqual(newObj.name,'')
    def test_blank_description(self):
        newObj = Category.objects.get(pk=1)
        self.assertNotEqual(newObj.description,None)
        self.assertNotEqual(newObj.description,'')