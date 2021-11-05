from django.urls import path
from . import views

app_name = "Tracking"

urlpatterns = [
    path("",views.index,name="workout"),
]