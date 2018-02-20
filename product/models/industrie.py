from product.models import *
from utils.product_attributes.industrie import *
from utils.unite_prix import UNITE



#=====================================================
# 1. PRODUIT DE NETTOYAGE
#=====================================================
class ProduitDeNettoyage(productbase.ProductBase):


	type_produit =models.CharField("TYPE DE PRODUIT",max_length=100, blank=True,null=True,choices=TYPE_PRODUIT)

	prix = models.DecimalField(max_digits=10, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# 1. PRODUIT DE DERATISATION
#=====================================================
class ProduitDeDeratisation(productbase.ProductBase):


	type_produit =models.CharField("TYPE DE PRODUIT",max_length=100, blank=True,null=True,choices=TYPE_PRODUIT)

	prix = models.DecimalField(max_digits=10, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#ordonner les produits
	class Meta:
		ordering = ['prix']