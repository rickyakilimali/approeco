from django.conf.urls import url
from category import views

urlpatterns = [
        url(r'^$', views.index, name='catalogue_index'),
        url(r'^search_product_type/$', views.search_product_type, name='search_suggestion'),
        #url(r'^fournitures-de-bureau-et-papeterie/$', views.papeterie_wizard, name='papeterie'),
        url(r'^search_product_results/$', views.search_product_list_view, name='product_search_list_view'),
        url(r'^(?P<topcategory>.+)/$', views.category_list, name='topcategory'),
        url(r'^(?P<topcategory>.+)/(?P<subcategory>.+)$', views.category_list, name='subcategory'),




	]