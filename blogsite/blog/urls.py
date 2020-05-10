from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('viewpost', views.displayBlogContent, name='post-content'),
    path('createblog', views.createNewBlog, name='create-blog'),
]
