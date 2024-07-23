from django import forms

from mailings.models import Mailing


class MailingForm(forms.ModelForm):

    class Meta:
        model = Mailing
        fields = ('message_title',
                  'message_body',
                  'start',
                  'stop',
                  'period',
                  )

