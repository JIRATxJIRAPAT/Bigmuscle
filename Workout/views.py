from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse 
from Users.models import *
from .models import *

# Create uwu your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("Users:login"))
    else:
        all_wo = Workout.objects.all()
        all_ex = Exercise.objects.all()
        all_dp = Day_Program.objects.all()
        user = Customer.objects.get(user=request.user)
        userTrack = Tracks.objects.get(customer_track = user)
        return render(request, "workout/program_management.html", {
            "all_wo": all_wo,
            "all_ex": all_ex,
            "all_dp": all_dp,
            "userTrack": userTrack,
        })