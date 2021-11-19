from datetime import date
from django.contrib.auth.forms import UsernameField
from django.test import TestCase,Client,SimpleTestCase,TransactionTestCase
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from Trainer.models import Trainer
from Users.models import *
from News.forms import CreateNewsForm
from News.models import *


class AdministratorTestCase(TestCase):

    def setUp(self):
        password = make_password('abc12345')
        _user = User.objects.create(username = 'abc' , email='abc@example.com')
        _user.set_password(password)
        
        _user.is_staff = True
        _user.is_superuser = True
        
        _user.save()
        customer = User.objects.create(username = 'cus1', password=password , email='abc@example.com')
        tr1 = User.objects.create(username = 'tr1', password=password , email='abc@example.com')
        Trainer.objects.create(user = tr1 , age=30,gender='male',bio="thai",specialist="cardio",tel="0617349815",approve=False)
        
    #################################################################job apply system
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
        self.assertEquals(response.status_code, 302)

    
    def test_applicant_info(self):
        """ can see info"""
        #user1 = User.objects.create(username = "user1" , password = 'abc12345' , email = "user1@example.com")
        user = User.objects.get(username = "abc") 
        tr = Trainer.objects.first().id
        c = Client()
        c.force_login(user)
        response = c.get(reverse("administrator:applicant_info",args=(tr,)))
        self.assertEqual(response.status_code , 200)

    
    def test_approve(self):
        user = User.objects.get(username = "abc") 
        tr = Trainer.objects.first().id
        c = Client()
        c.force_login(user)
        response = c.get(reverse("administrator:approve",args=(tr,)))
        self.assertEqual(response.status_code , 302)
    

    def test_decline(self):
        user = User.objects.get(username = "abc")
        tr = Trainer.objects.first().id
        c = Client()
        c.force_login(user)
        response = c.get(reverse("administrator:decline",args=(tr,)))
        self.assertEqual(response.status_code , 302)

    #################################################################report system
    def test_report_list(self):

        user = User.objects.get(username='abc')
        
        c = Client()
        c.force_login(user)
        response = c.get(reverse("administrator:report_list"))
        self.assertEqual(response.status_code , 200)
    
    def test_non_admin_report_list(self):

        user = User.objects.get(username='cus1')

        c = Client()
        c.force_login(user)
        response = c.get(reverse("administrator:report_list"))
        self.assertEqual(response.status_code , 302)
    
    
    def test_report_info(self):

        user = User.objects.get(username = "abc")
        tr = Trainer.objects.first() 
        Report.objects.create(trainer=tr,reason="Bad word",context="N-words")
        rep = Report.objects.first().id
        c = Client()
        c.force_login(user)
        response = c.get(reverse("administrator:report_info",args=(rep,)))
        self.assertEqual(response.status_code , 200)

    ##################################################################profile

    def test_admin_profile(self):
        user = User.objects.get(username = "abc")
        c = Client()
        c.force_login(user)
        response = c.get(reverse("administrator:profile"))
        self.assertEqual(response.status_code , 200)


class TestForm(TransactionTestCase):
    
    def setUp(self):
        password = make_password('abc12345')
        _user = User.objects.create(username = 'abc' , email='abc@example.com')
        _user.set_password(password)
        
        _user.is_staff = True
        _user.is_superuser = True
        
        _user.save()
        user1 = User.objects.create(username = "user1" , password = "1234" , email = "user2@example.com")

    def test_create_news_form_valid(self):
        user = User.objects.get(username = "abc")
        c = Client()
        c.force_login(user)
        
        form = CreateNewsForm(data={
            'title':"สุขภาพดี",
            'context':"ข้อมูล",
            'ps': "written by",
            'pic1':None,
            'pic2':None,
            'pic3':None,
            'pic4':None,
        })
        
        response = c.post(reverse("administrator:create_news"))
        form.save()
        self.assertTrue(form.is_valid())
        self.assertTrue(response.status_code , 302)

    """
        if form.is_valid():
            form.save()
            self.assertTrue(News.objects.filter(title='สุขภาพดี').exists())
        """
    def test_non_admin_create_news_view(self):
        user = User.objects.get(username = "user1")
        c = Client()
        c.force_login(user)
        
        response = c.get(reverse("administrator:create_news"))
        self.assertTrue(response.status_code , 302)