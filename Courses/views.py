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
from .forms import AppointmentForm,CourseForm
import re
from django.contrib.auth import authenticate

def sort_course(c):
    sort_course = []
    n = len(c)

    for x in c:
        sort_course.append(x)
 
    for i in range(n-1):
        for j in range(0, n-i-1):
            a = sort_course[j].name
            b = sort_course[j + 1].name
            if a > b :
                print(f"{a}>{b} = {a > b}")
                sort_course[j], sort_course[j + 1] = sort_course[j + 1], sort_course[j]
    return sort_course

def course_page(request):
    if  request.user.is_authenticated:
        try:
            checkTr = Trainer.objects.get(user=request.user)
        except Trainer.DoesNotExist:
            checkTr = None

        if checkTr is not None:
            return HttpResponseRedirect(reverse("Trainer:trainer_course"))

    all_course_name = "nothing here"


    if request.method == "POST":
        search_course = request.POST['search_course']
        all_course_name = "i'm in"
        course_list = Course.objects.all()
        if search_course == "\w":

            return render(request, 'courses/course_list.html', {
                'course_list': course_list,
                'all_course_name': all_course_name
            })
        # split input to list
        search_course = search_course.upper()

        search_course = re.split(r'\s', search_course)

        course_filtered = []

        for j in search_course:
            #print(j)
            for i in course_list:
                if re.search(j, i.name.upper()):
                    print(i.name.upper())
                    course_filtered.append(i)

        all_course_name = "done"
        course_list = course_filtered
        course_list = sort_course(course_list)
    else:
        course_list = Course.objects.all()
        course_list = sort_course(course_list)
    return render(request, 'courses/course_list.html', {
        'course_list': course_list,
        'all_course_name': all_course_name
    })


def show_course(request, id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("Users:login"))
    else:
        x = get_object_or_404(Course, pk=id)
        tr = get_object_or_404(Course, pk=x.id).teach.all()

        listTr = []
        for i in tr:
            listTr.append(i.user)
        try:
            checkTr = Trainer.objects.get(user=request.user)
        except Trainer.DoesNotExist:
            checkTr = None
        if checkTr is None:
            customer1 = get_object_or_404(Customer, user=request.user)
            customer_owned = customer1.owned
            course_details = Course.objects.get(id=id)

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
            check_tr_teach = 0
            course_teach = Course.objects.get(id=id).teach.all()
            teach_id = []
            for i in course_teach:
                teach_id.append(i.id)
            if request.user.trainer.id in teach_id:
                check_tr_teach = 1
            course_details = Course.objects.get(id=id)

            return render(request, 'courses/course_details.html', {'course_details': course_details, 'checkTr': checkTr, "check_tr_teach": check_tr_teach, "listTr": listTr, })
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

    count_tr = 1
    tr_index = tr[count_tr-1]

    cus = Customer.objects.get(user=request.user)
    if request.method == "POST":
        cus = Customer.objects.filter(user=request.user)
        addtr = request.POST["trainer"]
        trainer = get_object_or_404(Trainer, pk=(addtr))
        track = Tracks.objects.create(track_trainer=trainer, day=course.days)
        cus.update(trainer=addtr, track_customer=track)

        return HttpResponseRedirect(reverse("Courses:timeslot", args=(id,)))

    return render(request, 'courses/TRselect.html',
                  {
                      'trainer': tr_index,
                      'course': course,
                      "count_tr": count_tr

                  })


def removeCourse(request, id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("Users:login"))

    x = get_object_or_404(Course, pk=id)
    cus = Customer.objects.get(user=request.user)
    if cus.owned == x:
        cus = Customer.objects.filter(user=request.user)
        select = Appointment.objects.filter(customer__in=cus)
        select1 = Tracks.objects.filter(tracks_owner__in=cus)
        select2 = get_object_or_404(
            Tracks, tracks_owner__in=cus).day_program.all()

        for i in select2:
            i.delete()
        select.delete()
        select1.delete()
        cus.update(owned=None)
        cus.update(trainer=None)
    return HttpResponseRedirect(reverse("Courses:course_details", args=(id,)))


def new_appointment(request, id):
    if request.method == 'POST':
        user = Customer.objects.get(user=request.user)
        form = AppointmentForm(request.POST)
        x = get_object_or_404(Course, pk=id)
        if form.is_valid():
            val = form.save(commit=False)
            val.trainer = user.trainer
            val.customer = user
            val = form.save()
            return HttpResponseRedirect(reverse("home:index"))
    else:
        form = AppointmentForm()
    return render(request, 'courses/timeselect.html', {'form': form})


def slidenext(request, course_id, count_tr):
    count_tr += 1
    course = get_object_or_404(Course, pk=course_id)
    tr = get_object_or_404(Course, pk=course.id).teach.all()
    select_tr = counttrselect(count_tr, tr)
    tr_index = tr[select_tr-1]
    if request.method == "POST":
        cus = Customer.objects.filter(user=request.user)
        addtr = request.POST["trainer"]
        trainer = get_object_or_404(Trainer, pk=(addtr))
        track = Tracks.objects.create(track_trainer=trainer, day=course.days)
        cus.update(trainer=addtr, track_customer=track)

        return HttpResponseRedirect(reverse("Courses:timeslot", args=(course_id,)))

    return render(request, 'courses/TRselect.html',
                  {
                      'trainer': tr_index,
                      'course': course,
                      "count_tr": select_tr
                  })


def slideback(request, course_id, count_tr):

    course = get_object_or_404(Course, pk=course_id)
    tr = get_object_or_404(Course, pk=course.id).teach.all()
    if (count_tr == 1):
        count_tr = len(tr)
    else:
        count_tr -= 1
    select_tr = counttrselect(count_tr, tr)
    tr_index = tr[select_tr-1]
    if request.method == "POST":
        cus = Customer.objects.filter(user=request.user)
        addtr = request.POST["trainer"]
        print(addtr)
        trainer = get_object_or_404(Trainer, pk=(addtr))
        track = Tracks.objects.create(track_trainer=trainer, day=course.days)
        cus.update(trainer=addtr, track_customer=track)

        return HttpResponseRedirect(reverse("Courses:timeslot", args=(course_id,)))

    return render(request, 'courses/TRselect.html',
                  {
                      'trainer': tr_index,
                      'course': course,
                      "count_tr": count_tr
                  })


def counttrselect(count_tr, tr):

    if count_tr < 1:
        print("reach here ")
        count_tr = (len(tr))
    if count_tr >= len(tr)+1:
        count_tr = 1
    print(count_tr)
    return count_tr


def editcourse(request, id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("Users:login"))
    course_details = Course.objects.get(id=id)
    form = CourseForm()
    return render(request, 'courses/editcourse.html', {"course_details": course_details, "form": form})