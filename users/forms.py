from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import AppUser


class CreationForm(UserCreationForm):
    class Meta:
        model = AppUser
        fields = ('username',)


class AuthForm(AuthenticationForm):
    class Meta:
        model = AppUser
        fields = ('username',)
