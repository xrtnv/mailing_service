from django.urls import path

from clients.apps import ClientsConfig
from clients.views import ClientCreateView

app_name = ClientsConfig.name

urlpatterns = [
    path('create/', ClientCreateView.as_view(), name='create'),

]