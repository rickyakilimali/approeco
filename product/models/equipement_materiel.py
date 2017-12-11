from product.models import *
from utils.product_attributes.equipement_materiel import FORCE,POIDS,DIMENSION,DIMENSION_BOITE_CUISINIERE, DIMENSION_CLEF_MOLETTE, MARQUE_EQUIPEMENT, INTENSITE, NOMBRE_PHASE, NOMBRE_POLE, SENSIBILITE_INTERRUPTEUR, DIMENSION_EQUERRE, MATIERE_SECHE_MAIN, POIDS_MONTE_CHARGE, MARQUE_PRISE_ELECTRIQUE, DIMENSION_PAUMELLE, TYPE_GANT, TYPE_CYLINDRE, INTENSITE_INVERSEUR, TYPES_APPAREIL_MESURE, MARQUE_PRISE_ELECTRIQUE, LONGUEUR, NOMBRE_PRISE, TYPE_DERIVATION, NOMBRE_MODULE, ENCASTRE_SAILLI, PUISSANCE_CONTACTEUR, TYPE_ACCESSOIRES_HYDROPHORE, UTILISATION, SANITAIRE, REDUCTION_PVC, TYPE_AMPOULE, CULOT, PUISSANCE_AMPOULE_ELECTRIQUE, FORME_AMPOULE, TENSION, INTENSITE, DIAMETRE, TYPE_OUTILS_JARDINAGE, TYPES_BALANCE, MATIERE_TUYAUTERIE, LOCALISATION_TUYAUTERIE,MOTEUR, SECTION_MOTO_POMPE, PUISSANCE_MOTO_POMPE,MARQUE_MACHINE_ATELIER,CAPACITE_CHARGEUR_BATTERIE,FORMAT,LONGUEUR,MARQUE_MACHINE_ATELIER,CAPACITE_POMPE,PUISSANCE_POMPE,HAUTEUR_POMPE,DEBIT_POMPE,TYPE_MACHINE_ATELIER_NON_PORTATIF,PUISSANCE_MACHINE_ATELIER_NON_PORTATIF,TYPE_MACHINE_ATELIER_PORTATIF,MOTEUR,OUI_NON,PUISSANCE_GROUPE_ELECTROGENE,CAPACITE_COMPRESSEUR,PUISSANCE_COMPRESSEUR,PRESSION,MODE_DETECTION,MARQUE_MOTEUR,TENSION_MOTEUR,PUISSANCE_MOTEUR,MARQUE_CONVERTISSEUR, PUISSANCE_CONVERTISSEUR, TENSION_CONVERTISSEUR,MODE_FONCTIONNEMENT,NOMBRE_CANAUX,SCHEMA_INTERRUPTEUR,INTENSITE_DISJONCTEUR_MOTEUR,TYPE_PRISE_ELECTRIQUE
from utils.unite_prix import UNITE

# Create your models here.

#=====================================================
# 1. Boite cuisinière
#=====================================================
class BoiteCuisiniere(productbase.ProductBase):
	dimension = models.CharField(max_length=50, choices=DIMENSION_BOITE_CUISINIERE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 2. Clef à molette
#=====================================================
class ClefMolette(productbase.ProductBase):
	dimension_clef_molette = models.CharField(max_length=50, choices=DIMENSION_CLEF_MOLETTE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 3. Disjoncteur
#=====================================================
class Disjoncteur(productbase.ProductBase):
	marque = models.CharField(max_length=50, choices=MARQUE_EQUIPEMENT)
	intensite = models.CharField(max_length=50, choices=INTENSITE)
	nombre_phase = models.CharField(max_length=50, choices=NOMBRE_PHASE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 4. Interrupteur differentiel
#=====================================================
class InterrupteurDifferentiel(productbase.ProductBase):
	marque = models.CharField(max_length=50, choices=MARQUE_EQUIPEMENT)
	intensite = models.CharField(max_length=50, choices=INTENSITE)
	nombre_phase = models.CharField(max_length=50, choices=NOMBRE_POLE)
	sensibilite = models.CharField(max_length=50, choices=SENSIBILITE_INTERRUPTEUR)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 5. Fusible
#=====================================================
class Fusible(productbase.ProductBase):
	marque = models.CharField(max_length=50, choices=MARQUE_EQUIPEMENT)
	intensite = models.CharField(max_length=50, choices=INTENSITE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 6. Equerre
#=====================================================
class Equerre(productbase.ProductBase):
	dimension = models.CharField(max_length=50, choices=DIMENSION_EQUERRE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 7. Seche main
#=====================================================
class SecheMain(productbase.ProductBase):
	matiere = models.CharField(max_length=50, choices=MATIERE_SECHE_MAIN)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 8. Monte charge
#=====================================================
class MonteCharge(productbase.ProductBase):
	poids = models.CharField(max_length=50, choices=POIDS_MONTE_CHARGE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 9. Interrupteur électrique
#=====================================================
class InterrupteurElectrique(productbase.ProductBase):
	marque = models.CharField(max_length=50, choices=MARQUE_PRISE_ELECTRIQUE)
	schema = models.CharField(max_length=50, choices=SCHEMA_INTERRUPTEUR)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 10. Disjoncteur moteur 
#=====================================================
class DisjoncteurMoteur(productbase.ProductBase):
	marque = models.CharField(max_length=50, choices=MARQUE_EQUIPEMENT)
	intensite = models.CharField(max_length=50, choices=INTENSITE_DISJONCTEUR_MOTEUR)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 11. Paumelle
#=====================================================
class Paumelle(productbase.ProductBase):
	dimension = models.CharField(max_length=50, choices=DIMENSION_PAUMELLE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 12. Paumelle
#=====================================================
class Gant(productbase.ProductBase):
	type_gant = models.CharField(max_length=50, choices=TYPE_GANT)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 13. Cylindre
#=====================================================
class Cylindre(productbase.ProductBase):
	type_cylindre = models.CharField(max_length=50, choices=TYPE_CYLINDRE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 14. Palan mécanique 
#=====================================================
class PalanMecanique(productbase.ProductBase):
	poids = models.CharField(max_length=50, choices=POIDS_MONTE_CHARGE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 15. Inverseur
#=====================================================
class Inverseur(productbase.ProductBase):
	intensite = models.CharField(max_length=50, choices=INTENSITE_INVERSEUR)
	nombre_prise = models.CharField(max_length=50, choices=NOMBRE_PRISE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)



#=====================================================
# 16. Appreil de mesure
#=====================================================
class AppareilDeMesure(productbase.ProductBase):
	type_appareil_mesure = models.CharField(max_length=1, choices=TYPES_APPAREIL_MESURE)
	tension = models.CharField(max_length=20, choices=TENSION)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	unite_prix = models.CharField(max_length=20, choices=UNITE)

#=====================================================
# 17. Prise électrique
#=====================================================
class PriseElectrique(productbase.ProductBase):
	marque = models.CharField(max_length=20, choices=MARQUE_PRISE_ELECTRIQUE)
	type_prise = models.CharField(max_length=20, choices=TYPE_PRISE_ELECTRIQUE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)

#=====================================================
# 18. Rallonge 
#=====================================================
class Rallonge(productbase.ProductBase):
	longueur = models.CharField(max_length=20, choices=LONGUEUR)
	nombre_prise = models.CharField(max_length=20, choices=NOMBRE_PRISE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)

#=====================================================
# 19. Boite de dérivation
#=====================================================
class BoiteDerivation(productbase.ProductBase):
	marque = models.CharField(max_length=20, choices=MARQUE_EQUIPEMENT)
	type_derivation = models.CharField(max_length=20, choices=TYPE_DERIVATION)
	dimension=models.CharField(max_length=20, choices=DIMENSION)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)

#=====================================================
# 20. Coffret électrique
#=====================================================
class CoffretElectrique(productbase.ProductBase):
	marque = models.CharField(max_length=20, choices=MARQUE_EQUIPEMENT)
	nombre_module = models.CharField(max_length=20, choices=NOMBRE_MODULE)
	encastre_sailli=models.CharField(max_length=20, choices=ENCASTRE_SAILLI)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)

#=====================================================
# 21. Contacteur
#=====================================================
class Contacteur(productbase.ProductBase):
	marque = models.CharField(max_length=20, choices=MARQUE_EQUIPEMENT)
	puissance = models.CharField(max_length=20, choices=PUISSANCE_CONTACTEUR)
	tension=models.CharField(max_length=20, choices=TENSION)
	intensite=models.CharField(max_length=20, choices=INTENSITE)
	nombre_pole=models.CharField(max_length=20, choices=NOMBRE_POLE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)

#=====================================================
# 22. Mèche à beton 
#=====================================================
class MecheBeton(productbase.ProductBase):
	diametre = models.CharField(max_length=20, choices=DIAMETRE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)

#=====================================================
# 23. Outils de jardinage
#=====================================================
class OutilsJardinage(productbase.ProductBase):
	type_outils = models.CharField(max_length=20, choices=TYPE_OUTILS_JARDINAGE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)

#=====================================================
# 24. Balance
#=====================================================
class Balance(productbase.ProductBase):
	type_balance = models.CharField(max_length=20, choices=TYPES_BALANCE)
	poids=models.CharField(max_length=10, choices=POIDS)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)

#=====================================================
# 25. Tuyauterie
#=====================================================
class Tuyauterie(productbase.ProductBase):
	matiere_tuyauterie = models.CharField(max_length=20, choices=MATIERE_TUYAUTERIE)
	localisation=models.CharField(max_length=10, choices=LOCALISATION_TUYAUTERIE)
	diametre=models.CharField(max_length=20, choices=DIAMETRE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)

#=====================================================
# 26. Accessoires hydrophore
#=====================================================
class AccessoiresHydrophore(productbase.ProductBase):
	type_accessoires_hydrophore = models.CharField(max_length=20, choices=TYPE_ACCESSOIRES_HYDROPHORE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)

#=====================================================
# 27. Flexibe 
#=====================================================
class Flexible(productbase.ProductBase):
	utilisation = models.CharField(max_length=20, choices=UTILISATION)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)

#=====================================================
# 28. Siphon
#=====================================================
class Siphon(productbase.ProductBase):
	sanitaire = models.CharField(max_length=20, choices=SANITAIRE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)

#=====================================================
# 29. Réduction PVC
#=====================================================
class ReductionPvc(productbase.ProductBase):
	reduction = models.CharField(max_length=20, choices=REDUCTION_PVC)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)

#=====================================================
# 30. Ampoule électrique
#=====================================================
class AmpouleElectrique(productbase.ProductBase):
	type_ampoule = models.CharField(max_length=20, choices=TYPE_AMPOULE)
	culot = models.CharField(max_length=20, choices=CULOT)
	puissance_ampoule = models.CharField(max_length=20, choices=PUISSANCE_AMPOULE_ELECTRIQUE)
	forme_ampoule = models.CharField(max_length=20, choices=FORME_AMPOULE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)

#=====================================================
# 31. Moto pompe 
#=====================================================
class MotoPompe(productbase.ProductBase):
	moteur = models.CharField(max_length=20, choices=MOTEUR)
	section_moto_pompe = models.CharField(max_length=20, choices=SECTION_MOTO_POMPE)
	puissance_moto_pompe = models.CharField(max_length=20, choices=PUISSANCE_MOTO_POMPE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)

#=====================================================
# 32. Chargeur Batterie
#=====================================================
class ChargeurBatterie(productbase.ProductBase):
	marque_chargeur=models.CharField(max_length=20, choices=MARQUE_MACHINE_ATELIER)
	capacite_chargeur = models.CharField(max_length=20, choices=CAPACITE_CHARGEUR_BATTERIE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)

#=====================================================
# 33. Enseigne lumineuse
#=====================================================
class EnseigneLumineuse(productbase.ProductBase):
	format_enseigne=models.CharField(max_length=20, choices=FORMAT)
	longueur = models.CharField(max_length=20, choices=LONGUEUR)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)

#=====================================================
# 34. Pompe hydrophore 
#=====================================================
class PompeHydrophore(productbase.ProductBase):
	marque_pompe=models.CharField(max_length=20, choices=MARQUE_MACHINE_ATELIER)
	capacite_pompe = models.CharField(max_length=20, choices=CAPACITE_POMPE)
	puissance_pompe=models.CharField(max_length=20, choices=PUISSANCE_POMPE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)

#=====================================================
# 35. Pompe de forage
#=====================================================
class PompeForage(productbase.ProductBase):
	marque_pompe=models.CharField(max_length=20, choices=MARQUE_MACHINE_ATELIER)
	force_pompe = models.CharField(max_length=20, choices=FORCE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)

#=====================================================
# 36. Pompe à eau
#=====================================================
class PompeEau(productbase.ProductBase):
	marque_pompe=models.CharField(max_length=20, choices=MARQUE_MACHINE_ATELIER)
	hauteur_pompe = models.CharField(max_length=20, choices=HAUTEUR_POMPE)
	puissance_pompe=models.CharField(max_length=20, choices=PUISSANCE_POMPE)
	debit_pompe = models.CharField(max_length=20, choices=DEBIT_POMPE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)

#=====================================================
# 37. Machine atelier non portatif 
#=====================================================
class MachineAtelierNonPortatif(productbase.ProductBase):
	marque_marchine=models.CharField(max_length=20, choices=MARQUE_MACHINE_ATELIER)
	type_machine_non_portatif = models.CharField(max_length=20, choices=TYPE_MACHINE_ATELIER_NON_PORTATIF)
	puissance_machine=models.CharField(max_length=20, choices=PUISSANCE_MACHINE_ATELIER_NON_PORTATIF)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)

#=====================================================
# 38. Machine atelier portatif
#=====================================================
class MachineAtelierPortatif(productbase.ProductBase):
	marque_marchine=models.CharField(max_length=20, choices=MARQUE_MACHINE_ATELIER)
	type_machine_portatif = models.CharField(max_length=20, choices=TYPE_MACHINE_ATELIER_PORTATIF)
	tension=models.CharField(max_length=20, choices=TENSION)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)

#=====================================================
# 39. Groupe électrogène
#=====================================================
class GroupeElectrogene(productbase.ProductBase):
	marque_marchine=models.CharField(max_length=20, choices=MARQUE_MACHINE_ATELIER)
	moteur = models.CharField(max_length=20, choices=MOTEUR)
	silencieux=models.CharField(max_length=20, choices=OUI_NON)
	puissance_groupe=models.CharField(max_length=20, choices=PUISSANCE_GROUPE_ELECTROGENE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)

#=====================================================
# 40. Compresseur 
#=====================================================
class Compresseur(productbase.ProductBase):
	marque_marchine=models.CharField(max_length=20, choices=MARQUE_MACHINE_ATELIER)
	capacite_compresseur = models.CharField(max_length=20, choices=CAPACITE_COMPRESSEUR)
	puissance_compresseur=models.CharField(max_length=20, choices=PUISSANCE_COMPRESSEUR)
	pression=models.CharField(max_length=20, choices=PRESSION)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)

#=====================================================
# 41. Detecteur d'intrusion
#=====================================================
class DetecteurIntrusion(productbase.ProductBase):
	mode_detection=models.CharField(max_length=20, choices=MODE_DETECTION)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)

#=====================================================
# 42. Moteur électrique
#=====================================================
class MoteurElectrique(productbase.ProductBase):
	marque_moteur=models.CharField(max_length=20, choices=MARQUE_MOTEUR)
	tension_moteur=models.CharField(max_length=20, choices=TENSION_MOTEUR)
	puissance_moteur=models.CharField(max_length=20, choices=PUISSANCE_MOTEUR)
	nombre_pole=models.CharField(max_length=20, choices=NOMBRE_POLE)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)

#=====================================================
# 43. Convertisseur 
#=====================================================
class Convertisseur(productbase.ProductBase):
	marque_convertisseur=models.CharField(max_length=20, choices=MARQUE_CONVERTISSEUR)
	puissance_convertisseur=models.CharField(max_length=20, choices=PUISSANCE_CONVERTISSEUR)
	tension_convertisseur=models.CharField(max_length=20, choices=TENSION_CONVERTISSEUR)
	Chargeur_convertisseur=models.CharField(max_length=20, choices=OUI_NON)
	sinus_pur=models.CharField(max_length=20, choices=OUI_NON)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)

#=====================================================
# 44. Controle d'accès et pointage
#=====================================================
class ControleAccesEtPointage(productbase.ProductBase):
	marque_equipement=models.CharField(max_length=50, choices=MARQUE_EQUIPEMENT)
	mode_fonctionnement=models.CharField(max_length=50, choices=MODE_FONCTIONNEMENT)
	pointage_presence=models.CharField(max_length=50, choices=OUI_NON)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)

#=====================================================
# 45. Enregistreur caméra de surveillance
#=====================================================
class EnregistreurCameraSurveillance(productbase.ProductBase):
	nombre_canaux=models.CharField(max_length=20, choices=NOMBRE_CANAUX)
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	units = models.CharField(max_length=20, choices=UNITE)