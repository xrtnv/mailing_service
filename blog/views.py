from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Group
from django.core.cache import cache
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from blog.models import Post
from clients.models import Client
from config.settings import CACHE_ENABLED
from mailings.models import Mailing
from users.models import User


class PostCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Post
    fields = ('title', 'body', 'image')
    success_url = reverse_lazy('blog:list')

    permission_required = 'blog.add_post'
    login_url = 'users:login'

class PostListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Post

    permission_required = 'blog.view_post'
    login_url = 'users:login'

class PostDetailView(DetailView):
    model = Post

    login_url = 'users:login'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object

class PostUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Post
    fields = ('title', 'body', 'image')

    success_url = reverse_lazy('blog:list')

    permission_required = 'blog.change_post'
    login_url = 'users:login'

class PostDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model =  Post
    success_url = reverse_lazy('blog:list')

    permission_required = 'blog.delete_post'
    login_url = 'users:login'


def main(request):
    mailings_count = len(Mailing.objects.all())

    mailings_active_count = len(Mailing.objects.filter(status='Активна'))

    posts = Post.objects.all()[:3]



    if CACHE_ENABLED:

        key = f'clients_count'
        clients_count = cache.get(key)
        if clients_count is None:
            clients_count = len(Client.objects.all())
            cache.set(key, clients_count)
    else:
        clients_count = len(Client.objects.all())



    context = {
        'mailings_count': mailings_count,
        'mailings_active_count': mailings_active_count,
        'clients_count': clients_count,
        'posts': posts
    }

    return render(request, 'blog/main_menu.html', context)

