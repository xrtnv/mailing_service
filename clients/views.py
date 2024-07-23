from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from clients.forms import ClientForm
from clients.models import Client
from mailings.models import Mailing


class ClientCreateView(CreateView):
    model = Client
    success_url = reverse_lazy('mailings:mailings_list')
    form_class = ClientForm


    def form_valid(self, form):
        new_client = form.save()
        new_client.user = self.request.user
        new_client.id = self.request.user.id
        new_client.save()

        content_type = ContentType.objects.get_for_model(Mailing)
        #try:
        permission1 = Permission.objects.get(
            codename='add_mailing',
            content_type=content_type,
        )
        permission2 = Permission.objects.get(
            codename='change_mailing',
            content_type=content_type,
        )
        permission3 = Permission.objects.get(
            codename='delete_mailing',
            content_type=content_type,
        )
        #except Permission.DoesNotExist:
            # Если разрешение не существует, создадим его
        #    permission = Permission.objects.create(
        #        codename='add_mailing',
        #        content_type=content_type,
        #        name='Can add mailing'
        #    )

        # Получим или создадим группу
        clients_group, created = Group.objects.get_or_create(name='Клиенты')

        # Проверим, что разрешение еще не добавлено к группе
        #if permission not in clients_group.permissions.all():
        clients_group.permissions.add(permission1, permission2, permission3)

        clients_group.user_set.add(self.request.user)

        return super().form_valid(form)

        
