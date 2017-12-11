from product.models import *
from utils.product_attributes.ameublement import TYPE_SIEGE, REVETEMENT_SIEGE, TYPES_ARMOIRE, TYPE_PORTE_ARMOIRE, DIMENSION_AMEUBLEMENT
from utils.unite_prix import UNITE

# Create your models here.

#=====================================================
# 1. Siège et fauteuil de bureau
#=====================================================
class SiegeEtFauteuilDeBureau(productbase.ProductBase):
	type_siege =models.CharField(max_length=50, choices=TYPE_SIEGE)
	revetement_siege =models.CharField(max_length=50, choices=REVETEMENT_SIEGE)
	prix = models.DecimalField(max_digits=5, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 2. Armoire
#=====================================================
class Armoire(productbase.ProductBase):
	type_armoire =models.CharField(max_length=50, choices=TYPES_ARMOIRE)
	type_porte =models.CharField(max_length=50, choices=TYPE_PORTE_ARMOIRE)
	dimension_armoire=models.CharField(max_length=50, choices=DIMENSION_AMEUBLEMENT)
	prix = models.DecimalField(max_digits=5, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)