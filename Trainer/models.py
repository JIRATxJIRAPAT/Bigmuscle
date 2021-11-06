from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    gender = models.CharField(max_length=20)
    specialist = models.CharField(max_length=100)
    approve = models.BooleanField(default=False)  
    def __str__(self):
        return f"{self.user.username} {self.approve}"

    #@receiver(post_save, sender=User)
    #def create_user_picks(sender, instance, created, **kwargs):
    #    if created:
    #        Trainer.objects.create(user=instance)