from django.test import TestCase,Client
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Max
from .models import Course


class CoursesViewTestCase(TestCase):

    def setUp(self):
        password = make_password('1234')
        Course.objects.create(name="dd",info="dd",teach="T1234")
        User.objects.create(username = "user1" , password = password , email = "user2@example.com")


    def test_authenticate_Course_page(self):

        user = User.objects.get(username = "user1")

        c = Client()
        c.force_login(user)
        response = c.get(reverse("Courses:course_list"))
        self.assertEqual(response.status_code , 200)


    def test_valid_Course_page(self):

        c = Client()
        s = Course.objects.first()
        response = c.get(reverse("Courses:course_page"))
        self.assertEqual(response.status_code,200)

    
    def test_Course_list_View_context(self):
        s = Course.objects.first()
        c = Client()
        response = self.client.get(reverse('Courses:course_page'))


    def test_valid_newsdetail_page(self):
        """valid  detailpage should return status code 200"""
        c = Client()
        s = Course.objects.get(id=id)
        response = c.get(reverse("Courses:course_details", args=(s.id,)))
        self.assertEqual(response.status_code,200)


    def test_guest_user_cannot_apply_course(self):
        """ guest cannot apply course """
        user = User.objects.create(username = "user2" , password = "1234" , email = "user2@example.com")
        s = Course.objects.first()

        c = Client()
        response = c.get(reverse('Courses:apply' ,args=(s.name,)))
        self.assertEqual(s.teach.count(),0)



    def test_authenticated_user_can_apply_course(self):
        """ authenticated user can apply course """
        user = User.objects.create(username="user2",password="1234",email="user2@gmail.com")
        s = Course.objects.first()

        c = Client()
        c.force_login(user)
        response = c.get(reverse('Courses:apply' ,args=(s.name,)))
        self.assertEqual(s.teach.count(),1)



    def test__authenticated_user_can_remove_course(self):
        """ authenticated user can remove course """
        user = User.objects.create(username="user2",password="1234",email="user2@gmail.com")
        s = Course.objects.first()
        

        c = Client()
        c.force_login(user)
        response = c.get(reverse('Courses:removeCourse' ,args=(s.name,)))
        self.assertEqual(s.teach.count(),0)