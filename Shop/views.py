
from django.shortcuts import render
from .models import Shop

def shop_list(request):
    # Query all posts
    all_posts = Shop.objects.all()

    return render(request, 'shop/shop-list.html', {'all_posts': all_posts})

def shop_detail(request, id):
    # Query only single post
    single_post = Shop.objects.get(id=id)

    return render(request, 'shop/shop-detail.html', {'single_post': single_post})