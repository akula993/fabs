from django.shortcuts import render

from django.views.generic import ListView

from blog.models import Post


class HomeViews(ListView):
    model = Post
    queryset = Post.objects.filter(draft=False)
    template_name = 'blog/index.html'
    context_object_name = 'posts'