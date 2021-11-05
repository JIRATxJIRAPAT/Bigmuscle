from django.db import models
from django.db.models.deletion import CASCADE
from Users.models import *

# Create your models here.

class Exercise(models.Model):
    ex_name = models.CharField(max_length = 500)
    bd_part = models.CharField(max_length = 500)
    
    def __str__(self):
        return f"{self.ex_name} {self.bd_part}"

class Workout(models.Model):
    wo_set = models.CharField(max_length = 500, blank= False)
    wo_time = models.CharField(max_length = 500, blank= False)
    wo_status = models.BooleanField(default=False)
    exercise = models.ForeignKey(Exercise ,on_delete=CASCADE ,related_name="workout",blank = False)
    
    def __str__(self):
        return f"{self.exercise} {self.wo_set} {self.wo_time}"

class Day_Program(models.Model):
    workouts = models.ManyToManyField(Workout,related_name="workoutplan", blank= True)
    dp_date = models.DateField(blank= True)
    dp_status = models.BooleanField(default= False)

    def __str__(self):
        return f"{self.dp_date} {self.dp_status}"

class Tracks(models.Model):
    day_pragram = models.ForeignKey(Day_Program, blank=True, on_delete=CASCADE)
    #track_customer = models.OneToOneField('Users.Customer', on_delete=CASCADE, related_name="tracks", null=True)
    track_trainer = models.ForeignKey('Users.Trainer', on_delete=CASCADE, related_name="trainer", null=True)
    all_program_status = models.BooleanField(default= False)

    def __str__(self):
        return f"{self.track_trainer} {self.all_program_status}"