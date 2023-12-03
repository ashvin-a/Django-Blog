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
            'tags':post.tag.all(),
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
            'tags':post.tag.all(),
            'comment_form': comment_form, #Ivide kodukunna saadanam ella                    nokkim kandum kodukkane 💀
            'comments':post.comments.all().order_by('-id')

        })

class ReadLater(View):

    def get(self,request):
        stored_post = request.session.get('stored_posts')

        context = {}
        if stored_post is None:
            context['posts'] = []
            context['has_posts'] = False
        else:
            posts = PostModel.objects.filter(id__in=stored_post)
            context['posts'] = posts
            context['has_posts'] = True
        
        return render(request,'blog/stored-posts.html',context)



    def post(self,request):
        stored_post = request.session.get('stored_posts')

        if stored_post is None:
            stored_post = []
        post_id = request.POST['post_id'] # form name = post_id
        if post_id not in stored_post:
            stored_post.append(post_id)
            request.session['stored_posts'] = stored_post #This block of code is dicey.
        return HttpResponseRedirect('/')
        

    