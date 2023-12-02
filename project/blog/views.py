from django.shortcuts import render
from django.views import View
from django.views.generic import ListView,DetailView
# Create your views here.
class HomeView(View):

    def get(self,request):
        return render(request,'blog/index.html')

# class AllPosts(ListView):
#     model = ''
#     template_name = 'blog/all-posts.html'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context
class AllPosts(View):

    def get(self,request): 
        return render(request,'blog/all-posts.html')
        
class SinglePost(DetailView):
    pass