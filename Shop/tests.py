
from django.test import TestCase,Client
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Max

import Shop
from .models import Shop


class ShopViewTestCase(TestCase):

    def setUp(self):
        password = make_password('1234')
        Shop.objects.create(title="dd",context="dd",date='2021-10-30')
        User.objects.create(username = "user1" , password = password , email = "user2@example.com")


    def test_authenticate_Shop_page(self):

        user = User.objects.get(username = "user1")

        c = Client()
        c.force_login(user)
        response = c.get(reverse("Shop:shop_list"))
        self.assertEqual(response.status_code , 200)


    def test_guest_user_can_view_Shop_page(self):
        c = Client()
        response = c.get(reverse("Shop:shop_list"))
        self.assertEqual(response.status_code , 200)


    def test_valid_Shop_page(self):

        c = Client()
        s = Shop.objects.first()
        response = c.get(reverse("Shop:shop_list"))
        self.assertEqual(response.status_code,200)


    def test_Shop_list_View_context(self):
        s = Shop.objects.first()
        c = Client()
        response = self.client.get(reverse('Shop:shop_list'))



    def test_valid_Shopdetail_page(self):
        """valid  detailpage should return status code 200"""
        c = Client()
        s = Shop.objects.first()
        response = c.get(reverse("Shop:shop_detail", args=(s.id,)))
        self.assertEqual(response.status_code,200)