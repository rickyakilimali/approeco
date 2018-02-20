from product.models import *
from utils.product_attributes.batiment_construction import *
from utils.unite_prix import UNITE


#=====================================================
# 1. PEINTURE MURALE
#=====================================================
class Peinture(productbase.ProductBase):
	type_peinture =models.CharField("TYPE DE PEINTURE", max_length=20, choices= TYPE_PEINTURE)
	composition =models.CharField("COMPOSITION", max_length=20, choices= COMPOSITION)
	teinte =models.CharField("TEINTE", max_length=20, choices= TEINTE)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
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
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
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
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
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
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  LOCATIONDEPOT
#=====================================================

class LocationDepot(productbase.ProductBase):

	#les attributs
	plage_surface  = models.CharField("PLAGE DE SURFACE",max_length=100, choices=PLAGE_SURFACE)
	avenue  = models.CharField("AVENUE",max_length=100, choices=AVENUE)
	commune  = models.CharField("COMMUNE",max_length=100, choices=COMMUNE)
	surface  = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

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
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
#  MISSION DE CONTROLE CHANTIER  ==> BATIMENT CONSTRUCTION
#=====================================================

class MissionControleChantier(productbase.ProductBase):

	#les attributs

	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

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
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

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
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']