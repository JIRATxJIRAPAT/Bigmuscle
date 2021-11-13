from django.core.exceptions import ImproperlyConfigured
from django.db import models
from Users.models import Customer

# Create uwu your models here.

class Exercise(models.Model):
    exercise_name = models.CharField(max_length = 100)
    parts = models.CharField(max_length = 100)
    
    def __str__(self):
        return f"{self.exercise_name}"


class Workout(models.Model):
    exercise = models.ForeignKey(Exercise,on_delete=models.CASCADE,null=True)
    reps = models.PositiveIntegerField()
    sets = models.PositiveIntegerField()
    status = models.BooleanField(default=False)
    
    
    def __str__(self):
        return f"{self.exercise}"

class Program(models.Model):
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_date = models.DateTimeField()
    objective = models.ManyToManyField(Workout,related_name="workout")
    day = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    def __str__(self):
        return f"day {self.day}"

class Tracks(models.Model):
    day_program = models.ManyToManyField(Program, blank=True,related_name="daily")
    track_trainer = models.ForeignKey('Trainer.Trainer',related_name="trainer",on_delete=models.SET_NULL,blank=True,null=True)
    all_program_status = models.BooleanField(default= False)
    day = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.track_trainer} / status = {self.all_program_status}"