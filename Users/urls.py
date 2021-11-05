from django.urls import path
from . import views

app_name = "Users"

urlpatterns = [
    path("",views.index,name="userprofile"),
    path("login",views.login_view,name="login"),
    path('logout',views.logout_view,name="logout"),
    path('register',views.registerPage,name="register"),

]

