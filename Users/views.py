from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib import messages

from Trainer.models import Trainer
from .forms import CreateUserForm, CustomerForm
from django.contrib.auth.forms import UserCreationForm
from .models import Customer

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("Users:login"))
    else:
        try:
            checkTr = Trainer.objects.get(user=request.user)
        except Trainer.DoesNotExist:
            checkTr = None

        if checkTr is not None:
            return render(request, "trainer/trainerProfile.html")
        else:

            Customer1 = request.user.customer
            form = CustomerForm(instance=Customer1)
            if request.method == 'POST':
                form = CustomerForm(request.POST, request.FILES, instance=Customer1)
                if form.is_valid():
                    form.save()
            context = {'form': form}
            return render(request, "users/userprofile.html", context)


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home:index"))
        else:
            return render(request, "users/login.html", {
                "message": "Invalid Username or Password."
            })
    return render(request, "users/login.html")


def logout_view(request):
    logout(request)

    return HttpResponseRedirect(reverse("home:index"))


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            customer = Customer.objects.create(user=user)
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home:index")
    context = {'form': form}
    return render(request, 'users/register.html', context)


