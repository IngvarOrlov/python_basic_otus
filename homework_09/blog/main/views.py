from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView

from .models import Post, User
from .forms import PostForm


# Create your views here.

def posts(request):
    posts = Post.objects.select_related("user").all()
    # print(posts.query)
    return render(request, 'blog/posts.html', {"posts": posts})


def index(request):

    return render(request, 'index.html')


def addpost(request):
    # get
    if request.method == 'GET':
        newform = PostForm()
        return render(request, 'main/addpost.html', {'form': newform})
    # post
    try:
        # проверяем есть ли среди пользователей автор поста
        new_user = User.objects.get(name=request.POST.get('name'))
    except:
        # нет так нет
        new_user = User.objects.create(name=request.POST.get('name'))
    finally:
        Post.objects.create(
            title=request.POST.get('title'),
            body=request.POST.get('body'),
            user=new_user
        )
        return redirect('posts')


def show_post(request, id):
    post = Post.objects.select_related("user").get(id=id)
    return render(request, 'blog/post.html', {'post': post})


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post


class PostListView(ListView):
    model = Post
