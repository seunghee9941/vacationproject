from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog, Comment
from .forms import NewBlog, CommentForm

def welcome(request):
    return render(request, 'crud/index.html')

def create(request):
    if request.method == 'POST':
        form = NewBlog(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
        return redirect('home')
    else:
        form = NewBlog()
        return render(request, 'crud/new.html', {'form':form})

def read(request):
    blogs = Blog.objects.all()
    return render(request, 'crud/crud.html', {'blogs':blogs})

def update(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    form = NewBlog(request.POST, instance=blog)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'crud/new.html', {'form':form})

def delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return redirect('home')


def comment(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('home')
    else:
        form = CommentForm()
    return render(request, 'crud/comment.html', {'form': form})


def comment_update(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    form = CommentForm(request.POST, instance=comment)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'crud/comment.html', {'form':form})

def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('home')