from django.urls import path

from . import views

app_name = "Courses"

urlpatterns = [
    path("",views.course_page,name="course_list"),
    path("<int:id>",views.show_course,name="course_details"),
    
]