from django.urls import path
from . import views

app_name = "Workout"

urlpatterns = [
    path("",views.index,name="workout"),
]

