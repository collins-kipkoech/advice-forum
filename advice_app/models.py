from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    category = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,default=None, null=True, blank=True)
    


class Comments(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,default=None, null=True, blank=True)
    