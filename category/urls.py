from django.conf.urls import url
from category import views

urlpatterns = [
        url(r'^$', views.index, name='catalogue_index'),
        url(r'^(?P<topcategory>.+)/$', views.category_list, name='topcategory'),
        url(r'^(?P<topcategory>.+)/(?P<subcategory>.+)$', views.category_list, name='subcategory'),
        
        

	]