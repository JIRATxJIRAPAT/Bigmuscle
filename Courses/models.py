from django.db import models


# Create your models here.
class Course(models.Model):
    course_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length = 500)
    info = models.CharField(max_length = 500)
    teach = models.ManyToManyField('Users.Trainer' ,related_name="teacher",blank = False)
    days = models.PositiveIntegerField(default = 0)
    def __str__(self):
        return f"{self.name} "