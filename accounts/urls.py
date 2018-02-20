from django.conf.urls import url
from django.views.generic.base import TemplateView

from .views import BusinessProfileDetailView, BusinessProfileUpdate, BusinessLoginView
from category.views import CategoryProfileListView
from .views import SellerLoginView, BuyerLoginView, LogOutView, ProfilView, ProfileView


urlpatterns = [

			#url(r'^buyer/login/$', BuyerLoginView.as_view(), name='buyer-login'),
			#url(r'^seller/login/$', SellerLoginView.as_view(), name='seller-login'),
			url(r'^profil/$', ProfilView.as_view(), name='profil'),
			#url(r'^logout/$', LogOutView.as_view(), name='logout'),
			url(r'^profile/(?P<pk>[-\d]+)/$', BusinessProfileDetailView.as_view(), name='businessprofile-detail'),
			url(r'^edit/businessprofile/$', BusinessProfileUpdate.as_view(), name='businessprofile-detail'),
			#url(r'^business/login/$', BusinessLoginView.as_view(), name='login'),
			#url(r'^login_success/$', views.login_success, name='login_success')
]

