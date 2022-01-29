from django.shortcuts import render
from app.models import User, Post
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView


def base(request):
    return render(request, 'app/base.html')


class UsersListView(ListView):
    model = User
    template_name = 'app/user_list.html'
    context_object_name = 'users'


class UserDetailView(DetailView):
    model = User
    context_object_name = 'user'


class AddUserCreateView(CreateView):
    model = User
    success_url = reverse_lazy('journal:user_list')
    fields = ('name', 'username', 'email')


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'


class PostsListView(ListView):
    model = Post
    template_name = 'app/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related('user').all()
        return qs


class AddPostCreateView(CreateView):
    model = Post
    success_url = reverse_lazy('journal:post_list')
    fields = ('title', 'user', 'body')
