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
from .forms import TrainerForm, VideocallForm
from Users.models import *
from Tracking.models import *
from Users.forms import *
import datetime
from social.models import *
from social.forms import *
from django.views import View
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
        return render(request, "trainer/trainerProfile.html", context2)


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
    customer = get_object_or_404(Customer, pk=id)
    customer_join = get_object_or_404(Customer, pk=id).track_customer
    customer_track = get_object_or_404(Tracks, pk=customer_join.id)
    customer_program_day = customer_track.day_program.all()
    posts = customer.my_post.all()
    postform = PostForm()
    for i in customer_program_day:
        print(i.id)
    if request.method == "POST":
        print("reachhere")
        form = PostForm(request.POST)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.for_author = customer
            new_post.save()

    return render(request, "trainer/customerTrack.html", {
        "customer": customer,
        "track": customer_join,
        "program": customer_program_day,
        "posts":posts,
        "form":postform,

    }
    )


def program_customer(request, id):
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
    return render(request, 'trainer/customerworkout.html', context)


def add_link(request):
    form = VideocallForm()
    tr = Trainer.objects.get(user=request.user)
    if request.method == 'POST':
        form = VideocallForm(request.POST)
        if form.is_valid():
            tr.videocall_link = form.cleaned_data['link']
            tr.save()
            return HttpResponseRedirect(reverse("Trainer:index"))
    return render(request, "trainer/trainerProfile.html", {'form1': form})


def show_program(request, id, customer_id):
    print(customer_id, id, "reach here")
    cus_tracks_objective = get_object_or_404(
        Program, id=id).objective.all()
    print(cus_tracks_objective)
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
    return render(request, 'trainer/customerworkout.html', context)


def track_approve(request, id, idprogram):
    select_workout = Workout.objects.filter(id=id)
    select_workout.update(status=True)
    print(select_workout)
    return HttpResponseRedirect(reverse("Trainer:program_customer", args=(idprogram,)))


def track_remove(request, id, idprogram):
    select_workout = Workout.objects.filter(id=id)
    select_workout.update(status=False)
    print(select_workout)
    return HttpResponseRedirect(reverse("Trainer:program_customer", args=(idprogram,)))


def edittrack(request, customer_id):
    
    select_track = get_object_or_404(
        Customer, id=customer_id).track_customer
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
        return render(request, "trainer/customer_edittrack.html", {"check_context": check_context, "programlist": select_program, "customer_id": customer_id, })
    return render(request, "trainer/customer_edittrack.html", {"check_context": check_context, })


def addprogram(request, customer_id):

    if request.method == "POST":
        print(customer_id, "aaaaaa")
        select_track = get_object_or_404(
            Customer, id=customer_id).track_customer
        select_tracks = Tracks.objects.get(id=select_track.id).day_program.all()

        count_day = request.POST["day_id"]
        track_start = select_track.start_date
        start = track_start + datetime.timedelta(days=int(count_day))
        end = track_start + datetime.timedelta(days=int(count_day)+1)
        x = datetime.datetime.now()
        program_exist = False
        for i in select_tracks:
            print(i.start_date.day)
            if (i.start_date.day == start.day) and (i.start_date.month == start.month) and (i.start_date.year == start.year):
                program_exist = True
        if  not program_exist:
            select_add = Program.objects.create(
            end_date=end, start_date=start, day=count_day)
        select_track.day_program.add(select_add)
    return HttpResponseRedirect(reverse("Trainer:edittrack", args=(customer_id,)))


def remove_program(request, id_program, customer_id):
    print(id_program, "aaaaa")
    val = Program.objects.get(id=id_program)
    val.delete()
    return HttpResponseRedirect(reverse("Trainer:edittrack", args=(customer_id,)))


def addworkout(request, idprogram):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            val = form.save()
            select_program = Program.objects.get(id=idprogram)
            select_program.objective.add(val)

    return HttpResponseRedirect(reverse("Trainer:program_customer", args=(idprogram,)))


def deleteworkout(request, id, idprogram):

    val = Workout.objects.get(id=id)
    val.delete()
    return HttpResponseRedirect(reverse("Trainer:program_customer", args=(idprogram,)))


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
                print(f"{a}>{b} = {a > b}")
                sort_program[j], sort_program[j + 1] = sort_program[j + 1], sort_program[j]
    return sort_program

class PostDetailView(View):
    def get(self, request, pk, *args, **kwargs):

        post = Post.objects.get(pk=pk)
        form = CommentForm()
        comments = Comment.objects.filter(post=post).order_by('-created_on')
        context = {
            'post': post,
            'form': form,
            'comments': comments,


        }

        return render(request, 'social/post_detail.html', context)

    def post(self, request,pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()

        comments = Comment.objects.filter(post=post).order_by('-created_on')

        context = {
            'post': post,
            'form': form,
            'comments': comments,

        }

        return render(request, 'social/post_detail.html', context)