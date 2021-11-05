
from django.urls import path
from . import views

app_name = "Trainer"

urlpatterns = [
    path('apply',views.registerPageTR,name="apply"),
]

