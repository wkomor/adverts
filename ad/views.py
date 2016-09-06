from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from hitcount.views import HitCountDetailView
from .models import Ad
from .forms import AddAdForm


class AdListView(ListView):
    """
    View for all ads
    """
    model = Ad
    template_name = 'ad/index.html'
    context_object_name = 'ads'


class AdMixinDetailView(object):
    """
    Mixin to same us some typing.  Adds context for us!
    """
    model = Ad

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AdDetailView(AdMixinDetailView, HitCountDetailView):
    """
    Ad detail view
    """
    model = Ad
    template_name = 'ad/detail_ad.html'
    count_hit = True


class AdAdd(CreateView):
    """
    Add Ad
    """
    form_class = AddAdForm
    template_name = 'ad/add.html'
    model = Ad
    success_url = '/'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class AdUpdate(UpdateView):
    """
    Update ad
    """
    form_class = AddAdForm
    template_name = 'ad/add.html'
    model = Ad
    success_url = '/'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)



