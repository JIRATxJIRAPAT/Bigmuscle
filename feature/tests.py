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
        Customer.objects.create(user=user1)
    
    def test_bodytest_normal_weight(self):
        """can use bodytest fn."""
        user = User.objects.get(username = "user1")
        
        c = Client()
        c.force_login(user)
        response = c.post(reverse('feature:bdTest'),{"height":180,"weight":60})
        self.assertEqual(response.status_code, 200 )

    def test_bodytest_underweight(self):
        """can use bodytest fn."""
        user = User.objects.get(username = "user1")
       
        c = Client()
        c.force_login(user)
        response = c.post(reverse('feature:bdTest'),{"height":180,"weight":50})
        self.assertEqual(response.status_code, 200 )


    def test_bodytest_overweight(self):
        """can use bodytest fn."""
        user = User.objects.get(username = "user1")
        
        c = Client()
        c.force_login(user)
        response = c.post(reverse('feature:bdTest'),{"height":180,"weight":90})
        self.assertEqual(response.status_code, 200 )

    def test_bodytest_obese(self):
        """can use bodytest fn."""
        user = User.objects.get(username = "user1")
        
        c = Client()
        c.force_login(user)
        response = c.post(reverse('feature:bdTest'),{"height":160,"weight":100})
        self.assertEqual(response.status_code, 200 )

    def test_bodytest_view(self):
        
        c = Client()
        response = c.get(reverse('feature:bdTest'))
        self.assertEqual(response.status_code, 200 )