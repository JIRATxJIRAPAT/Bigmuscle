from django.urls import path
from . import views

app_name = 'News'
urlpatterns = [
    path('', views.home, name="home"),
    path('News/<int:id>', views.blog_details, name="news-details"),

]