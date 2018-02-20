from product.models import *
from utils.product_attributes.agribusiness import *
from utils.unite_prix import UNITE
#=====================================================
# 1. RIZ
#=====================================================
class Riz(productbase.ProductBase):

	variete =models.CharField("VARIETE",max_length=100, choices=VARIETE)
	type_riz =models.CharField("TYPE RIZ",max_length=100, blank=True,null=True,choices=TYPE_RIZ)
	qualite =models.CharField("QUALITE",max_length=50, blank=True,null=True,choices=QUALITE_RIZ)
	prix = models.DecimalField(max_digits=10, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# BOUILLIE
#=====================================================
class Bouillie(productbase.ProductBase):


	composition_bouillie =models.CharField("COMPOSITION BOUILLIE",max_length=100, choices=COMPOSITION_BOUILLIE)
	qualite_bouillie =models.CharField("QUALITE BOUILLIE",max_length=100, choices= QUALITE_BOUILLIE)
	prix = models.DecimalField(max_digits=10, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
#  SEMENCE  ==> AGRIBUSINESS
#=====================================================

class Semence(productbase.ProductBase):

	#les attributs
	produit_agricole = models.CharField("PRODUIT AGRICOLE",max_length=100, choices=PRODUIT_AGRICOLE)
	variete = models.CharField("VARIETE",max_length=100,blank=True,null=True, choices=VARIETE)
	poids = models.CharField("POIDS",max_length=100, choices=POIDS)

	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  BOUTURE MANIOC  ==> AGRIBUSINESS
#=====================================================

class BoutureManioc(productbase.ProductBase):

	#les attributs

	longueur = models.CharField("LONGUEUR",max_length=100, choices=LONGUEUR)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  HUILE  ==> AGRIBUSINESS
#=====================================================

class Huile(productbase.ProductBase):

	#les attributs

	base = models.CharField("BASE",max_length=100, choices=BASE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  FARINE  ==> AGRIBUSINESS
#=====================================================

class Farine(productbase.ProductBase):

	#les attributs

	base = models.CharField("BASE",max_length=100, choices=BASE)


	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  TOURTEAU  ==> AGRIBUSINESS
#=====================================================

class Tourteau(productbase.ProductBase):

	#les attributs

	base = models.CharField("BASE",max_length=100, choices=BASE)


	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  REBOISEMENT ==> AGRIBUSINESS
#=====================================================

class Reboisement(productbase.ProductBase):

	#les attributs


	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

