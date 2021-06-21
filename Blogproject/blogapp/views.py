from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from . models import Post
from django.urls import reverse_lazy
# Create your views here.
'''
def home(request):
    return render(request,"blogapp/home.html",{}) '''
class HomeView(ListView):
    model = Post
    template_name = 'blogapp/home.html'
    ordering = ['-id']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blogapp/article.html'

class AddPostView(CreateView):
    model = Post
    fields = '__all__'
    template_name = 'blogapp/newpost.html'

class UpdatePost(UpdateView):
    model = Post
    template_name = "blogapp/updatepost.html"
    fields = ['title','title_tag','body']
class DeletepostView(DeleteView):
    model = Post
    template_name = "blogapp/deletepost.html"
    success_url = reverse_lazy('home')