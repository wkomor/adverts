from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Ad
from .forms import AddAdForm


class AdListView(ListView):
    model = Ad
    template_name = 'ad/index.html'
    context_object_name = 'ads'


class AdDetailView(DetailView):
    model = Ad
    template_name = 'ad/detail_ad.html'


class AdAdd(CreateView):
    form_class = AddAdForm
    template_name = 'ad/add.html'
    model = Ad
    success_url = '/'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class AdUpdate(UpdateView):
    form_class = AddAdForm
    template_name = 'ad/add.html'
    model = Ad
    success_url = '/'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)



