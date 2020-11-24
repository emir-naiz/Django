from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def userlist(request):
    users = User.objects.all()
    return HttpResponse(users)


