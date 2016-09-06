from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView, View
from django.contrib.auth import login, logout
from .forms import AuthForm, CreationForm


class RegisterFormView(FormView):
    form_class = CreationForm
    success_url = "/user/login"
    template_name = "users/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthForm
    template_name = "users/login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")