from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Post(models.Model):
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    for_author = models.ForeignKey('Users.Customer',on_delete=models.CASCADE,related_name="my_post", null=True, blank=True)

class Comment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)