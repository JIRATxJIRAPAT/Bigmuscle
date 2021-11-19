from django.test import TestCase,Client
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Max
from .models import News


class NewsViewTestCase(TestCase):

    def setUp(self):
        password = make_password('1234')
        News.objects.create(title="dd",context="dd",date='2021-10-30')
        User.objects.create(username = "user1" , password = password , email = "user2@example.com")


    def test_authenticate_News_page(self):

        user = User.objects.get(username = "user1")

        c = Client()
        c.force_login(user)
        response = c.get(reverse("News:news-list"))
        self.assertEqual(response.status_code , 200)


    def test_guest_user_can_view_News_page(self):
        c = Client()
        response = c.get(reverse("News:news-list"))
        self.assertEqual(response.status_code , 200)


    def test_valid_News_page(self):

        c = Client()
        s = News.objects.first()
        response = c.get(reverse("News:news-list"))
        self.assertEqual(response.status_code,200)


    def test_news_list_View_context(self):
        s = News.objects.first()
        c = Client()
        response = self.client.get(reverse('News:news-list'))



    def test_valid_newsdetail_page(self):
        """valid  detailpage should return status code 200"""
        c = Client()
        s = News.objects.first()
        response = c.get(reverse("News:news-details", args=(s.id,)))
        self.assertEqual(response.status_code,200)