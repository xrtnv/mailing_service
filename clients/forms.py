from django import forms

from clients.models import Client


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'comment',)


