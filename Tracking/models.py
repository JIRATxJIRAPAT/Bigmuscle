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
    created_by = models.ForeignKey('Users.Trainer', on_delete=models.CASCADE)
    owner = models.ForeignKey('Users.Customer',on_delete=models.CASCADE,null=True)
    def __str__(self):
        return f"{self.exercise} in {self.date} {self.owner}"


class Program(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    owner = models.ForeignKey('Users.Customer',on_delete=models.CASCADE)
    objective = models.ManyToManyField(Workout,related_name="workout")
    def __str__(self):
        return f"{self.owner} {self.start_date}"
