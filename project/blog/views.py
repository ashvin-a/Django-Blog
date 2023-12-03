from django.views.generic import ListView
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import View
from .models import PostModel
from .forms import CommentForm
# Create your views here.

class HomeView(ListView):

    template_name = 'blog/index.html'
    model = PostModel
    ordering = ['-date']
    context_object_name = 'posts'

    def get_queryset(self):
        query = super().get_queryset()[:3]
        return query
    
class AllPosts(ListView):

    template_name = 'blog/all-posts.html'
    model = PostModel
    context_object_name = 'posts'
    ordering = ['-date']

    def get_queryset(self):
        query = super().get_queryset()
        return query
        
class SinglePost(View):
    
    def get(self,request,slug):
        post = PostModel.objects.get(slug=slug) 
        return render(request,'blog/post-detail.html',{
            'post':post,
            'tag':post.tag.all(),
            'comment_form':CommentForm(),
            'comments':post.comments.all().order_by('-id')
        })
    
    def post(self,request,slug):
        comment_form = CommentForm(request.POST)
        post = PostModel.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            #Here we take the data from user, adds our post 
            #relation from our side, then updates the db.
            return HttpResponseRedirect(reverse('post-detail-page',args=[slug]))

        return render(request,'blog/post-detail.html',{
            'post':post,
            'tag':post.tag.all(),
            'comment_form': comment_form, #Ivide kodukunna saadanam ella                    nokkim kandum kodukkane 💀
            'comments':post.comments.all().order_by('-id')

        })

    