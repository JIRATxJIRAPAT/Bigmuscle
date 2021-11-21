from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from Trainer.models import Trainer
from News.forms import CreateNewsForm
from Users.models import *
from Courses.forms import *
from Courses.models import *

# job application
def applicant_list(request):
    if request.user.is_superuser:
        applicant = Trainer.objects.all().filter(approve=False)
        return render(request, 'administrator/applicant_list.html', {'applicant': applicant})
    
    return HttpResponseRedirect(reverse("home:index"))
 
def applicant_info(request,id):
    select_user = Trainer.objects.filter(id=id)
    return render(request, 'administrator/applicant_info.html', {'select_user': select_user})

def approve(request,id):
    select_user = Trainer.objects.filter(id=id)
    select_user.update(approve=True)
    return HttpResponseRedirect(reverse("administrator:applicant_list"))

def decline(request,id):
    select_user = Trainer.objects.filter(id=id)
    select_user.delete()
    return HttpResponseRedirect(reverse("administrator:applicant_list"))

# News sections

def create_news(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = CreateNewsForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse("home:index"))
        else:
            form = CreateNewsForm()
        return render(request, 'administrator/create_news.html', {'form': form})
    else:
        return HttpResponseRedirect(reverse("home:index"))

# Report system
def report_list(request):
    if request.user.is_superuser:
        report = Report.objects.all()
        return render(request, 'administrator/report_list.html', {'report': report})
    
    return HttpResponseRedirect(reverse("home:index"))

def report_info(request,id):
    select_report = Report.objects.filter(id=id)
    return render(request, 'administrator/report_info.html', {'select_report': select_report})

#profile
def index(request):

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("Users:login"))
    else:
        if request.user.is_superuser:
            return render(request, "administrator/adminprofile.html")

#Courses
def create_course(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = CourseForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse("home:index"))
        else:
            form = CreateCourseForm()
        return render(request, 'administrator/create_course.html', {'form': form})
    else:
        return HttpResponseRedirect(reverse("home:index"))