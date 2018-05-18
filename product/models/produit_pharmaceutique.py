from product.models import *
from utils.product_attributes.produit_pharmaceutique import *
from utils.unite_prix import UNITE

# Create your models here.

#=====================================================
# 1. produit pharmaceutique
#=====================================================
class ProduitPharmaceutique(productbase.ProductBase):
	classe_therapeutique =models.CharField("CLASSE THERAPEUTIQUE", max_length=50, choices=CLASSE_THERAPEUTIQUE)
	produit =models.CharField("PRODUIT", max_length=50, choices=PRODUIT)
	presentation =models.CharField("PRESENTATION", max_length=50, choices=PRESENTATION)
	dosage =models.CharField("DOSAGE", max_length=50, choices=DOSAGE)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
