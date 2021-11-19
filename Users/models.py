from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    owned = models.ForeignKey('Courses.Course', on_delete=models.CASCADE,
                              blank=True, related_name="study", null=True)
    weight = models.FloatField(default=0)
    height = models.FloatField(default=0)
    bmi = models.FloatField(default=0)
    trainer = models.ForeignKey('Trainer.Trainer', on_delete=models.CASCADE,related_name="my_trainer", null=True, blank=True)
                
    track_customer = models.OneToOneField(
        'Tracking.Tracks', related_name="tracks_owner", on_delete=models.SET_NULL, null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, default="user_default_pic.jfif")
    last_login = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return f"{self.user} {self.id}"

    # @receiver(post_save, sender=User)
    # def create_user_picks(sender, instance, created, **kwargs):
    #   if created:
    #        Customer.objects.create(user=instance)


class Report(models.Model):

    REPORT_LIST = (
        ('Harassment', 'harassment'),
        ('Bad word', 'use bad word'),
        ('Threaten', 'threaten'),
        ('Hate speeches', 'hate speeches'),
        ('Not helpful', 'advice not helpful'),
    )

    trainer = models.ForeignKey('Trainer.Trainer', on_delete=models.CASCADE, related_name="re_trainer", null=True, blank=True )
    reason = models.CharField(max_length=30,choices=REPORT_LIST)
    context = models.TextField()
    date = models.DateField(auto_now=False,auto_now_add=True)
    evidence = models.ImageField(null=True,blank=True)
    report_by = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="reportby", null=True, blank=True )
    def __str__(self):
        return f"{self.trainer} {self.reason}"