from django.urls import path

from blog.apps import BlogConfig
from blog.views import PostCreateView, PostListView, PostUpdateView, PostDeleteView, PostDetailView

app_name = BlogConfig.name

urlpatterns = [
    path('', PostListView.as_view(), name='list'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('detail/<int:pk>', PostDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete'),

]