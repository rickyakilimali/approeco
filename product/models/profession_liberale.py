from product.models import *
from utils.product_attributes.profession_liberale import TYPE_INTERVENTION,NOMBRE_EMPLOYES
from utils.unite_prix import UNITE

# Create your models here.

#=====================================================
# 1. Conseil 
#=====================================================
class Conseil(productbase.ProductBase):
	type_intervention =models.CharField(max_length=50, choices=TYPE_INTERVENTION)
	nombre_employes=models.CharField(max_length=50, choices=NOMBRE_EMPLOYES)
	prix = models.DecimalField(max_digits=12, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 2. Rédaction des procédures 
#=====================================================
class RedactionDesProcedures(productbase.ProductBase):
	type_intervention =models.CharField(max_length=50, choices=TYPE_INTERVENTION)
	nombre_employes=models.CharField(max_length=50, choices=NOMBRE_EMPLOYES)
	prix = models.DecimalField(max_digits=12, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 3. Assistance fiscale 
#=====================================================
class AssistanceFiscale(productbase.ProductBase):
	type_intervention =models.CharField(max_length=50, choices=TYPE_INTERVENTION)
	nombre_employes=models.CharField(max_length=50, choices=NOMBRE_EMPLOYES)
	prix = models.DecimalField(max_digits=12, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 4. Audit et contrôle interne 
#=====================================================
class AuditEtControleInterne(productbase.ProductBase):
	type_intervention =models.CharField(max_length=50, choices=TYPE_INTERVENTION)
	nombre_employes=models.CharField(max_length=50, choices=NOMBRE_EMPLOYES)
	prix = models.DecimalField(max_digits=12, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 5. Assistance comptable
#=====================================================
class AssistanceComptable(productbase.ProductBase):
	type_intervention =models.CharField(max_length=50, choices=TYPE_INTERVENTION)
	nombre_employes=models.CharField(max_length=50, choices=NOMBRE_EMPLOYES)
	prix = models.DecimalField(max_digits=12, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 6. Audit financier
#=====================================================
class AuditFinancier(productbase.ProductBase):
	type_intervention =models.CharField(max_length=50, choices=TYPE_INTERVENTION)
	nombre_employes=models.CharField(max_length=50, choices=NOMBRE_EMPLOYES)
	prix = models.DecimalField(max_digits=12, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)