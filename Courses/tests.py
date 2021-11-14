from django.test import TestCase,Client
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Max
from .models import Course
from Trainer.models import Trainer
from Users.models import Customer
from .forms import AppointmentForm

class CoursesViewTestCase(TestCase):

    def setUp(self):
        
        password = make_password('1234')
        user1 = User.objects.create(username = "user1" , password = password , email = "user1@example.com")
        tr1 = User.objects.create(username = "user2" , password = password , email = "user2@example.com")
        Course.objects.create(name="subj1",info="info")
        Customer.objects.create(user=user1)
        Trainer.objects.create(user = tr1 , age=30,gender='male',bio="thai",specialist="cardio",tel="0617349815",approve=True)
        subj1 = Course.objects.first()
        #subj1.teach.set(tr1)
        
        

    def test_can_view_course_list(self):
        c = Client()
        response = c.get(reverse("Courses:course_list"))
        self.assertEqual(response.status_code , 200)
    
    def test_can_view_course_detail(self):
        """ login can view detail""" 
        user = Customer.objects.first()
        course = Course.objects.first().id
        c = Client()
        c.force_login(user.user)
        response = c.get(reverse("Courses:course_details", args=(course,)))
        self.assertEqual(response.status_code , 200)

    def test_notlogin_cannot_view_course_detail(self):
        """not login cannot view detail""" 
        c = Client()
        course = Course.objects.first().id
        response = c.get(reverse("Courses:course_details", args=(course,)))
        self.assertEqual(response.status_code , 302)

   
    def test_authenticated_user_can_apply_course(self):
        """ not finish"""
        user = Customer.objects.first()
        course = Course.objects.first().id
        c = Client()
        c.force_login(user)
        response = c.get(reverse('Courses:apply' ,args=(course,)))
        self.assertEqual(response.status_code , 200)

    def test_nonauthenticated_user_cannot_apply_course(self):
        user = Customer.objects.first()
        course = Course.objects.first().id
        c = Client()
        response = c.get(reverse('Courses:apply' ,args=(course,)))
        self.assertEqual(response.status_code , 200)

    def test_nonauthenticated_user_cannot_select_trainer(self):
        user = Customer.objects.first()
        course = Course.objects.first().id
        c = Client()
        response = c.get(reverse('Courses:select' ,args=(course,)))
        self.assertEqual(response.status_code , 302)

    def test_user_can_appointment_trainer(self):
        """useless"""
        user = Customer.objects.first()
        tr = Trainer.objects.first()
        course = Course.objects.first().id
        c = Client()
        c.force_login(user)
        #checkform = AppointmentForm()
        form = AppointmentForm(data = {'trainer': tr ,'date':'2021-11-12','timeslot':'0','customer':user})
        #checkform = AppointmentForm(form_data)
        response = c.get(reverse('Courses:timeslot' ,args=(course,)))
        self.assertEqual(form.is_valid(), True)
        self.assertEqual(response.status_code , 200)