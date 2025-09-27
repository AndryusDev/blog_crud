from django.shortcuts import render

from .models import Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

"""def post_list(request):
    return render(request, 'blog.html')"""


class PostListView(ListView):
    model = Post
    template_name = "blog.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class PostNewView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ['title','body', 'author']
    