from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import BusinessProfile
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
from .forms import LoginForm

# Create your views here.

class BusinessProfileDetailView(DetailView):

    model = User
    context_object_name = 'business' 
    template_name = 'businessprofile_detail.html'

class LoginView(generic.FormView):
    form_class = LoginForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)


class LogOutView(generic.RedirectView):
    url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogOutView, self).get(request, *args, **kwargs)

class ProfilView(TemplateView):
    template_name = 'accounts/profil.html'