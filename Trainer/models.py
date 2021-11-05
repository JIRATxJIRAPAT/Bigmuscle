from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Trainer(models.Model):
    user = models.CharField(max_length=10)
    email = models.EmailField()
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    specialist = models.CharField(max_length=100)
    approve = models.BooleanField(default=False)
    
    def __str__(self):
        return f" {self.approve}"

