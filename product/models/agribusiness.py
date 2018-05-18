from product.models import *
from utils.product_attributes.agribusiness import *
from utils.unite_prix import *

#=====================================================
# 1. RIZ
#=====================================================
class Riz(productbase.ProductBase):

	variete =models.CharField("VARIETE",max_length=100, choices=VARIETE)
	type_riz =models.CharField("TYPE RIZ",max_length=100, blank=True,null=True,choices=TYPE_RIZ)
	qualite =models.CharField("QUALITE",max_length=50, blank=True,null=True,choices=QUALITE_RIZ)
	prix = models.DecimalField(max_digits=10, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE_USD_KG)

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
	units = models.CharField(max_length=50, choices=UNITE_USD_KG)

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
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_LITRE)

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
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_KG)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  REBOISEMENT ==> AGRIBUSINESS
#=====================================================

class Reboisement(productbase.ProductBase):

	#les attributs


	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_M2)

	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# LEGUME
#=====================================================
class Legume(productbase.ProductBase):
	type_legume =models.CharField("TYPE LEGUME",max_length=50, choices=TYPE_LEGUME)
	prix = models.DecimalField(max_digits=5, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE_USD_KG)

#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
#  POISSON
#=====================================================
class Poisson(productbase.ProductBase):
	type_de_poisson =models.CharField("TYPE POISSON",max_length=50, choices=TYPE_POISSON)
	prix = models.DecimalField(max_digits=5, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE_USD_KG)

#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  BOEUF
#=====================================================
class Boeuf(productbase.ProductBase):
	type_de_morceau =models.CharField("TYPE DE MORCEAU",max_length=50, choices=TYPE_MORCEAU_BOEUF)
	prix = models.DecimalField(max_digits=5, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE_USD_KG)

#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  PORC
#=====================================================
class Porc(productbase.ProductBase):
	type_de_morceau =models.CharField("TYPE DE MORCEAU",max_length=50, choices=TYPE_MORCEAU_PORC)
	prix = models.DecimalField(max_digits=5, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE_USD_KG)

#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
#  POULET
#=====================================================
class Poulet(productbase.ProductBase):
	type_de_poulet =models.CharField("TYPE DE POULET",max_length=50, choices=TYPE_POULET)
	prix = models.DecimalField(max_digits=5, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE_USD_PIECE)

#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  CHEVRE
#=====================================================
class Chevre(productbase.ProductBase):
	prix = models.DecimalField(max_digits=5, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  COSSETTE DE MANIOC
#=====================================================
class CossetteManioc(productbase.ProductBase):
	poids_par_sac=models.CharField("POIDS PAR SAC",max_length=50, choices=POIDS_PAR_SAC)
	prix = models.DecimalField(max_digits=5, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE_USD_KG)

#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  MIEL PUR
#=====================================================
class MielPur(productbase.ProductBase):
	prix = models.DecimalField(max_digits=5, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE_LITRE)

#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# AMARANTE
#=====================================================

class Amarante(productbase.ProductBase):
	#les attributs
	contenant= models.CharField("CONTENANT",max_length=100, choices=CONTENANT_AMARANTE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_KG)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# GINGEMBRE
#=====================================================

class Gingembre(productbase.ProductBase):
	#les attributs
	contenant= models.CharField("CONTENANT",max_length=100, choices=CONTENANT_GINGEMBRE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_KG)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# PONDU
#=====================================================

class Pondu(productbase.ProductBase):
	#les attributs
	contenant= models.CharField("CONTENANT",max_length=100, choices=CONTENANT_PONDU)
	type_legume= models.CharField("TYPE DE LEGUME",max_length=100, choices=TYPE_LEGUME)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_KG)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# FARINE
#=====================================================

class Farine(productbase.ProductBase):
	#les attributs
	contenant= models.CharField("CONTENANT",max_length=100, choices=CONTENANT_FARINE)
	produit_de_base= models.CharField("PRODUIT DE BASE",max_length=100, choices=PRODUIT_BASE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_KG)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# MAIS
#=====================================================

class Mais(productbase.ProductBase):
	#les attributs
	contenant= models.CharField("CONTENANT",max_length=100, choices=CONTENANT_MAIS)
	variete= models.CharField("VARIETE DU MAIS",max_length=100, choices=VARIETE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_KG)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# MANIOC
#=====================================================

class Manioc(productbase.ProductBase):
	#les attributs
	contenant= models.CharField("CONTENANT",max_length=100, choices=CONTENANT_MANIOC)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_KG)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# ARACHIDE
#=====================================================

class Arachide(productbase.ProductBase):
	#les attributs
	contenant= models.CharField("CONTENANT",max_length=100, choices=CONTENANT_ARACHIDE)
	caracteristique= models.CharField("CONTENANT",max_length=100, choices=CARACTERISTIQUE_ARACHIDE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_KG)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# SEMOULE
#=====================================================

class Semoule(productbase.ProductBase):
	#les attributs
	contenant= models.CharField("CONTENANT",max_length=100, choices=CONTENANT_SEMOULE)
	produit_de_base= models.CharField("PRODUIT DE BASE",max_length=100, choices=PRODUIT_BASE_SEMOULE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_KG)

	#ordonner les produits
	class Meta:
		ordering = ['prix']
