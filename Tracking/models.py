from django.db import models

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
    def __str__(self):
        return f"{self.start_date}"

class Tracks(models.Model):
    day_pragram = models.ManyToManyField(Program, blank=True,related_name="daily")
    track_trainer = models.OneToOneField('Trainer.Trainer',related_name="trainer",on_delete=models.CASCADE)
    all_program_status = models.BooleanField(default= False)
    day = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"{self.track_trainer} {self.all_program_status}"