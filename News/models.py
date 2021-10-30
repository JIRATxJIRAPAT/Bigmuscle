from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=100)
    context = models.TextField()
    slug = models.SlugField(null=True, blank=True)
    date = models.DateField(auto_now=False, auto_now_add=False)
    ps = models.TextField(null=True, blank=True)
    pic1 = models.ImageField(null = True,blank = True)
    pic2 = models.ImageField(null = True,blank = True)
    pic3 = models.ImageField(null = True,blank = True)
    pic4 = models.ImageField(null = True,blank = True)

    def __str__(self):
        return self.title

