from product.models import *
from utils.product_attributes.profession_liberale import *
from utils.unite_prix import UNITE

# Create your models here.

#=====================================================
# 1. Assistance comptable
#=====================================================
class AssistanceComptable(productbase.ProductBase):
	secteur=models.CharField("SECTEUR ", max_length=100, choices= SECTEUR)
	type_intervention =models.CharField("TYPE INTERVENTION", max_length=20, choices= TYPE_INTERVENTION  )
	nombre_employes =models.CharField("NOMBRE EMPLOYES", max_length=20, choices= NOMBRE_EMPLOYES )
	prix = models.DecimalField("PRIX", max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# 1. Conseil
#=====================================================
class Conseil(productbase.ProductBase):
	secteur=models.CharField("SECTEUR ", max_length=100, choices= SECTEUR)
	type_intervention =models.CharField("TYPE INTERVENTION", max_length=20, choices= TYPE_INTERVENTION  )
	nombre_employes =models.CharField("NOMBRE EMPLOYES", max_length=20, choices= NOMBRE_EMPLOYES )
	prix = models.DecimalField("PRIX", max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# 3. Assistance fiscale
#=====================================================
class AssistanceFiscale(productbase.ProductBase):
	secteur=models.CharField("SECTEUR ", max_length=100, choices= SECTEUR)
	type_intervention =models.CharField("TYPE INTERVENTION", max_length=20, choices= TYPE_INTERVENTION  )
	nombre_employes =models.CharField("NOMBRE EMPLOYES", max_length=20, choices= NOMBRE_EMPLOYES )
	prix = models.DecimalField("PRIX", max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# 4. Audit et contrôle interne
#=====================================================
class AuditControleInterne(productbase.ProductBase):
	secteur=models.CharField("SECTEUR ", max_length=100, choices= SECTEUR)
	type_intervention =models.CharField("TYPE INTERVENTION", max_length=20, choices= TYPE_INTERVENTION  )
	nombre_employes =models.CharField("NOMBRE EMPLOYÉS", max_length=20, choices= NOMBRE_EMPLOYES )
	prix = models.DecimalField("PRIX", max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# 5. Rédaction des procédures
#=====================================================
class RedactionProcedures(productbase.ProductBase):
	secteur=models.CharField("SECTEUR ", max_length=100, choices= SECTEUR)
	type_intervention =models.CharField("TYPE INTERVENTION", max_length=20, choices= TYPE_INTERVENTION  )
	nombre_employes =models.CharField("NOMBRE EMPLOYÉS", max_length=20, choices= NOMBRE_EMPLOYES )
	prix = models.DecimalField("PRIX", max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# 6. Audit financier
#=====================================================
class AuditFinancier(productbase.ProductBase):
	secteur=models.CharField("SECTEUR ", max_length=100, choices= SECTEUR)
	type_intervention =models.CharField("TYPE INTERVENTION", max_length=20, choices= TYPE_INTERVENTION  )
	nombre_employes =models.CharField("NOMBRE EMPLOYÉS", max_length=20, choices= NOMBRE_EMPLOYES )
	prix = models.DecimalField("PRIX", max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 6. PUBLICATION
#=====================================================
class Publication(productbase.ProductBase):
	titre=models.CharField("TITRE ", max_length=100, choices= TITRE)
	prix = models.DecimalField("PRIX", max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
