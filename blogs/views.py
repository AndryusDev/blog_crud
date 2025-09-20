from django.shortcuts import render

from .models import Post
from django.views.generic import ListView

"""def post_list(request):
    return render(request, 'blog.html')"""


class PostListView(ListView):
    model = Post
    template_name = 'blog.html'
