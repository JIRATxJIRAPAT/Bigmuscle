
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib import messages





def news_views(request):
    
    return render(request, "news/news1.html")
# Create your views here.
