from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm  

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("Users:login"))
    #get_subject = request.user.enroll.all()
    return render(request, "users/userprofile.html")
        #"subject":get_subject,
    
        
    
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("Users:userprofile"))
        else:
            return render(request, "users/login.html",{
                "message": "Invalid Username or Password."
            })
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)

    return HttpResponseRedirect(reverse("Users:login"))

"""
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home:index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="users/register.html", context={"register_form":form})
"""
def registerPage(request):
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
			
		context = {'form':form}
		return render(request, 'users/register.html', context)