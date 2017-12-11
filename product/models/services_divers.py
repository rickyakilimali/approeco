from product.models import *
from utils.product_attributes.services_divers import TYPE_SERVICE_TRAITEUR,TYPE_NETTOYAGE,NIVEAU_COURS,LANGUES_INTERPRETARIAT,LANGUES,TYPE_DOCUMENT
from utils.unite_prix import UNITE

# Create your models here.

#=====================================================
# 1. Service traiteur
#=====================================================
class ServiceTraiteur(productbase.ProductBase):
	type_service_traiteur =models.CharField(max_length=20, choices=TYPE_SERVICE_TRAITEUR)
	prix = models.DecimalField(max_digits=5, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 2. Service nettoyage
#=====================================================
class ServiceNettoyage(productbase.ProductBase):
	type_service_nettoyage =models.CharField(max_length=20, choices=TYPE_NETTOYAGE)
	prix = models.DecimalField(max_digits=5, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 3. Cours d'anglais
#=====================================================
class CoursAnglais(productbase.ProductBase):
	niveau_cours =models.CharField(max_length=20, choices=NIVEAU_COURS)
	prix = models.DecimalField(max_digits=5, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 4. Interprétariat
#=====================================================
class Interpretariat(productbase.ProductBase):
	langue_interpretariat =models.CharField(max_length=20, choices=LANGUES_INTERPRETARIAT)
	prix = models.DecimalField(max_digits=5, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 5. Service de traduction
#=====================================================
class ServiceDeTraduction(productbase.ProductBase):
	langue =models.CharField(max_length=20, choices=LANGUES)
	type_document =models.CharField(max_length=20, choices=TYPE_DOCUMENT)
	prix = models.DecimalField(max_digits=5, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)