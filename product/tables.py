# tutorial/tables.py
import django_tables2 as tables
from django_tables2.utils import A
from .models import *

class ProductTable(tables.Table):
	vendeur = tables.LinkColumn('businessprofile-detail', args=[A('vendeur.pk')], attrs={'a': {'target': '_blank'}})


class LaptopTable(tables.Table):
	class Meta:
		model = Laptop
		exclude = exclude = ('id','category','polymorphic_ctype','is_active','productbase_ptr',)





class DesktopTable(tables.Table):
	class Meta:
		model = Desktop
		exclude = exclude = ('id','category','is_active','productbase_ptr',)

class ImprimanteTable(tables.Table):
	class Meta:
		model = Imprimante
		exclude = exclude = ('id','category','is_active','productbase_ptr',)

class SiegeEtFauteuilDeBureauTable(tables.Table):
	class Meta:
		model = SiegeEtFauteuilDeBureau
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class ArmoireTable(tables.Table):
	class Meta:
		model = Armoire
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class PieceDeRechangeRefroidissementTable(tables.Table):
	class Meta:
		model = PieceDeRechangeRefroidissement
		exclude = exclude = ('id','category','is_active','productbase_ptr',)



class PieceDeRechangeDirectionSuspensionTable(tables.Table):
	class Meta:
		model = PieceDeRechangeDirectionSuspension
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class PieceDeRechangeTransmissionTable(tables.Table):
	class Meta:
		model = PieceDeRechangeTransmission
		exclude = exclude = ('id','category','is_active','productbase_ptr',)



class PieceDeRechangeCarrosserieTable(tables.Table):
	class Meta:
		model = PieceDeRechangeCarrosserie
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class PieceDeRechangeElectriqueTable(tables.Table):
	class Meta:
		model = PieceDeRechangeElectrique
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class PieceDeRechangeEmbrayageTable(tables.Table):
	class Meta:
		model = PieceDeRechangeEmbrayage
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class PieceDeRechangeFreinageTable(tables.Table):
	class Meta:
		model = PieceDeRechangeFreinage
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class PieceRevisionMoteurTable(tables.Table):
	class Meta:
		model = PieceRevisionMoteur
		exclude = exclude = ('id','category','is_active','productbase_ptr',)

class PieceRechangeMoteurTable(tables.Table):
	class Meta:
		model = PieceRechangeMoteur
		exclude = exclude = ('id','category','is_active','productbase_ptr',)






class CarteServiceTable(tables.Table):
	class Meta:
		model = CarteService
		exclude = exclude = ('id','category','is_active','productbase_ptr',)






class CarteVisiteTable(tables.Table):
	class Meta:
		model = CarteVisite
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class ShoppingBagTable(tables.Table):
	class Meta:
		model = ShoppingBag
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class StyloTable(tables.Table):
	class Meta:
		model = Stylo
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class TShirtBlancTable(tables.Table):
	class Meta:
		model = TShirtBlanc
		exclude = exclude = ('id','category','is_active','productbase_ptr',)

class TShirtTable(tables.Table):
	class Meta:
		model = TShirt
		exclude = exclude = ('id','category','is_active','productbase_ptr',)

class DepliantTable(tables.Table):
	class Meta:
		model = Depliant
		exclude = exclude = ('id','category','is_active','productbase_ptr',)

class PinsTable(tables.Table):
	class Meta:
		model = Pins
		exclude = exclude = ('id','category','is_active','productbase_ptr',)

class AfficheTable(tables.Table):
	class Meta:
		model = Affiche
		exclude = exclude = ('id','category','is_active','productbase_ptr',)



class PorteClefTable(tables.Table):
	class Meta:
		model = PorteClef
		exclude = exclude = ('id','category','is_active','productbase_ptr',)



class LaniereTable(tables.Table):
	class Meta:
		model = Laniere
		exclude = exclude = ('id','category','is_active','productbase_ptr',)




class FlyerTable(tables.Table):
	class Meta:
		model = Flyer
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class CarnetTable(tables.Table):
	class Meta:
		model = Carnet
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class GravureTable(tables.Table):
	class Meta:
		model = Gravure
		exclude = exclude = ('id','category','is_active','productbase_ptr',)




class ConseilTable(tables.Table):
	class Meta:
		model = Conseil
		exclude = exclude = ('id','category','is_active','productbase_ptr',)




class AssistanceFiscaleTable(tables.Table):
	class Meta:
		model = AssistanceFiscale
		exclude = exclude = ('id','category','is_active','productbase_ptr',)





class AssistanceComptableTable(tables.Table):
	class Meta:
		model = AssistanceComptable
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class AuditFinancierTable(tables.Table):
	class Meta:
		model = AuditFinancier
		exclude = exclude = ('id','category','is_active','productbase_ptr',)

class ServiceTraiteurTable(tables.Table):
	class Meta:
		model = ServiceTraiteur
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class ServiceNettoyageTable(tables.Table):
	class Meta:
		model = ServiceNettoyage
		exclude = exclude = ('id','category','is_active','productbase_ptr',)




class InterpretariatTable(tables.Table):
	class Meta:
		model = Interpretariat
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class ServiceDeTraductionTable(tables.Table):
	class Meta:
		model = ServiceDeTraduction
		exclude = exclude = ('id','category','is_active','productbase_ptr',)




