from django.conf.urls import url
from django.views.generic.base import TemplateView
from .views import MaQuotationView


urlpatterns = [

			url(r'^ma-quotation/$', MaQuotationView.as_view(), name='ma-quotation'),
]

