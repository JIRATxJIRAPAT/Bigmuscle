from django.db import models

# Create your models here.

class Exercise(models.Model):
    exercise_name = models.CharField(max_length = 100)
    parts = models.CharField(max_length = 100)
    
    def __str__(self):
        return f"{self.exercise_name}"


class Workout(models.Model):
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    reps = models.PositiveIntegerField()
    sets = models.PositiveIntegerField()
    status = models.BooleanField(default=False)
    exercise = models.ForeignKey(Exercise,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return f"{self.exercise} in {self.date}"

class Program(models.Model):
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_date = models.DateTimeField()
    owner = models.ForeignKey('Users.Customer',on_delete=models.CASCADE)
    objective = models.ManyToManyField(Workout,related_name="workout")
    def __str__(self):
        return f"{self.owner} {self.start_date}"

class Tracks(models.Model):
    day_pragram = models.ManyToManyField(Program, blank=True,related_name="daily")
    track_customer = models.OneToOneField('Users.Customer', related_name="tracks_owner",on_delete=models.CASCADE)
    track_trainer = models.OneToOneField('Users.Trainer',related_name="trainer",on_delete=models.CASCADE)
    all_program_status = models.BooleanField(default= False)
    day = models.PositiveIntegerField(default=0)
    def str(self):
        return f"{self.track_trainer} {self.track_customer} {self.all_program_status}"