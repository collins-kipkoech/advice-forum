from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def home_view(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request,'advice/home.html',context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account Created Successfully')
            return redirect('home-view')

    else:
        form = UserCreationForm()
    return render(request, 'advice/register.html',{'form':form})
