from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView
from django.http import HttpResponse, QueryDict
from .forms import _ProductForm
from django.forms import modelform_factory
from .models import *
from .filters import *
from django.contrib.contenttypes.models import ContentType
from category.models import *
from django.urls import reverse


from django.core import urlresolvers

from django.contrib.contenttypes.models import ContentType
from django_tables2 import RequestConfig
from .tables import *

from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin, SingleTableView
from django.views.generic.list import ListView
from django_filters.filterset import *
from django_tables2.tables import *


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
		return context

	def get_queryset(self):
		product_db=ContentType.objects.get(app_label="product", model=self.kwargs['model']).model_class()
		return product_db.objects.all()


class MyProductView(TemplateView):
    template_name = 'product/my-product.html'

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


class MyProductListView(SingleTableMixin, ListView):

    template_name = 'product/my-product-list.html'
    context_object_name = 'mes_produits_model'

    def get_table_class(self):
        the_model = self.kwargs['conttype']
        return producttable_factory_withoutlink(modele=the_model)




    def get_queryset(self):

    	#recupere l'instance de Content Type representé par le parametre nommé de l'url, ensuite recupere la classe

        ctype = ContentType.objects.get(app_label="product", model=self.kwargs['conttype']).model_class()

        #crée le queryset à renvoyer

        return ctype.objects.filter(vendeur__username=self.request.user.username)


class ProductUpdateView(UpdateView):

    template_name = 'product/update.html'

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

class EditProductView(TemplateView):
    template_name = 'product/edit-product.html'

#--------------------------------------------------------#
#--------------------------------------------------------#


class FilteredLaptopListView(SingleTableMixin, FilterView):
	table_class = LaptopTable
	model = Laptop
	template_name = 'productfilter.html'
	filterset_class = LaptopFilter

class FilteredDesktopListView(SingleTableMixin, FilterView):
	table_class = DesktopTable
	model = Desktop
	template_name = 'productfilter.html'
	filterset_class = DesktopFilter

class FilteredImprimanteListView(SingleTableMixin, FilterView):
	table_class = ImprimanteTable
	model = Imprimante
	template_name = 'productfilter.html'
	filterset_class = ImprimanteFilter


class FilteredSiegeEtFauteuilDeBureauListView(SingleTableMixin, FilterView):
	table_class = SiegeEtFauteuilDeBureauTable
	model = SiegeEtFauteuilDeBureau
	template_name = 'productfilter.html'
	filterset_class = SiegeEtFauteuilDeBureauFilter


class FilteredArmoireListView(SingleTableMixin, FilterView):
	table_class = ArmoireTable
	model = Armoire
	template_name = 'productfilter.html'
	filterset_class = ArmoireFilter

class FilteredPieceDeRechangeRefroidissementListView(SingleTableMixin, FilterView):
	table_class = PieceDeRechangeRefroidissementTable
	model = PieceDeRechangeRefroidissement
	template_name = 'productfilter.html'
	filterset_class = PieceDeRechangeRefroidissementFilter


class FilteredPieceDeRechangeDirectionSuspensionListView(SingleTableMixin, FilterView):
	table_class = PieceDeRechangeDirectionSuspensionTable
	model = PieceDeRechangeDirectionSuspension
	template_name = 'productfilter.html'
	filterset_class = PieceDeRechangeDirectionSuspensionFilter

class FilteredPieceDeRechangeTransmissionListView(SingleTableMixin, FilterView):
	table_class = PieceDeRechangeTransmissionTable
	model = PieceDeRechangeTransmission
	template_name = 'productfilter.html'
	filterset_class = PieceDeRechangeTransmissionFilter

class FilteredPieceDeRechangeCarrosserieListView(SingleTableMixin, FilterView):
	table_class = PieceDeRechangeCarrosserieTable
	model = PieceDeRechangeCarrosserie
	template_name = 'productfilter.html'
	filterset_class = PieceDeRechangeCarrosserieFilter

class FilteredPieceDeRechangeElectriqueListView(SingleTableMixin, FilterView):
	table_class = PieceDeRechangeElectriqueTable
	model = PieceDeRechangeElectrique
	template_name = 'productfilter.html'
	filterset_class = PieceDeRechangeElectriqueFilter

class FilteredPieceDeRechangeEmbrayageListView(SingleTableMixin, FilterView):
	table_class = PieceDeRechangeEmbrayageTable
	model = PieceDeRechangeEmbrayage
	template_name = 'productfilter.html'
	filterset_class = PieceDeRechangeEmbrayageFilter

class FilteredPieceDeRechangeFreinageListView(SingleTableMixin, FilterView):
	table_class = PieceDeRechangeFreinageTable
	model = PieceDeRechangeFreinage
	template_name = 'productfilter.html'
	filterset_class = PieceDeRechangeFreinageFilter

class FilteredPieceRevisionMoteurListView(SingleTableMixin, FilterView):
	table_class = PieceRevisionMoteurTable
	model = PieceRevisionMoteur
	template_name = 'productfilter.html'
	filterset_class = PieceRevisionMoteurFilter

class FilteredPieceRechangeMoteurListView(SingleTableMixin, FilterView):
	table_class = PieceRechangeMoteurTable
	model = PieceRechangeMoteur
	template_name = 'productfilter.html'
	filterset_class = PieceRechangeMoteurFilter


class FilteredCarteServiceListView(SingleTableMixin, FilterView):
	table_class = CarteServiceTable
	model = CarteService
	template_name = 'productfilter.html'
	filterset_class = CarteServiceFilter

class FilteredCarteVisiteListView(SingleTableMixin, FilterView):
	table_class = CarteVisiteTable
	model = CarteVisite
	template_name = 'productfilter.html'
	filterset_class = CarteVisiteFilter

class FilteredShoppingBagListView(SingleTableMixin, FilterView):
	table_class = ShoppingBagTable
	model = ShoppingBag
	template_name = 'productfilter.html'
	filterset_class = ShoppingBagFilter


class FilteredStyloListView(SingleTableMixin, FilterView):
	table_class = StyloTable
	model = Stylo
	template_name = 'productfilter.html'
	filterset_class = StyloFilter

class FilteredTShirtBlancListView(SingleTableMixin, FilterView):
	table_class = TShirtBlancTable
	model = TShirtBlanc
	template_name = 'productfilter.html'
	filterset_class = TShirtBlancFilter


class FilteredTShirtListView(SingleTableMixin, FilterView):
	table_class = TShirtTable
	model = TShirt
	template_name = 'productfilter.html'
	filterset_class = TShirtFilter

class FilteredDepliantListView(SingleTableMixin, FilterView):
	table_class = DepliantTable
	model = Depliant
	template_name = 'productfilter.html'
	filterset_class = DepliantFilter


class FilteredPinsListView(SingleTableMixin, FilterView):
	table_class = PinsTable
	model = Pins
	template_name = 'productfilter.html'
	filterset_class = PinsFilter

class FilteredAfficheListView(SingleTableMixin, FilterView):
	table_class = AfficheTable
	model = Affiche
	template_name = 'productfilter.html'
	filterset_class = AfficheFilter





class FilteredPorteClefListView(SingleTableMixin, FilterView):
	table_class = PorteClefTable
	model = PorteClef
	template_name = 'productfilter.html'
	filterset_class = PorteClefFilter


class FilteredLaniereListView(SingleTableMixin, FilterView):
	table_class = LaniereTable
	model = Laniere
	template_name = 'productfilter.html'
	filterset_class = LaniereFilter



class FilteredFlyerListView(SingleTableMixin, FilterView):
	table_class = FlyerTable
	model = Flyer
	template_name = 'productfilter.html'
	filterset_class = FlyerFilter

class FilteredCarnetListView(SingleTableMixin, FilterView):
	table_class = CarnetTable
	model = Carnet
	template_name = 'productfilter.html'
	filterset_class = CarnetFilter


class FilteredGravureListView(SingleTableMixin, FilterView):
	table_class = GravureTable
	model = Gravure
	template_name = 'productfilter.html'
	filterset_class = GravureFilter




class FilteredConseilListView(SingleTableMixin, FilterView):
	table_class = ConseilTable
	model = Conseil
	template_name = 'productfilter.html'
	filterset_class = ConseilFilter







class FilteredAssistanceFiscaleListView(SingleTableMixin, FilterView):
	table_class = AssistanceFiscaleTable
	model = AssistanceFiscale
	template_name = 'productfilter.html'
	filterset_class = AssistanceFiscaleFilter




class FilteredAssistanceComptableListView(SingleTableMixin, FilterView):
	table_class = AssistanceComptableTable
	model = AssistanceComptable
	template_name = 'productfilter.html'
	filterset_class = AssistanceComptableFilter


class FilteredAuditFinancierListView(SingleTableMixin, FilterView):
	table_class = AuditFinancierTable
	model = AuditFinancier
	template_name = 'productfilter.html'
	filterset_class = AuditFinancierFilter


class FilteredServiceTraiteurListView(SingleTableMixin, FilterView):
	table_class = ServiceTraiteurTable
	model = ServiceTraiteur
	template_name = 'productfilter.html'
	filterset_class = ServiceTraiteurFilter


class FilteredServiceNettoyageListView(SingleTableMixin, FilterView):
	table_class = ServiceNettoyageTable
	model = ServiceNettoyage
	template_name = 'productfilter.html'
	filterset_class = ServiceNettoyageFilter






class FilteredInterpretariatListView(SingleTableMixin, FilterView):
	table_class = InterpretariatTable
	model = Interpretariat
	template_name = 'productfilter.html'
	filterset_class = InterpretariatFilter


class FilteredServiceDeTraductionListView(SingleTableMixin, FilterView):
	table_class = ServiceDeTraductionTable
	model = ServiceDeTraduction
	template_name = 'productfilter.html'
	filterset_class = ServiceDeTraductionFilter






