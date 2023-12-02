from django.urls import path
from .views import *
urlpatterns = [
    path('',HomeView.as_view(),name='home-page'),
    path('posts',AllPosts.as_view(),name='posts-page'),
    path('posts/<slug:slug>',SinglePost.as_view(),name='post-detail-page')
]
