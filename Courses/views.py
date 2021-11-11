from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from Users.models import Customer
from .models import Appointment, Course
from Trainer.models import *
from Tracking.models import *
from .forms import AppointmentForm

def course_page(request):

    course_list = Course.objects.all()
    return render(request, 'courses/course_list.html', {'course_list': course_list})


def show_course(request, id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("Users:login"))
    else:
        try:
            checkTr = Trainer.objects.get(user=request.user)
        except Trainer.DoesNotExist:
            checkTr = None
        if checkTr is None:
            customer1 = get_object_or_404(Customer,user=request.user)
            customer_owned = customer1.owned
            course_details = Course.objects.get(id=id)
            x = get_object_or_404(Course, pk=id)
            tr = get_object_or_404(Course, pk=x.id).teach.all()

            listTr = []
            for i in tr:
                listTr.append(i.user)
            print(listTr)
            check_add = True
            check_remove = False

            if customer_owned is not None:

                customer_owned_id = customer_owned.id
                if customer_owned.id == course_details.id:
                    check_add = False
                    check_remove = True
                else:
                    check_add = False
                    check_remove = False
        else: 
            course_details = Course.objects.get(id=id)
            return render(request,'courses/course_details.html' , {'course_details': course_details,'checkTr':checkTr})
    return render(request, 'courses/course_details.html', {'course_details': course_details, "check_add": check_add, "check_remove": check_remove, "listTr": listTr, })


def apply(request, id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("Users:login"))

    x = get_object_or_404(Course, pk=id)
    cus = Customer.objects.get(user=request.user)
    if cus.owned == None:
        cus = Customer.objects.filter(user=request.user)
        cus.update(owned=x)

    return HttpResponseRedirect(reverse("Courses:select", args=(id,)))


def selectTrainer(request, id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("Users:login"))
    course = get_object_or_404(Course, pk=id)
    tr = get_object_or_404(Course, pk=course.id).teach.all()
    cus = Customer.objects.get(user=request.user)
    if request.method == "POST":
        cus = Customer.objects.filter(user=request.user)
        addtr = request.POST["trainer"]
        trainer = get_object_or_404(Trainer, pk=(addtr))
        track = Tracks.objects.create(track_trainer=trainer, day=course.days)
        cus.update(trainer=addtr, track_customer=track)
        return HttpResponseRedirect(reverse("Courses:time",args=(id,)))
    return render(request, 'courses/TRselect.html',
                  {
                      'trainer': tr,
                      'course': course,
                  })


def removeCourse(request, id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("Users:login"))

    x = get_object_or_404(Course, pk=id)
    cus = Customer.objects.get(user=request.user)
    if cus.owned == x:
        cus = Customer.objects.filter(user=request.user)
        cus.update(owned=None)
        cus.update(trainer=None)
    return HttpResponseRedirect(reverse("Courses:course_details", args=(id,)))


def new_appointment(request,id):
    if request.method == 'POST':
        user = Customer.objects.get(user=request.user)
        form = AppointmentForm(request.POST)
        if form.is_valid():
            val = form.save(commit=False)
            val.trainer = user.trainer
            val.customer = user
            val = form.save()
            return HttpResponseRedirect(reverse("home:index"))
    else:
        form = AppointmentForm()
    return render(request, 'Courses/timeselect.html', {'form': form})
