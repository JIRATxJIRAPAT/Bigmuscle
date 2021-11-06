from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from Users.models import Customer
from .models import Course


def course_page(request):

    course_list = Course.objects.all()
    return render(request, 'courses/course_list.html', {'course_list': course_list})


def show_course(request, id):

    course_details = Course.objects.get(id=id)

    return render(request, 'courses/course_details.html', {'course_details': course_details})


def apply(request, id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("Users:login"))

    x = get_object_or_404(Course, pk=id)

    cus = Customer.objects.get(user=request.user)
    if cus.owned == None:
        cus = Customer.objects.filter(user=request.user)
        cus.update(owned=x)
    return HttpResponseRedirect(reverse("Courses:course_details", args=(id,)))


def removeCourse(request, id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("Users:login"))

    x = get_object_or_404(Course, pk=id)
    cus = Customer.objects.get(user=request.user)
    if cus.owned == x:
        cus = Customer.objects.filter(user=request.user)
        cus.update(owned=None)
    return HttpResponseRedirect(reverse("Courses:course_details", args=(id,)))
