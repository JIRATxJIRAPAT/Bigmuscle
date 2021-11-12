from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    age = models.PositiveIntegerField(default=0)
    gender = models.CharField(max_length=20)
    bio = models.CharField(max_length=250, null=True)
    specialist = models.CharField(max_length=100)
    tel = models.CharField(max_length=10, null=True)
    approve = models.BooleanField(default=False)
    profile_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
