from django.contrib import admin

from mailings.models import Mailing, LogMailing


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'message_title', 'message_body', 'start', 'stop', 'period', 'status',)
    list_filter = ('status',)
    search_fields = ('owner',)

@admin.register(LogMailing)
class LogsMailAdmin(admin.ModelAdmin):
    list_display = ('id', 'mailing_key', 'status_try', 'date_try', 'response',)
    list_filter = ('status_try',)