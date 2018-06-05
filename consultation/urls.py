from django.conf.urls import url
from consultation import views


urlpatterns = [
		url(r'^category/$', views.index, name='consultation_index'),
        url(r'^category/(?P<hierarchy>.+)/$', views.show_category, name='category'),
		url(r'^add/$', views.add, name='add_product'),
		url(r'^remove/$', views.remove, name='remove_product'),
        url(r'^submitcart/$', views.submit, name='submit_cart'),





	]