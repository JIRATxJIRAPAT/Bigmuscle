
from django.urls import path
from . import views

app_name = "Trainer"

urlpatterns = [
    path('', views.index, name="index"),
    path('trainer_course', views.trainer_course, name="trainer_course"),
    path('info/<int:id>', views.courseInfo, name="courseInfo"),
    path('info', views.courseInfo, name="courseInfo"),
    path('apply', views.registerPageTR, name="apply"),
    path('track/<int:id>', views.customerTrack, name="customerTrack"),
    path("addlink", views.add_link, name="addlink"),
]
