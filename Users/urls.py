from django.urls import path
from . import views

app_name = "Users"

urlpatterns = [
    path("", views.index, name="userprofile"),
    path("login", views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('register', views.registerPage, name="register"),
    path("<int:id>", views.show_program, name="show_program"),
    path("<int:id_program>/remove", views.remove_program, name="remove_program"),
    path("<int:id>/approve <int:idprogram>",
         views.track_approve, name="trackapprove"),
    path("<int:id>/remove <int:idprogram>",
         views.track_remove, name="trackremove"),
    path("<int:id>/delete <int:idprogram>",
         views.deleteworkout, name="deleteworkout"),
    path('edittrack', views.edittrack, name="edittrack"),
    path("addprogram", views.addprogram, name="addprogram"),
    path("addworkout/<int:idprogram>", views.addworkout, name="addworkout"),
    path("report/",views.report,name="report"),
    path("showlink",views.videocall_noti,name="dd")
]

