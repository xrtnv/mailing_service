from django.urls import path, re_path

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, UserUpdateView, make_active, varning, UserListView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    #path('profile/', UserUpdateView.as_view(), name='profile'),

    path('varning/', varning, name='varning'),
    path('verificate/', make_active, name='verificate'),

    path('users/', UserListView.as_view(), name='users_list'),
    path('profile/edit/<int:pk>/', UserUpdateView.as_view(), name='profile_edit')
]
