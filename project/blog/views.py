from django.views.generic import ListView,DetailView
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
        
class SinglePost(DetailView):
    
    template_name = 'blog/post-detail.html'
    model = PostModel
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context["tags"] = self.object.tag.all() 
        return context
    