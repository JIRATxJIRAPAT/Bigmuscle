from django.test import TestCase,Client
from django.http import HttpRequest
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import render
from django.http import request
from Trainer.forms import CreateUserTRForm,TrainerForm,VideocallForm
from Trainer.models import Trainer
from Tracking.models import *

class TrainerTestCase(TestCase):

    def setUp(self):
        """set up"""
        self.register_url=reverse('Trainer:apply')
        password = make_password('123')
        user1 = User.objects.create(username = "user1" , password = password , email = "user1@example.com")
        user2 = User.objects.create(username = "user2" , password = password , email = "user2@example.com")
        ex = Exercise.objects.create(exercise_name="plank",parts="Abs")
        wo = Workout.objects.create(exercise=ex,reps = 30,sets=3,status=False)
        
        
        Trainer.objects.create(user = user1 , age=30,gender='male',bio="thai",specialist="cardio",tel="0617349815",approve=True)
        self.user={
            'username':'username',
            'email':'testemail@gmail.com',
            'password1':'password1',
            'password2':'password2',
            'first_name':'first_name',
            'last_name':'last_name',
            'age':'age',
            'number':'tel',
            'bio':'bio', 
            'gender':'gender',
            'sp':'specialist',
        }
       
    def test_register_tr(self):
        """undone"""
        form_data = {'username':'username', 'email':'email', 'password1':'password1','password2':'password2','first_name':'first_name', 'last_name':'last_name',}
        form = CreateUserTRForm(data=form_data)
        response = self.client.post("/trainer/apply", data={'age':'18','number':'tel','bio':'bio', 'gender':'gender','sp':'specialist'})
        response2 = self.client.get("/trainer/apply", data={'age':'18','number':'tel','bio':'bio', 'gender':'gender','sp':'specialist'})
        self.assertEqual(response.status_code , 200)
        self.assertFalse(form.is_valid())
        self.assertEqual(response2.status_code , 200)
    
    def test_can_register_user(self):
        """test register from github"""
        response=self.client.post(self.register_url,self.user,format='text/html')
        self.assertEqual(response.status_code,200)

    #####################################################################
    def test_cannot_view_trainer_profile(self):
        """ guest cannot view user page """
        
        c = Client()
        response = c.get(reverse("Trainer:index"))
        self.assertEqual(response.status_code , 302)

    def test_view_trainer_profile(self):
        """ tr can view tr page """
        user = User.objects.get(username = "user1")
        c = Client()
        c.force_login(user)
        form = TrainerForm(data={
            
        })
        response = c.post(reverse("Trainer:index"))
        self.assertEqual(response.status_code , 200)
        self.assertTrue(form.is_valid())

        
#####################################################################
    def test_cannot_view_trainer_course(self):
        """ guest cannot view user page """

        c = Client()
        response = c.get(reverse("Trainer:trainer_course"))
        self.assertEqual(response.status_code , 302)
####################################################################

    def test_not_trainer_cannot_view_trainer_course(self):
        
        user = User.objects.get(username = "user2")
        c = Client()
        c.force_login(user)
        response = c.get(reverse("Trainer:courseInfo"))
        self.assertEqual(response.status_code , 302)

    def test_cannot_view_trainer_course_info(self):
        c = Client()
        response = c.get(reverse("Trainer:courseInfo"))
        self.assertEqual(response.status_code , 302)

    def test_trainer_can_view_trainer_course(self):
        
        user = User.objects.get(username = "user1")
        if Trainer.objects.get(user=user)!=None:
            c = Client()
            c.force_login(user)
            response = c.get(reverse("Trainer:courseInfo"))
            self.assertEqual(response.status_code , 200)
       
####################################################################
    def test_add_link(self):
        user = User.objects.get(username = "user1")
        c = Client()
        c.force_login(user)
        form = VideocallForm(data={
            'link':"www.google.com",
        })
        response = c.post(reverse("Trainer:addlink"))
        self.assertEqual(response.status_code , 200)
######################################################################
    