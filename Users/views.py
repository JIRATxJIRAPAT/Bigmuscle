from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from Trainer.models import Trainer
from .forms import CreateUserForm, CustomerForm, WorkoutForm,ReportForm
from .models import Customer
from Courses.models import Appointment
from Tracking.models import *
import datetime 
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    temp = []
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
            check_program_none = 0
            check_workout = "None"
            if tr is not None:
                tr_name = tr.user
                cus_track_join = get_object_or_404(
                    Customer, user=request.user).track_customer
                if cus_track_join is not None:
                    check_program_none = 1
                    cus_tracks_program = get_object_or_404(
                        Tracks, id=cus_track_join.id).day_program.all()

                    check_day_program_length = len(cus_tracks_program)

                    thisday = datetime.datetime.now()
                    print(f"thisday: {thisday}")
                    
                    temp = []

                    for i in cus_tracks_program:
                        check = date_compare(i.end_date)
                        if not check:
                            i.enable_check = False
                        print(i.end_date)
                        print(i.enable_check)
                        cus_tracks_objective = get_object_or_404(
                            Program, id=i.id).objective.all()
                        print("cus")
                        print(cus_tracks_program)
                        check_workout_length = len(cus_tracks_objective)
                        check_workout_finish = 0
                        workout = [i]
                        check_workout = []
                        for x in cus_tracks_objective:
                            workout.append(x)
                            if x.status:
                                check_workout_finish += 1

                        if check_workout_finish != check_workout_length:
                            check_workout.append(0)
                        else:
                            check_workout.append(1)
                        
                        temp.append(workout)
                    cus_tracks_program = sort_program(cus_tracks_program)
            if request.method == 'POST':
                form = CustomerForm(
                    request.POST, request.FILES, instance=Customer1)
                if form.is_valid():
                    form.save()
            context = {'form': form,
                       'trainer': tr_name,
                       'program': cus_tracks_program, "workout":  temp,
                       "program_check": check_program_none,
                       "check_workout": check_workout,
                       }
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
    if check_program == check_program_length & check_program_length != 0:

        select_program.update(status=True)
        show_program_status = 1
    else:
        select_program.update(status=False)
        show_program_status = 0
    form = WorkoutForm()
    context = {"id": id,
               "workout":  cus_tracks_objective,
               "status_day": show_program_status, "form": form}
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
    check_context = 0
    if select_track is not None:
        select_program = get_object_or_404(
            Tracks, id=select_track.id).day_program.all()

        check_empty = (len(select_program))
        print(check_empty)

        if check_empty == 0:
            check_context = 0
        else:
            check_context = 1
        select_program = sort_program(select_program)
        return render(request, "users/edit_track.html", {"check_context": check_context, "programlist": select_program})
    return render(request, "users/edit_track.html", {"check_context": check_context, })


def remove_program(request, id_program):
    print(id_program)
    val = Program.objects.get(id=id_program)
    val.delete()
    return HttpResponseRedirect(reverse("Users:edittrack"))


def addworkout(request, idprogram):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            val = form.save()
            select_program = Program.objects.get(id=idprogram)
            select_program.objective.add(val)

    return HttpResponseRedirect(reverse("Users:show_program", args=(idprogram,)))


def deleteworkout(request, id, idprogram):

    val = Workout.objects.get(id=id)
    val.delete()
    return HttpResponseRedirect(reverse("Users:show_program", args=(idprogram,)))


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

def videocall_noti(request):
    x = Customer.objects.get(user=request.user)
    ap = Appointment.objects.get(customer=x)
    time = ap.timeslot
    user = x.trainer.id 
    y = Trainer.objects.get(id=user)
    z = y.videocall_link
    return render(request, "users/getlink.html", {'link':z ,'time':time})


def date_compare(d):
    today = datetime.datetime.now()
    thisday = datetime.date(today.year, today.month, today.day)
    end = datetime.date(d.year, d.month, d.day)


    a = today.replace(hour = int(today.hour), minute = int(today.minute))
    b = today.replace(hour = int(d.hour), minute = int(d.minute))

    #print(f"today:{thisday}")
    #print(f"end: {end}")
    #print(thisday > end)
    #print(a <= b)
    
    if thisday > end:
        return False
    elif a > b and thisday > end:
        return False
    else:
        return True


def sort_program(q):
    sort_program = []
    n = len(q)

    for x in q:
        sort_program.append(x)
 
    for i in range(n-1):
        for j in range(0, n-i-1):
            a = sort_program[j].start_date
            b = sort_program[j + 1].start_date
            if a > b :
                #print(f"{a}>{b} = {a > b}")
                sort_program[j], sort_program[j + 1] = sort_program[j + 1], sort_program[j]
    return sort_program