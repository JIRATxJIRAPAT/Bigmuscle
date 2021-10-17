from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Trainer(models.Model):
    trainer_id = models.PositiveIntegerField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank = True)
    gender = models.CharField(max_length = 20)
    specialist = models.CharField(max_length = 50)
    
    
    def __str__(self):
        return f"{self.trainer_id}"

class Course(models.Model):
    course_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length = 20)
    info = models.CharField(max_length = 500)
    teach = models.ManyToManyField(Trainer ,related_name="teacher")
    
    def __str__(self):
        return f"{self.name} "
    
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank = True)
    owned = models.ForeignKey(Course,on_delete=models.CASCADE,blank = True,related_name="study",null = True)
    weight = models.PositiveIntegerField(default = 0)
    height = models.PositiveIntegerField(default = 0)
    trainer = models.ForeignKey(Trainer,on_delete=models.CASCADE,related_name="my_trainer",null = True,blank = True)
    
    def __str__(self):
        return f"{self.user} {self.id}"