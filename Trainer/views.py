from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .forms import CreateUserTRForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



# Create your views here.
def registerPageTR(request):
    form = CreateUserTRForm()
    if request.method == 'POST':
        form = CreateUserTRForm(request.POST)
        if form.is_valid():
            
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home:index")
    context = {'form': form}
    return render(request, 'Trainer/registerTR.html', context)

#user = User.objects.create_user(value['user'], value['email'], value['password'])