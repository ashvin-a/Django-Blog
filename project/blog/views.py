from django.shortcuts import render
from django.views import View
from django.views.generic import ListView,DetailView
# Create your views here.
class HomeView(View):

    def get(self,request):
        return render(request,'blog/index.html')

class AllPosts(ListView):
    pass 

class SinglePost(DetailView):
    pass