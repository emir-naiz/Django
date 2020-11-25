from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.

def userlist(request):
    users = User.objects.all()
    return HttpResponse(users)


def bloglist(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs}
    return render(request,'blog/blog-template.html',context)

def postlist(request):
    posts = Post.objects.all()
    context = {'post':posts}
    return render(request,'blog/post-template.html',context)
