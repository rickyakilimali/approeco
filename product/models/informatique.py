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
	marque_imprimante  = models.CharField("MARQUE IMPRIMANTE",max_length=50, choices=MARQUE_IMPRIMANTE)
	technologie = models.CharField("TECHNOLOGIE",max_length=50, choices=TECHNOLOGIE_IMPRESSION)
	modele	= models.CharField("MODELE",max_length=50, choices=MODEL_IMPRIMANTE)
	couleur = models.CharField("COULEUR D'IMPRESSION",max_length=50, choices=COULEUR)
	multifonction = models.CharField("MULTIFONCTION",max_length=50, choices=MULTIFONCTION)
	recto_verso = models.CharField("RECTO VERSO",max_length=50, choices=RECTO_VERSO)
	format_max_papier = models.CharField("FORMAT MAXIMUM PAPIER",max_length=50, choices=FORMAT_MAXIMUM_PAPIER)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']



#=====================================================
# PHOTOCOPIEUSE
#=====================================================
# Nom de la class
class Photocopieuse(productbase.ProductBase):

	#les attributs
	marque_imprimante  = models.CharField("MARQUE PHOTOCOPIEUSE",max_length=50, choices=MARQUE_IMPRIMANTE)
	technologie = models.CharField("TECHNOLOGIE",max_length=50, choices=TECHNOLOGIE_IMPRESSION)



	recto_verso = models.CharField("RECTO VERSO",max_length=50, choices=RECTO_VERSO)
	reseau = models.CharField("RESEAU",max_length=50, choices=RESEAU)
	format_max_papier = models.CharField("FORMAT MAXIMUM PAPIER",max_length=50, choices=FORMAT_MAXIMUM_PAPIER)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# 2. DESKTOP
#=====================================================
# Nom de la class
class Desktop(productbase.ProductBase):

	#les attributs
	marque_desktop= models.CharField("MARQUE DESKTOP",max_length=50, choices=MARQUE_ORDINATEUR)
	type_processeur = models.CharField("TYPE DE PROCESSEUR",max_length=50, choices= TYPE_DE_PROCESSEUR)
	memoire_ram = models.CharField("MEMOIRE RAM",max_length=50, choices=CAPACITE_MEMOIRE)
	capacite_disque_dur = models.CharField("CAPACITE DU DISQUE DUR",max_length=50, choices= CAPACITE_DISQUE_DUR)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

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
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']



#=====================================================
# 4. CARTOUCHE
#=====================================================
class Cartouche(productbase.ProductBase):

	#les attributs
	marque_cartouche= models.CharField("MARQUE DE CARTOUCHE",max_length=50, choices=MARQUE_CARTOUCHE)
	numero_cartouche = models.CharField("NUMERO DE CARTOUCHE",max_length=50, choices=NUMERO_CARTOUCHE)
	couleur_cartouche = models.CharField("COULEUR DE CARTOUCHE",max_length=50, choices=COULEUR_CARTOUCHE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']



#=====================================================
# 5. UNITÉS DE STOCKAGES
#=====================================================
class Unite_stockage(productbase.ProductBase):

	#les attributs
	marque = models.CharField("MARQUE",max_length=50, choices=MARQUE_UNITE_STOCKAGE)
	type_stockage= models.CharField("TYPE DE STOCKAGE",max_length=50, choices=TYPE_DE_STOCKAGE)
	capacite_memoire = models.CharField("CAPAPCITE DE STOCKAGE",max_length=50, choices=CAPACITE_MEMOIRE_STOCKAGE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

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
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 8. SWITCH
#=====================================================
class Switch(productbase.ProductBase):

	#les attributs
	type_equipement= models.CharField("TYPE_EQUIPEMENT",max_length=50, choices=TYPE_EQUIPEMENT)
	marque = models.CharField("MARQUE",max_length=50, choices=MARQUE_RESEAU)
	nombre_port= models.CharField("NOMBRE DES PORTS",max_length=50, choices= NOMBRE_PORT_SWITCH)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

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
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

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
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 11. SOURIS
#=====================================================
class Souris(productbase.ProductBase):

	#les attributs
	avec_fil = models.CharField("AVEC FIL",max_length=50, choices= AVEC_FIL)
	prix = models.DecimalField("PRIX",max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 11. CLAVIER
#=====================================================
class Clavier(productbase.ProductBase):

	#les attributs
	type_clavier = models.CharField("TYPE CLAVIER",max_length=50, choices= TYPE_CLAVIER)
	prix = models.DecimalField("PRIX",max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

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
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 12. CABLE INFORMATIQUE
#=====================================================
class CableInformatique(productbase.ProductBase):

	#les attributs
	type_cable = models.CharField("TYPE CABLE",max_length=50, choices= TYPE_CABLE_INFORMATIQUE)
	longueur = models.CharField("LONGUEUR CABLE(METRE)",max_length=50, choices= LONGUEUR_CABLE_INFORMATIQUE)
	prix = models.DecimalField("PRIX",max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

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
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 14. COFFRE FORT
#=====================================================

#=====================================================
# 15. GRAVEUR
#=====================================================
class Graveur(productbase.ProductBase):
	type_graveur = models.CharField("POID",max_length=50, choices=TYPE_GRAVEUR)
	prix = models.DecimalField("PRIX",max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 16. MONITEUR
#=====================================================
class Moniteur(productbase.ProductBase):
	marque= models.CharField("MARQUE",max_length=50, choices=MARQUE_INFORMATIQUE)
	taille_ecran = models.CharField("TAILLE ECRAN",max_length=50, choices=TAILLE_ECRAN)
	type= models.CharField("TYPE",max_length=50, choices=TYPE_ECRAN)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# 17. PATCH PANEL
#=====================================================
class PatchPanel(productbase.ProductBase):
	nombre_port = models.CharField("NOMBRE PORTS",max_length=50, choices=NOMBRE_PORT_PATCH_PANEL)
	prix = models.DecimalField("PRIX",max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']



#=====================================================
# 18. RACK
#=====================================================
class Rack(productbase.ProductBase):
	montage = models.CharField("MONTAGE",max_length=50, choices=MONTAGE_RACK)
	unites = models.CharField("UNITE",max_length=50, choices=UNITE_RACK)
	dimension = models.CharField("DIMENSION",max_length=50, choices=DIMENSION_RACK)
	prix = models.DecimalField("PRIX",max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']



#=====================================================
# 19. SERVEUR
#=====================================================
class Serveur(productbase.ProductBase):
	marque = models.CharField("MARQUE",max_length=50, choices=MARQUE_ORDINATEUR)
	modele_serveur = models.CharField("MODELE SERVEUR",max_length=50, choices= MODELE_SERVEUR)
	type_serveur = models.CharField("TYPE SERVEUR",max_length=50, choices= TYPE_SERVEUR)
	type_processeur = models.CharField("TYPE DE PROCESSEUR",max_length=50, choices= TYPE_DE_PROCESSEUR)
	capacite_disque_dur = models.CharField("CAPACITE DU DISQUE DUR",max_length=50, choices= CAPACITE_DISQUE_DUR)
	controleur_raid = models.CharField("CONTROLEUR RAID",max_length=50, choices= CONTROLEUR_RAID)
	capacite_ram_max = models.CharField("MEMOIRE RAM maximum",max_length=50, choices=CAPACITE_MEMOIRE)

	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 20. ADRESSE IP PUBLIQUE
#=====================================================
class AdresseIpPublique(productbase.ProductBase):
	nombre_adresse_maximum =models.CharField("NOMBRE ADRESSE IP PUBLIQUE MAXIMUM", max_length=20, choices= NOMBRE_ADRESSE_MAXIMUM)
	prix = models.DecimalField("PRIX", max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_AN)
	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 21. BANDE PASSANTE
#=====================================================
class BandePassante(productbase.ProductBase):
	type_bande_passante =models.CharField("TYPE BANDE PASSANTE", max_length=20, choices= TYPE_BANDE_PASSANTE)
	debit_download =models.CharField("DEBIT EN DOWNLOAD", max_length=20, choices= DEBIT_DOWNLOAD)
	debit_upload =models.CharField("DEBIT EN UPLOAD", max_length=20, choices= DEBIT_UPLOAD)
	frais_installation =models.CharField("FRAIS INSTALLATION", max_length=20, choices= FRAIS_INSTALLATION)
	prix = models.DecimalField("PRIX", max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_MOIS)
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
	type_hebergement=models.CharField("TYPE HEBERGEMENT", max_length=50, choices= TYPE_HEBERGEMENT)
	prix = models.DecimalField("PRIX", max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_AN)
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
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# CAHIER DE CHARGES
#=====================================================
class CahierCharges(productbase.ProductBase):

	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# HELPDESK
#=====================================================
class Helpdesk(productbase.ProductBase):

	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_HEURE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# Installation logiciel serveur
#=====================================================
class InstallationLogicielServeur(productbase.ProductBase):

	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# Integration et customisation standard
#=====================================================
class IntegrationCustomisationStandard(productbase.ProductBase):

	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# MAINTENANCE ET BACKUP
#=====================================================
class MaintenanceBackup(productbase.ProductBase):

	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_MOIS)
	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# Numerisation données
#=====================================================
class NumerisationDonnees(productbase.ProductBase):

	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_PAGE)
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
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# INSTALLATION RESEAU INFORMATIQUE
#=====================================================
class InstallationReseauInformatique(productbase.ProductBase):

	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

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
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']