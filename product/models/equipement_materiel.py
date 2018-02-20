from product.models import *
from utils.product_attributes.equipement_materiel import *
from utils.unite_prix import UNITE

# Create your models here.

#=====================================================
# 1. Boite cuisinière
#=====================================================
class BoiteCuisiniere(productbase.ProductBase):
	dimension =models.CharField("DIMENSION", max_length=20, choices= DIMENSION	)
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
	intensite = models.CharField("INTENSITE",max_length=50, choices=INTENSITE)
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
	intensite = models.CharField("INTENSITE",max_length=50, choices=INTENSITE)
	nombre_phase = models.CharField("NOMBRE DE PHASE",max_length=50, choices=NOMBRE_POLE)
	sensibilite = models.CharField("SENSIBILITTE",max_length=50, choices=SENSIBILITE_INTERRUPTEUR)
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
	intensite = models.CharField("INTENSITE",max_length=50, choices=INTENSITE)
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
	intensite = models.CharField("INTENSITE",max_length=50, choices=INTENSITE_DISJONCTEUR_MOTEUR)
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
	intensite = models.CharField("INTENSITE",max_length=50, choices=INTENSITE_INVERSEUR)
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
	units = models.CharField(max_length=20, choices=UNITE)
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
	puissance_groupe=models.CharField("PUISSANCE",max_length=20, choices=PUISSANCE_GROUPE_ELECTROGENE)
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
	marque_marchine=models.CharField("MARQUE",max_length=20, choices=MARQUE_MACHINE_ATELIER)
	puissance_compresseur=models.CharField("PUISSANCE",max_length=20, choices=PUISSANCE_COMPRESSEUR)
	debit=models.CharField("DEBIT",max_length=20, choices= DEBIT_L_MIN)
	capacite_compresseur=models.CharField("CAPACITE",max_length=20, choices=CAPACITE_COMPRESSEUR)
	pression=models.CharField("CAPACITE",max_length=20, choices=PRESSION)
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
	capacite=models.CharField("CAPACITE",max_length=20, choices=CAPACITE_L)
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
	marque=models.CharField("MARQUE ", max_length=20, choices= MARQUE)
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
	section =models.CharField("SECTION", max_length=20, choices= SECTION )
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 62. CABLE MASSE
#=====================================================
class CableMasse(productbase.ProductBase):
	section =models.CharField("SECTION", max_length=20, choices= SECTION )
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
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
	intensite =models.CharField("INTENSITE", max_length=20, choices= INTENSITE )
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
	intensite =models.CharField("INTENSITE", max_length=20, choices= INTENSITE )
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
	intensite =models.CharField("INTENSITE", max_length=20, choices= INTENSITE )
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
	section =models.CharField("SECTION", max_length=20, choices= SECTION )
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# 71. INVERSEUR A COFFRET
#=====================================================
class InverseurCoffret(productbase.ProductBase):
	marque =models.CharField("MARQUE", max_length=20, choices= MARQUE )
	intensite =models.CharField("INTENSITE", max_length=20, choices= INTENSITE )
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
	marque =models.CharField("MARQUE", max_length=20, choices= MARQUE)
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
	longueur = models.CharField("LONGUEUR",max_length=100, choices=LONGUEUR)
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
	marque = models.CharField("PUISSANCE TONDEUSE",max_length=100, choices=MARQUE_EQUIPEMENT)




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
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']