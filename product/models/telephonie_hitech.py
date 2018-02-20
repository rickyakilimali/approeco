from product.models import *
from utils.product_attributes.telephonie_hitech import *

from utils.unite_prix import UNITE



#=====================================================
#  SMARTPHONE
#=====================================================

class Smartphone(productbase.ProductBase):

	#les attributs
	marque_smartphone= models.CharField("MARQUE SMARTPHONE",max_length=100, choices=MARQUE_SMARTPHONE)
	modele_smartphone = models.CharField("MODELE SMARTPHONE",max_length=100, choices=MODELE_SMARTPHONE)
	systeme_exploitation = models.CharField("SYSTEME D'EXPLOITATION",max_length=50, choices=SYSTEME_EXPLOITATION)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  TELEPHONE MOBILE SIMPLE
#=====================================================

class TelephoneMobileSimple(productbase.ProductBase):

	#les attributs
	marque_mobile= models.CharField("MARQUE TELEPHONE",max_length=100, choices=MARQUE_MOBILE)
	modele_mobile = models.CharField("MODELE TELEPHONE",max_length=100, choices=MODELE_MOBILE)

	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']