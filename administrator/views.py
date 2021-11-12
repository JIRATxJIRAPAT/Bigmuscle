from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from Trainer.models import Trainer

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

