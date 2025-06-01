from django.shortcuts import render, redirect
from .forms import PostForm
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseForbidden
from .models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('user_dashboard')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

@login_required
def user_dashboard(request):
    posts = Post.objects.filter(author=request.user, is_deleted=False).order_by('-created_at')
    return render(request, 'user_dashboard.html', {'posts': posts})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user, is_deleted=False)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('user_dashboard')
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user, is_deleted=False)
    post.is_deleted = True
    post.save()
    return redirect('user_dashboard')