from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import AppUser


class CreationForm(UserCreationForm):
    """
    Create user
    """
    class Meta:
        model = AppUser
        fields = ('username',)


class AuthForm(AuthenticationForm):
    """
    Login User
    """
    class Meta:
        model = AppUser
        fields = ('username',)
