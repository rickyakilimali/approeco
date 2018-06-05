from product.models import *
from utils.product_attributes.informatique import *
#MARQUE_INFORMATIQUE, TYPE_DE_PROCESSEUR, CAPACITE_DISQUE_DUR, CAPAPCITE_MEMOIRE_RAM, SYSTEME_EXPLOITATION, TAILLE_ECRAN, TECHNOLOGIE_IMPRESSION, COULEUR, RECTOVERSO, MULTIFONCTION, FORMAT
from utils.unite_prix import *

#=====================================================
# 1. IMPRIMANTE
#=====================================================
# Nom de la class
class Imprimante(productbase.ProductBase):

	#les attributs
	marque_imprimante  = models.CharField("MARQUE",max_length=50, choices=MARQUE_IMPRIMANTE)
	technologie = models.CharField("TECHNOLOGIE",max_length=50, choices=TECHNOLOGIE_IMPRESSION)
	modele	= models.CharField("MODELE",max_length=50, choices=MODEL_IMPRIMANTE)
	couleur = models.CharField("COULEUR D'IMPRESSION",max_length=50, choices=COULEUR_IMPRIMANTE)
	multifonction = models.CharField("OPTION MULTIFONCTION",max_length=50, choices=MULTIFONCTION)
	recto_verso = models.CharField("RECTO VERSO",max_length=50, choices=RECTO_VERSO)
	format_max_papier = models.CharField("FORMAT MAXIMUM",max_length=50, choices=FORMAT_MAXIMUM_PAPIER)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']



#=====================================================
# PHOTOCOPIEUSE
#=====================================================
# Nom de la class
class Photocopieuse(productbase.ProductBase):

	#les attributs
	marque_photocopieuse  = models.CharField("MARQUE PHOTOCOPIEUSE",max_length=50, choices=MARQUE_IMPRIMANTE)
	technologie = models.CharField("TECHNOLOGIE",max_length=50, choices=TECHNOLOGIE_IMPRESSION)



	recto_verso = models.CharField("RECTO VERSO",max_length=50, choices=RECTO_VERSO)
	reseau = models.CharField("CONNEXION RESEAU",max_length=50, choices=RESEAU)
	format_max_papier = models.CharField("FORMAT MAXIMUM",max_length=50, choices=FORMAT_MAXIMUM_PAPIER)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# 2. DESKTOP
#=====================================================
# Nom de la class
class Desktop(productbase.ProductBase):

	#les attributs
	marque_desktop= models.CharField("MARQUE",max_length=50, choices=MARQUE_ORDINATEUR)
	type_processeur = models.CharField("TYPE DE PROCESSEUR",max_length=50, choices= TYPE_DE_PROCESSEUR)
	memoire_ram = models.CharField("MEMOIRE RAM",max_length=50, choices=CAPACITE_MEMOIRE)
	capacite_disque_dur = models.CharField("CAPACITE DU DISQUE DUR",max_length=50, choices= CAPACITE_DISQUE_DUR)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 3. LAPTOP
#=====================================================
# Nom de la class
class Laptop(productbase.ProductBase):

	#les attributs
	marque_laptop= models.CharField("MARQUE LAPTOP",max_length=50, choices=MARQUE_ORDINATEUR)
	type_processeur = models.CharField("TYPE DE PROCESSEUR",max_length=50, choices= TYPE_DE_PROCESSEUR)
	memoire_ram = models.CharField("MEMOIRE RAM",max_length=50, choices=CAPACITE_MEMOIRE)
	capacite_disque_dur = models.CharField("CAPACITE DU DISQUE DUR",max_length=50, choices=CAPACITE_DISQUE_DUR)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']



#=====================================================
# 4. CARTOUCHE
#=====================================================
class Cartouche(productbase.ProductBase):

	#les attributs
	marque_cartouche= models.CharField("MARQUE DE LA CARTOUCHE",max_length=50, choices=MARQUE_CARTOUCHE)
	numero_cartouche = models.CharField("NUMERO DE SERIE",max_length=50, choices=NUMERO_CARTOUCHE)
	couleur_cartouche = models.CharField("COULEUR DE LA CARTOUCHE",max_length=50, choices=COULEUR_CARTOUCHE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']



#=====================================================
# 5. UNITE DE STOCKAGES
#=====================================================
class Unite_stockage(productbase.ProductBase):

	#les attributs
	marque = models.CharField("MARQUE",max_length=50, choices=MARQUE_UNITE_STOCKAGE)
	type_stockage= models.CharField("TYPE DE STOCKAGE",max_length=50, choices=TYPE_DE_STOCKAGE)
	capacite_memoire = models.CharField("CAPAPCITE DE STOCKAGE",max_length=50, choices=CAPACITE_MEMOIRE_STOCKAGE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# 6. SMARTPHONE
#=====================================================


#=====================================================
# 7. LOGICIEL
#=====================================================
class Logiciel(productbase.ProductBase):

	#les attributs
	marque= models.CharField("MARQUE",max_length=50, choices=MARQUE_ANTIVIRUS)
	type_logiciel= models.CharField("TYPE DE LOGICIEL",max_length=50, choices=TYPE_LOGICIEL)

	licence = models.CharField("LICENCE",max_length=50, choices=LICENCE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 8. SWITCH
#=====================================================
class Switch(productbase.ProductBase):

	#les attributs
	type_equipement= models.CharField("TYPE D'EQUIPEMENT",max_length=50, choices=TYPE_EQUIPEMENT)
	marque = models.CharField("MARQUE",max_length=50, choices=MARQUE_RESEAU)
	nombre_port= models.CharField("NOMBRE DE PORTS",max_length=50, choices= NOMBRE_PORT_SWITCH)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# 9. VIDEO PROJECTEUR
#=====================================================
class Videoprojecteur(productbase.ProductBase):

	#les attributs
	marque = models.CharField("MARQUE",max_length=50, choices=MARQUE_VIDEOPROJECTEUR)
	puissance= models.CharField("PUISSANCE",max_length=50, choices= PUISSANCE_VIDEOPROJECTEUR)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 10. ROUTEUR
#=====================================================
class Routeur(productbase.ProductBase):

	#les attributs
	marque = models.CharField("MARQUE",max_length=50, choices=MARQUE_RESEAU)
	wifi= models.CharField("WIFI",max_length=50, choices= WIFI)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 11. SOURIS
#=====================================================
class Souris(productbase.ProductBase):

	#les attributs
	technologie = models.CharField("TECHNOLOGIE",max_length=50, choices= AVEC_FIL)
	prix = models.DecimalField("PRIX",max_digits=5, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 11. CLAVIER
#=====================================================
class Clavier(productbase.ProductBase):

	#les attributs
	type_clavier = models.CharField("TYPE",max_length=50, choices= TYPE_CLAVIER)
	prix = models.DecimalField("PRIX",max_digits=5, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 12. MODEM WIFI
#=====================================================
class ModemWifi(productbase.ProductBase):

	#les attributs
	marque = models.CharField("MARQUE",max_length=50, choices= MARQUE_INFORMATIQUE)
	prix = models.DecimalField("PRIX",max_digits=5, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 12. CABLE INFORMATIQUE
#=====================================================
class CableInformatique(productbase.ProductBase):

	#les attributs
	type_cable = models.CharField("TYPE DE CABLE",max_length=50, choices= TYPE_CABLE_INFORMATIQUE)
	longueur = models.CharField("LONGUEUR",max_length=50, choices= LONGUEUR_CABLE_INFORMATIQUE)
	prix = models.DecimalField("PRIX",max_digits=5, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']



#=====================================================
# 14. POINT D'ACCES
#=====================================================
class PointAcces(productbase.ProductBase):
	marque= models.CharField("MARQUE",max_length=50, choices=MARQUE_INFORMATIQUE)
	fonction_modem = models.CharField("FONCTION MODEM",max_length=50, choices=FONCTION_MODEM)
	prix = models.DecimalField("PRIX",max_digits=5, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 14. COFFRE FORT
#=====================================================






#=====================================================
# 19. SERVEUR
#=====================================================
class Serveur(productbase.ProductBase):
	marque = models.CharField("MARQUE",max_length=50, choices=MARQUE_ORDINATEUR)
	modele_serveur = models.CharField("MODELE",max_length=50, choices= MODELE_SERVEUR)
	type_serveur = models.CharField("TYPE DE SERVEUR",max_length=50, choices= TYPE_SERVEUR)
	type_processeur = models.CharField("TYPE DE PROCESSEUR",max_length=50, choices= TYPE_DE_PROCESSEUR)
	capacite_disque_dur = models.CharField("CAPACITE DU DISQUE DUR",max_length=50, choices= CAPACITE_DISQUE_DUR)
	controleur_raid = models.CharField("CONTROLEUR RAID",max_length=50, choices= CONTROLEUR_RAID)
	capacite_ram_max = models.CharField("MEMOIRE RAM MAXIMUM",max_length=50, choices=CAPACITE_MEMOIRE)

	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 20. ADRESSE IP PUBLIQUE
#=====================================================
class AdresseIpPublique(productbase.ProductBase):
	nombre_adresse_maximum =models.CharField("NOMBRE D'IP PUBLIQUE MAXIMUM", max_length=20, choices= NOMBRE_ADRESSE_MAXIMUM)
	prix = models.DecimalField("PRIX", max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_AN)
	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 21. BANDE PASSANTE
#=====================================================
class BandePassante(productbase.ProductBase):
	type_bande_passante =models.CharField("TYPE DE BANDE PASSANTE", max_length=20, choices= TYPE_BANDE_PASSANTE)
	debit_download =models.CharField("DEBIT EN DOWNLOAD", max_length=20, choices= DEBIT_DOWNLOAD)
	debit_upload =models.CharField("DEBIT EN UPLOAD", max_length=20, choices= DEBIT_UPLOAD)
	frais_installation =models.CharField("FRAIS D'INSTALLATION", max_length=20, choices= FRAIS_INSTALLATION)
	prix = models.DecimalField("PRIX", max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_MOIS)
	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
#
#=====================================================

#=====================================================
# 23. HEBERGEMENT SITE WEB
#=====================================================
class HebergementSiteWeb(productbase.ProductBase):
	type_hebergement=models.CharField("TYPE D'HEBERGEMENT", max_length=50, choices= TYPE_HEBERGEMENT)
	prix = models.DecimalField("PRIX", max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_AN)
	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 24.
#=====================================================
class Tablette(productbase.ProductBase):
	marque_tablette=models.CharField("MARQUE", max_length=100, choices= MARQUE_TABLETTE)
	modele_tablette=models.CharField("MODELE", max_length=100, choices= MODELE_TABLETTE)
	systeme_exploitation=models.CharField("SYSTEME D'EXPLOITATION", max_length=100, choices= SYSTEME_EXPLOITATION)
	memoire_tablette=models.CharField("MEMOIRE", max_length=20, choices= CAPACITE_MEMOIRE)
	prix = models.DecimalField("PRIX", max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# CAHIER DE CHARGES
#=====================================================
class CahierCharges(productbase.ProductBase):

	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# HELPDESK
#=====================================================
class Helpdesk(productbase.ProductBase):

	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_HEURE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# Installation logiciel serveur
#=====================================================
class InstallationLogicielServeur(productbase.ProductBase):

	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# Integration et customisation standard
#=====================================================
class IntegrationCustomisationStandard(productbase.ProductBase):

	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_MODULE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# MAINTENANCE ET BACKUP
#=====================================================
class MaintenanceBackup(productbase.ProductBase):

	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_MOIS)
	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# Numerisation données
#=====================================================
class NumerisationDonnees(productbase.ProductBase):

	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PAGE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# CreationSiteWeb
#=====================================================
class CreationSiteWeb(productbase.ProductBase):

	#les attributs
	type_site_web  = models.CharField("TYPE DE SITE",max_length=100, choices=TYPE_SITE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# INSTALLATION RESEAU INFORMATIQUE
#=====================================================
class InstallationReseauInformatique(productbase.ProductBase):

	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_POURC_DEVIS)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# INSTALLATION RESEAU TELEPHONIQUE
#=====================================================
class InstallationReseauTelephonique(productbase.ProductBase):

	#les attributs
	ipbx_voip = models.CharField("IPBX & VOIP",max_length=100, choices=IPBX_VOIP)
	call_manager  = models.CharField("CALL MANAGER",max_length=100, choices=CALL_MANAGER)

	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_POSTE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# ADAPTATEUR
#=====================================================

class Adaptateur(productbase.ProductBase):
	#les attributs
	type_adaptateur= models.CharField("TYPE D'ADAPTATEUR ",max_length=100, choices=TYPE_ADAPTATEUR)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# ANTENNE WIFI
#=====================================================

class AntenneWifi(productbase.ProductBase):
	#les attributs
	marque_antenne= models.CharField("MARQUE",max_length=100, choices=MARQUE_ANTENNE)
	modele_antenne= models.CharField("MODELE ",max_length=100, choices=MODELE_ANTENNE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# AUTOCOLLANT CODE BAR
#=====================================================

class AutocollantCodeBar(productbase.ProductBase):
	#les attributs
	dimension_autocollant= models.CharField("DIMENSION",max_length=100, choices=DIMENSION_AUTOCOLLANT)
	quantite_autocollant= models.CharField("QUANTITE",max_length=100, choices=QUANTITE_AUTOCOLLANT)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# BATTERIE LAPTOP
#=====================================================

class BatterieLaptop(productbase.ProductBase):
	#les attributs
	marque_laptop= models.CharField("MARQUE DU LAPTOP",max_length=100, choices=MARQUE_LAPTOP)
	modeles_laptop= models.CharField("MODELE DU LAPTOP",max_length=100, choices=MODELE_LAPTOP)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# BOITIER DISQUE DUR 2.5’’
#=====================================================

class BoitierDisqueDur(productbase.ProductBase):
	#les attributs
	type_disque_dur= models.CharField("TYPE DE DISQUE",max_length=100, choices=TYPE_DISQUE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# CARTE
#=====================================================

class Carte(productbase.ProductBase):
	#les attributs
	type_carte= models.CharField("TYPE DE CARTE",max_length=100, choices=TYPE_CARTE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# CHARGEUR LAPTOP
#=====================================================

class ChargeurLaptop(productbase.ProductBase):
	#les attributs
	marque_appareil= models.CharField("MARQUE",max_length=100, choices=MARQUE_CHARGEUR)
	tension= models.CharField("TENSION",max_length=100, choices=TENSION_CHARGEUR)
	intensite= models.CharField("INTENSITE",max_length=100, choices=INTENSITE_CHARGEUR)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# CONNECTEUR
#=====================================================

class Connecteur(productbase.ProductBase):
	#les attributs
	type_connecteur= models.CharField("TYPE DE CONNECTEUR",max_length=100, choices=TYPE_CONNECTEUR)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# MEMOIRES RAM
#=====================================================

class MemoireRam(productbase.ProductBase):
	#les attributs
	type_ordinateur= models.CharField("TYPE D'ORDINATEUR",max_length=100, choices=TYPE_ORDINATEUR)
	type_memoire= models.CharField("TYPE DE MEMOIRE",max_length=100, choices=TYPE_MEMOIRE_RAM)
	capacite_memoire= models.CharField("CAPACITE MEMOIRE",max_length=100, choices=CAPACITE_MEMOIRE_RAM)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# PATCH CORD
#=====================================================

class PatchCord(productbase.ProductBase):
	#les attributs
	longueur= models.CharField("LONGUEUR",max_length=100, choices=LONGUEUR_PATCHCORD)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# PATCH PANEL
#=====================================================

class PatchPanel(productbase.ProductBase):
	#les attributs
	type_patch_panel= models.CharField("TYPE DE PATCH PANEL",max_length=100, choices=TYPE_PATCHPANEL)
	nombre_port= models.CharField("NOMBRE DE PORT",max_length=100, choices=NOMBRE_PORT_PATCHPANEL)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# PROTECTION CONTRE LES SURTENSIONS
#=====================================================

class ProtectionSurtensions(productbase.ProductBase):
	#les attributs
	marque= models.CharField("MARQUE",max_length=100, choices=MARQUE_SURTENSIONS)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# RACK
#=====================================================

class Rack(productbase.ProductBase):
	#les attributs
	montage= models.CharField("MONTAGE",max_length=100, choices=MONTAGE_RACK)
	avec_fan= models.CharField("RACK AVEC FAN",max_length=100, choices=FAN_RACK)
	nombre_unites= models.CharField("UNITE",max_length=100, choices=UNITE_RACK)
	dimension= models.CharField("DIMENSION",max_length=100, choices=DIMENSION_RACK)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']



#=====================================================
# REPARTITEUR HDMI
#=====================================================

class RepartiteurHdmi(productbase.ProductBase):
	#les attributs
	entree_sortie= models.CharField("ENTRE ET SORTIE",max_length=100, choices=ENTRE_SORTIE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# WEBCAM
#=====================================================
class Webcam(productbase.ProductBase):
	#les attributs
	type_webcam= models.CharField("TYPE",max_length=100, choices=TYPE_WEBCAM)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#BOUTEILLE D’ENCRE
#=====================================================

class BouteilleEncre(productbase.ProductBase):
	#les attributs
	marque_bouteille_encre= models.CharField("MARQUE DE L'ENCRE",max_length=100, choices=MARQUE_ENCRE)
	couleur= models.CharField("COULEUR",max_length=100, choices=COULEUR)
	nombre_pages_max= models.CharField("NOMBRE DE PAGE MAX",max_length=100, choices=NOMBRE_PAGE_MAX)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']



#=====================================================
#COUPLEUR
#=====================================================

class Coupleur(productbase.ProductBase):
	#les attributs
	type_coupleur= models.CharField("TYPE",max_length=100, choices=TYPE_COUPLEUR)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#DISTRIBUTEUR D’ALIMENTATION ELECTRIQUE
#=====================================================

class DistributeurElectrique(productbase.ProductBase):
	#les attributs
	nombre_prise= models.CharField("NOMBRE DE PRISE",max_length=100, choices=NOMBRE_PRISE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#HUB USB
#=====================================================

class HubUsb(productbase.ProductBase):
	#les attributs
	type_hub= models.CharField("TYPE DE HUB",max_length=100, choices=TYPE_HUB)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']



#=====================================================
#LECTEUR DVD
#=====================================================

class LecteurDvd(productbase.ProductBase):
	#les attributs
	taille_ecran= models.CharField("TAILLE DE L'ECRAN",max_length=100, choices=TAILLE_ECRAN)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#GRAVEUR
#=====================================================

class Graveur(productbase.ProductBase):
	#les attributs
	Type_graveur= models.CharField("TYPE DE GRAVEUR",max_length=100, choices=TYPE_GRAVEUR)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#OUTIL DE SERTISSAGE
#=====================================================

class OutilSertissage(productbase.ProductBase):
	#les attributs
	modele_outil_sertissage= models.CharField("MODELE D'OUTIL DE SERTISSAGE",max_length=100, choices=MODELE_SERTISSAGE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#PRISE WIFI
#=====================================================

class PriseWifi(productbase.ProductBase):
	#les attributs
	marque= models.CharField("MARQUE",max_length=100, choices=MARQUE_PRISE_WIFI)
	modele_prise= models.CharField("MODEL",max_length=100, choices=MODELE_PRISE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']



#=====================================================
#PROCESSEUR
#=====================================================

class Processeur(productbase.ProductBase):
	#les attributs
	marque_processeur= models.CharField("MARQUE",max_length=100, choices=MARQUE_PROCESSEUR)
	modele_processeur= models.CharField("MODEL",max_length=100, choices=MODELE_PROCESSEUR)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']



#=====================================================
#REPARTITEUR ADSL
#=====================================================

class RepartiteurAdsl(productbase.ProductBase):
	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#====== 22-05-2018 =================================
# CAMERA CLOUD
#===================================================

class CameraCloud(productbase.ProductBase):
	#les attributs
	marque = models.CharField("MARQUE",max_length=100, choices=MARQUE_CAMERA_CLOUD)
	modele = models.CharField("MODELE",max_length=100, choices=MODELE_CAMERA_CLOUD)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#====== 22-05-2018 =================================
# MONITEUR ORDINATEUR
#===================================================

class Moniteur(productbase.ProductBase):
	#les attributs
	marque = models.CharField("MARQUE",max_length=100, choices=MARQUE_MONITEUR)
	type_ecran = models.CharField("TYPE",max_length=100, choices=TYPE_MONITEUR)
	taille_ecran = models.CharField("TAILLE",max_length=100, choices=TAILLE_MONITEUR)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#====== 22-05-2018 =================================
# RUBAN D’IMPRESSION
#===================================================

class RubanImpression(productbase.ProductBase):
	#les attributs
	modele = models.CharField("MODELE",max_length=100, choices=MODELE_RUBAN)
	longueur = models.CharField("LONGUEUR",max_length=100, choices=LONGUEUR_RUBAN)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#====== 22-05-2018 =================================
# RUBAN PAPIER
#===================================================

class RubanPapier(productbase.ProductBase):
	#les attributs
	marque = models.CharField("MARQUE",max_length=100, choices=MARQUE_RUBAN)
	modele = models.CharField("MODELE",max_length=100, choices=MODELE_RUBAN)
	numero = models.CharField("LONGUEUR",max_length=100, choices=NUMERO_RUBAN)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#====== 22-05-2018 =================================
# RUBAN POUR ETIQUETEUSE
#===================================================

class RubanPourEtiqueteuse(productbase.ProductBase):
	#les attributs
	marque = models.CharField("MARQUE",max_length=100, choices=MARQUE_RUBAN)
	modele = models.CharField("MODELE",max_length=100, choices=MODELE_RUBAN_ETIQ)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#====== 22-05-2018 =================================
# SWITCH HDMI
#===================================================

class SwitchHDMI(productbase.ProductBase):
	#les attributs
	marque = models.CharField("MARQUE",max_length=100, choices=MARQUE_SWITCH_HDMI)
	nombre_port = models.CharField("NOMBRE DE PORT",max_length=100, choices=NOMBRE_PORT_HDMI)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#====== 22-05-2018 =================================
# SWITCH KVM
#===================================================

class SwitchKVM(productbase.ProductBase):
	#les attributs
	nombre_port = models.CharField("NOMBRE DE PORT",max_length=100, choices=NOMBRE_PORT_KVM)
	nombre_pc = models.CharField("NOMBRE DE PC",max_length=100, choices=NOMBRE_PC)

	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#====== 22-05-2018 =================================
# TABLEAU BLANC
#===================================================

class TableauBlanc(productbase.ProductBase):
	#les attributs
	dimension = models.CharField("DIMENSION",max_length=100, choices=DIMENSION_TABLEAU)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']



#====== 22-05-2018 =================================
# TAMBOUR
#===================================================

class Tambour(productbase.ProductBase):
	#les attributs
	marque = models.CharField("MARQUE",max_length=100, choices=MARQUE_TAMBOUR)
	numero = models.CharField("NUMERO",max_length=100, choices=NUM_TAMBOUR)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#====== 22-05-2018 =================================
# TESTEUR DE CABLE
#===================================================

class TesteurDeCable(productbase.ProductBase):
	#les attributs
	type_testeur = models.CharField("TYPE DE TESTEUR",max_length=100, choices=TYPE_TESTEUR)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']



#====== 22-05-2018 =================================
# TROUSSE A OUTIL
#===================================================

class TrousseAOutil(productbase.ProductBase):
	#les attributs
	nombre_d_outil = models.CharField("NOMBRE D'OUTIL",max_length=100, choices=NBRE_OUTIL)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']



#====== 22-05-2018 =================================
# VENTILATEUR CARTE MERE
#===================================================

class VentilateurCarteMere(productbase.ProductBase):
	#les attributs
	marque = models.CharField("MARQUE DE VENTILATEUR",max_length=100, choices=MARQUE_VENTIL)
	type_socket = models.CharField("NOMBRE DE SOCKET",max_length=100, choices=TYPE_SOCKET)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=============== 23-05-2018 ==========================
#BATTERIE POUR CMOS
#=====================================================

class BatterieCmos(productbase.ProductBase):
	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=============== 23-05-2018 ==========================
#CABLE RESEAU
#=====================================================

class CableReseau(productbase.ProductBase):
	#les attributs
	type_cable_reseau= models.CharField("TYPE DE CABLE",max_length=100, choices=TYPE_CABLE_RX)
	categorie_cable_reseau= models.CharField("CATEGORIE DE CABLE",max_length=100, choices=CATEGORIE_CABLE_RX)
	longueur= models.CharField("LONGUEUR",max_length=100, choices=LONGUEUR_RX)
	marque_cable_reseau= models.CharField("MARQUE",max_length=100, choices=MARQUE_RX)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=============== 23-05-2018 ==========================
#CAMERA
#=====================================================

class Camera(productbase.ProductBase):
	#les attributs
	marque_camera= models.CharField("MARQUE",max_length=100, choices=MARQUE_CAMERA)
	modele_camera= models.CharField("MODELE",max_length=100, choices=MODELE_CAMERA)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=============== 23-05-2018 ==========================
#CASQUE AVEC MICRO
#=====================================================

class CasqueAvecMicro(productbase.ProductBase):
	#les attributs
	marque_casque_micro= models.CharField("MARQUE",max_length=100, choices=MARQUE_CASQUE_MICRO)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=============== 23-05-2018 ==========================
#CASQUE DE MUSIQUE
#=====================================================

class CasqueMusique(productbase.ProductBase):
	#les attributs
	marque_casque_musique= models.CharField("MARQUE",max_length=100, choices=MARQUE_CASQUE_MUSIQUE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=============== 23-05-2018 ==========================
#CASQUE MUSIQUE ET HAUT PARLEUR
#=====================================================

class CasqueMusiqueHautParleur(productbase.ProductBase):
	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=============== 23-05-2018 ==========================
#COMPTEUSE DE MONNAIE
#=====================================================

class CompteurMonnaie(productbase.ProductBase):
	#les attributs
	marque_compteur_monnaie= models.CharField("MARQUE",max_length=100, choices=MARQUE_COMPTEUR_MONNAIE)
	model_compteur_monnaie= models.CharField("MODELE",max_length=100, choices=MODEL_COMPTEUR_MONNAIE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=============== 23-05-2018 ==========================
#ECOUTEUR AVEC MICRO
#=====================================================

class EcouteurMicro(productbase.ProductBase):
	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=============== 23-05-2018 ==========================
#ECRAN DE PROJECTION
#=====================================================

class EcranProjection(productbase.ProductBase):
	#les attributs
	dimension= models.CharField("DIMENSION",max_length=100, choices=DIMENSION_ECRAN_PROJECTION)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']



#=============== 23-05-2018 ==========================
#EQUIPEMENT CPE
#=====================================================

class EquipementCpe(productbase.ProductBase):
	#les attributs
	marque_cpe= models.CharField("MARQUE",max_length=100, choices=MARQUE_CPE)
	modele_cpe= models.CharField("MODELE",max_length=100, choices=MODELE_CPE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=============== 23-05-2018 ==========================
#HAUT PARLEUR USB
#=====================================================

class HautParleurUsb(productbase.ProductBase):
	#les attributs
	marque_haut_parleur= models.CharField("MARQUE",max_length=100, choices=MARQUE_HAUT_PARLEUR)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=============== 23-05-2018 ==========================
#IMPRIMANTE D’ETIQUETTE
#=====================================================

class ImprimanteEtiquette(productbase.ProductBase):
	#les attributs
	marque= models.CharField("MARQUE",max_length=100, choices=MARQUE_IMPRIMANTE_ETIQUETTE)
	modele_imprimante_etiquette= models.CharField("MODELE",max_length=100, choices=MODELE_IMPRIMANTE_ETIQUETTE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=============== 23-05-2018 ==========================
#KIT ACCESSOIRES POUR SPLIT
#=====================================================

class KitAccessoiresSplit(productbase.ProductBase):
	#les attributs
	puissance_split= models.CharField("PUISSANCE DU SPLIT",max_length=100, choices=PUISSANCE_SPLIT_KIT)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=============== 23-05-2018 ==========================
#MOUSSE NETTOYANTE
#=====================================================

class MousseNettoyante(productbase.ProductBase):
	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=============== 23-05-2018 ==========================
#STAND LAPTOP
#=====================================================

class StandLaptop(productbase.ProductBase):
	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']




#=============== 23-05-2018 ==========================
#TAPIS DE SOURIS
#=====================================================

class TapisSouris(productbase.ProductBase):
	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#====== 23-05-2018 =================================
# BLOC D'ALIMENTATION POUR PC
#===================================================

class BlocDAlimentationPourPC(productbase.ProductBase):
	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#====== 23-05-2018 =================================
# CLAVIER ET SOURIS SANS FIL
#===================================================

class ClavierEtSourisSansFil(productbase.ProductBase):
	#les attributs
	marque = models.CharField("MARQUE",max_length=100, choices=MARQUE_CLAVIER_SOURIS)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']



#====== 23-05-2018 =================================
# CLAVIER SANS FIL
#===================================================

class ClavierSansFil(productbase.ProductBase):
	#les attributs
	marque = models.CharField("MARQUE",max_length=100, choices=MARQUE_CLAVIER_SOURIS)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#====== 23-05-2018 =================================
# IMPRIMANTE PHOTO
#===================================================

class ImprimantePhoto(productbase.ProductBase):
	#les attributs
	marque_imprimante = models.CharField("MARQUE DE L'IMPRIMANTE",max_length=100, choices=MARQUE_IMPR_PHOTO)
	modele_imprimante = models.CharField("MODELE DE L'IMPRIMANTE",max_length=100, choices=MODELE_IMPR_PHOTO)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']



#====== 23-05-2018 =================================
# KIT DE NETTOYAGE POUR IMPRIMANTE
#===================================================

class KitDeNettoyageImprimante(productbase.ProductBase):
	#les attributs
	modele_imprimante = models.CharField("MODELE DE L'IMPRIMANTE",max_length=100, choices=MODELE_KIT_NET)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']



#====== 23-05-2018 =================================
# EQUIPEMENT BLUETOOTH PORTABLE
#===================================================

class EquipementBluetoothPortable(productbase.ProductBase):
	#les attributs
	type_appareil = models.CharField("TYPE D'APPAREIL",max_length=100, choices=TYPE_APP_BT)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

