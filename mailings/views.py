from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from clients.models import Client
from mailings.forms import MailingForm
from mailings.models import Mailing, LogMailing



class MailingListView(ListView):
    model = Mailing

class MailingCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailings:mailings_list')

    login_url = 'users:login'
    permission_required = 'mailings.add_mailing'

    def form_valid(self, form):
        if form.is_valid():
            new_mailing = form.save()
            new_mailing.owner = Client.objects.get(pk=self.request.user.pk)
            new_mailing.save()

        return super().form_valid(form)


class MailingUpdateView(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    model = Mailing
    fields = ('message_title', 'message_body', 'start', 'stop', 'period',)
    success_url = reverse_lazy('mailings:mailings_list')

    permission_required = 'mailings.change_mailing'
    login_url = 'users:login'
    def form_valid(self, form):
        if form.is_valid():
            new_mailing = form.save()
            if new_mailing.owner == Client.objects.get(pk=self.request.user.pk):
                new_mailing.save()
            else:
                raise Http404

        return super().form_valid(form)

class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailings:mailings_list')
    login_url = 'users:login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()

        # Проверяем, принадлежит ли рассылка текущему пользователю
        if obj.owner == Client.objects.get(pk=self.request.user.pk) or request.user.is_staff == True:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404

class LogDetailView(LoginRequiredMixin, DetailView):
    model = LogMailing
    template_name = 'mailings/logs_detail.html'

    login_url = 'users:login'
