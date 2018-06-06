from product.models import *
from utils.product_attributes.agribusiness import *
from utils.unite_prix import *

#=====================================================
# 1. RIZ
#=====================================================
class Riz(productbase.ProductBase):

	variete = models.CharField("VARIETE",max_length=100, choices=VARIETE_RIZ)
	type_riz =models.CharField("TYPE DE RIZ",max_length=100, blank=True,null=True,choices=TYPE_RIZ)
	qualite =models.CharField("QUALITE",max_length=50, blank=True,null=True,choices=QUALITE_RIZ)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_KG)

#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# BOUILLIE
#=====================================================
class Bouillie(productbase.ProductBase):


	composition_bouillie =models.CharField("COMPOSITION",max_length=100, choices=COMPOSITION_BOUILLIE)
	qualite_bouillie =models.CharField("QUALITE ",max_length=100, choices= QUALITE_BOUILLIE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_KG)

#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
#  SEMENCE  ==> AGRIBUSINESS
#=====================================================

class Semence(productbase.ProductBase):

	#les attributs
	produit_agricole = models.CharField("PRODUIT AGRICOLE",max_length=100, choices=PRODUIT_AGRICOLE)
	variete = models.CharField("VARIETE",max_length=100,blank=True,null=True, choices=VARIETE_SEMENCE)
	poids = models.CharField("CONTENANT",max_length=100, choices=POIDS_SEMENCE)

	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_KG)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  BOUTURE MANIOC  ==> AGRIBUSINESS
#=====================================================

class BoutureManioc(productbase.ProductBase):

	#les attributs

	longueur = models.CharField("LONGUEUR",max_length=100, choices=LONGUEUR_BOUTURE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  HUILE  ==> AGRIBUSINESS
#=====================================================

class Huile(productbase.ProductBase):

	#les attributs

	base = models.CharField("PRODUIT DE BASE",max_length=100, choices=BASE_HUILE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_LITRE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  TOURTEAU  ==> AGRIBUSINESS
#=====================================================

class Tourteau(productbase.ProductBase):

	#les attributs

	base = models.CharField("PRODUIT DE BASE",max_length=100, choices=BASE_TOURTEAU)


	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_KG)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  REBOISEMENT ==> AGRIBUSINESS
#=====================================================

class Reboisement(productbase.ProductBase):

	#les attributs


	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_M2)

	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# LEGUME
#=====================================================
class Legume(productbase.ProductBase):
	type_legume =models.CharField("TYPE DE LEGUME",max_length=50, choices=TYPE_LEGUME_1)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_KG)

#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
#  POISSON
#=====================================================
class Poisson(productbase.ProductBase):
	type_de_poisson =models.CharField("TYPE DE POISSON",max_length=50, choices=TYPE_POISSON)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_KG)

#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  BOEUF
#=====================================================
class Boeuf(productbase.ProductBase):
	type_de_morceau =models.CharField("TYPE DE MORCEAU",max_length=50, choices=TYPE_MORCEAU_BOEUF)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_KG)

#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  PORC
#=====================================================
class Porc(productbase.ProductBase):
	type_de_morceau =models.CharField("TYPE DE MORCEAU",max_length=50, choices=TYPE_MORCEAU_PORC)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_KG)

#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
#  POULET
#=====================================================
class Poulet(productbase.ProductBase):
	type_de_poulet =models.CharField("TYPE DE POULET",max_length=50, choices=TYPE_POULET)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)

#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  CHEVRE
#=====================================================
class Chevre(productbase.ProductBase):
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  COSSETTE DE MANIOC
#=====================================================
class CossetteManioc(productbase.ProductBase):
	poids_par_sac=models.CharField("POIDS PAR SAC",max_length=50, choices=POIDS_PAR_SAC)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_KG)

#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  MIEL PUR
#=====================================================
class MielPur(productbase.ProductBase):
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_LITRE)

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
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_KG)

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
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_KG)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# LEGUME SECHE
#=====================================================

class LegumeSeche(productbase.ProductBase):
	#les attributs
	contenant= models.CharField("CONTENANT",max_length=100, choices=CONTENANT_LEGUME_SECHE)
	type_legume= models.CharField("TYPE DE LEGUME",max_length=100, choices=TYPE_LEGUME)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_KG)

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
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_KG)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# MAIS
#=====================================================

class Mais(productbase.ProductBase):
	#les attributs
	contenant= models.CharField("CONTENANT",max_length=100, choices=CONTENANT_MAIS)
	variete= models.CharField("VARIETE DU MAIS",max_length=100, choices=VARIETE_MAIS)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_KG)

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
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_KG)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# ARACHIDE
#=====================================================

class Arachide(productbase.ProductBase):
	#les attributs
	contenant= models.CharField("CONTENANT",max_length=100, choices=CONTENANT_ARACHIDE)
	caracteristique= models.CharField("CARACTERISTIQUE",max_length=100, choices=CARACTERISTIQUE_ARACHIDE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_KG)

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
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_KG)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# PATE D'ARACHIDE
#=====================================================

class PateDArachide(productbase.ProductBase):
	#les attributs
	conditionnement_arrachide= models.CharField("CONDITIONNEMENT",max_length=100, choices=CONDITIONNEMENT_ARACHIDE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_KG)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# PIMENT
#=====================================================

class PimentDeTable(productbase.ProductBase):
	#les attributs
	forme_piment= models.CharField("FORME",max_length=100, choices=FORME_PIMENT)
	type_piment= models.CharField("TYPE",max_length=100, choices=TYPE_PIMENT)
	conditionnement_piment = models.CharField("CONDITIONNEMENT",max_length=100, choices=CONDITIONNEMENT_PIMENT)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_KG)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# SECHAGE ET EMBALLAGE  DE LEGUMES
#=====================================================

class SechageEtEmballageDeLegumes(productbase.ProductBase):
	#les attributs
	poids_avant_sechage= models.CharField("POIDS AVANT SECHAGE",max_length=100, choices=POIDS_AVANT_LEGUMES)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_KG)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

