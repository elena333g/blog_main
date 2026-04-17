# -*- coding: utf-8 -*-
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, render,redirect

from .models import Post, Category
from .forms import commentFormm
# Create your views here.
def home(request):
    posts = Post.objects.filter(status=Post.ACTIVE).order_by('-created_at')
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def detail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.ACTIVE)
    

    if request.method == "POST":
      form = commentFormm(request.POST)

      if form.is_valid():
         comment = form.save(commit=False)
         comment.post = post
         comment.save()


    context = {
        "post" : post,
    }
    return render(request, "blog/detail.html", context)
