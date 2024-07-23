from django.urls import path

from mailings.apps import MailingsConfig
from mailings.models import LogMailing
from mailings.views import MailingListView, MailingCreateView, MailingUpdateView, MailingDeleteView, LogDetailView

app_name = MailingsConfig.name


#from mailings.tasks import schedule_mailings
#schedule_mailings()

urlpatterns = [
    path('', MailingListView.as_view(), name='mailings_list'),
    path('create/', MailingCreateView.as_view(), name='mailing_create'),
    path('update/<int:pk>', MailingUpdateView.as_view(), name='mailing_update'),
    path('delete/<int:pk>', MailingDeleteView.as_view(), name='mailing_delete'),

    path('logs/<int:pk>/', LogDetailView.as_view(), name='logs')


    #path('start-schedule_mailings/', lambda request: None, name='start-schedule_mailings')

]