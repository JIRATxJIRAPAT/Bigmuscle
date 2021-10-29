from django.db import models

# Create your models here.

class News(models.Model):
    context = models.CharField(max_length=9999)