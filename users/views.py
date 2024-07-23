import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, ListView, DetailView

from blog.models import Post
from mailings.services import send_mail
from users.forms import UserForm, ProfileForm, ManagerForm
from users.models import User



class LoginView(BaseLoginView):
    template_name = 'users/login.html'

class LogoutView(BaseLogoutView):
    def get_success_url(self):
        return reverse_lazy('users:login')

class RegisterView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:varning')

    def form_valid(self, form):
        new_user = form.save()
        code = ''.join([str(random.randint(0, 9)) for _ in range(12)])
        user_mail = new_user.email
        send_mail(
            _to_mail=new_user.email,
            _subject='Поздравляю, вы зарегистрировались на нашем сайте!',
            _message=f'Перейдите по ссылке, чтобы активировать ваш профиль:'
                     f'http://127.0.0.1:8000/user/verificate/?c={code}&m={user_mail}'
        )
        new_user.ver_code = code


        return super().form_valid(form)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'users/profile_form.html'
    success_url = reverse_lazy('users:users_list')
    #form_class = ProfileForm

    login_url = 'users:login'

    def get_form_class(self):
        if self.request.user.is_staff:
            return ManagerForm
        else:
            return ProfileForm

    #def get_object(self, queryset=None):
    #    return self.request.user

class UserListView(ListView):
    model = User


def varning(request):
    return render(request,'users/varning.html')

def make_active(request):
    code = request.GET.get('c', '')
    user_email = request.GET.get('m', '')
    user = User.objects.get(email=user_email)
    print(f'code: {code}')
    if  user.ver_code == code:

        user.is_active = True
        user.save()

    return redirect(reverse('users:login'))
