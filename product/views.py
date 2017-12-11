from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, QueryDict
from .forms import _ProductForm
from .models import *
from .filters import *
from django.contrib.contenttypes.models import ContentType 


from django.core import urlresolvers

from django.contrib.contenttypes.models import ContentType
from django_tables2 import RequestConfig
from .tables import *

from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django.views.generic.list import ListView


# Create your views here.

class MyProductView(TemplateView):
    template_name = 'product/my-product.html'

class EditProductView(TemplateView):
    template_name = 'product/edit-product.html'




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



class FilteredFardeListView(SingleTableMixin, FilterView):
	table_class = FardeTable
	model = Farde
	template_name = 'productfilter.html'
	filterset_class = FardeFilter


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

class FilteredCasquetteBlancheListView(SingleTableMixin, FilterView):
	table_class = CasquetteBlancheTable
	model = CasquetteBlanche
	template_name = 'productfilter.html'
	filterset_class = CasquetteBlancheFilter

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

class FilteredCachetHumideListView(SingleTableMixin, FilterView):
	table_class = CachetHumideTable
	model = CachetHumide
	template_name = 'productfilter.html'
	filterset_class = CachetHumideFilter

class FilteredCachetNumeriqueListView(SingleTableMixin, FilterView):
	table_class = CachetNumeriqueTable
	model = CachetNumerique
	template_name = 'productfilter.html'
	filterset_class = CachetNumeriqueFilter

class FilteredCachetImprimeListView(SingleTableMixin, FilterView):
	table_class = CachetImprimeTable
	model = CachetImprime
	template_name = 'productfilter.html'
	filterset_class = CachetImprimeFilter

class FilteredCachetSecListView(SingleTableMixin, FilterView):
	table_class = CachetSecTable
	model = CachetSec
	template_name = 'productfilter.html'
	filterset_class = CachetSecFilter

class FilteredGravureListView(SingleTableMixin, FilterView):
	table_class = GravureTable
	model = Gravure
	template_name = 'productfilter.html'
	filterset_class = GravureFilter

class FilteredBoiteCuisiniereListView(SingleTableMixin, FilterView):
	table_class = BoiteCuisiniereTable
	model = BoiteCuisiniere
	template_name = 'productfilter.html'
	filterset_class = BoiteCuisiniereFilter

class FilteredClefMoletteListView(SingleTableMixin, FilterView):
	table_class = ClefMoletteTable
	model = ClefMolette
	template_name = 'productfilter.html'
	filterset_class = ClefMoletteFilter

class FilteredDisjoncteurListView(SingleTableMixin, FilterView):
	table_class = DisjoncteurTable
	model = Disjoncteur
	template_name = 'productfilter.html'
	filterset_class = DisjoncteurFilter


class FilteredInterrupteurDifferentielListView(SingleTableMixin, FilterView):
	table_class = InterrupteurDifferentielTable
	model = InterrupteurDifferentiel
	template_name = 'productfilter.html'
	filterset_class = InterrupteurDifferentielFilter

class FilteredFusibleListView(SingleTableMixin, FilterView):
	table_class = FusibleTable
	model = Fusible
	template_name = 'productfilter.html'
	filterset_class = FusibleFilter

class FilteredEquerreListView(SingleTableMixin, FilterView):
	table_class = EquerreTable
	model = Equerre
	template_name = 'productfilter.html'
	filterset_class = EquerreFilter

class FilteredSecheMainListView(SingleTableMixin, FilterView):
	table_class = SecheMainTable
	model = SecheMain
	template_name = 'productfilter.html'
	filterset_class = SecheMainFilter

class FilteredMonteChargeListView(SingleTableMixin, FilterView):
	table_class = MonteChargeTable
	model = MonteCharge
	template_name = 'productfilter.html'
	filterset_class = MonteChargeFilter

class FilteredInterrupteurElectriqueListView(SingleTableMixin, FilterView):
	table_class = InterrupteurElectriqueTable
	model = InterrupteurElectrique
	template_name = 'productfilter.html'
	filterset_class = InterrupteurElectriqueFilter

#class FilteredInterrupteurElectriqueMoteurListView(SingleTableMixin, FilterView):
#	table_class = InterrupteurElectriqueMoteurTable
#	model = InterrupteurElectriqueMoteur
#	template_name = 'productfilter.html'
#	filterset_class = InterrupteurElectriqueMoteurFilter


class FilteredPaumelleListView(SingleTableMixin, FilterView):
	table_class = PaumelleTable
	model = Paumelle
	template_name = 'productfilter.html'
	filterset_class = PaumelleFilter


class FilteredGantListView(SingleTableMixin, FilterView):
	table_class = GantTable
	model = Gant
	template_name = 'productfilter.html'
	filterset_class = GantFilter


class FilteredCylindreListView(SingleTableMixin, FilterView):
	table_class = CylindreTable
	model = Cylindre
	template_name = 'productfilter.html'
	filterset_class = CylindreFilter


class FilteredPalanMecaniqueListView(SingleTableMixin, FilterView):
	table_class = PalanMecaniqueTable
	model = PalanMecanique
	template_name = 'productfilter.html'
	filterset_class = PalanMecaniqueFilter


class FilteredInverseurListView(SingleTableMixin, FilterView):
	table_class = InverseurTable
	model = Inverseur
	template_name = 'productfilter.html'
	filterset_class = InverseurFilter


class FilteredAppareilDeMesureListView(SingleTableMixin, FilterView):
	table_class = AppareilDeMesureTable
	model = AppareilDeMesure
	template_name = 'productfilter.html'
	filterset_class = AppareilDeMesureFilter


class FilteredPriseElectriqueListView(SingleTableMixin, FilterView):
	table_class = PriseElectriqueTable
	model = PriseElectrique
	template_name = 'productfilter.html'
	filterset_class = PriseElectriqueFilter


class FilteredRallongeListView(SingleTableMixin, FilterView):
	table_class = RallongeTable
	model = Rallonge
	template_name = 'productfilter.html'
	filterset_class = RallongeFilter


class FilteredBoiteDerivationListView(SingleTableMixin, FilterView):
	table_class = BoiteDerivationTable
	model = BoiteDerivation
	template_name = 'productfilter.html'
	filterset_class = BoiteDerivationFilter


class FilteredCoffretElectriqueListView(SingleTableMixin, FilterView):
	table_class = CoffretElectriqueTable
	model = CoffretElectrique
	template_name = 'productfilter.html'
	filterset_class = CoffretElectriqueFilter


class FilteredContacteurListView(SingleTableMixin, FilterView):
	table_class = ContacteurTable
	model = Contacteur
	template_name = 'productfilter.html'
	filterset_class = ContacteurFilter


class FilteredMecheBetonListView(SingleTableMixin, FilterView):
	table_class = MecheBetonTable
	model = MecheBeton
	template_name = 'productfilter.html'
	filterset_class = MecheBetonFilter


class FilteredOutilsJardinageListView(SingleTableMixin, FilterView):
	table_class = OutilsJardinageTable
	model = OutilsJardinage
	template_name = 'productfilter.html'
	filterset_class = OutilsJardinageFilter


class FilteredBalanceListView(SingleTableMixin, FilterView):
	table_class = BalanceTable
	model = Balance
	template_name = 'productfilter.html'
	filterset_class = BalanceFilter


class FilteredTuyauterieListView(SingleTableMixin, FilterView):
	table_class = TuyauterieTable
	model = Tuyauterie
	template_name = 'productfilter.html'
	filterset_class = TuyauterieFilter


class FilteredAccessoiresHydrophoreListView(SingleTableMixin, FilterView):
	table_class = AccessoiresHydrophoreTable
	model = AccessoiresHydrophore
	template_name = 'productfilter.html'
	filterset_class = AccessoiresHydrophoreFilter


class FilteredFlexibleListView(SingleTableMixin, FilterView):
	table_class = FlexibleTable
	model = Flexible
	template_name = 'productfilter.html'
	filterset_class = FlexibleFilter



class FilteredSiphonListView(SingleTableMixin, FilterView):
	table_class = SiphonTable
	model = Siphon
	template_name = 'productfilter.html'
	filterset_class = SiphonFilter


class FilteredReductionPvcListView(SingleTableMixin, FilterView):
	table_class = ReductionPvcTable
	model = ReductionPvc
	template_name = 'productfilter.html'
	filterset_class = ReductionPvcFilter


class FilteredAmpouleElectriqueListView(SingleTableMixin, FilterView):
	table_class = AmpouleElectriqueTable
	model = AmpouleElectrique
	template_name = 'productfilter.html'
	filterset_class = AmpouleElectriqueFilter


class FilteredMotoPompeListView(SingleTableMixin, FilterView):
	table_class = MotoPompeTable
	model = MotoPompe
	template_name = 'productfilter.html'
	filterset_class = MotoPompeFilter


class FilteredChargeurBatterieListView(SingleTableMixin, FilterView):
	table_class = ChargeurBatterieTable
	model = ChargeurBatterie
	template_name = 'productfilter.html'
	filterset_class = ChargeurBatterieFilter


class FilteredEnseigneLumineuseListView(SingleTableMixin, FilterView):
	table_class = EnseigneLumineuseTable
	model = EnseigneLumineuse
	template_name = 'productfilter.html'
	filterset_class = EnseigneLumineuseFilter


class FilteredPompeHydrophoreListView(SingleTableMixin, FilterView):
	table_class = PompeHydrophoreTable
	model = PompeHydrophore
	template_name = 'productfilter.html'
	filterset_class = PompeHydrophoreFilter


class FilteredPompeForageListView(SingleTableMixin, FilterView):
	table_class = PompeForageTable
	model = PompeForage
	template_name = 'productfilter.html'
	filterset_class = PompeForageFilter


class FilteredPompeEauListView(SingleTableMixin, FilterView):
	table_class = PompeEauTable
	model = PompeEau
	template_name = 'productfilter.html'
	filterset_class = PompeEauFilter


class FilteredMachineAtelierNonPortatifListView(SingleTableMixin, FilterView):
	table_class = MachineAtelierNonPortatifTable
	model = MachineAtelierNonPortatif
	template_name = 'productfilter.html'
	filterset_class = MachineAtelierNonPortatifFilter


class FilteredMachineAtelierPortatifListView(SingleTableMixin, FilterView):
	table_class = MachineAtelierPortatifTable
	model = MachineAtelierPortatif
	template_name = 'productfilter.html'
	filterset_class = MachineAtelierPortatifFilter


class FilteredGroupeElectrogeneListView(SingleTableMixin, FilterView):
	table_class = GroupeElectrogeneTable
	model = GroupeElectrogene
	template_name = 'productfilter.html'
	filterset_class = GroupeElectrogeneFilter


class FilteredCompresseurListView(SingleTableMixin, FilterView):
	table_class = CompresseurTable
	model = Compresseur
	template_name = 'productfilter.html'
	filterset_class = CompresseurFilter



class FilteredDetecteurIntrusionListView(SingleTableMixin, FilterView):
	table_class = DetecteurIntrusionTable
	model = DetecteurIntrusion
	template_name = 'productfilter.html'
	filterset_class = DetecteurIntrusionFilter


class FilteredMoteurElectriqueListView(SingleTableMixin, FilterView):
	table_class = MoteurElectriqueTable
	model = MoteurElectrique
	template_name = 'productfilter.html'
	filterset_class = MoteurElectriqueFilter

class FilteredConvertisseurListView(SingleTableMixin, FilterView):
	table_class = ConvertisseurTable
	model = Convertisseur
	template_name = 'productfilter.html'
	filterset_class = ConvertisseurFilter



class FilteredControleAccesEtPointageListView(SingleTableMixin, FilterView):
	table_class = ControleAccesEtPointageTable
	model = ControleAccesEtPointage
	template_name = 'productfilter.html'
	filterset_class = ControleAccesEtPointageFilter


class FilteredEnregistreurCameraSurveillanceListView(SingleTableMixin, FilterView):
	table_class = EnregistreurCameraSurveillanceTable
	model = EnregistreurCameraSurveillance
	template_name = 'productfilter.html'
	filterset_class = EnregistreurCameraSurveillanceFilter


class FilteredConseilListView(SingleTableMixin, FilterView):
	table_class = ConseilTable
	model = Conseil
	template_name = 'productfilter.html'
	filterset_class = ConseilFilter



class FilteredRedactionDesProceduresListView(SingleTableMixin, FilterView):
	table_class = RedactionDesProceduresTable
	model = RedactionDesProcedures
	template_name = 'productfilter.html'
	filterset_class = RedactionDesProceduresFilter



class FilteredAssistanceFiscaleListView(SingleTableMixin, FilterView):
	table_class = AssistanceFiscaleTable
	model = AssistanceFiscale
	template_name = 'productfilter.html'
	filterset_class = AssistanceFiscaleFilter


class FilteredAuditEtControleInterneListView(SingleTableMixin, FilterView):
	table_class = AuditEtControleInterneTable
	model = AuditEtControleInterne
	template_name = 'productfilter.html'
	filterset_class = AuditEtControleInterneFilter


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



class FilteredCoursAnglaisListView(SingleTableMixin, FilterView):
	table_class = CoursAnglaisTable
	model = CoursAnglais
	template_name = 'productfilter.html'
	filterset_class = CoursAnglaisFilter


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


	


										
