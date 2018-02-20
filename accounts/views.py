from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import BusinessProfile
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
from .forms import LoginForm
from braces.views import LoginRequiredMixin, GroupRequiredMixin
from django.views.generic.edit import UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import Group

# Create your views here.

class BusinessProfileDetailView(DetailView):

    model = User
    context_object_name = 'business'
    template_name = 'businessprofile_detail.html'
    #group_required = 'acheteur'

class BuyerLoginView(generic.FormView):
    form_class = LoginForm
    success_url = reverse_lazy('catalogue_index')
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(BuyerLoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)

class SellerLoginView(generic.FormView):
    form_class = LoginForm
    success_url = reverse_lazy('profil')
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(SellerLoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)


class BusinessLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = 'catalogue_index'




class LogOutView(generic.RedirectView):
    url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogOutView, self).get(request, *args, **kwargs)

class ProfilView(TemplateView):
    template_name = 'accounts/profil.html'



class ProfileView(LoginRequiredMixin, GroupRequiredMixin,DetailView):
    template_name = 'businessprofile_detail.html'
    group_required = 'vendeur'
    def get_object(self):
        return self.request.user.businessprofile


class BusinessProfileUpdate(UpdateView):
    model = BusinessProfile
    fields = ['logo','presentation','pays', 'province', 'ville', 'commune', 'adresse', 'telephone', 'email', 'website', 'certifications', 'business_partners', 'business_references']
    template_name_suffix = '_update_form'

    def get_object(self):
        return self.request.user.businessprofile