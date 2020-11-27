from django.conf import settings
from django.db import models
from django.utils import timezone

class Blog(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()
    blog = models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
