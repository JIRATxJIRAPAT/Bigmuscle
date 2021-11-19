from django.contrib.auth.hashers import make_password
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .views import *
# Create your tests here.

class TrackingViewTestCase(TestCase):
    def setUp(self):
        password = make_password("1234")
        user = User.objects.create(username = "user1" , password = password , email = "user1@example.com")
        Customer.objects.create(user=user)
    
    def test_index_view_with_authentication(self):
        user = User.objects.get(username="user1")
        c = Client()
        c.force_login(user)
        response = c.get(reverse("Tracking:workout"))
        self.assertEqual(response.status_code, 404)

    def test_index_view_without_authentication(self):
        c = Client()
        response = c.get(reverse("Tracking:workout"))
        self.assertEqual(response.status_code , 302)

    def test_index_view_object_create(self):
        ob1 = Exercise.objects.create(exercise_name = 'prank' , parts = 'abc')
        ob2 = Workout.objects.create(exercise=ob1 , reps=1 , sets=2 , status = True )
        ob3 = Program.objects.create(objective=ob2 , day=1 , status=True)
        ob4 = Tracks.objects.create(day_program=ob3 , all_program_status=True , day=1)

        Workout.objects.create(exercise=ob2)
        Program.objects.create(objective=ob3)
        Tracks.objects.create(day_program=ob4)