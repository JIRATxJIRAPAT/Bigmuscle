from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from Workout.models import Tracks

# Create your models here.


class Trainer(models.Model):
    trainer_id = models.PositiveIntegerField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    gender = models.CharField(max_length=20)
    specialist = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.trainer_id}"


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    owned = models.ForeignKey('Courses.Course', on_delete=models.CASCADE,
                              blank=True, related_name="study", null=True)
    weight = models.FloatField(default=0)
    height = models.FloatField(default=0)
    bmi = models.FloatField(default=0)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name="my_trainer", null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True)
    track = models.OneToOneField(Tracks, blank=True, on_delete=models.CASCADE, related_name="customer_track", null=True)
    
    def __str__(self):
        return f"{self.user} {self.id}"

    @receiver(post_save, sender=User)
    def create_user_picks(sender, instance, created, **kwargs):
        if created:
            Customer.objects.create(user=instance)
