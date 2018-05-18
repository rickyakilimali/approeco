from product.models import *
from utils.product_attributes.energie import *
from utils.unite_prix import UNITE
#=====================================================
# 1. AMPOULE SOLAIRE
#=====================================================
class AmpouleSolaire(productbase.ProductBase):
	puissance =models.CharField("PUISSANCE", max_length=20, choices= PUISSANCE)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 2. BATTERIE SOLAIRE
#=====================================================
class BatterieSolaire(productbase.ProductBase):
	marque =models.CharField("MARQUE", max_length=20, choices= MARQUE)
	tension =models.CharField("TENSION(VOLT)", max_length=20, choices= TENSION)
	duree_vie=models.CharField("DUREE DE VIE", max_length=20, choices= DUREE_VIE)
	garantie=models.CharField("GARANTIE", max_length=20, choices= GARANTIE)
	capacite =models.CharField("CAPACITE(AMPERE-HEURE)", max_length=20, choices= CAPACITE_BATTERIE)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 3. PANNEAUX SOLAIRE
#=====================================================
class PanneauxSolaire(productbase.ProductBase):
	marque =models.CharField("MARQUE", max_length=20, choices= MARQUE_PANNEAU)
	type_cellule=models.CharField("TYPE CELLULE", max_length=20, choices= TYPE_CELLULE_PANNEAU)
	duree_vie=models.CharField("DUREE DE VIE", max_length=20, choices= DUREE_VIE)
	garantie=models.CharField("GARANTIE", max_length=20, choices= GARANTIE)
	puissance =models.CharField("PUISSANCE(WATT)", max_length=20, choices= PUISSANCE)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 4. REGULATEUR
#=====================================================
class Regulateur(productbase.ProductBase):
	marque =models.CharField("MARQUE", max_length=20, choices= MARQUE)
	type_regulation =models.CharField("TYPE REGULATION", max_length=20, choices= TYPE_REGULATION)
	intensite =models.CharField("INTENSITE(AMPERE)", max_length=20, choices= INTENSITE)
	prix = models.DecimalField("PRIX", max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# 5. CONVERTISSEUR
#=====================================================
class Convertisseur(productbase.ProductBase):
	marque_convertisseur =models.CharField("MARQUE CONVERTISSEUR", max_length=20, choices= MARQUE)
	puissance_convertisseur =models.CharField("PUISSANCE CONVERTISSEUR(WATT)", max_length=20, choices= PUISSANCE_CONVERTISSEUR )
	tension_convertisseur =models.CharField("TENSION CONVERTISSEUR(VOLT)", max_length=20, choices= TENSION_CONVERTISSEUR )
	chargeur =models.CharField("CHARGEUR", max_length=20, blank=True, null=True,choices= CHARGEUR )
	duree_vie=models.CharField("DUREE DE VIE", max_length=20, choices= DUREE_VIE)
	garantie=models.CharField("GARANTIE", max_length=20, choices= GARANTIE)
	sinus_pur =models.CharField("SINUS PUR", max_length=20, choices= SINUS_PUR )
	prix = models.DecimalField("PRIX", max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 6. INSTALLATION SOLAIRE
#=====================================================
class InstallationSolaire(productbase.ProductBase):
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_POURC_DEVIS)
	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 6. REPARATION INSTALLATION SOLAIRE
#=====================================================
class ReparationInstallationSolaire(productbase.ProductBase):
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_HEURE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']

