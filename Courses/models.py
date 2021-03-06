from django.db import models
from Trainer.models import *

# Create your models here.


class Course(models.Model):

    name = models.CharField(max_length=500)
    info = models.CharField(max_length=500)
    teach = models.ManyToManyField(
        'Trainer.Trainer', related_name="teacher", blank=False)
    days = models.PositiveIntegerField(default=0)
    pic = models.ImageField(null=True, blank=True,default="default-image.png")

    def __str__(self):
        return f"{self.name}"


class Appointment(models.Model):
    """Contains info about appointment"""
    class Meta:
        unique_together = ('date', 'timeslot')

    TIMESLOT_LIST = (
        ('04:00 – 05:30', '04:00 – 05:30'),
        ('06:00 – 07:30', '06:00 – 07:30'),
        ('08:00 – 09:30', '08:00 – 09:30'),
        ('10:00 – 11:30', '10:00 – 11:30'),
        ('13:00 – 14:30', '13:00 – 14:30'),
        ('15:00 – 16:30', '15:00 – 16:30'),
        ('17:00 – 18:30', '17:00 – 18:30'),
        ('19:00 – 20:30', '19:00 – 20:30'),
        ('21:00 – 22:30', '21:00 – 22:30'),
        ('23:00 – 01:30', '23:00 – 01:30'),
    )

    trainer = models.ForeignKey("Trainer.Trainer",on_delete = models.CASCADE,null=True,blank=True)
    date = models.DateField(help_text="YYYY-MM-DD")
    timeslot = models.TextField(choices=TIMESLOT_LIST)
    customer = models.ForeignKey('Users.Customer',on_delete = models.CASCADE,null=True,blank=True,related_name='customer')

    def __str__(self):
        return f"{self.trainer} w/ {self.customer}"

    @property
    def time(self):
        return self.TIMESLOT_LIST[self.timeslot][1]