from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Trainer(models.Model):
    tr_id = models.IntegerField(primary_key=True)
    gender = models.CharField(max_length = 20)
    specialist = models.CharField(max_length = 50)
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank = True)
    def __str__(self):
        return f"{self.tr_id}"

class Course(models.Model):
    name = models.CharField(max_length = 20 , primary_key = True)
    info = models.CharField(max_length = 500)
    teach = models.ManyToManyField(Trainer ,related_name="teach")
    
    def __str__(self):
        return f"{self.name} "
    
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank = True)
    owned = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="member") #null
    weight = models.PositiveIntegerField(default = 0)
    height = models.PositiveIntegerField(default = 0)
    
    trainer = models.ForeignKey(Trainer,on_delete=models.CASCADE,related_name="member")
    def __str__(self):
        return f"{self.user}"