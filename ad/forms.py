from django.forms import ModelForm
from .models import Ad


class AddAdForm(ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'text']