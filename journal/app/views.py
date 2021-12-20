from django.shortcuts import render
from app.models import User, Post


def base(request):
    return render(request, 'app/base.html')


def users_list(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'app/user_list.html', context=context)


def posts_list(request):
    posts = Post.objects.select_related('user').all()
    context = {
        'posts': posts
    }
    return render(request, 'app/post_list.html', context=context)

