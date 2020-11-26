from django.urls import path, include
from .views import *
urlpatterns = [
    path('users/', userlist),
    path('blog/', bloglist),
    path('post/', postlist),
    path('blog/<int:blog_id>/', blogDetailView)
]
