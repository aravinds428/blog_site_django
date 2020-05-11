from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . forms import UserRegisterForm

from django.contrib.auth.models import User
from blog.models import Post

# Create your views here.


def register(request):
    if(request.method == "POST"):
        form = UserRegisterForm(request.POST)
        if(form.is_valid()):
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username} !')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    user = User.objects.get(username=request.user.username)
    posts = Post.objects.filter(author=user).order_by('-date_posted')
    # return render(request, 'blog/blogs_headings.html', {'posts': posts})
    return render(request, 'users/profile.html', {'posts': posts})


@login_required
def delete_post(request):
    id_val = int(request.POST['id_value'])
    Post.objects.filter(id=id_val).delete()
    messages.success(request, 'Blog deleted !')
    return redirect('profile')
