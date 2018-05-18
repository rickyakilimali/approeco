from django.conf.urls import url
from django.views.generic.base import TemplateView
from .views import MaQuotationView
from quotation import views


urlpatterns = [

			#url(r'^ma-quotation/$', MaQuotationView.as_view(), name='ma-quotation'),
			#url(r'^ma-quotation/$', views.addquotation, name='ma-quotation'),
			url(r'^ma-new-quotation/$', views.addnewquotation, name='ma-quotation'),
			url(r'^ma-new-quotation-simple/$', views.addnewquotationnoattributes, name='ma-quotation-simple'),
]

