from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    category = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=None, null=True, blank=True)

    class Meta:
        ordering = ['-date_posted']
    


class Comments(models.Model):
    name = models.CharField(max_length=120)
    text = models.TextField()
    post = models.ForeignKey(Post,related_name='comments', on_delete=models.CASCADE)
   
   
    