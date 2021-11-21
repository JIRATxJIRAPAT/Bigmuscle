from django.shortcuts import render
from .models import News
from django.http import HttpResponseRedirect
from django.urls import reverse

def news_list(request):
    # Query all posts
    all_posts = News.objects.all()

    return render(request, 'news/listnews.html', {'all_posts': all_posts})

def blog_details(request, id):
    # Query only single post
    single_post = News.objects.get(id=id)

    return render(request, 'news/news-details.html', {'single_post': single_post})

def new_delete(request,id):
    single_post = News.objects.get(id=id)
    single_post.delete()
    return HttpResponseRedirect(reverse("News:news-list"))