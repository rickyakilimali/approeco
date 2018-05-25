from product.models import *
from utils.product_attributes.equipement_materiel import *
from utils.unite_prix import *

# Create your models here.

#=====================================================
# 1. Boite cuisinière
#=====================================================
class BoiteCuisiniere(productbase.ProductBase):
	dimension =models.CharField("DIMENSION(MILLIMETRE)", max_length=20, choices= DIMENSION_BOITE_CUISINIERE	)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 2. Clef à molette
#=====================================================
class ClefMolette(productbase.ProductBase):
	dimension_clef_molette = models.CharField("DIMENSION CLEF",max_length=50, choices=DIMENSION_CLEF_MOLETTE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 3. Disjoncteur
#=====================================================
class Disjoncteur(productbase.ProductBase):
	marque = models.CharField("MARQUE",max_length=50, choices=MARQUE_EQUIPEMENT)
	intensite = models.CharField("INTENSITE(AMPERE)",max_length=50, choices=INTENSITE)
	nombre_phase = models.CharField("NOMBRE DE PHASE",max_length=50, choices=NOMBRE_PHASE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 4. Interrupteur differentiel
#=====================================================
class InterrupteurDifferentiel(productbase.ProductBase):
	marque = models.CharField("MARQUE",max_length=50, choices=MARQUE_EQUIPEMENT)
	intensite = models.CharField("INTENSITE(AMPERE)",max_length=50, choices=INTENSITE)
	nombre_phase = models.CharField("NOMBRE DE PHASE",max_length=50, choices=NOMBRE_POLE)
	sensibilite = models.CharField("SENSIBILITTE(MILLIAMPERE)",max_length=50, choices=SENSIBILITE_INTERRUPTEUR)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 5. Fusible
#=====================================================
class Fusible(productbase.ProductBase):
	marque = models.CharField("MARQUE",max_length=50, choices=MARQUE_EQUIPEMENT)
	intensite = models.CharField("INTENSITE(AMPERE)",max_length=50, choices=INTENSITE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 6. Equerre
#=====================================================
class Equerre(productbase.ProductBase):
	dimension = models.CharField("DIMENSION",max_length=50, choices=DIMENSION_EQUERRE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 7. Seche main
#=====================================================
class SecheMain(productbase.ProductBase):
	matiere = models.CharField("MATIERE",max_length=50, choices=MATIERE_SECHE_MAIN)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 8. Monte charge
#=====================================================
class MonteCharge(productbase.ProductBase):
	poids = models.CharField("POIDS",max_length=50, choices=POIDS_MONTE_CHARGE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 9. Interrupteur électrique
#=====================================================
class InterrupteurElectrique(productbase.ProductBase):
	marque = models.CharField("MARQUE",max_length=50, choices=MARQUE_PRISE_ELECTRIQUE)
	schema = models.CharField("SCHEMA",max_length=50, choices=SCHEMA_INTERRUPTEUR)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 10. Disjoncteur moteur
#=====================================================
class DisjoncteurMoteur(productbase.ProductBase):
	marque = models.CharField("MARQUE",max_length=50, choices=MARQUE_EQUIPEMENT)
	intensite = models.CharField("INTENSITE(AMPERE)",max_length=50, choices=INTENSITE_DISJONCTEUR_MOTEUR)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 11. Paumelle
#=====================================================
class Paumelle(productbase.ProductBase):
	dimension = models.CharField("DIMENSION",max_length=50, choices=DIMENSION_PAUMELLE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 12. Gant
#=====================================================
class Gant(productbase.ProductBase):
	type_gant = models.CharField("TYPE DE GANT",max_length=50, choices=TYPE_GANT)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 13. Cylindre
#=====================================================
class Cylindre(productbase.ProductBase):
	type_cylindre = models.CharField("TYPE CYLINDRE",max_length=50, choices=TYPE_CYLINDRE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 14. Palan mécanique
#=====================================================
class PalanMecanique(productbase.ProductBase):
	poids = models.CharField("POID PALAN",max_length=50, choices=POIDS_MONTE_CHARGE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 15. Inverseur
#=====================================================
class Inverseur(productbase.ProductBase):
	intensite = models.CharField("INTENSITE(AMPERE)",max_length=50, choices=INTENSITE_INVERSEUR)
	nombre_prise = models.CharField("NOMBRE DE PRISE",max_length=50, choices=NOMBRE_PRISE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# 16. Appreil de mesure
#=====================================================
class AppareilDeMesure(productbase.ProductBase):
	type_appareil_mesure = models.CharField("TYPE APPAREIL DE MESURE",max_length=1, choices=TYPES_APPAREIL_MESURE)
	tension = models.CharField("TENSION",max_length=20, choices=TENSION)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	unite_prix = models.CharField(max_length=20, choices=UNITE)
	units = models.CharField(max_length=50, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 17. Prise électrique
#=====================================================
class PriseElectrique(productbase.ProductBase):
	marque = models.CharField("MARQUE",max_length=20, choices=MARQUE_PRISE_ELECTRIQUE)
	type_prise = models.CharField("TYPE DE PRISE",max_length=20, choices=TYPE_PRISE_ELECTRIQUE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 18. Rallonge
#=====================================================
class Rallonge(productbase.ProductBase):
	longueur = models.CharField("LONGUEUR",max_length=20, choices=LONGUEUR_RALLONGE)
	nombre_prise = models.CharField("NOMBRE	 DE PRISE",max_length=20, choices=NOMBRE_PRISE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE_USD_PIECE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 19. Boite de dérivation
#=====================================================
class BoiteDerivation(productbase.ProductBase):
	marque = models.CharField("MARQUE",max_length=20, choices=MARQUE_EQUIPEMENT)

	dimension=models.CharField("DIMENSION(MILLIMETRES)",max_length=20, choices=DIMENSION)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 20. Coffret électrique
#=====================================================
class CoffretElectrique(productbase.ProductBase):
	marque = models.CharField("MARQUE",max_length=20, choices=MARQUE_EQUIPEMENT)
	nombre_module = models.CharField("NOMBRE DE MODULE",max_length=20, choices=NOMBRE_MODULE)
	encastre_sailli=models.CharField("ENCASTRE_SAILLI",max_length=20, choices=ENCASTRE_SAILLI)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 21.
#=====================================================

#=====================================================
# 22. Mèche à beton
#=====================================================
class MecheBeton(productbase.ProductBase):
	diametre = models.CharField("DIAMETRE",max_length=20, choices=DIAMETRE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 23. Outils manuel
#=====================================================
class OutilsManuel(productbase.ProductBase):
	type_outils = models.CharField("OUTILLAGE MANUEL",max_length=20, choices=TYPE_OUTILS_MANUEL)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 24. Balance
#=====================================================
class Balance(productbase.ProductBase):
	type_balance = models.CharField("BALANCE",max_length=20, choices=TYPES_BALANCE)
	poids=models.CharField("POIDS",max_length=10, choices=POIDS)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 25. Tuyauterie
#=====================================================
class Tuyauterie(productbase.ProductBase):
	matiere_tuyauterie = models.CharField("MATIERE",max_length=20, choices=MATIERE_TUYAUTERIE)
	localisation=models.CharField("LOCALISATION",max_length=10, choices=LOCALISATION_TUYAUTERIE)
	diametre=models.CharField("DIAMETRE",max_length=20, choices=DIAMETRE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 26. Accessoires hydrophore
#=====================================================
class AccessoiresHydrophore(productbase.ProductBase):
	type_accessoires_hydrophore = models.CharField("ACCESSOIRE HYDROPHORES",max_length=20, choices=TYPE_ACCESSOIRES_HYDROPHORE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 27. Flexibe
#=====================================================
class Flexible(productbase.ProductBase):
	utilisation = models.CharField("FLEXIBLE",max_length=20, choices=UTILISATION_FLEXIBLE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 28. Siphon
#=====================================================
class Siphon(productbase.ProductBase):
	type_sanitaire = models.CharField("TYPE SANITAIRE",max_length=20, choices=SANITAIRE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 29. Réduction PVC
#=====================================================
class ReductionPvc(productbase.ProductBase):
	reduction = models.CharField("REDUCTION",max_length=20, choices=REDUCTION_PVC)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 30. Ampoule électrique
#=====================================================
class AmpouleElectrique(productbase.ProductBase):
	type_ampoule = models.CharField("TYPE EMPOULE",max_length=20, choices=TYPE_AMPOULE)
	culot = models.CharField("CULOT",max_length=20, choices=CULOT)
	puissance_ampoule = models.CharField("PUISSANCE AMPOULE",max_length=20, choices=PUISSANCE_AMPOULE_ELECTRIQUE)
	forme_ampoule = models.CharField("FORME AMPOULE",max_length=20, choices=FORME_AMPOULE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 31. Moto pompe
#=====================================================
class MotoPompe(productbase.ProductBase):
	marque = models.CharField("MARQUE",max_length=20, choices=MARQUE_MACHINE_ATELIER)
	moteur = models.CharField("MOTEUR",max_length=20, choices=MOTEUR)
	section_moto_pompe = models.CharField("SECTION",max_length=20, choices=SECTION_MOTO_POMPE)
	puissance_moto_pompe = models.CharField("PUISSANCE",max_length=20, choices=PUISSANCE_MOTO_POMPE)

	hauteur_max = models.CharField("HAUTEUR",max_length=20, blank=True, null=True, choices=HAUTEUR_POMPE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 32. Chargeur Batterie
#=====================================================
class ChargeurBatterie(productbase.ProductBase):
	capacite_chargeur = models.CharField("CAPACITE",max_length=20, choices=CAPACITE_CHARGEUR_BATTERIE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 33. Enseigne lumineuse
#=====================================================
class EnseigneLumineuse(productbase.ProductBase):
	format_enseigne=models.CharField("FORMAT ENSEIGNE",max_length=20, choices=FORMAT)
	longueur = models.CharField("LONGUEUR",max_length=20, choices=LONGUEUR)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 34. Pompe hydrophore
#=====================================================
class PompeHydrophore(productbase.ProductBase):
	puissance_pompe= models.CharField("PUISSANCE",max_length=20, choices=PUISSANCE_HP)
	debit = models.CharField("DEBIT",max_length=20, choices=DEBIT_POMPE)
	hauteur_max = models.CharField("HAUTEUR",max_length=20, choices=HAUTEUR_POMPE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 35. Pompe de forage
#=====================================================
class PompeForage(productbase.ProductBase):
	marque_pompe=models.CharField("MARQUE",max_length=20, choices=MARQUE_MACHINE_ATELIER)
	force_pompe = models.CharField("FORCE POMPE",max_length=20, choices=FORCE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 36. Pompe à eau
#=====================================================
class PompeEau(productbase.ProductBase):
	marque_pompe=models.CharField("MARQUE",max_length=20, choices=MARQUE_MACHINE_ATELIER)
	hauteur_pompe = models.CharField("HAUTEUR",max_length=20, choices=HAUTEUR_POMPE)
	puissance_pompe=models.CharField("PUISSANCE",max_length=20, choices=PUISSANCE_POMPE)
	debit_pompe = models.CharField("DEBIT",max_length=20, choices=DEBIT_POMPE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 37. Machine atelier non portatif
#=====================================================
class MachineAtelierNonPortatif(productbase.ProductBase):
	marque_marchine=models.CharField("MACHINE PORTATIF",max_length=20, choices=MARQUE_MACHINE_ATELIER)
	diametre=models.CharField("DIAMETRE",max_length=20, choices=DIAMETRE)
	type_machine_non_portatif = models.CharField("TYPE MACHINE",max_length=20, choices=TYPE_MACHINE_ATELIER_NON_PORTATIF)
	puissance_machine=models.CharField("PUISSANCE",max_length=20, choices=PUISSANCE_MACHINE_ATELIER_NON_PORTATIF)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 38. Machine atelier portatif
#=====================================================
class MachineAtelierPortatif(productbase.ProductBase):
	marque_marchine=models.CharField("MACHINE PORTATIF",max_length=20, choices=MARQUE_MACHINE_ATELIER)
	diametre=models.CharField("DIAMETRE",max_length=20, choices=DIAMETRE)
	type_machine_non_portatif = models.CharField("TYPE MACHINE",max_length=20, choices=TYPE_MACHINE_ATELIER_PORTATIF)
	puissance_machine=models.CharField("PUISSANCE",max_length=20, choices=PUISSANCE_MACHINE_PORTATIF)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 39. Groupe électrogène
#=====================================================
class GroupeElectrogene(productbase.ProductBase):
	marque=models.CharField("MARQUE",max_length=20, blank=True,null=True, choices=MARQUE_MACHINE_ATELIER)
	silencieux=models.CharField("SILENCIEUX",max_length=20, choices=SILENCIEUX)
	puissance_groupe=models.CharField("PUISSANCE(KILO VOLT-AMPERE)",max_length=20, choices=PUISSANCE_GROUPE_ELECTROGENE)
	carburant=models.CharField("TYPE CARBURANT",max_length=20, choices= TYPE_CARBURANT)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 40. Compresseur
#=====================================================
class Compresseur(productbase.ProductBase):
	marque_marchine=models.CharField("MARQUE",max_length=20, choices=MARQUE_COMPRESSEUR)
	puissance_compresseur=models.CharField("PUISSANCE (WATT)",max_length=20, choices=PUISSANCE_COMPRESSEUR)
	capacite_compresseur=models.CharField("CAPACITE (LITRE)",max_length=20, choices=CAPACITE_COMPRESSEUR)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 41. Detecteur d'intrusion
#=====================================================
class DetecteurIntrusion(productbase.ProductBase):
	marque_detecteur =models.CharField("MARQUE DETECTEUR",max_length=100, choices=MARQUE_EQUIPEMENT)
	type_detecteur=models.CharField("TYPE DE DETECTEUR",max_length=100, choices=TYPE_DETECTEUR)
	adressable=models.CharField("ADRESSABLE",max_length=100, choices=OUI_NON)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 42. Moteur électrique
#=====================================================
class MoteurElectrique(productbase.ProductBase):
	marque_moteur=models.CharField("MARQUE",max_length=20, choices=MARQUE_MOTEUR)
	tension_moteur=models.CharField("TENSION",max_length=20, choices=TENSION_MOTEUR)
	puissance_moteur=models.CharField("PUISSANCE",max_length=20, choices=PUISSANCE_MOTEUR)
	nombre_pole=models.CharField("NOMBRE DE POLE",max_length=20, choices=NOMBRE_POLE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# 44. Controle d'accès et pointage
#=====================================================
class ControleAccesEtPointage(productbase.ProductBase):
	marque_equipement=models.CharField("MARQUE",max_length=50, choices=MARQUE_EQUIPEMENT)
	mode_fonctionnement=models.CharField("MODE DE FONCTIONNEMENT",max_length=50, choices=MODE_FONCTIONNEMENT)
	pointage_presence=models.CharField("POINTAGE PRESENCE",max_length=50, choices=OUI_NON)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 45. Enregistreur caméra de surveillance
#=====================================================
class EnregistreurCameraSurveillance(productbase.ProductBase):
	nombre_canaux=models.CharField("NOMBRE DE CANEAUX",max_length=20, choices=NOMBRE_CANAUX)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 46. Detecteur d'incendie
#=====================================================
class DetecteurIncendie(productbase.ProductBase):
	mode_detection=models.CharField("MODE DE DETECTION",max_length=20, choices=MODE_DETECTION_DETECTEUR_INCENDIE)
	adressable =models.CharField("ADRESSABLE", max_length=20, choices= ADRESSABLE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 47. EXTINCTEUR
#=====================================================
class Extincteur(productbase.ProductBase):
	agent=models.CharField("AGENT",max_length=20, choices=AGENT_EXTINCTEUR)
	poids=models.CharField("POIDS",max_length=20, choices= POIDS_AGENT_EXTINCTEUR)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 47. PANNEAU SIGNALISATION
#=====================================================
class PanneauSignalisation(productbase.ProductBase):
	type_signalisation=models.CharField("TYPE SIGNALISATION",max_length=100, choices=TYPE_SIGNALISATION)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 48. CITERNE
#=====================================================
class Citerne(productbase.ProductBase):
	capacite=models.CharField("CAPACITE(LITRE)",max_length=20, choices=CAPACITE_L)
	materiau=models.CharField("MATERIAU",max_length=20, choices= MATERIAU_CITERNE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 49.
#=====================================================



#=====================================================
# 50.
#=====================================================


#=====================================================
# 48.
#=====================================================







#=====================================================
# 52. Moto pompe
#=====================================================





#=====================================================
# 53.
#=====================================================


#=====================================================
# 54. contacteurs
#=====================================================

#=====================================================
# 55. Fusible
#=====================================================


#=====================================================
# 56. Boite de derivation
#=====================================================

#=====================================================
# 57. COFFRET ELECTRIQUE MODULAIRE 2
#=====================================================
class CoffretElectriqueModulaire(productbase.ProductBase):
	marque =models.CharField("MARQUE ", max_length=20, choices= MARQUE)
	nombre_module =models.CharField("NOMBRE DE MODULE", max_length=20, choices= NOMBRE_MODULE )
	encastre_saili =models.CharField("ENCASTRÉ OU SAILI", max_length=20, choices= ENCASTRE_SAILLI )
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 58. ONDULEUR
#=====================================================
class Onduleur(productbase.ProductBase):
	marque=models.CharField("MARQUE ", max_length=20, choices= MARQUE_ONDULEUR)
	puissance =models.CharField("PUISSANCE", max_length=20, choices= PUISSANCE_ONDULEUR )
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# 59. STABILISATEUR
#=====================================================
class Stabilisateur(productbase.ProductBase):
	marque=models.CharField("MARQUE", max_length=20, choices= MARQUE)
	puissance =models.CharField("PUISSANCE", max_length=20, choices= PUISSANCE_STABISATEUR )
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# 60. AMPOULE
#=====================================================
class Ampoule(productbase.ProductBase):
	puissance =models.CharField("PUISSANCE", max_length=20, choices= PUISSANCE)
	type_ampoule =models.CharField("TYPE", max_length=20, choices= TYPE_AMPOULE )
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# 61. CABLE SOUPLE
#=====================================================
class CableSouple(productbase.ProductBase):
	type_cable =models.CharField("TYPE DE CABLE", max_length=20, choices= TYPE_CABLE)
	nombre_fil =models.CharField("NOMBRE DE FIL", max_length=20, choices= NOMBRE_DE_FIL )
	section =models.CharField("SECTION(MILLIMETRE CARRÉ)", max_length=20, choices= SECTION )
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_M)
	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 62. CABLE MASSE
#=====================================================
class CableMasse(productbase.ProductBase):
	section =models.CharField("SECTION", max_length=20, choices= SECTION )
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_M)
	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 63. COFFRET DIVISIONNAIRE
#=====================================================
class CoffretDivisionnaire(productbase.ProductBase):
	nombre_circuit =models.CharField("NOMBRE CIRCUIT", max_length=20, choices= NOMBRE_CIRCUIT )
	marque =models.CharField("MARQUE", max_length=20, choices= MARQUE )
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 64. COFFRET JEU DE BARRE
#=====================================================
class CoffretJeuBarre(productbase.ProductBase):
	intensite =models.CharField("INTENSITE(AMPERE)", max_length=20, choices= INTENSITE )
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 65. COFFRET MANOEUVRE
#=====================================================


#=====================================================
# 66. CONTACTEUR
#=====================================================



#=====================================================
# 67. DISJONCTEUR COMPACT
#=====================================================
class DisjoncteurCompact(productbase.ProductBase):
	marque =models.CharField("MARQUE", max_length=20, choices= MARQUE )
	intensite =models.CharField("INTENSITE(AMPERE)", max_length=20, choices= INTENSITE )
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 68. DISJONCTEUR CONTACTEUR
#=====================================================
class DisjoncteurContacteur(productbase.ProductBase):
	marque =models.CharField("MARQUE", max_length=20, choices= MARQUE )
	intensite =models.CharField("INTENSITE(AMPERE)", max_length=20, choices= INTENSITE )
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']




#=====================================================
# 69. DISJONCTEUR
#=====================================================


#=====================================================
# 70. FIL PLASTIQUE
#=====================================================
class FilPlastique(productbase.ProductBase):
	nombre_fil =models.CharField("NOMBRE DE FIL", max_length=20, choices= NOMBRE_DE_FIL )
	section =models.CharField("SECTION(MILLIMETRE CARRÉ)", max_length=20, choices= SECTION )
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_M)
	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# 71. INVERSEUR A COFFRET
#=====================================================
class InverseurCoffret(productbase.ProductBase):
	marque =models.CharField("MARQUE", max_length=20, choices= MARQUE )
	intensite =models.CharField("INTENSITE(AMPERE)", max_length=20, choices= INTENSITE )
	nombre_circuit =models.CharField("NOMBRE CIRCUIT", max_length=20, choices= NOMBRE_CIRCUIT )
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# 72. PLAFONIER A LED
#=====================================================
class PlafonnierLed(productbase.ProductBase):
	puissance =models.CharField("PUISSANCE", max_length=20, choices= PUISSANCE )
	tension =models.CharField("TENSION", max_length=20, choices= TENSION )
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 73. PROJECTEUR
#=====================================================
class Projecteur(productbase.ProductBase):
	puissance =models.CharField("PUISSANCE", max_length=20, choices= PUISSANCE )
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']




#=====================================================
# 74. REGLETTE
#=====================================================
class reglette(productbase.ProductBase):
	puissance =models.CharField("PUISSANCE", max_length=20, choices= PUISSANCE )
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 75. ROULEAU_FLEXIBLE
#=====================================================
class RouleauFlexuble(productbase.ProductBase):
	dimension =models.CharField("DIMENSION", max_length=20, choices= DIMENSION_ROULEAU_FLEXIBLE )
	longueur =models.CharField("LONGUEUR", max_length=20, choices= LONGUEUR_ROULEAU_FLEXIBLE )
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']



#=====================================================
# 78. TUBE
#=====================================================
class Tube(productbase.ProductBase):
	puissance =models.CharField("PUISSANCE", max_length=20, choices= PUISSANCE )
	type_tube=models.CharField("TYPE TUBE", max_length=20, choices= TYPE_TUBE )
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 79. APPAREIL DE MESURE
#=====================================================
class AppareilMesure(productbase.ProductBase):
	type_appareil_mesure =models.CharField("TYPE APPAREIL", max_length=20, choices= TYPE_APPAREIL_MESURE )
	tension=models.CharField("TENSION", max_length=20, choices= TENSION )
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# 80. BOITE CUISINIERE
#=====================================================

#=====================================================
# 81. INTERRUPTEUR
#=====================================================
class Interrupteur(productbase.ProductBase):
	marque =models.CharField("MARQUE", max_length=20, choices= MARQUE)
	schema =models.CharField("SCHEMA", max_length=20, choices= SCHEMA_INTERRUPTEUR)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 82. RALLONGE
#=====================================================


#=====================================================
# 83. PRISE ELECTRIQUE
#=====================================================

#=====================================================
# 81. FONTAINE D’EAU
#=====================================================
class FontaineEau(productbase.ProductBase):
	model =models.CharField("MODEL", max_length=20, choices= MODE_FONTAINE)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 81. SPLIT
#=====================================================
class Split(productbase.ProductBase):
	marque =models.CharField("MARQUE", max_length=20, choices= MARQUE_SPLIT)
	puissance =models.CharField("PUISSANCE SPLIT", max_length=20, choices= PUISSANCE_SPLIT)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 82.
#=====================================================

#=====================================================
#  INTERRUPTEUR SECTIONNEUR  ==> EQUIPEMENT MATERIEL
#=====================================================
class InterrupteurSectionneur(productbase.ProductBase):

	#les attributs
	marque = models.CharField("MARQUE",max_length=50, choices=MARQUE_EQUIPEMENT)
	nombre_phase = models.CharField("NOMBRE DE PHASES",max_length=100, choices=NOMBRE_PHASE)
	intensite = models.CharField("INTENSITE(AMPERE)",max_length=100, choices=INTENSITE)
	tension = models.CharField("TENSION(VOLT)",max_length=100, choices=TENSION)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
#  MINUTEUR POUR CONTACTEUR  ==> EQUIPEMENT MATERIEL
#=====================================================

class MinuteurContacteur(productbase.ProductBase):

	#les attributs
	marque = models.CharField("MARQUE",max_length=50, choices=MARQUE_EQUIPEMENT)
	type_temporisation = models.CharField("TYPE DE TEMPORISATION",max_length=100, choices=TYPE_TEMPORISATION)
	domaine_reglage = models.CharField("DOMAINE DE REGLAGE(SECONDES)",max_length=100, choices=DOMAINE_REGLAGE)

	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  DISJONCTEUR DIFFERENTIEL  ==> EQUIPEMENT MATERIEL
#=====================================================

class DisjoncteurDifferentiel(productbase.ProductBase):

	#les attributs
	marque = models.CharField("MARQUE",max_length=50, choices=MARQUE_EQUIPEMENT)
	nombre_phase = models.CharField("NOMBRE DE PHASES",max_length=100, choices=NOMBRE_PHASE)
	intensite = models.CharField("INTENSITE(AMPERE)",max_length=100, choices=INTENSITE)
	sensibilite = models.CharField("SENSIBILITE(MILLIAMPERE)",max_length=100, choices=SENSIBILITE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
#  CONTACTEURS  ==> EQUIPEMENT MATERIEL
#=====================================================

class Contacteur(productbase.ProductBase):

	#les attributs
	marque = models.CharField("MARQUE",max_length=50, choices=MARQUE_EQUIPEMENT)
	nombre_phase = models.CharField("NOMBRE DE PHASES",max_length=100, choices=NOMBRE_PHASE)
	intensite = models.CharField("INTENSITE(AMPERE)",max_length=100, choices=INTENSITE)
	tension = models.CharField("TENSION(VOLT)",max_length=100, choices=TENSION)
	puissance = models.CharField("PUISSANCE(KILOWATT)",max_length=100, choices=TENSION)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
#  BETONNIERE  ==> EQUIPEMENT MATERIEL
#=====================================================
class Betonniere(productbase.ProductBase):

	#les attributs
	capacite_betonniere = models.CharField("CAPACITE(LITRE)",max_length=100, choices=CAPACITE_BETONNIERE)
	type_betonniere = models.CharField("TYPE BETONNIERE",max_length=100, choices=TYPE_BETONNIERE)

	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  COMPACTEUR  ==> EQUIPEMENT MATERIEL
#=====================================================

class Compacteur(productbase.ProductBase):

	#les attributs
	type_compacteur = models.CharField("TYPE COMPACTEUR",max_length=100, choices=TYPE_COMPACTEUR)
	puissance_compacteur = models.CharField("PUISSANCE",max_length=100, choices=PUISSANCE_COMPACTEUR)
	carburant = models.CharField("CARBURANT",max_length=100, choices=CARBURANT)

	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
#  COMPRESSEUR AIR  ==> EQUIPEMENT MATERIEL
#=====================================================

class CompresseurAir(productbase.ProductBase):

	#les attributs
	capacite_compresseur = models.CharField("CAPACITE COMPRESSEUR",max_length=100, choices=CAPACITE_COMPRESSEUR)
	puissance_compresseur = models.CharField("PUISSANCE",max_length=100, choices=PUISSANCE_COMPRESSEUR)
	debit = models.CharField("DEBIT(LITRE/MIN)",max_length=100, choices=DEBIT)

	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  PALAN  ==> EQUIPEMENT MATERIEL
#=====================================================

class Palan(productbase.ProductBase):

	#les attributs
	puissance_palan = models.CharField("PUISSANCE PALAN",max_length=100, choices=PUISSANCE_PALAN)
	longueur = models.CharField("LONGUEUR(METRE)",max_length=100, choices=LONGUEUR)
	poids_max = models.CharField("POIDS MAX(TONNE)",max_length=100, choices=POIDS_MAX)
	type_palan = models.CharField("TYPE",max_length=100, choices=TYPE_PALAN)

	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']



#=====================================================
#  OUTILLAGE MANUEL  ==> EQUIPEMENT MATERIEL
#=====================================================

class OutillageManuel(productbase.ProductBase):

	#les attributs
	type_outillage = models.CharField("TYPE OUTILLAGE",max_length=100, choices=TYPE_OUTILLAGE)


	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  POMPE IMMERGEE  ==> EQUIPEMENT MATERIEL
#=====================================================

class PompeImmergee(productbase.ProductBase):

	#les attributs
	hauteur_pompe = models.CharField("HAUTEUR POMPE",max_length=100, choices=HAUTEUR_POMPE)
	puissance_pompe = models.CharField("PUISSANCE POMPE(CHEVAUX)",max_length=100, choices=PUISSANCE_HP)
	debit_pompe = models.CharField("DEBIT POMPE(LITRE PAR HEURE)",max_length=100, choices=DEBIT_POMPE)


	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  TRONCONNEUSE  ==> EQUIPEMENT MATERIEL
#=====================================================

class Tronconneuse(productbase.ProductBase):

	#les attributs
	marque = models.CharField("MARQUE TRONCONNEUSE",max_length=100, choices=MARQUE_MACHINE_ATELIER)
	modele_tronconneuse = models.CharField("MODELE TRONCONNEUSE",max_length=100, choices=MODELE_TRONCONNEUSE)



	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  meuleuse  ==> EQUIPEMENT MATERIEL
#=====================================================

class Meuleuse(productbase.ProductBase):

	#les attributs
	puissance_meuleuse = models.CharField("PUISSANCE MEULEUSE",max_length=100, choices=PUISSANCE_MEULEUSE)
	diametre = models.CharField("DIAMETRE",max_length=100, choices=DIAMETRE)



	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  tondeuse  ==> EQUIPEMENT MATERIEL
#=====================================================

class Tondeuse(productbase.ProductBase):

	#les attributs
	puissance_tondeuse = models.CharField("PUISSANCE TONDEUSE",max_length=100, choices=PUISSANCE_TONDEUSE)
	type_tondeuse = models.CharField("TYPE TONDEUSE",max_length=100, choices=TYPE_TONDEUSE)



	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  SIRENE  ==> EQUIPEMENT MATERIEL
#=====================================================

class Sirene(productbase.ProductBase):

	#les attributs
	marque = models.CharField("MARQUE",max_length=100, choices=MARQUE_EQUIPEMENT)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  TELEPHONE DE BUREAU ==> EQUIPEMENT MATERIEL
#=====================================================

class TelephoneBureau(productbase.ProductBase):

	#les attributs
	marque = models.CharField("MARQUE TELEPHONE",max_length=100, choices=MARQUE_EQUIPEMENT)
	interface = models.CharField("INTERFACE",max_length=100, choices=INTERFACE)



	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  IMPRIMANTE A BADGE ==> EQUIPEMENT MATERIEL
#=====================================================

class ImprimanteABadge(productbase.ProductBase):

	#les attributs
	marque_imprimante_badge = models.CharField("MARQUE IMPRIMANTE",max_length=100, choices=MARQUE_IMPRIMANTE_BAGE)
	technologe_impression_badge = models.CharField("TECHNOLOGIE IMPRESSION",max_length=100, choices=TECHNOLOGIE_IMPRESSION)
	faces_imprimes = models.CharField("FACES IMPRIMES",max_length=100, choices=FACES_IMPRIMES)
	vitesse_impression = models.CharField("VITESSE D'IMPRESSION",max_length=100, choices=VITESSE_IMPRESSION)
	option_encodage = models.CharField("OPTION D'ENCODAGE",max_length=100, choices=OPTION_ENCODAGE)



	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  REPARATION SPLIT
#=====================================================

class ReparationSplit(productbase.ProductBase):

	#les attributs


	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_POURC_DEVIS)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  BOOSTER
#=====================================================

class Booster(productbase.ProductBase):
	#les attributs
	marque= models.CharField("MARQUE",max_length=100, choices=MARQUE_BOOSTER)
	tension = models.CharField("TENSION (VOLT)",max_length=100, choices=TENSION_BOOSTER)
	intesite = models.CharField("INTESITE (AMPERE)",max_length=100, choices=INTENSITE_BOOSTER)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
#  MELANGEUR
#=====================================================

class Melangeur(productbase.ProductBase):
	#les attributs
	marque= models.CharField("MARQUE",max_length=100, choices=MARQUE_MELANGEUR)
	puissance = models.CharField("PUISSANCE (WATT)",max_length=100, choices=PUISSANCE_MELANGEUR)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  COUPE HAIE ELECTRIQUE
#=====================================================

class CoupHaieElectrique(productbase.ProductBase):
	#les attributs
	marque= models.CharField("MARQUE",max_length=100, choices=MARQUE_COUP_HAIE)
	puissance = models.CharField("PUISSANCE (WATT)",max_length=100, choices=PUISSANCE_COUP_HAIE)
	longueur_de_coupe= models.CharField("LONGUEUR DE COUPE (CENTIMETRE)",max_length=100, choices=LONGUEUR_COUP_HAIE)
	alimentation= models.CharField("ALIMENTATION",max_length=100, choices=ALIMENTATION_COUP_HAIE)
	tension= models.CharField("TENSION",max_length=100, choices=TENSION_COUP_HAIE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
#  DECAPEUR THERMIQUE
#=====================================================

class DecapeurThermique(productbase.ProductBase):
	#les attributs
	marque= models.CharField("MARQUE",max_length=100, choices=MARQUE_DECAPEUR)
	puissance = models.CharField("PUISSANCE (WATT)",max_length=100, choices=PUISSANCE_DECAPEUR)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
#  SCIE SAUTEUSE
#=====================================================

class ScieSauteuse(productbase.ProductBase):
	#les attributs
	marque= models.CharField("MARQUE",max_length=100, choices=MARQUE_SCIE)
	puissance = models.CharField("PUISSANCE (WATT)",max_length=100, choices=PUISSANCE_SCIE)
	alimentation= models.CharField("ALIMENTATION",max_length=100, choices=ALIMENTATION_SCIE)
	tension= models.CharField("TENSION",max_length=100, choices=TENSION_SCIE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# ASPIRATEUR
#=====================================================

class Aspirateur(productbase.ProductBase):
	#les attributs
	marque= models.CharField("MARQUE",max_length=100, choices=MARQUE_ASPIRATEUR)
	puissance = models.CharField("PUISSANCE (WATT)",max_length=100, choices=PUISSANCE_ASPIRATEUR)
	type_aspirateur= models.CharField("TYPE D'ASPIRATEUR",max_length=100, choices=TYPE_ASPIRATEUR)
	capacite_reservoir= models.CharField("CAPACITE RESERVOIR(LITRE)",max_length=100, choices=CAPACITE_ASPIRATEUR)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# MACHINE AGRICOLE
#=====================================================

class MachineAgricole(productbase.ProductBase):
	#les attributs
	type_machine_agricole= models.CharField("TYPE MACHINE AGRICOLE",max_length=100, choices=TYPE_MA)
	rendement= models.CharField("RENDEMENT (KILOGRAMME/HEURE)",max_length=100, choices=RENDEMENT_MA)
	puissance = models.CharField("PUISSANCE (WATT)",max_length=100, choices=PUISSANCE_MA)
	garantie= models.CharField("GUARANTIE",max_length=100, choices=GUARANTIE_MA)
	carburant= models.CharField("CARBURANT",max_length=100, choices=CARBURANT_MA)
	consommation= models.CharField("CONSOMMATION(LITRE/HEURE)",max_length=100, choices=CONSOMMATION_MA)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# SONNERIE ELECTRIQUE
#=====================================================
class SonnerieElectrique(productbase.ProductBase):
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# WC
#=====================================================

class WC(productbase.ProductBase):
	#les attributs
	type_wc= models.CharField("TYPE DE WC",max_length=100, choices=TYPE_WC)
	marque= models.CharField("MARQUE",max_length=100, choices=MARQUE_WC)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# INSTALLATION SANITAIRE
#=====================================================

class InstallationSanitaire(productbase.ProductBase):
	#les attributs
	type_sanitaire= models.CharField("TYPE D'INSTALLATION SANITAIRE",max_length=100, choices=TYPE_SANITAIRE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# KARCHER
#=====================================================

class Karcher(productbase.ProductBase):
	#les attributs
	type_karcher= models.CharField("TYPE DE KARCHER",max_length=100, choices=TYPE_KARCHER)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# SOCKET
#=====================================================

class Socket(productbase.ProductBase):
	#les attributs
	type_socket= models.CharField("TYPE DE SOCKET",max_length=100, choices=TYPE_SOCKET)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# RIVET
#=====================================================

class Rivet(productbase.ProductBase):
	#les attributs
	dimension= models.CharField("DIMENSION (en mm)",max_length=100, choices=DIMENSION)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# HUBLOT
#=====================================================

class Hublot(productbase.ProductBase):
	#les attributs
	type_hublot= models.CharField("TYPE DE HUBLOT",max_length=100, choices=TYPE_HUBLOT)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# COUPE CARREAU
#=====================================================

class CoupeCarreau(productbase.ProductBase):
	#les attributs
	type_coupe_carreau= models.CharField("TYPE DE COUPE CARREAU",max_length=100, choices=TYPE_CARREAU)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']



#=====================================================
# SILICONE
#=====================================================

class Silicone(productbase.ProductBase):
	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# TREILLIS
#=====================================================

class Treillis(productbase.ProductBase):
	#les attributs
	type_treillis = models.CharField("TYPE DE TREILLIS",max_length=100, choices=TYPE_TREILLIS)
	dimension = models.CharField("DIMENSION (m x m)",max_length=100, choices=DIMENSION_TREILLIS)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# TENTE
#=====================================================

class Tente(productbase.ProductBase):
	#les attributs
	dimension = models.CharField("DIMENSION (m x m)",max_length=100, choices=DIMENSION_TENTE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# CHARNIERE
#=====================================================

class Charniere(productbase.ProductBase):
	#les attributs
	taille_charniere = models.CharField("TAILLE DE LA CHARNIERE",max_length=100, choices=TAILLE_CHARNIERE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# CLINCHE
#=====================================================

class Clinche(productbase.ProductBase):
	#les attributs
	taille_clinche = models.CharField("TAILLE DE LA CLINCHE",max_length=100, choices=TAILLE_CLINCHE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# SPRAY
#=====================================================

class Spray(productbase.ProductBase):
	#les attributs
	couleur_spray = models.CharField("COULEUR SPRAY",max_length=100, choices=COULEUR_SPRAY)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# SCIE CLOCHE
#=====================================================

class ScieCloche(productbase.ProductBase):
	#les attributs
	quantite_par_jeu = models.CharField("QUANTITE PAR JEU",max_length=100, choices=QUANTITE_PAR_JEU)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# DIABLE
#=====================================================

class Diable(productbase.ProductBase):
	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# ARRACHE CLOU
#=====================================================

class ArracheClou(productbase.ProductBase):
	#les attributs
	dimension_arrache_clou = models.CharField("DIMENSION ARRACHE CLOU",max_length=100, choices=DIMENSION_ARRACHE_CLOU)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# ATTACHE CABLE A CLOUER
#=====================================================

class AttacheCableAClouer(productbase.ProductBase):
	#les attributs
	dimension_attache_mm = models.CharField("DIMENSION ATTACHE EN MM",max_length=100, choices=DIMENSION_ATTACHE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']





#=====================================================
# BARRE DE MINE
#=====================================================



#=====================================================
# BANDE DE SIGNALISATION
#=====================================================

class BandeDeSignalisation(productbase.ProductBase):
	#les attributs
	longueur= models.CharField("LONGUEUR EN METTRE",max_length=100, choices=LONGUEUR_BANDE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# ROULEAU BANDE A PONCER
#=====================================================

class RouleauBandeAPoncer(productbase.ProductBase):
	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# SOUFFLEUR ASPIRATEUR
#=====================================================

class SouffleurAspirateur(productbase.ProductBase):
	#les attributs
	puissance_machine = models.CharField("PUISSANCE DE LA MACHINE",max_length=100, choices=PUISSANCE_MACHINE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# SELF POUR PROJECTEUR
#=====================================================

class SelfPourProjecteur(productbase.ProductBase):
	#les attributs
	puissance = models.CharField("PUISSANCE DE LA MACHINE",max_length=100, choices=PUISSANCE_EN_WATT)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# TEFLON
#=====================================================

class Teflon(productbase.ProductBase):
	#les attributs
	modele_teflon = models.CharField("MODELE TEFLON",max_length=100, choices=MODEL_TEFLON)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# TUYAU POUR MOTOPOMPE
#=====================================================

class TuyauMotopompe(productbase.ProductBase):
	#les attributs
	type_tuyau = models.CharField("TYPE DE TUYAU",max_length=100, choices=TYPE_TUYAU)
	dimension_tuyau = models.CharField("DIMENSION DU TUYAU",max_length=100, choices=DIMENSION_TUYAU)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# TENAILLE
#=====================================================

class Tenaille(productbase.ProductBase):
	#les attributs
	dimension_tenaille = models.CharField("DIMENSION TENAILLE",max_length=100, choices=DIMENSION_TENAILLE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# TOITURE
#=====================================================

class Toiture(productbase.ProductBase):
	#les attributs
	type_toiture = models.CharField("TYPE DE TOLE",max_length=100, choices=TYPE_TOLE)
	dimension = models.CharField("DIMENSION (M x M)",max_length=100, choices=DIMENSION_TOLE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# TETE DE VISSEUSE
#=====================================================

class TeteDeVisseuse(productbase.ProductBase):
	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# AIGUILLE A VIBRER LE BETON
#=====================================================

class AiguilleAVibrerLeBeton(productbase.ProductBase):
	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# BALASTRE
#=====================================================

class Balastre(productbase.ProductBase):
	#les attributs
	type_balastre= models.CharField("TYPE DE BALASTRE",max_length=100, choices=TYPE_BALASTRE)
	marque= models.CharField("MARQUE",max_length=100, choices=MARQUE_BALASTRE)
	puissance_balastre= models.CharField("PUISSANCE DU BALASTRE",max_length=100, choices=PUISSANCE_BALASTRE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# BOTE
#=====================================================

class Botte(productbase.ProductBase):
	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# CABLE EN ACIER
#=====================================================

class CableEnAcier(productbase.ProductBase):
	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# CYCLOMETRE
#=====================================================

class Cyclometre(productbase.ProductBase):
	#les attributs
	type_cyclometre= models.CharField("TYPE DE CYCLOMETRE",max_length=100, choices=TYPE_CYCLOMETRE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# DAME SAUTEUSE
#=====================================================

class DameSauteuse(productbase.ProductBase):
	#les attributs
	marque= models.CharField("MARQUE",max_length=100, choices=MARQUE_SAUTEUSE)
	puissance= models.CharField("PUISSANCE",max_length=100, choices=PUISSANCE_SAUTEUSE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# DIAMANT COUPE CARREAUX
#=====================================================

class DiamantCoupeCarreaux(productbase.ProductBase):
	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# DISQUE DE SCIE
#=====================================================

class DisqueDeScie(productbase.ProductBase):
	#les attributs
	type_surface= models.CharField("TYPE DE SURFACE",max_length=100, choices=TYPE_SURFACE_SCIE)
	diametre= models.CharField("DIAMETRE(MILLIMETRE)",max_length=100, choices=DIAMETRE_SCIE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# FILTRE A EAU
#=====================================================

class FiltreAEau(productbase.ProductBase):
	#les attributs
	equipement= models.CharField("EQUIPEMENT",max_length=100, choices=EQUIPEMENT_FILTRE)
	dimension= models.CharField("DIMENSION (POUCE)",max_length=100, choices=DIMENSION_FILTRE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# FUMIGATEUR
#=====================================================

class Fumigateur(productbase.ProductBase):
	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# GLOBE POUR ECLAIRAGE
#=====================================================

class GlobePourEclairage(productbase.ProductBase):
	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# IMPERMEABLE
#=====================================================

class Impermeable(productbase.ProductBase):
	#les attributs
	type_impermeable= models.CharField("TYPE D'IMPERMEABLE",max_length=100, choices=TYPE_IMPERMEABLE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# LAME DE SCIE
#=====================================================

class LameDeScie(productbase.ProductBase):
	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# NETTOYEUR HAUTE PRESSION
#=====================================================

class NettoyeurHautePression(productbase.ProductBase):
	#les attributs
	pression= models.CharField("PRESSION",max_length=100, choices=PRESSION_NHP)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# PAPIER A PONCER
#=====================================================

class PapierAPoncer(productbase.ProductBase):
	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# PAQUET DE CLOUS A BETOUS
#=====================================================

class Clous(productbase.ProductBase):
	#les attributs
	dimension= models.CharField("DIMENSION",max_length=100, choices=DIMENSION_CLOUS)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# VISEUSE ÉLECTRIQUE
#=====================================================

class VisseuseElectrique(productbase.ProductBase):
	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# PLANTOIR
#=====================================================

class Plantoir(productbase.ProductBase):
	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# HALOGENE
#=====================================================

class Halogene(productbase.ProductBase):
	#les attributs
	type_halogene= models.CharField("TYPE D'HALOGENE",max_length=100, choices=TYPE_HALOGENE)
	puissance_halogene= models.CharField("PUISSANCE",max_length=100, choices=PUISSANCE_HALOGENE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# DEBROUSAILLEUSE
#=====================================================

class Debrousailleuse(productbase.ProductBase):
	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# CLE ALLEN
#=====================================================

class CleAllen(productbase.ProductBase):
	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# COFFRET DE CLE COMPLET
#=====================================================

class CoffretDeCleComplet(productbase.ProductBase):
	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# FIXATION TV
#=====================================================

class FixationTV(productbase.ProductBase):
	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# VIS METALLIQUE
#=====================================================

class VisMetallique(productbase.ProductBase):
	#les attributs
	quantite_par_paquet= models.CharField("QUANTITE PAR PAQUET",max_length=100, choices=QUANTITE_PAQUET)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# PINCEAU
#=====================================================

class Pinceau(productbase.ProductBase):
	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# FIL BARBELE
#=====================================================

class FilBarbele(productbase.ProductBase):
	#les attributs
	type_fil_barbele= models.CharField("DIMENSION",max_length=100, choices=TYPE_FIL_BARBELE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# SCIE CIRCULAIRE
#=====================================================

class ScieCirculaire(productbase.ProductBase):
	#les attributs
	type_scie_circulaire= models.CharField("TYPE DE SCIE",max_length=100, choices=TYPE_SCIE_CIRCULAIRE)
	marque_outillage= models.CharField("MARQUE",max_length=100, choices=MARQUE_SCIE)
	puissance_outillage= models.CharField("PUISSANCE",max_length=100, choices=PUISSANCE_SCIE)
	diametre_lame= models.CharField("DIAMETRE DE LAME(MILLIMETRE)",max_length=100, choices=DIAMETRE_LAME_SCIE)
	alimentation= models.CharField("ALIMENTATION",max_length=100, choices=ALIMENTATION_SCIE)
	tension= models.CharField("TENSION",max_length=100, choices=TENSION_SCIE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# FOREUSE
#=====================================================

class ForeusePerceuse(productbase.ProductBase):
	#les attributs
	type_de_perceuse= models.CharField("TYPE DE PERCEUSE",max_length=100, choices=TYPE_PERCEUSE)
	marque_outillage= models.CharField("MARQUE",max_length=100, choices=MARQUE_PERCEUSE)
	puissance_outillage= models.CharField("PUISSANCE",max_length=100, choices=PUISSANCE_PERCEUSE)
	transmission= models.CharField("TRANSMISSION",max_length=100, choices=TRASMISSION_PERCEUSE)
	porte_outils= models.CharField("PORTE OUTILS",max_length=100, choices=PORTE_OUTILS_PERCEUSE)
	tension_fonctionnement= models.CharField("TENSION",max_length=100, choices=TENSION_PERCEUSE)
	alimentation= models.CharField("ALIMENTATION",max_length=100, choices=ALIMENTATION_PERCEUSE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# TOURET A MEULET
#=====================================================

class TouretAMeulet(productbase.ProductBase):
	#les attributs
	marque_marchine= models.CharField("MARQUE",max_length=100, choices=MARQUE_TOURET)
	puissance_machine= models.CharField("PUISSANCE",max_length=100, choices=PUISSANCE_TOURET)
	diametre_disque= models.CharField("DIAMETRE DE DISQUE",max_length=100, choices=DIAMETRE_TOURET)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# MARTEAU
#=====================================================

class Marteau(productbase.ProductBase):
	#les attributs
	type_marteau= models.CharField("TYPE MARTEAU PIQUEUR",max_length=100, choices=TYPE_MARTEAU)
	marque_outillage= models.CharField("MARQUE",max_length=100, choices=MARQUE_MARTEAU)
	puissance_outillage= models.CharField("PUISSANCE",max_length=100, choices=PUISSANCE_MARTEAU)
	poids= models.CharField("POIDS(KILOGRAMME)",max_length=100, choices=POIDS_MARTEAU)
	alimentation= models.CharField("ALIMENTATION",max_length=100, choices=ALIMENTATION_MARTEAU)
	tension_fonctionnement= models.CharField("TENSION",max_length=100, choices=TENSION_MARTEAU)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# PROTECTIONS DE TRAVAIL
#=====================================================

class ProtectionDeTravail(productbase.ProductBase):
	#les attributs
	type_protection= models.CharField("TYPE DE PROTECTION",max_length=100, choices=TYPE_PROTECTION)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# LAMPE TORCHE
#=====================================================

class LampeTorche(productbase.ProductBase):
	#les attributs
	marque_torche= models.CharField("MARQUE",max_length=100, choices=MARQUE_TORCHE)
	type_de_lampe= models.CharField("TYPE DE LAMPE",max_length=100, choices=TYPE_LAMPE_TORCHE)
	type_ampoule= models.CharField("TYPE D'AMPOULE",max_length=100, choices=TYPE_EMPOULE_TORCHE)
	tension= models.CharField("TENSION",max_length=100, choices=TENSION_TORCHE)
	flux_lumineux= models.CharField("FLUX LUMINEUX",max_length=100, choices=FLUX_LUMINEUX_TORCHE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# RABOTEUSE
#=====================================================

class Raboteuse(productbase.ProductBase):
	#les attributs
	type_raboteuse= models.CharField("TYPE RABOTEUSE",max_length=100, choices=TYPE_RABOTEUSE)
	marque_outillage= models.CharField("MARQUE",max_length=100, choices=MARQUE_RABOTEUSE)
	puissance_outillage= models.CharField("PUISSANCE",max_length=100, choices=PUISSANCE_RABOTEUSE)
	largeur_rabotage= models.CharField("LARGEUR DE RABOTAGE",max_length=100, choices=LARGEUR_RABOTEUSE)
	alimentation= models.CharField("ALIMENTATION",max_length=100, choices=ALIMENTATION_RABOTEUSE)
	tension= models.CharField("TENSION",max_length=100, choices=TENSION_RABOTEUSE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# BURINEUR
#=====================================================

class Burineur(productbase.ProductBase):
	#les attributs
	marque_outillage= models.CharField("MARQUE",max_length=100, choices=MARQUE_BURINEUR)
	transmission= models.CharField("TRANSMISSION",max_length=100, choices=TRANSMISSION_BURINEUR)
	alimentation= models.CharField("ALIMENTATION",max_length=100, choices=ALIMENTATION_BURINEUR)
	consommation_air= models.CharField("CONSOMMATION D'AIR",max_length=100, choices=CONSOMMATION_BURINEUR)
	pression_air= models.CharField("PRESSION D'AIR",max_length=100, choices=PRESSION_BURINEUR)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# BOULONNEUSE
#=====================================================

class Boulonneuse(productbase.ProductBase):
	#les attributs
	marque_outillage= models.CharField("MARQUE",max_length=100, choices=MARQUE_BOULONNEUSE)
	puissance_outillage= models.CharField("TRANSMISSION",max_length=100, choices=PUISSANCE_BOULONNEUSE)
	transmission= models.CharField("ALIMENTATION",max_length=100, choices=TRANSMISSION_BOULONNEUSE)
	porte_outils= models.CharField("CONSOMMATION D'AIR",max_length=100, choices=PORTE_OUTIL_BOULONNEUSE)
	tension_fonctionnement= models.CharField("PRESSION D'AIR",max_length=100, choices=TENSION_BOULONNEUSE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']



#=====================================================
# VISSEUSE
#=====================================================

class Visseuse(productbase.ProductBase):
	#les attributs
	marque_outillage= models.CharField("MARQUE",max_length=100, choices=MARQUE_VISSEUSE)
	tension_batterie= models.CharField("TENSION",max_length=100, choices=TENSION_VISSEUSE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# VENTILATEUR PLAFONNIER
#=====================================================

class VentilateurPlafonier(productbase.ProductBase):
	#les attributs
	dimension_ventilateur  = models.CharField("DIMENSION VENTILATEUR",max_length=100, choices=DIMENSION_VENTILATEUR)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# TABLE PLASTIQUE
#=====================================================

class TablePlastique(productbase.ProductBase):
	#les attributs
	forme  = models.CharField("FORME",max_length=100, choices=FORME_TABLE)
	dimensions= models.CharField("DIMENSION",max_length=100, choices=DIMENSION_TABLE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# BOUILLOIRE
#=====================================================

class Bouilloire(productbase.ProductBase):
	#les attributs
	marque  = models.CharField("MARQUE",max_length=100, choices=MARQUE_BOUILLOIRE)
	volume = models.CharField("VOLUME",max_length=100, choices=VOLUME_BOUILLOIRE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# CAFETIERE
#=====================================================

class Cafetiere(productbase.ProductBase):
	#les attributs
	marque  = models.CharField("MARQUE",max_length=100, choices=MARQUE_CAFETIERE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# CHAUFFE EAU
#=====================================================

class ChauffeEau(productbase.ProductBase):
	#les attributs
	marque  = models.CharField("MARQUE",max_length=100, choices=MARQUE_CHAUFFE_EAU)
	volume = models.CharField("VOLUME EN LITRE",max_length=100, choices=VOLUME_CHAUFFE_EAU)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# DESTRUCTEUR PAPIER
#=====================================================

class DestructeurPapier(productbase.ProductBase):
	#les attributs
	marque  = models.CharField("MARQUE",max_length=100, choices=MARQUE_DESTR_PAPIER)
	capacite_papier  = models.CharField("CAPACITE PAPIER",max_length=100, choices=CAPACITE_DESTR_PAPIER)
	Volume_panier_dechet  = models.CharField("VOLUME PANIER DECHIQUETEUSE",max_length=100, choices=VOLUME_DESTR_PAPIER)
	destruction_cd  = models.CharField("AVEC DESRTUCTEUR CD",max_length=100, choices=DEST_CD)
	destruction_carte_credit = models.CharField("AVEC DESRTUCTEUR CARTE DE CREDIT",max_length=100, choices=DESTR_CARTE_CREDIT)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# CONGELATEUR
#=====================================================

class Congelateur(productbase.ProductBase):
	#les attributs
	marque  = models.CharField("MARQUE",max_length=100, choices=MARQUE_CONGELATEUR)
	volume = models.CharField("VOLUME EN LITRE",max_length=100, choices=VOLUME_CONGELATEUR)
	type_congelateur  = models.CharField("TYPE DE CONGELATEUR",max_length=100, choices=TYPE_CONGELATEUR)
	alimentation = models.CharField("ALIMENTATION",max_length=100, choices=ALIMENTATION)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# FRIGO
#=====================================================

class Frigo(productbase.ProductBase):
	#les attributs
	marque  = models.CharField("MARQUE",max_length=100, choices=MARQUE_FRIGO)
	volume = models.CharField("VOLUME EN LITRE",max_length=100, choices=VOLUME_FRIGO)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# MICRO ONDE
#=====================================================

class MicroOnde(productbase.ProductBase):
	#les attributs
	marque  = models.CharField("MARQUE",max_length=100, choices=MARQUE_MICROONDE)
	capacite  = models.CharField("CAPACITE",max_length=100, choices=CAPACITE_MICROONDE)
	puissance = models.CharField("PUISSANCE EN WATT",max_length=100, choices=PUISSANCE_MICROONDE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# TUYAU D'ARROSAGE
#=====================================================

class TuyauArrosage(productbase.ProductBase):
	#les attributs
	diametre  = models.CharField("DIAMETRE EN POUCE",max_length=100, choices=DIAMETRE_TUYAU)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']



#===21 - 05 - 2018 =================================
# CABLE COAXIAL
#===================================================

class CableCoaxial(productbase.ProductBase):
	#les attributs
	type_cable = models.CharField("TYPE DE CABLE",max_length=100, choices=TYPE_CABLE_COAXIAL)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#===21 - 05 - 2018 =================================
# CABLE POUR CAMERA CCD
#===================================================

class CableCameraCCD(productbase.ProductBase):
	#les attributs
	longueur = models.CharField("LONGUEUR DE CABLE",max_length=100, choices=LONGEUR_CABLE_CCD)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#===21 - 05 - 2018 =================================
# CAMERA IP
#===================================================

class CameraIP(productbase.ProductBase):
	#les attributs
	style_camera = models.CharField("STYLE DE CAMERA",max_length=100, choices=STYLE_CCD)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#===21 - 05 - 2018 =================================
# CAMERA CCD
#===================================================

class CameraCCD(productbase.ProductBase):
	#les attributs
	technologie = models.CharField("TECHNOLOGIE DE CAMERA CCD",max_length=100, choices=TECHNOLOGIE_CCD)
	style_camera = models.CharField("STYLE DE CAMERA",max_length=100, choices=STYLE_CCD)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#===21 - 05 - 2018 =================================
# CHAINE DE SECURITE POUR LAPTOP
#===================================================

class ChaineDeSecuritePourLaptop(productbase.ProductBase):
	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#===21 - 05 - 2018 =================================
# CHARGEUR POUR CAMERA CCD
#===================================================

class ChargeurCameraCCD(productbase.ProductBase):
	#les attributs
	tension = models.CharField("TENSION DU CHARGEUR",max_length=100, choices=TENSION_CHARGEUR_CCD)
	intensite = models.CharField("INTENSITE DU CHARGEUR",max_length=100, choices=INTENSITE_CHARGEUR_CCD)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#===21 - 05 - 2018 =================================
# CONNECTEUR BNC
#===================================================

class ConnecteurBNC(productbase.ProductBase):
	#les attributs
	type_connecteur = models.CharField("TYPE DE CONNECTEUR",max_length=100, choices=TYPE_CONNECTEUR_BNC)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#===21 - 05 - 2018 =================================
# CONNECTEUR D’ALIMENTATION FEMELLE POUR CAMERA CCD
#===================================================

class ConnecteurAlimentationFemmelleCCD(productbase.ProductBase):
	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#===21 - 05 - 2018 =================================
# ENREGISTREUR CCD
#===================================================

class EnregistreurCCD(productbase.ProductBase):
	#les attributs
	type_enregisteur = models.CharField("TYPE D'ENREGISTREUR",max_length=100, choices=TYPE_ENREGISTREUR)
	nombre_canaux = models.CharField("NOMBRE DE CANAUX",max_length=100, choices=NBRE_CANAUX)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#===21 - 05 - 2018 =================================
# LENTILLE POUR CAMERA CCD
#===================================================

class LentilleCameraCCD(productbase.ProductBase):
	#les attributs
	distance_focale = models.CharField("DISTANCE FOCALE EN MILLIMETRE",max_length=100, choices=DISTANCE_FOCALE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#===21 - 05 - 2018 =================================
# MICROPHONE POUR CAMERA IP
#===================================================

class MicrophonePourCameraIP(productbase.ProductBase):
	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#===21 - 05 - 2018 =================================
# ROULEAU CABLE COAXIAL
#===================================================

class RouleauCableCoaxial(productbase.ProductBase):
	#les attributs
	type_cable = models.CharField("TYPE DE CABLE",max_length=100, choices=TYPE_CABLE_COAXIAL)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#===21 - 05 - 2018 =================================
# SAC A DOS
#===================================================

class SacADos(productbase.ProductBase):
	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#===21 - 05 - 2018 =================================
# UNITE D’ALIMENTATION POUR CAMERA CCD
#===================================================

class UniteAlimlentationCameraCCD(productbase.ProductBase):
	#les attributs
	tension = models.CharField("TENSION DE L'ALIMENTATION",max_length=100, choices=TENSION_CHARGEUR_CCD)
	intensite = models.CharField("INTENSITE  DE L'ALIMENTATION",max_length=100, choices=INTENSITE_ALIMENTATION_CCD)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']



#====== 23-05-2018 =================================
# APPAREIL DE GYM
#===================================================

class AppareilDeGym(productbase.ProductBase):
	#les attributs
	nombre_station = models.CharField("NOMBRE DE STATION",max_length=100, choices=NOMBRE_STATION)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#====== 23-05-2018 =================================
# BOITIER ARRIERE POUR SOCKET MURAL
#===================================================

class BoitierSocketMural(productbase.ProductBase):
	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']




#====== 23-05-2018 =================================
# ENSEMBLE DE POIDS POUR BANC DE MUSCULATION
#===================================================

class EnsemblePoidsMuscul(productbase.ProductBase):
	#les attributs
	poids = models.CharField("POIDS EN KILOGRAMME",max_length=100, choices=POIDS_MUSCUL)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']



#====== 23-05-2018 =================================
# VELO ELLIPTIQUE
#===================================================

class VeloElliptique(productbase.ProductBase):
	#les attributs
	modele = models.CharField("MODELE VELO",max_length=100, choices=MODELE_VELO)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#====== 23-05-2018 =================================
# TAPIS DE COURSE
#===================================================

class TapisDeCourse(productbase.ProductBase):
	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']



#====== 23-05-2018 =================================
# VELO MAGNETIQUE
#===================================================

class VeloMagnetique(productbase.ProductBase):
	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']



#======== 23-05-2018 =================================
# PLAQUE DE FACE DOUBLE POUR SOCKET MURALE
#=====================================================

class PlaqueAFaceDoublePourSocketMural(productbase.ProductBase):
	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']



#====== 23-05-2018 =================================
# POINCON
#===================================================

class Poincon(productbase.ProductBase):
	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']
