from django.shortcuts import render,get_object_or_404
from django.views import View
from django.views.generic import ListView,DetailView
from datetime import date
from .models import PostModel,AuthorModel,TagModel
# Create your views here.

class HomeView(View):

    def get(self,request):
        posts = PostModel.objects.all().order_by("-date")[:3]
        return render(request,'blog/index.html',{
            "posts":posts
        })
    
class AllPosts(View):

    def get(self,request):
        posts = PostModel.objects.all().order_by("-date")
        return render(request,'blog/all-posts.html',{
            "posts":posts
        })
        
class SinglePost(View):
    
    def get(self,request,slug):
        selected_post = get_object_or_404(PostModel,slug=slug)
        # selected_post = PostModel.objects.get(slug=slug)
        # selected_post = next(post for post in posts if post['slug'] == slug)
        return render(request,'blog/post-detail.html',{
            "post":selected_post,
            "tags":selected_post.tag.all()
        })