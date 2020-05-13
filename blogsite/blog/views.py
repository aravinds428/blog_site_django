from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from . import models
# Create your views here.


def home(request):
    posts = models.Post.objects.all().order_by('-date_posted')
    return render(request, 'blog/blogs_headings.html', {'posts': posts})


def displayBlogContent(request):
    id_val = int(request.POST['id_value'])
    post = models.Post.objects.get(id=id_val)
    return render(request, 'blog/blog_content.html', {'post': post})


@login_required
def createNewBlog(request):
    if(request.method == "POST"):
        title_value = request.POST['title_value']
        content_value = request.POST['content_value']
        user_id = User.objects.get(username=request.user.username).id
        post_obj = models.Post(
            title=title_value, content=content_value, author_id=user_id)  # , user=user_value)
        post_obj.save()
        messages.success(request, 'Blog successfully posted !')
        return redirect('create-blog')
    else:
        return render(request, 'blog/create_blog.html')
