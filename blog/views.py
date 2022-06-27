from django.db.models import F
from django.shortcuts import render

from django.views.generic import ListView, DetailView

from blog.models import Post, Category


class HomeViews(ListView):
    model = Post
    template_name = 'blog/index.html'
    queryset = Post.objects.filter(draft=False)
    context_object_name = 'posts'
    paginate_by = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'сайт написан на django'
        return context


class CategoryViews(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(category__url=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(url=self.kwargs['slug'])
        return context

def get_post(request, slug):
    return render(request, 'blog/detail.html')

class PostView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context
