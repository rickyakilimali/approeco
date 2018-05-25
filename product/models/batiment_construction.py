from product.models import *
from utils.product_attributes.batiment_construction import *
from utils.unite_prix import *


#=====================================================
# 1. PEINTURE MURALE
#=====================================================
class Peinture(productbase.ProductBase):
	type_peinture =models.CharField("TYPE DE PEINTURE", max_length=20, choices= TYPE_PEINTURE)
	composition =models.CharField("COMPOSITION", max_length=20, choices= COMPOSITION)
	teinte =models.CharField("TEINTE", max_length=20, choices= TEINTE)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_KG_LITRE)
#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# 2. PEINTURE SPECIALE
#=====================================================
class PeintureSpeciale(productbase.ProductBase):
	type_produit=models.CharField(" TYPE PRODUIT", max_length=50, choices= PEINTURE_SPECIALE)
	domaine_application=models.CharField("DOMAINE APPLICATION", max_length=50, choices= DOMAINE_APPLICATION)
	caracteristique=models.CharField("CARACTERISTIQUE", max_length=20, choices= CARACTERISTIQUE)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_KG_LITRE)
#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 3. BRIQUE
#=====================================================
class Brique(productbase.ProductBase):
	type_brique=models.CharField("TYPE DE BRIQUE", max_length=50, choices= TYPE_BRIQUE)
	largeur =models.CharField("LARGEUR", max_length=20, choices= LARGEUR_BRIQUE )
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_PIECE)
#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 4. CARREAU
#=====================================================
class Carreau(productbase.ProductBase):
	type_carreaux =models.CharField("TYPE DE CARREAU", max_length=20, choices= TYPE_CARREAU)
	dimension =models.CharField("DIMENSION", max_length=20, choices= DIMENSION_CARREAU )
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 4.
#=====================================================


#=====================================================
# 4.
#=====================================================



#=====================================================
# 5. TRAVEAUX DE PEINTURE
#=====================================================
class TravauxPeinture(productbase.ProductBase):
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_POURC_DEVIS)
#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  LOCATION DEPOT
#=====================================================

class LocationDepot(productbase.ProductBase):

	#les attributs
	plage_surface  = models.CharField("PLAGE DE SURFACE",max_length=100, choices=PLAGE_SURFACE)
	avenue  = models.CharField("AVENUE",max_length=100, choices=AVENUE)
	commune  = models.CharField("COMMUNE",max_length=100, choices=COMMUNE)
	surface  = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_MOIS)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  LOCATIONSTAND
#=====================================================


class LocationStand(productbase.ProductBase):

	#les attributs
	surface_stand  = models.CharField("SURFACE (M²)",max_length=100, choices=SURFACE_STAND)
	duree_maximum  = models.CharField("DUREE MAXIMUM",max_length=100, choices=DUREE_MAXIMUM)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
#  MOELLON  ==> BATIMENT CONSTRUCTION
#=====================================================

class Moellon(productbase.ProductBase):

	#les attributs
	type_moellon = models.CharField("TYPE MOELLON",max_length=100, choices=TYPE_MOELLON)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_TONE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
#  MISSION DE CONTROLE CHANTIER  ==> BATIMENT CONSTRUCTION
#=====================================================

class MissionControleChantier(productbase.ProductBase):

	#les attributs

	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_MOIS)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  LOCATION CAMION  ==> BATIMENT CONSTRUCTION
#=====================================================

class LocationCamion(productbase.ProductBase):

	#les attributs
	tonnage = models.CharField("TONNAGE",max_length=100, choices=TONNAGE)
	zone = models.CharField("ZONE",max_length=100, choices=ZONE)

	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_JOUR)

	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
#  LOCATION REMORQUE MATADI-KIN  ==> BATIMENT CONSTRUCTION
#=====================================================

class LocationRemorqueMatadi(productbase.ProductBase):

	#les attributs
	nombre_pied = models.CharField("NOMBRE DE PIED",max_length=100, choices=NOMBRE_PIED)


	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#   INSTALLATION ELECTRIQUE
#=====================================================
class InstallationElectrique(productbase.ProductBase):
	prix = models.DecimalField("PRIX", max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_POURC_DEVIS)
#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# CONSTRUCTION BATIMENT
#=====================================================
class ConstructionBatiment(productbase.ProductBase):
	qualite_du_terrain=models.CharField("QUALITE DU TERRAIN", max_length=50, choices= QUALITE_DU_TERRAIN)
	usage_du_batiment=models.CharField("USAGE DU BATIMENT", max_length=50, choices= USAGE_DU_BATIMENT)
	nombre_d_etages=models.CharField("NOMBRE D'ETAGE", max_length=50, choices= NOMBRE_ETAGE)
	nombre_de_pieces=models.CharField("NOMBRE DE PIECES", max_length=50, choices= NOMBRE_DE_PIECES)
	type_de_terrain=models.CharField("TYPE DE TERRAIN", max_length=50, choices= TYPE_DE_TERRAIN)
	prix = models.DecimalField("PRIX", max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_M2)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# CONSTRUCTION ROUTE
#=====================================================
class ConstructionRoute(productbase.ProductBase):
	type_de_route=models.CharField("TYPE DE ROUTE", max_length=50, choices= TYPE_DE_ROUTE)
	largeur_de_route=models.CharField("LARGEUR DE ROUTE", max_length=50, choices= LARGEUR_DE_ROUTE)
	couche_de_tout_venant=models.CharField("COUCHE DE TOUT VENANT", max_length=50, choices= COUCHE_DE_TOUT_VENANT)
	couche_de_beton=models.CharField("COUCHE DE BETON", max_length=50, choices= COUCHE_DE_BETON)
	couche_de_terre_jaune=models.CharField("COUCHE DE TERRE JAUNE", max_length=50, choices= COUCHE_DE_TERRE_JAUNE)
	matiere=models.CharField("MATIERE", max_length=50, choices= MATIERE)
	canalisation_d_eau=models.CharField("CANALISATION D'EAU", max_length=50, choices= CANALISATION_EAU)
	prix = models.DecimalField("PRIX", max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_KM)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 18. CHAMBRE
#=====================================================
class Chambre(productbase.ProductBase):
	nombre_etoile =models.CharField("NOMBRE ETOILE", max_length=20, choices= NOMBRE_ETOILE)
	acces_wifi_gratuit =models.CharField("ACCES WIFI GRATUIT", max_length=20, choices= ACCES_WIFI_GRATUIT)
	petit_dejeune_gratuit =models.CharField("PETIT DEJEUNE GRATUIT", max_length=20, choices= PETIT_DEJEUNE_GRATUIT)
	type_lit =models.CharField("TYPE DE LIT", max_length=20, choices= TYPE_LIT)
	avenue =models.CharField("AVENUE", max_length=20, choices= AVENUE_1)
	commune =models.CharField("COMMUNE", max_length=20, choices= COMMUNE)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
#=====================================================
#TRIPLEX
#=====================================================

class Triplex(productbase.ProductBase):
	#les attributs
	dimension_triplex  = models.CharField("DIMENSION",max_length=100, choices=DIMENSION_TRIPLEX)
	type_triplex= models.CharField("TYPE",max_length=100, choices=TYPE_TRIPLEX)
	epaisseur= models.CharField("MARQUE",max_length=100, choices=EPAISSEUR_TRIPLEX)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_KG)

	#ordonner les produits
	class Meta:
		ordering = ['prix']