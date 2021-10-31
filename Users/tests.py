from django.test import TestCase, Client
from .models import *
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Max
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from .forms import *
# Create your tests here.



class RegTestCase(TestCase):

    def setUp(self):
        pwd_test = make_password('12345')
        test_user = User.objects.create(
            username="user5", password=pwd_test, email="usermail")

    def test_index_failed_view(self):
        c = Client()
        response = c.get(reverse("Users:userprofile"))
        self.assertEqual(response.status_code, 302)

    def test_index_success_view(self):
        c = Client()
        c.force_login(User.objects.first())
        response = c.get(reverse("Users:userprofile"))
        self.assertEqual(response.status_code, 200)

    def test_index_view(self):
        c = Client()
        response = c.get(reverse("Users:login"))
        self.assertEqual(response.status_code, 200)

    def test_login_view_success(self):
        c = Client()
        response = c.post(reverse('Users:login'), {
                          "username": "user5", "password": "12345"}, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_login_view_failed(self):
        c = Client()
        response = c.post(reverse('Users:login'), {
                          "username": "", "password": "12345"}, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        c = Client()
        response = c.get(reverse("Users:logout"))
        self.assertEqual(response.status_code, 302)

    def test_register_page(self):
        c = Client()
        response = c.get(reverse("Users:register"))
        self.assertEqual(response.status_code, 200)

    def test_register_page_form(self):
        c = Client()
        form_data = {
            "username": "kik1239",
            "email": "first123456@hotmail.com",
            "password1": "test12345",
            "password2": "test12345",
            "first_name": "ariya",
            "last_name": "woddw"}
        form = CreateUserForm(data=form_data)
        response = c.post(reverse('Users:register'), {
            "username": "kik1239",
            "email": "",
            "password1": "test12345",
            "password2": "test12345",
            "first_name": "ariya",
            "last_name": "woddw"}, follow=True)
        self.assertEqual(response.status_code, 200)