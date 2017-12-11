# tutorial/tables.py
import django_tables2 as tables
from .models import *

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


class FardeTable(tables.Table):
	class Meta:
		model = Farde
		exclude = exclude = ('id','category','is_active','productbase_ptr',)

class PorteClefTable(tables.Table):
	class Meta:
		model = PorteClef
		exclude = exclude = ('id','category','is_active','productbase_ptr',)



class LaniereTable(tables.Table):
	class Meta:
		model = Laniere
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class CasquetteBlancheTable(tables.Table):
	class Meta:
		model = CasquetteBlanche
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class FlyerTable(tables.Table):
	class Meta:
		model = Flyer
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class CarnetTable(tables.Table):
	class Meta:
		model = Carnet
		exclude = exclude = ('id','category','is_active','productbase_ptr',)

class CachetHumideTable(tables.Table):
	class Meta:
		model = CachetHumide
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class CachetNumeriqueTable(tables.Table):
	class Meta:
		model = CachetNumerique
		exclude = exclude = ('id','category','is_active','productbase_ptr',)

class CachetImprimeTable(tables.Table):
	class Meta:
		model = CachetImprime
		exclude = exclude = ('id','category','is_active','productbase_ptr',)

class CachetSecTable(tables.Table):
	class Meta:
		model = CachetSec
		exclude = exclude = ('id','category','is_active','productbase_ptr',)

class GravureTable(tables.Table):
	class Meta:
		model = Gravure
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class BoiteCuisiniereTable(tables.Table):
	class Meta:
		model = BoiteCuisiniere
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class ClefMoletteTable(tables.Table):
	class Meta:
		model = ClefMolette
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class DisjoncteurTable(tables.Table):
	class Meta:
		model = Disjoncteur
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class InterrupteurDifferentielTable(tables.Table):
	class Meta:
		model = InterrupteurDifferentiel
		exclude = exclude = ('id','category','is_active','productbase_ptr',)

class FusibleTable(tables.Table):
	class Meta:
		model = Fusible
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class EquerreTable(tables.Table):
	class Meta:
		model = Equerre
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class SecheMainTable(tables.Table):
	class Meta:
		model = SecheMain
		exclude = exclude = ('id','category','is_active','productbase_ptr',)

class MonteChargeTable(tables.Table):
	class Meta:
		model = MonteCharge
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class InterrupteurElectriqueTable(tables.Table):
	class Meta:
		model = InterrupteurElectrique
		exclude = exclude = ('id','category','is_active','productbase_ptr',)

#class InterrupteurElectriqueMoteurTable(tables.Table):
#	class Meta:
#		model = InterrupteurElectriqueMoteur
#		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class PaumelleTable(tables.Table):
	class Meta:
		model = Paumelle
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class GantTable(tables.Table):
	class Meta:
		model = Gant
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class CylindreTable(tables.Table):
	class Meta:
		model = Cylindre
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class PalanMecaniqueTable(tables.Table):
	class Meta:
		model = PalanMecanique
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class InverseurTable(tables.Table):
	class Meta:
		model = Inverseur
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class AppareilDeMesureTable(tables.Table):
	class Meta:
		model = AppareilDeMesure
		exclude = exclude = ('id','category','is_active','productbase_ptr',)



class PriseElectriqueTable(tables.Table):
	class Meta:
		model = PriseElectrique
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class RallongeTable(tables.Table):
	class Meta:
		model = Rallonge
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class BoiteDerivationTable(tables.Table):
	class Meta:
		model = BoiteDerivation
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class CoffretElectriqueTable(tables.Table):
	class Meta:
		model = CoffretElectrique
		exclude = exclude = ('id','category','is_active','productbase_ptr',)

class ContacteurTable(tables.Table):
	class Meta:
		model = Contacteur
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class MecheBetonTable(tables.Table):
	class Meta:
		model = MecheBeton
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class OutilsJardinageTable(tables.Table):
	class Meta:
		model = OutilsJardinage
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class BalanceTable(tables.Table):
	class Meta:
		model = Balance
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class TuyauterieTable(tables.Table):
	class Meta:
		model = Tuyauterie
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class AccessoiresHydrophoreTable(tables.Table):
	class Meta:
		model = AccessoiresHydrophore
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class FlexibleTable(tables.Table):
	class Meta:
		model = Flexible
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class SiphonTable(tables.Table):
	class Meta:
		model = Siphon
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class ReductionPvcTable(tables.Table):
	class Meta:
		model = ReductionPvc
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class AmpouleElectriqueTable(tables.Table):
	class Meta:
		model = AmpouleElectrique
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class MotoPompeTable(tables.Table):
	class Meta:
		model = MotoPompe
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class ChargeurBatterieTable(tables.Table):
	class Meta:
		model = ChargeurBatterie
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class EnseigneLumineuseTable(tables.Table):
	class Meta:
		model = EnseigneLumineuse
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class PompeHydrophoreTable(tables.Table):
	class Meta:
		model = PompeHydrophore
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class PompeForageTable(tables.Table):
	class Meta:
		model = PompeForage
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class PompeEauTable(tables.Table):
	class Meta:
		model = PompeEau
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class MachineAtelierNonPortatifTable(tables.Table):
	class Meta:
		model = MachineAtelierNonPortatif
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class MachineAtelierPortatifTable(tables.Table):
	class Meta:
		model = MachineAtelierPortatif
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class GroupeElectrogeneTable(tables.Table):
	class Meta:
		model = GroupeElectrogene
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class CompresseurTable(tables.Table):
	class Meta:
		model = Compresseur
		exclude = exclude = ('id','category','is_active','productbase_ptr',)



class DetecteurIntrusionTable(tables.Table):
	class Meta:
		model = DetecteurIntrusion
		exclude = exclude = ('id','category','is_active','productbase_ptr',)



class MoteurElectriqueTable(tables.Table):
	class Meta:
		model = MoteurElectrique
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class ConvertisseurTable(tables.Table):
	class Meta:
		model = Convertisseur
		exclude = exclude = ('id','category','is_active','productbase_ptr',)



class ControleAccesEtPointageTable(tables.Table):
	class Meta:
		model = ControleAccesEtPointage
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class EnregistreurCameraSurveillanceTable(tables.Table):
	class Meta:
		model = EnregistreurCameraSurveillance
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class ConseilTable(tables.Table):
	class Meta:
		model = Conseil
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class RedactionDesProceduresTable(tables.Table):
	class Meta:
		model = RedactionDesProcedures
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class AssistanceFiscaleTable(tables.Table):
	class Meta:
		model = AssistanceFiscale
		exclude = exclude = ('id','category','is_active','productbase_ptr',)



class AuditEtControleInterneTable(tables.Table):
	class Meta:
		model = AuditEtControleInterne
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


class CoursAnglaisTable(tables.Table):
	class Meta:
		model = CoursAnglais
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class InterpretariatTable(tables.Table):
	class Meta:
		model = Interpretariat
		exclude = exclude = ('id','category','is_active','productbase_ptr',)


class ServiceDeTraductionTable(tables.Table):
	class Meta:
		model = ServiceDeTraduction
		exclude = exclude = ('id','category','is_active','productbase_ptr',)




