from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .forms import CreateUserTRForm
from django.contrib.auth.forms import UserCreationForm
from .models import Trainer
from Courses.models import Course
from .forms import TrainerForm
from Users.models import *
# Create your views here.


def index(request):

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("Users:login"))
    else:
        checkTr = Trainer.objects.get(user=request.user)
        form = TrainerForm(instance=checkTr)
        if request.method == 'POST':
            form = TrainerForm(
                request.POST, request.FILES, instance=checkTr)
            if form.is_valid():
                form.save()
        context2 = {'form': form}
        return render(request, "Trainer/trainerprofile.html", context2)


def trainer_course(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("Users:login"))
    else:
        try:
            tr = Trainer.objects.get(user=request.user)
        except Trainer.DoesNotExist:
            tr = None
        if tr is None:
            return HttpResponseRedirect(reverse("home:index"))
        else:
            cus = "this course has no customer"
            track = None
            all_course = get_object_or_404(
                Trainer, user=request.user).teacher.all()
            blanklist = []
            for i in all_course:
                blanklist.append(i)

            if request.method == "POST":
                trCourse = request.POST["course"]
                # course = get_object_or_404(Course, pk=trCourse)
                course = get_object_or_404(Course, pk=trCourse)
                cus = get_object_or_404(Course, pk=trCourse).study.all()
                # cus = Customer.objects.get(owned=course).all()
                cusList = []
                for i in cus:
                    cusList.append(i)
                    # cus = Customer.objects.get(owned=course).all()
                return render(request, "trainer/trainercourse.html", {
                    "all_course": blanklist,
                    "course_info": course,
                    "customerList": cusList,
                })

            return render(request, "trainer/trainercourse.html", {
                "all_course": blanklist,
                "all_cus": cus,
                "track": track,
            })


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
            tr = Trainer.objects.create(
                user=user, gender=gender, specialist=sp, age=age, tel=number, bio=bio)
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home:index")
    context = {'form': form}
    return render(request, "trainer/registerTR.html", context)


def courseInfo(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("Users:login"))
    else:
        try:
            tr = Trainer.objects.get(user=request.user)
        except Trainer.DoesNotExist:
            tr = None
        if tr is None:
            return HttpResponseRedirect(reverse("home:index"))
        else:
            return render(request, "trainer/courseInfo.html")


def customerTrack(request, id):
    customer = get_object_or_404(Customer, pk=id).track_customer
    return render(request, "trainer/customerTrack.html", {
        "customer": customer,
    })
