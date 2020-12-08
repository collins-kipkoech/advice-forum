from django.shortcuts import render
from .models import Post
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home_view(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request,'advice/home.html',context)

def register(request):
    form = UserCreationForm()
    context = {
        'form':form,
    }
    return render(request,'advice/register.html',context)
