from django.db import models

# Create your models here.

class Shop(models.Model):
    title = models.CharField(max_length=100)
    context = models.TextField()
    price = models.PositiveIntegerField(default=0)
    date = models.DateField(auto_now=False, auto_now_add=True)
    pic1 = models.ImageField(null = True,blank = True,default="default-image.png")

    def __str__(self):
        return f"{self.title}"