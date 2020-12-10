from django.shortcuts import render,redirect
from .models import Post, Comments
from .forms import RegistrationForm, CommentsForm
from django.contrib import messages

# Create your views here.
def home_view(request):
    posts = Post.objects.all()
    comments = Comments.objects.all()
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('home-view')
    else:
        form = CommentsForm()
        context = {
            'posts': posts,
            'comments':comments,
            'form':form,
        }
    return render(request,'advice/home.html',context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account Created Successfully')
            return redirect('home-view')

    else:
        form = RegistrationForm()
    return render(request, 'advice/register.html',{'form':form})


