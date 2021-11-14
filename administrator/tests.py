from django.contrib.auth.forms import UsernameField
from django.test import TestCase,Client, client
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from Trainer.models import Trainer


class AdministratorTestCase(TestCase):

    def setUp(self):
        password = make_password('abc12345')
        _user = User.objects.create(username = 'abc' , email='abc@example.com')
        _user.set_password(password)
        
        _user.is_staff = True
        _user.is_superuser = True
        
        _user.save()
        customer = User.objects.create(username = 'cus1', password=password , email='abc@example.com')

        
    
    def test_is_superuser_applicant_list(self):

        c = Client()
        user = User.objects.get(username='abc')
        self.user = user

        c.force_login(self.user)
        response = c.get(reverse('administrator:applicant_list'))
        self.assertEquals(response.status_code, 200)

    def test_normal_user_cannot_view_applicant_list(self):

        c = Client()
        user = User.objects.get(username='cus1')
        self.user = user

        c.force_login(self.user)
        response = c.get(reverse('administrator:applicant_list'))
        self.assertEquals(response.status_code, 200)

    
    def test_applicant_info(self):

        user1 = User.objects.create(username = "user1" , password = 'abc12345' , email = "user1@example.com")
        user = User.objects.get(username = "user1") 

        c = Client()
        c.force_login(user)
        response = c.get(reverse("administrator:applicant_info"))
        self.assertEqual(response.status_code , 200)

    
    def test_approve(self):

        user1 = User.objects.create(username = "user1" , password = 'abc12345' , email = "user1@example.com")
        user = User.objects.get(username = "user1") 

        c = Client()
        c.force_login(user)
        response = c.get(reverse("administrator:approve"))
        self.assertEqual(response.status_code , 200)
    

    def test_decline(self):

        user1 = User.objects.create(username = "user1" , password = 'abc12345' , email = "user1@example.com")
        user = User.objects.get(username = "user1") 

        c = Client()
        c.force_login(user)
        response = c.get(reverse("administrator:decline"))
        self.assertEqual(response.status_code , 200)

    
    def test_report_list(self):

        user = User.objects.get(username='abc')

        c = Client()
        c.force_login(user)
        response = c.get(reverse("administrator:report_list"))
        self.assertEqual(response.status_code , 200)
    

    def test_report_info(self):

        user1 = User.objects.create(username = "user1" , password = 'abc12345' , email = "user1@example.com")
        user = User.objects.get(username = "user1") 

        c = Client()
        c.force_login(user)
        response = c.get(reverse("administrator:report_info"))
        self.assertEqual(response.status_code , 200)
