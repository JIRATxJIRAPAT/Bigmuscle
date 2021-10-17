from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Trainer(models.Model):
    trainer_id = models.PositiveIntegerField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank = True)
    gender = models.CharField(max_length = 20)
    specialist = models.CharField(max_length = 100)
    
    
    def __str__(self):
        return f"{self.trainer_id}"

    
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank = True)
    owned = models.ForeignKey('Courses.Course',on_delete=models.CASCADE,blank = True,related_name="study",null = True)
    weight = models.PositiveIntegerField(default = 0)
    height = models.PositiveIntegerField(default = 0)
    trainer = models.ForeignKey(Trainer,on_delete=models.CASCADE,related_name="my_trainer",null = True,blank = True)
    
    def __str__(self):
        return f"{self.user} {self.id}"