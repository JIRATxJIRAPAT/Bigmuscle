from django.urls import path
from . import views

app_name = 'News'
urlpatterns = [
    path('', views.news_list, name="news-list"),
    path('<int:id>', views.blog_details, name="news-details"),

]