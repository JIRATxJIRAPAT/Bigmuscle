from django.test import TestCase,Client

# Create your tests here.
from django.contrib.auth.models import User
from django.urls import reverse
from Users.models import Customer 
from django.shortcuts import render
from django.http import request

class FeatureTestCase(TestCase):
    
    def setUp(self):
        user1 = User.objects.create(username = "user1" , password = "1234" , email = "user2@example.com")
        
    
    def test_bodytest(self):
        """is_seat_available should be True"""
        
        c = Client()
        response = c.get(reverse('feature:bdTest'))
        self.assertEqual(response.status_code, 200 )






    """""
    def test_bodytest_result(self):
       
        user = Customer.objects.get(username = "user1")
        c = Client()
        c.force_login(user)
        response = c.get(reverse('feature:bdTest'))
        
        self.assertEqual(response.status_code, 200 )
    """""