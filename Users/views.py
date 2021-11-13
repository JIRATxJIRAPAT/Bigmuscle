from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib import messages

from Trainer.models import Trainer
from .forms import CreateUserForm, CustomerForm,ReportForm
from django.contrib.auth.forms import UserCreationForm
from .models import Customer
from Tracking.models import *
import datetime

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
            return HttpResponseRedirect(reverse("Trainer:index"))
        else:
            Customer1 = request.user.customer
            form = CustomerForm(instance=Customer1)
            tr = get_object_or_404(Customer, user=request.user).trainer
            tr_name = "None"
            cus_track = "None"
            cus_tracks_program = "None"
            cus_tracks_objective = "None"

            if tr is not None:
                tr_name = tr.user
                cus_track_join = get_object_or_404(
                    Customer, user=request.user).track_customer
                cus_tracks_program = get_object_or_404(
                    Tracks, id=cus_track_join.id).day_program.all()
                print(cus_tracks_program)
                check_day_program_length = len(cus_tracks_program)
                for i in cus_tracks_program:
                    cus_tracks_objective = get_object_or_404(
                        Program, id=i.id).objective.all()

                    check_workout_length = len(cus_tracks_objective)
                    check_workout_finish = 0
                    check_workout = []
                    for x in cus_tracks_objective:
                        if x.status:
                            check_workout_finish += 1

                    if check_workout_finish != check_workout_length:
                        check_workout.append(0)
                    else:
                        check_workout.append(1)

            if request.method == 'POST':
                form = CustomerForm(
                    request.POST, request.FILES, instance=Customer1)
                if form.is_valid():
                    form.save()
            context = {'form': form,
                       'trainer': tr_name,
                       'program': cus_tracks_program, "workout":  cus_tracks_objective}
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


def show_program(request, id):
    cus_tracks_objective = get_object_or_404(
        Program, id=id).objective.all()

    check_program_length = len(cus_tracks_objective)
    check_program = 0
    show_program_status = 0
    for i in cus_tracks_objective:
        if i.status:
            check_program += 1

    select_program = Program.objects.filter(id=id)
    if check_program == check_program_length:

        select_program.update(status=True)
        show_program_status = 1
    else:

        select_program.update(status=False)
        show_program_status = 0
    context = {"id": id,
               "workout":  cus_tracks_objective,
               "status_day": show_program_status}
    return render(request, 'users/show_track.html', context)


def track_approve(request, id, idprogram):
    select_workout = Workout.objects.filter(id=id)
    select_workout.update(status=True)
    print(select_workout)
    return HttpResponseRedirect(reverse("Users:show_program", args=(idprogram,)))


def track_remove(request, id, idprogram):
    select_workout = Workout.objects.filter(id=id)
    select_workout.update(status=False)
    print(select_workout)
    return HttpResponseRedirect(reverse("Users:show_program", args=(idprogram,)))


def edittrack(request):
    select_track = get_object_or_404(
        Customer, user=request.user).track_customer
    select_program = get_object_or_404(
        Tracks, id=select_track.id).day_program.all()

    check_empty = (len(select_program))
    print(check_empty)
    check_context = 0
    if check_empty == 0:
        check_context = 0
    else:
        check_context = 1

    return render(request, "users/edit_track.html", {"check_context": check_context, "programlist": select_program})


def addprogram(request):

    if request.method == "POST":
        select_track = get_object_or_404(
            Customer, user=request.user).track_customer
        select_tracks = Tracks.objects.filter(id=select_track.id)

        count_day = request.POST["day_id"]
        x = datetime.datetime.now()
        select_add = Program.objects.create(
            end_date=x, start_date=x, day=count_day)
        select_track.day_program.add(select_add)
    return HttpResponseRedirect(reverse("Users:edittrack"))


def report(request):
    form = ReportForm()
    user = Customer.objects.get(user=request.user)
    re_trainer = user.trainer
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            val = form.save(commit=False)
            val.trainer = user.trainer
            val.report_by = user
            val = form.save()
            return HttpResponseRedirect(reverse("Users:userprofile"))
    return render(request, 'users/report.html', {'form': form,'trainer':re_trainer})