from django.urls import path
from . import views

app_name = "Users"

urlpatterns = [
    path("",views.index,name="userprofile"),
    path("login",views.login_view,name="login"),
    path('logout',views.logout_view,name="logout"),
    path('register',views.registerPage,name="register"),
    path("<int:id>", views.show_program, name="show_program"),
    path("<int:id>/approve <int:idprogram>",
         views.track_approve, name="trackapprove"),
    path("<int:id>/remove <int:idprogram>",
         views.track_remove, name="trackremove"),
    path('edittrack', views.edittrack, name="edittrack"),
    path("addprogram", views.addprogram, name="addprogram"),

]

