from product.models import *
from utils.product_attributes.ameublement import *
from utils.unite_prix import *

# Create your models here.


#=====================================================
# 2. Armoire
#=====================================================
class Armoire(productbase.ProductBase):
	type_armoire =models.CharField("TYPE D'ARMOIRE",max_length=50, choices=TYPES_ARMOIRE)
	materiau_armoire=models.CharField("MATERIAU", max_length=50, choices= MATERIAU_ARMOIRE)
	hauteur =models.CharField("HAUTEUR", max_length=50, choices=HAUTEUR_ARMOIRE)
	longueur =models.CharField("LONGUEUR", max_length=50, choices=LONGUEUR_ARMOIRE)
	largeur =models.CharField("LARGEUR", max_length=50, choices=LARGEUR)
	nombre_de_cases =models.CharField("NOMBRE DE CASES", max_length=50, choices=NOMBRE_CASES)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

#=====================================================
# 3. ETAGERE
#=====================================================
class Etagere(productbase.ProductBase):
	materiau_armoire =models.CharField("MATERIAU ", max_length=20, choices= MATERIAU_ETAGERE)
	type_armoire =models.CharField("TYPE", max_length=20, choices= TYPES_ARMOIRE  )
	hauteur =models.CharField("HAUTEUR", max_length=20, choices= HAUTEUR_ETAGERE )
	longueur =models.CharField("LONGUEUR", max_length=20, choices= LONGUEUR_ETAGERE )
	largeur =models.CharField("LARGEUR", max_length=20, choices= LARGEUR)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# 6. TABLE REUNION
#=====================================================
class TableReunion(productbase.ProductBase):
	longueur =models.CharField("LONGUEUR", max_length=20, choices= LONGUEUR_TB_REUNION )
	forme =models.CharField("FORME", max_length=20, choices= FORME_TABLE)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 7. BUREAU
#=====================================================
class Bureau(productbase.ProductBase):
	materiau_bureau =models.CharField("MATERIAU ", max_length=20, choices= MATERIAU_BUREAU)
	longueur =models.CharField("LONGUEUR", max_length=20, choices= LONGUEUR_BUREAU)
	type_bureau =models.CharField("TYPE DE BUREAU", max_length=20, choices= TYPE_BUREAU)
	forme =models.CharField("FORME", max_length=20, choices= FORME_BUREAU)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# 6. CHAISE DE SALLE D'ATTENTE
#=====================================================
class ChaiseSalleAttente(productbase.ProductBase):
	nombre_de_places =models.CharField("NOMBRE DE PLACES ", max_length=20, choices= NOMBRE_DE_PLACES)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# 6. CHAISE DE BUREAU
#=====================================================
class Chaisebureau(productbase.ProductBase):
	type_chaise =models.CharField("TYPE DE CHAISE", max_length=50, choices= TYPE_CHAISE)
	revetement=models.CharField("REVETEMENT", max_length=50, choices= REVETEMENT_CHAISE)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 7. CONSULTANCE DECORATION
#=====================================================
class ConsultanceDecoration(productbase.ProductBase):
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_HEURE)
#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 8. DECORATION AMENAGEMENT
#=====================================================
class DecorationAmenagement(productbase.ProductBase):
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_POURC_DEVIS)
	class Meta:
		ordering = ['prix']

#=====================================================
# 9. DECORATION SURFACE
#=====================================================
class DecorationSurface(productbase.ProductBase):
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_M2)
#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# 9. TABLEAU
#=====================================================
class Tableau(productbase.ProductBase):

	dimension_tableau =models.CharField("DIMENSION DU TABLEAU", max_length=20, choices= DIMENSION_TABLEAU)

	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
#POUBELLE
#=====================================================

class Poubelleuac(productbase.ProductBase):
	#les attributs
	type_poubelle  = models.CharField("TYPE DE POUBELLE",max_length=100, choices=TYPE_POUBELLE)
	matiere= models.CharField("MATIERE",max_length=100, choices=MATIERE_POUBELLE)
	volume= models.CharField("VOLUME EN LITRE",max_length=100, choices=VOLUME_POUBELLE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_KG)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#	VASE
#=====================================================

class Vase(productbase.ProductBase):
	#les attributs
	dimension_carreau  = models.CharField("DIMENSION DU CARREAU",max_length=100, choices=DIMENSION_VASE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_KG)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#====== 23-05-2018 =================================
# CAISSON DE BUREAU
#===================================================

class CaissonDeBureau(productbase.ProductBase):
	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']



#====== 23-05-2018 =================================
# TABLE D’ORDINATEUR
#===================================================

class TableOrdinateur(productbase.ProductBase):
	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

