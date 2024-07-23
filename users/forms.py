from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import User


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)


class ProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email',
                  'password',
                  'avatar',
                  'country',
                  'last_name',
                  'first_name',
                  )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()


class ManagerForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'is_active',
        )
