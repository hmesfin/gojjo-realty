from django.views.generic import ListView, DetailView
from gojjo_realty.blogs.models import Post, Category, BlogMeta
from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.urls import reverse_lazy

class PostListView(ListView):
    model = Post
    template_name = 'blogs/blog_list.html'
    context_object_name = 'blogs'
    paginate_by = 6
    ordering = ['-created_date']

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['meta'] = BlogMeta.objects.all().first()
        context['blog_title'] = 'Blogs List'
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'blogs/blog_detail.html'
    context_object_name = 'blog'
    slug_field ='slug'
    slug_url_kwarg ='slug'


    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['recent_posts'] = Post.objects.published().order_by('-pub_date')[:3]
        context['category_count'] = Category.objects.annotate(post_count=Count('post_set')).order_by('-post_count')
        context['meta'] = BlogMeta.objects.all().first()
        context['page_title'] = "Blogs List"
        context['list_view_url'] = reverse_lazy('blogs:blog_list')
        context['detail_page_title'] = self.object.title
        return context

    def increment_view_count(self):
        view_count = self.object.view_count
        self.object.view_count = view_count + 1
        self.object.save()
        return self.object.view_count

class CategoryListView(ListView):
    model = Post
    template_name = 'blogs/category_list.html'
    context_object_name = 'posts'
    paginate_by = 6
    
    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Post.objects.published().filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['meta'] = BlogMeta.objects.all().first()
        context['blog_category'] = self.category.name
        return context
    
    