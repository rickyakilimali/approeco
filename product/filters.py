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

class FardeFilter(django_filters.FilterSet):
	class Meta:
			model = Farde
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class PorteClefFilter(django_filters.FilterSet):
	class Meta:
			model = PorteClef
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class LaniereFilter(django_filters.FilterSet):
	class Meta:
			model = Laniere
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class CasquetteBlancheFilter(django_filters.FilterSet):
	class Meta:
			model = CasquetteBlanche
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]

class FlyerFilter(django_filters.FilterSet):
	class Meta:
			model = Flyer
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]

class CarnetFilter(django_filters.FilterSet):
	class Meta:
			model = Carnet
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class CachetHumideFilter(django_filters.FilterSet):
	class Meta:
			model = CachetHumide
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class CachetNumeriqueFilter(django_filters.FilterSet):
	class Meta:
			model = CachetNumerique
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]

class CachetImprimeFilter(django_filters.FilterSet):
	class Meta:
			model = CachetImprime
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class CachetSecFilter(django_filters.FilterSet):
	class Meta:
			model = CachetSec
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class GravureFilter(django_filters.FilterSet):
	class Meta:
			model = Gravure
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]



class BoiteCuisiniereFilter(django_filters.FilterSet):
	class Meta:
			model = BoiteCuisiniere
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]

class ClefMoletteFilter(django_filters.FilterSet):
	class Meta:
			model = ClefMolette
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class DisjoncteurFilter(django_filters.FilterSet):
	class Meta:
			model = Disjoncteur
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class InterrupteurDifferentielFilter(django_filters.FilterSet):
	class Meta:
			model = InterrupteurDifferentiel
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]

class FusibleFilter(django_filters.FilterSet):
	class Meta:
			model = Fusible
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]

class EquerreFilter(django_filters.FilterSet):
	class Meta:
			model = Equerre
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]

class SecheMainFilter(django_filters.FilterSet):
	class Meta:
			model = SecheMain
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class MonteChargeFilter(django_filters.FilterSet):
	class Meta:
			model = MonteCharge
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class InterrupteurElectriqueFilter(django_filters.FilterSet):
	class Meta:
			model = InterrupteurElectrique
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


#class InterrupteurElectriqueMoteurFilter(django_filters.FilterSet):
#	class Meta:
#			model = InterrupteurElectriqueMoteur
#			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class PaumelleFilter(django_filters.FilterSet):
	class Meta:
			model = Paumelle
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class GantFilter(django_filters.FilterSet):
	class Meta:
			model = Gant
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class CylindreFilter(django_filters.FilterSet):
	class Meta:
			model = Cylindre
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]

class PalanMecaniqueFilter(django_filters.FilterSet):
	class Meta:
			model = PalanMecanique
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class InverseurFilter(django_filters.FilterSet):
	class Meta:
			model = Inverseur
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class AppareilDeMesureFilter(django_filters.FilterSet):
	class Meta:
			model = AppareilDeMesure
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class PriseElectriqueFilter(django_filters.FilterSet):
	class Meta:
			model = PriseElectrique
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class RallongeFilter(django_filters.FilterSet):
	class Meta:
			model = Rallonge
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class BoiteDerivationFilter(django_filters.FilterSet):
	class Meta:
			model = BoiteDerivation
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class CoffretElectriqueFilter(django_filters.FilterSet):
	class Meta:
			model = CoffretElectrique
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class ContacteurFilter(django_filters.FilterSet):
	class Meta:
			model = Contacteur
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class MecheBetonFilter(django_filters.FilterSet):
	class Meta:
			model = MecheBeton
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]



class OutilsJardinageFilter(django_filters.FilterSet):
	class Meta:
			model = OutilsJardinage
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class BalanceFilter(django_filters.FilterSet):
	class Meta:
			model = Balance
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class TuyauterieFilter(django_filters.FilterSet):
	class Meta:
			model = Tuyauterie
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class AccessoiresHydrophoreFilter(django_filters.FilterSet):
	class Meta:
			model = AccessoiresHydrophore
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class FlexibleFilter(django_filters.FilterSet):
	class Meta:
			model = Flexible
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class SiphonFilter(django_filters.FilterSet):
	class Meta:
			model = Siphon
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class ReductionPvcFilter(django_filters.FilterSet):
	class Meta:
			model = ReductionPvc
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class AmpouleElectriqueFilter(django_filters.FilterSet):
	class Meta:
			model = AmpouleElectrique
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]



class MotoPompeFilter(django_filters.FilterSet):
	class Meta:
			model = MotoPompe
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class ChargeurBatterieFilter(django_filters.FilterSet):
	class Meta:
			model = ChargeurBatterie
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class EnseigneLumineuseFilter(django_filters.FilterSet):
	class Meta:
			model = EnseigneLumineuse
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class PompeHydrophoreFilter(django_filters.FilterSet):
	class Meta:
			model = PompeHydrophore
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]





class PompeForageFilter(django_filters.FilterSet):
	class Meta:
			model = PompeForage
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class PompeEauFilter(django_filters.FilterSet):
	class Meta:
			model = PompeEau
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]



class MachineAtelierNonPortatifFilter(django_filters.FilterSet):
	class Meta:
			model = MachineAtelierNonPortatif
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class MachineAtelierPortatifFilter(django_filters.FilterSet):
	class Meta:
			model = MachineAtelierPortatif
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class GroupeElectrogeneFilter(django_filters.FilterSet):
	class Meta:
			model = GroupeElectrogene
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]





class CompresseurFilter(django_filters.FilterSet):
	class Meta:
			model = Compresseur
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]






class DetecteurIntrusionFilter(django_filters.FilterSet):
	class Meta:
			model = DetecteurIntrusion
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]




class MoteurElectriqueFilter(django_filters.FilterSet):
	class Meta:
			model = MoteurElectrique
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]





class ConvertisseurFilter(django_filters.FilterSet):
	class Meta:
			model = Convertisseur
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]




class ControleAccesEtPointageFilter(django_filters.FilterSet):
	class Meta:
			model = ControleAccesEtPointage
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class EnregistreurCameraSurveillanceFilter(django_filters.FilterSet):
	class Meta:
			model = EnregistreurCameraSurveillance
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class ConseilFilter(django_filters.FilterSet):
	class Meta:
			model = Conseil
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class RedactionDesProceduresFilter(django_filters.FilterSet):
	class Meta:
			model = RedactionDesProcedures
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]



class AssistanceFiscaleFilter(django_filters.FilterSet):
	class Meta:
			model = AssistanceFiscale
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]


class AuditEtControleInterneFilter(django_filters.FilterSet):
	class Meta:
			model = AuditEtControleInterne
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



class CoursAnglaisFilter(django_filters.FilterSet):
	class Meta:
			model = CoursAnglais
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
