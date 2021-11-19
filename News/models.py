from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=100)
    context = models.TextField()
    slug = models.SlugField(null=True, blank=True)
    date = models.DateField(auto_now=False, auto_now_add=True)
    ps = models.TextField(null=True, blank=True)
    pic1 = models.ImageField(null = True,blank = True,default="default-image.png")
    pic2 = models.ImageField(null = True,blank = True,default="default-image.png")
    pic3 = models.ImageField(null = True,blank = True,default="default-image.png")
    pic4 = models.ImageField(null = True,blank = True,default="default-image.png")

    def __str__(self):
        return f"{self.title}"

