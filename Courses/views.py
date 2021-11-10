from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from Users.models import Customer
from .models import Course
from Trainer.models import *
from Tracking.models import Tracks


def course_page(request):

    course_list = Course.objects.all()
    return render(request, 'courses/course_list.html', {'course_list': course_list})


def show_course(request, id):
    customer1 = Customer.objects.get(user=request.user)
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

    return render(request, 'courses/course_details.html', {
        'course_details': course_details, 
        "check_add": check_add, 
        "check_remove": check_remove, 
        "listTr": listTr, })


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
    x = get_object_or_404(Course, pk=id)
    tr = get_object_or_404(Course, pk=x.id).teach.all()
    cus = Customer.objects.get(user=request.user)
    if request.method == "POST":
        cus = Customer.objects.filter(user=request.user)
        addtr = request.POST["trainer"]
        trainer = get_object_or_404(Trainer, pk=(addtr))
        track = Tracks.objects.create(track_trainer=trainer)
        cus.update(trainer=addtr, track_customer=track)
        return HttpResponseRedirect(reverse("home:index"))
    return render(request, 'courses/TRselect.html',
                  {
                      'trainer': tr,
                      'course': x,
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
        #Tracks.objects.filter(tracks_owner=cus).delete()
        cus.update(track_customer=None)
    return HttpResponseRedirect(reverse("Courses:course_details", args=(id,)))

"""
def selectTrainer(request, id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("Users:login"))
    x = get_object_or_404(Course, pk=id)
    tr = get_object_or_404(Course, pk=x.id).teach.all()
    cus = Customer.objects.get(user=request.user)
    if request.method == "POST":
        cus = Customer.objects.filter(user=request.user)
        addtr = request.POST["trainer"]
        cus.update(trainer=addtr)
        return HttpResponseRedirect(reverse("home:index"))
    return render(request, 'courses/TRselect.html',
                  {
                      'trainer': tr,
                      'course': x,
                  }
                  )


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
"""