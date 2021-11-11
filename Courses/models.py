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
        return f"{self.name} {self.days}"


class Appointment(models.Model):
    """Contains info about appointment"""
    class Meta:
        unique_together = ('trainer', 'date', 'timeslot')

    TIMESLOT_LIST = (
        (0, '09:00 – 09:30'),
        (1, '10:00 – 10:30'),
        (2, '11:00 – 11:30'),
        (3, '12:00 – 12:30'),
        (4, '13:00 – 13:30'),
        (5, '14:00 – 14:30'),
        (6, '15:00 – 15:30'),
        (7, '16:00 – 16:30'),
        (8, '17:00 – 17:30'),
    )

    trainer = models.ForeignKey("Trainer.Trainer",on_delete = models.CASCADE,null=True,blank=True)
    date = models.DateField(help_text="YYYY-MM-DD")
    timeslot = models.IntegerField(choices=TIMESLOT_LIST)
    customer = models.ForeignKey('Users.Customer',on_delete = models.CASCADE,null=True,blank=True)

    def __str__(self):
        return f'{self.trainer} {self.timeslot}'

    @property
    def time(self):
        return self.TIMESLOT_LIST[self.timeslot][1]