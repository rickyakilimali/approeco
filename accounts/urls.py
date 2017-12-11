from django.conf.urls import url
from django.views.generic.base import TemplateView
from .views import BusinessProfileDetailView
from category.views import CategoryProfileListView
from .views import LoginView, LogOutView, ProfilView


urlpatterns = [

			url(r'^login/$', LoginView.as_view(), name='login'),
			url(r'^profil/$', ProfilView.as_view(), name='profil'),
			url(r'^logout/$', LogOutView.as_view(), name='logout'),
]

