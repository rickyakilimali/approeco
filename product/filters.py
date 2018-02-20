from .models import *
import django_filters




class LaptopFilter(django_filters.FilterSet):
	class Meta:
			model = Laptop
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class DesktopFilter(django_filters.FilterSet):
	class Meta:
			model = Desktop
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class ImprimanteFilter(django_filters.FilterSet):
	class Meta:
			model = Imprimante
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]



class SiegeEtFauteuilDeBureauFilter(django_filters.FilterSet):
	class Meta:
			model = SiegeEtFauteuilDeBureau
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class ArmoireFilter(django_filters.FilterSet):
	class Meta:
			model = Armoire
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]



class PieceDeRechangeRefroidissementFilter(django_filters.FilterSet):
	class Meta:
			model = PieceDeRechangeRefroidissement
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class PieceDeRechangeDirectionSuspensionFilter(django_filters.FilterSet):
	class Meta:
			model = PieceDeRechangeDirectionSuspension
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class PieceDeRechangeTransmissionFilter(django_filters.FilterSet):
	class Meta:
			model = PieceDeRechangeTransmission
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class PieceDeRechangeCarrosserieFilter(django_filters.FilterSet):
	class Meta:
			model = PieceDeRechangeCarrosserie
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]




class PieceDeRechangeElectriqueFilter(django_filters.FilterSet):
	class Meta:
			model = PieceDeRechangeElectrique
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]



class PieceDeRechangeEmbrayageFilter(django_filters.FilterSet):
	class Meta:
			model = PieceDeRechangeEmbrayage
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class PieceDeRechangeFreinageFilter(django_filters.FilterSet):
	class Meta:
			model = PieceDeRechangeFreinage
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class PieceRevisionMoteurFilter(django_filters.FilterSet):
	class Meta:
			model = PieceRevisionMoteur
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class PieceRechangeMoteurFilter(django_filters.FilterSet):
	class Meta:
			model = PieceRechangeMoteur
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]








class CarteServiceFilter(django_filters.FilterSet):
	class Meta:
			model = CarteService
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]

class CarteVisiteFilter(django_filters.FilterSet):
	class Meta:
			model = CarteVisite
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]




class ShoppingBagFilter(django_filters.FilterSet):
	class Meta:
			model = ShoppingBag
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]

class StyloFilter(django_filters.FilterSet):
	class Meta:
			model = Stylo
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]

class TShirtBlancFilter(django_filters.FilterSet):
	class Meta:
			model = TShirtBlanc
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class TShirtFilter(django_filters.FilterSet):
	class Meta:
			model = TShirt
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]

class DepliantFilter(django_filters.FilterSet):
	class Meta:
			model = Depliant
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class PinsFilter(django_filters.FilterSet):
	class Meta:
			model = Pins
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class AfficheFilter(django_filters.FilterSet):
	class Meta:
			model = Affiche
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]



class PorteClefFilter(django_filters.FilterSet):
	class Meta:
			model = PorteClef
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class LaniereFilter(django_filters.FilterSet):
	class Meta:
			model = Laniere
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]



class FlyerFilter(django_filters.FilterSet):
	class Meta:
			model = Flyer
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]

class CarnetFilter(django_filters.FilterSet):
	class Meta:
			model = Carnet
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]




class GravureFilter(django_filters.FilterSet):
	class Meta:
			model = Gravure
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]





class ConseilFilter(django_filters.FilterSet):
	class Meta:
			model = Conseil
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]





class AssistanceFiscaleFilter(django_filters.FilterSet):
	class Meta:
			model = AssistanceFiscale
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]




class AssistanceComptableFilter(django_filters.FilterSet):
	class Meta:
			model = AssistanceComptable
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class AuditFinancierFilter(django_filters.FilterSet):
	class Meta:
			model = AuditFinancier
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class ServiceTraiteurFilter(django_filters.FilterSet):
	class Meta:
			model = ServiceTraiteur
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class ServiceNettoyageFilter(django_filters.FilterSet):
	class Meta:
			model = ServiceNettoyage
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]





class InterpretariatFilter(django_filters.FilterSet):
	class Meta:
			model = Interpretariat
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]



class ServiceDeTraductionFilter(django_filters.FilterSet):
	class Meta:
			model = ServiceDeTraduction
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]








def get_product_filter(product_model,criteria, queryset):


	class _ProductFilter(django_filters.FilterSet):
		class Meta:
			model = product_model
			exclude = ['nom','vendeur','prix','is_active','category','is_available','units',]

	return 	_ProductFilter(criteria, queryset)
