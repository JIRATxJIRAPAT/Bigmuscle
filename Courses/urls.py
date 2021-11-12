from django.urls import path

from . import views


app_name = "Courses"

urlpatterns = [
    path("", views.course_page, name="course_list"),
    path("<int:id>", views.show_course, name="course_details"),
    path("<int:id>/apply", views.apply, name="apply"),
    path("<int:id>/remove", views.removeCourse, name="remove"),
    path("<int:id>/apply/trainer", views.selectTrainer, name="select"),
    path("<int:id>/apply/trainer/timeslot", views.new_appointment, name="timeslot"),
    #path("<int:id>/apply/trainer/timeslot/cancel", views.cancel_appointment, name="cancel"),
]
