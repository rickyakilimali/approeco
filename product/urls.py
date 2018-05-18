from django.conf.urls import url
from django.views.generic.base import TemplateView
from .views import MyProductView, EditProductView, ProductUpdateView, productsearch
from product import views


urlpatterns = [

			url(r'^my-product/$', MyProductView.as_view(), name='my-product'),
			url(r'^edit-product/$', EditProductView.as_view(), name='edit-product'),
			url(r'^my_quotation/$', MyProductView.as_view(), name='my-quotation'),

            url(r'^my-product-list/(?P<conttype>[-\w]+)$', views.MyProductListView.as_view(), name='my-product-list'),
            url(r'^my-product-list/update/(?P<model>[-\w]+)/(?P<pk>[-\d]+)/$', views.ProductUpdateView.as_view(), name='my-product-update'),
			#url(r'^search/(?P<model>[-\w]+)/$', views.FilteredProductView.as_view()),
			url(r'^search/(?P<dbmodel>[-\w]+)/$', productsearch),






]

