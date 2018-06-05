from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView
from django.http import HttpResponse, QueryDict
from .forms import _ProductForm
from django.forms import modelform_factory
from .models import *
#from .filters import *
from django.contrib.contenttypes.models import ContentType
from category.models import *
from django.urls import reverse


from django.core import urlresolvers

from django.contrib.contenttypes.models import ContentType
from django_tables2 import RequestConfig
#from .tables import *

from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin, SingleTableView
from django.views.generic.list import ListView
from django_filters.filterset import *
from django_tables2.tables import *
from django.contrib.auth.decorators import user_passes_test
from utils.autorisation import acheteur_check
from django.contrib.auth.mixins import UserPassesTestMixin



# Create your views here.

ALL_FIELDS=['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]
ALL_FIELDS_TABLE= ('id','category','polymorphic_ctype','is_active','productbase_ptr',)
ALL_FIELDS_FORM = ('nom', 'prix',)

def productformclass_factory(modele, fields=ALL_FIELDS_FORM):
    the_model = ContentType.objects.get(app_label="product", model=modele).model_class()
    meta = type(str('Meta'), (object,), {'model': the_model, 'fields':fields})

    form_class = type(str('%sForm' %the_model._meta.object_name),(forms.ModelForm,), {'Meta':meta})

def productfilterset_factory(modele, exclude=ALL_FIELDS):
	the_model = ContentType.objects.get(app_label="product", model=modele).model_class()
	meta = type(str('Meta'), (object,), {'model': the_model, 'exclude': exclude})

	filterset = type(str('%sFilterSet' %the_model._meta.object_name),(FilterSet,), {'Meta': meta})
	return filterset


def producttable_factory(modele, exclude=ALL_FIELDS_TABLE):
	the_model = ContentType.objects.get(app_label="product", model=modele).model_class()
	meta = type(str('Meta'), (object,), {'model': the_model, 'exclude': exclude})

	table_class = type(str('%sTable' %the_model._meta.object_name),(ProductTable,), {'Meta': meta})
	return table_class


def producttable_factory_withoutlink(modele, exclude=ALL_FIELDS_TABLE):
	the_model = ContentType.objects.get(app_label="product", model=modele).model_class()
	meta = type(str('Meta'), (object,), {'model': the_model, 'exclude': exclude})

	table_class = type(str('%sTable' %the_model._meta.object_name),(Table,), {'Meta': meta})
	return table_class



class FilteredProductView(SingleTableMixin, FilterView):
	#table_class = LaptopTable
	model = Laptop
	template_name = 'productfilter.html'



	def get_filterset_class(self):
		"""
		Returns the filterset class to use in this view
		"""
		the_model = self.kwargs['model']
		return productfilterset_factory(modele=the_model)

	def get_table_class(self):
		'''
		Return the class to use for the table.
		'''
		the_model = self.kwargs['model']
		return producttable_factory(modele=the_model)

		#if self.table_class:
		#    return self.table_class
		#klass = type(self).__name__
		#raise ImproperlyConfigured('A table class was not specified. Define {}.table_class'.format(klass))


	def get_context_data(self, **kwargs):
		context = super(FilteredProductView, self).get_context_data(**kwargs)
		context['model'] = self.kwargs['model']
		context['criteria2'] = {k: v for k, v in self.request.GET.items() if v}
		context['products']=''
		context['product_type']=ProductType.objects.get(product_model=ContentType.objects.get(app_label="product", model=self.kwargs['model']))
		return context

	def get_queryset(self):
		product_db=ContentType.objects.get(app_label="product", model=self.kwargs['model']).model_class()


		return product_db.objects.all()




class MyProductView(UserPassesTestMixin,TemplateView):
    template_name = 'product/my-product.html'

    def test_func(self):
        return self.request.user.groups.filter(name='vendeurs').exists()

    def get_context_data(self, **kwargs):
        context = super(MyProductView, self).get_context_data(**kwargs)

        les_produits = ContentType.objects.filter(app_label="product")

        #recupere les content-type où le vendeur a des produits
        search_producttype=[]
        for dbtable in les_produits:
	        if dbtable.model_class().objects.filter(vendeur__username=self.request.user.username):
	            search_producttype.append(dbtable)


        #recupere les product-type où le vendeur a des produits
        producttype_list=[]
        for pt in search_producttype:
            type_produit=ProductType.objects.get(product_model=pt)
            producttype_list.append(type_produit)

        context['mes_produits'] = producttype_list
        return context


class MyProductListView(UserPassesTestMixin,SingleTableMixin, ListView):

    template_name = 'product/my-product-list.html'
    context_object_name = 'mes_produits_model'

    def test_func(self):
        return self.request.user.groups.filter(name='vendeurs').exists()

    def get_table_class(self):
        the_model = self.kwargs['conttype']
        return producttable_factory_withoutlink(modele=the_model)




    def get_queryset(self):

    	#recupere l'instance de Content Type representé par le parametre nommé de l'url, ensuite recupere la classe

        ctype = ContentType.objects.get(app_label="product", model=self.kwargs['conttype']).model_class()

        #crée le queryset à renvoyer

        return ctype.objects.filter(vendeur__username=self.request.user.username)


class ProductUpdateView(UserPassesTestMixin,UpdateView):

    template_name = 'product/update.html'

    def test_func(self):
        return self.request.user.groups.filter(name='vendeurs').exists()

    def get_success_url(self):
        the_model = self.kwargs['model']
        return reverse('my-product-list', kwargs={'conttype':the_model})

    def get_form_class(self):
        ctype = ContentType.objects.get(app_label="product", model=self.kwargs['model']).model_class()
        ProductForm = modelform_factory(ctype, fields=('prix',))
        return ProductForm

    def get_queryset(self):
        ctype = ContentType.objects.get(app_label="product", model=self.kwargs['model']).model_class()

        return ctype.objects.filter(pk=self.kwargs['pk'])

class EditProductView(UserPassesTestMixin,TemplateView):
    template_name = 'product/edit-product.html'

    def test_func(self):
        return self.request.user.groups.filter(name='vendeurs').exists()


def extractfields(classmodel):
	all_fields= classmodel._meta.get_fields(include_parents=False, include_hidden=False)
	attribute_fields = all_fields[5:len(all_fields)]
	product_fields = []
	for field in attribute_fields:
		product_fields.append(field.name)

	return product_fields

def extractfields_verbose_name(classmodel):
	all_fields= classmodel._meta.get_fields(include_parents=False, include_hidden=False)
	attribute_fields = all_fields[5:len(all_fields)]
	product_fields_verbose_name = []
	for field in attribute_fields:
		product_fields_verbose_name.append(field.verbose_name)

	return product_fields_verbose_name

@user_passes_test(acheteur_check,login_url='login')
def productsearch(request, dbmodel):
	product_list = ContentType.objects.get(app_label="product", model=dbmodel).model_class().objects.all()
	ProductFilter = productfilterset_factory(dbmodel)
	product_filter = ProductFilter(request.GET, queryset=product_list)
	productfields=extractfields(ContentType.objects.get(app_label="product", model=dbmodel).model_class())
	productfields_verbose=extractfields_verbose_name(ContentType.objects.get(app_label="product", model=dbmodel).model_class())
   #--------------------------------------------------------#


   #--------------------------------------------------------#
	product_type = ProductType.objects.get(product_model=ContentType.objects.get(app_label="product", model=dbmodel))
	criteria2 = {k: v for k, v in request.GET.items() if v}



	if len(productfields)>2:
		return render(request, 'product/product-filter-list.html', {'filter': product_filter,'fields_verbose_name':productfields_verbose  ,'fields':productfields, 'criteria2':criteria2, 'product_type':product_type, 'model':dbmodel,})

	else:
		return render(request, 'product/product-filter-list-without-attributes.html', {'product_list':product_list,'fields_verbose_name':productfields_verbose  ,'fields':productfields, 'product_type':product_type, 'model':dbmodel})



#--------------------------------------------------------#
#--------------------------------------------------------#






