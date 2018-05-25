from product.models import *
from utils.product_attributes.hotel_restaurant import *
from utils.unite_prix import *

#=====================================================
# TABLIER
#=====================================================

class Tablier(productbase.ProductBase):
	#les attributs
	couleur= models.CharField("COULEUR",max_length=100, choices=COULEUR_TABLIER)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_KG)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# BALANCE DE CUISINE
#=====================================================

class BalanceCuisine(productbase.ProductBase):
	#les attributs
	poids= models.CharField("POIDS ",max_length=100, choices=POIDS_BALANCE)
	marque= models.CharField("MARQUE",max_length=100, choices=MARQUE_BALANCE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_KG)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# COMPTOIRE
#=====================================================

class Comptoire(productbase.ProductBase):
	#les attributs
	format_comptoire= models.CharField("FORMAT ",max_length=100, choices=FORMAT_COMPTOIRE)
	marque= models.CharField("MARQUE",max_length=100, choices=MARQUE_COMPTOIRE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_KG)

	#ordonner les produits
	class Meta:
		ordering = ['prix']



#=====================================================
# COUVERCLE OVAL
#=====================================================

class CouvercleOval(productbase.ProductBase):
	#les attributs
	taille = models.CharField("TAILLE (POUCE)  ",max_length=100, choices=TAILLE_COUVERCLE)
	marque= models.CharField("MARQUE",max_length=100, choices=MARQUE_COUVERCLE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_KG)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#FOUR A PIZZA
#=====================================================

class FourPizza(productbase.ProductBase):
	#les attributs
	puissance = models.CharField("PUISSANCE",max_length=100, choices=PUISSANCE_FOUR)
	marque= models.CharField("MARQUE",max_length=100, choices=MARQUE_FOUR)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_KG)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#MACHINE A CREME GLACEE
#=====================================================

class MachineCreme(productbase.ProductBase):
	#les attributs
	puissance = models.CharField("PUISSANCE(KILOWATT)",max_length=100, choices=PUISSANCE_MACHINECREME)
	marque= models.CharField("MARQUE",max_length=100, choices=MARQUE_MACHINECREME)
	volume= models.CharField("VOLUME(LITTRE)",max_length=100, choices=VOLUME_MACHINECREME)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_KG)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#PARASOLEIL
#=====================================================

class Parasoleil(productbase.ProductBase):
	#les attributs
	diametre = models.CharField("PUISSANCE(CENTIMETRE)",max_length=100, choices=DIAMETRE_PARASOLEIL)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_KG)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#PLATEAU DE NOURRITURE
#=====================================================

class PlateauNourriture(productbase.ProductBase):
	#les attributs
	format  = models.CharField("FORMAT",max_length=100, choices=FORMAT_PLATEAU)
	marque= models.CharField("MARQUE",max_length=100, choices=MARQUE_PLATEAU)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_KG)

	#ordonner les produits
	class Meta:
		ordering = ['prix']



#=====================================================
#TASSE DE MESURE
#=====================================================

class TasseMesure(productbase.ProductBase):
	#les attributs
	volume  = models.CharField("VOLUME",max_length=100, choices=VOLUME_TASSE)
	marque= models.CharField("MARQUE",max_length=100, choices=MARQUE_TASSE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_KG)

	#ordonner les produits
	class Meta:
		ordering = ['prix']




#=====================================================
#VITRINE POUR BOISSON
#=====================================================

class VitrineBoisson(productbase.ProductBase):
	#les attributs
	nombre_porte = models.CharField("NOMBRE DE PORTE",max_length=100, choices=NOMBRE_PORTE_VITRINE)
	marque= models.CharField("MARQUE",max_length=100, choices=MARQUE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_KG)

	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
#POELE
#=====================================================

class Poele(productbase.ProductBase):
	#les attributs
	format_poele = models.CharField("NOMBRE DE PORTE",max_length=100, choices=FORMAT_POELE)
	marque= models.CharField("MARQUE",max_length=100, choices=MARQUE_POELE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_KG)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

