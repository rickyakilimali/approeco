from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout


class HomePageView(generic.TemplateView):
    template_name = 'home.html'


def login_success(request):
	"""
	Redirects users based on whether they are in the admins group
	"""
	if request.user.groups.filter(name='acheteurs').exists():

		return redirect('catalogue_index')
	else:
		return redirect('profil')


class LoginView(generic.FormView):
	form_class = LoginForm
	success_url = reverse_lazy('login_success')
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
	url = reverse_lazy('login')

	def get(self, request, *args, **kwargs):
		logout(request)
		return super(LogOutView, self).get(request, *args, **kwargs)