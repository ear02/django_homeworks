from django.contrib import admin
from django.urls import path
import app.views as app_views

app_name = 'journal'

urlpatterns = [
    path('', app_views.base, name='base'),
    path('users/',
         app_views.UsersListView.as_view(),
         name='user_list'
    ),
    path('posts/',
         app_views.PostsListView.as_view(),
         name='post_list'
    ),
    path('users/<int:pk>/',
         app_views.UserDetailView.as_view(),
         name='user_detail'
    ),
    path('posts/<int:pk>/',
         app_views.PostDetailView.as_view(),
         name='post_detail'
     ),
]
