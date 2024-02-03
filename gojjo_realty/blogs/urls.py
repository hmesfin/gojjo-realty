from django.urls import path
from gojjo_realty.blogs.views.views import PostListView, PostDetailView, CategoryListView

app_name = 'blogs'

urlpatterns = [
    path('', PostListView.as_view(), name='blog_list'),
    path('blog/<slug:slug>/', PostDetailView.as_view(), name='blog_detail'),
    path('category/<slug:slug>/', CategoryListView.as_view(), name='category_list'),
]