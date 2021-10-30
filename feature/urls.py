from django.urls import path

from . import views

app_name = "feature"

urlpatterns = [
    path("bdtest",views.bdTest,name="bdTest"),
]