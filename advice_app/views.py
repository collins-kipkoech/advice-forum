from django.shortcuts import render
from .models import Post

# Create your views here.
def home_view(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request,'advice/home.html',context)
