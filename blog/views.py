from django.shortcuts import render
from django.views.generic import ListView

from blog.models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'all_posts'
    ordering = '-date'