from django.urls import path


from . import views

app_name = "News"

urlpatterns = [

    path("news1",views.news_views,name="newspage1"),

]