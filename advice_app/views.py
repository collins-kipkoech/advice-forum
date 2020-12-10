from django.shortcuts import render,redirect
from .models import Post, Comments
from .forms import RegistrationForm, CommentsForm,PostQuestionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_view(request):
    posts = Post.objects.all()
    comments = Comments.objects.all()
    query = request.GET.get('q')
    if query:
        posts = posts.filter(category__icontains=query)
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        
        if form.is_valid():
            addComment = form.save(commit=False)
            addComment.save()
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


@login_required
def post_question(request):
    if request.method == 'POST':
        
        form = PostQuestionForm(request.POST)
        if form.is_valid():
            addProject = form.save(commit=False)
            addProject.save()
            
            messages.success(request,'Your project has been posted successfully')
            return redirect('home-view')

    else:
        form = PostQuestionForm()
    context = {'form':form,}
    return render(request,'advice/post.html',context)


