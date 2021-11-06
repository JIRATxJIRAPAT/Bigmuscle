from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .forms import CreateUserTRForm
from django.contrib.auth.forms import UserCreationForm
from .models import Trainer


# Create your views here.
def registerPageTR(request):
    form = CreateUserTRForm()
    if request.method == 'POST':
        form = CreateUserTRForm(request.POST)
        if form.is_valid():
            age = request.POST["age"]
            number = request.POST["tel"]
            bio = request.POST["bio"]
            gender = request.POST["gender"]
            sp = request.POST["specialist"]
            user = form.save()
            tr = Trainer.objects.create(user=user, gender=gender, specialist=sp,age=age,tel=number,bio=bio)
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home:index")
    context = {'form': form}
    return render(request, 'Trainer/registerTR.html', context)
