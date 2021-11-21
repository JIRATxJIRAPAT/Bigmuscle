from django.test import TestCase,Client,TransactionTestCase
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.urls import reverse
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
        x = Customer.objects.create(user=user1,owned = None)
        trainer = Trainer.objects.create(id=1,user = tr1 , age=30,gender='male',bio="thai",specialist="cardio",tel="0617349815",approve=True)
        subj1 = Course.objects.first()
        subj1.teach.add(trainer)
        self.select_trainer = reverse('Courses:select',args=[subj1.id,])
        

        

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
        user = User.objects.create(username="user3",password="1234",email="user3@gmail.com")
        customer = Customer.objects.create(user=user)
        course = Course.objects.first()
        check = Customer.objects.filter(user=user)
        c = Client()
        c.force_login(user)
        response = c.get(reverse('Courses:apply' ,args=(course.id,)))
        self.assertEqual(response.status_code , 302)
        self.assertEqual(check.owned ,course)

    def test_nonauthenticated_user_cannot_apply_course(self):
        user = Customer.objects.first()
        course = Course.objects.first().id
        c = Client()
        response = c.get(reverse('Courses:apply' ,args=(course,)))
        self.assertEqual(response.status_code , 302)

    def test_nonauthenticated_user_cannot_select_trainer(self):
        user = Customer.objects.first()
        course = Course.objects.first().id
        c = Client()
        response = c.get(reverse('Courses:select' ,args=(course,)))
        self.assertEqual(response.status_code , 302)

    
    def test_select_trainer(self):
        """ test select"""
        User.objects.create(username = "user3" , password = "password" , email = "user1@example.com")
        user = Customer.objects.first()
        tr = Trainer.objects.first()
        c = Client()
        c.force_login(user)
        response = c.post(reverse(self.select_trainer,{"trainer": tr.id}))
        self.assertEqual(response.status_code , 302)
        
    
class TestForm(TransactionTestCase):
    
    def setUp(self):
        password = make_password('1234')
        user1 = User.objects.create(username = "user1" , password = password , email = "user1@example.com")
        x = Customer.objects.create(user=user1,owned = None)
        tr1 = User.objects.create(username = "user2" , password = password , email = "user2@example.com")
        trainer = Trainer.objects.create(user = tr1 , age=30,gender='male',bio="thai",specialist="cardio",tel="0617349815",approve=True)
        Course.objects.create(name="subj1",info="info")
        subj1 = Course.objects.first()
        subj1.teach.add(trainer)

    def test_appointment_form_valid(self):
        user = User.objects.get(username = "user1")
        c = Client()
        c.force_login(user)
        tr = Trainer.objects.first()
        course = Course.objects.first().id
        response = c.post(reverse("Courses:timeslot",args=(course,)))
        form = AppointmentForm(data={
            'trainer': tr, 
            'date': "2021-11-19", 
            'timeslot':3, 
            'customer':user,
        })
        form.save()
        
        self.assertTrue(form.is_valid())
        self.assertTrue(response.status_code , 302)
