from django.urls import path

from . import views

app_name = "administrator"

urlpatterns = [
    path("",views.index,name="profile"),
    path("job/",views.applicant_list,name="applicant_list"),
    path("job/<int:id>",views.applicant_info,name="applicant_info"),
    path("job/<int:id>/approve",views.approve,name="approve"),
    path("job/<int:id>/decline",views.decline,name="decline"),
    path("news/",views.create_news,name="create_news"),
    path("report/",views.report_list,name="report_list"),
    path("report/<int:id>",views.report_info,name="report_info"),
    path("course/",views.create_course,name="create_course"),
]