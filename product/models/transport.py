from product.models import *
from utils.product_attributes.transport import *
from utils.unite_prix import UNITE
#=====================================================
# 1. DEMENAGEMENT
#=====================================================
class Demenagement(productbase.ProductBase):
	pays_source =models.CharField("PAYS SOURCE", max_length=20, choices= PAYS_SOURCE)
	ville_destination =models.CharField("VILLE DE DESTINATION", max_length=20, choices=VILLE_DE_DESTINATION)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 2. FRET ROUTIER
#=====================================================
class FretRoutier(productbase.ProductBase):
	lieu_depart = models.CharField("LIEU DEPART", max_length=20, choices= LIEU_DEPART)
	lieu_destination = models.CharField("LIEU DESTINATION", max_length=20, choices= LIEU_DESTINATION)
	capacite_max = models.CharField("CAPACITÉ MAXIMUM", max_length=20, choices= CAPACITE_MAX)
	prix = models.DecimalField("PRIX", max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
#  TRANSPORT DES BIENS INTRA KINSHASA
#=====================================================

class TransportBienIntraKinshasa(productbase.ProductBase):

	#les attributs
	poids  = models.CharField("POIDS",max_length=100, choices=POIDS_BIEN)
	assurance  = models.CharField("ASSURANCE",max_length=100, choices=ASSURANCE)
	duree_location = models.CharField("DUREE LOCATION",max_length=100, choices=DUREE_LOCATION)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  LOCATION PORTE-CONTENEUR
#=====================================================

class LocationPorteConteneur(productbase.ProductBase):

	#les attributs
	zone  = models.CharField("POIDS",max_length=100, choices=ZONE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']