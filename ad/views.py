from django.views.generic import ListView, DetailView, FormView
from .models import Ad


class AdListView(ListView):
    model = Ad
    template_name = 'ad/index.html'
    context_object_name = 'ads'


class AdDetailView(DetailView):
    model = Ad
    template_name = 'ad/detail_ad.html'
