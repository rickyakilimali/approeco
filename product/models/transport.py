from product.models import *
from utils.product_attributes.transport import *
from utils.unite_prix import *

#=====================================================
# 1. DEMENAGEMENT
#=====================================================
class Demenagement(productbase.ProductBase):
	pays_source =models.CharField("PAYS SOURCE", max_length=20, choices= PAYS_SOURCE)
	ville_destination =models.CharField("VILLE DE DESTINATION", max_length=20, choices=VILLE_DE_DESTINATION)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_KG)

#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 2. FRET ROUTIER
#=====================================================
class FretRoutier(productbase.ProductBase):
	lieu_depart = models.CharField("LIEU DEPART", max_length=20, choices= LIEU_DEPART)
	lieu_destination = models.CharField("LIEU DESTINATION", max_length=20, choices= LIEU_DESTINATION)
	capacite_max = models.CharField("CAPACITÉ MAXIMUM(TONNES)", max_length=20, choices= CAPACITE_MAX)
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

#=====================================================
# 3. ENVOI COLIS NATIONAL 0 A 20 KGS
#=====================================================
class Envoicolisnational0a20kgs(productbase.ProductBase):
	ville_de_depart = models.CharField("VILLE DEPART", max_length=20, choices= VILLE_DEPART)
	ville_de_destination = models.CharField("VILLE DESTINATION", max_length=20, choices= VILLE_DESTINATION)
	poids= models.CharField("POIDS", max_length=20, choices= POIDS)
	delai_de_livraison= models.CharField("DELAI LIVRAISON", max_length=20, choices= DELAI_LIVRAISON)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 4. ENVOI COLIS NATIONAL 20,01KGS A 99,99KGS
#=====================================================
class Envoicolisnational20kgsa99kgs(productbase.ProductBase):
	ville_de_depart = models.CharField("VILLE DEPART", max_length=20, choices= VILLE_DEPART)
	ville_de_destination = models.CharField("VILLE DESTINATION", max_length=20, choices= VILLE_DESTINATION)
	delai_de_livraison= models.CharField("DELAI LIVRAISON", max_length=20, choices= DELAI_LIVRAISON)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_KG)
	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 5. ENVOI COLIS NATIONAL 100KGS ET PLUS
#=====================================================
class Envoicolisnational100kgsetplus(productbase.ProductBase):
	ville_de_depart = models.CharField("VILLE DEPART", max_length=20, choices= VILLE_DEPART)
	ville_de_destination = models.CharField("VILLE DESTINATION", max_length=20, choices= VILLE_DESTINATION)
	delai_de_livraison= models.CharField("DELAI LIVRAISON", max_length=20, choices= DELAI_LIVRAISON)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_KG)
	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 6. DEDOUANEMENT
#=====================================================
class Dedouanement(productbase.ProductBase):
	produits_exoneres = models.CharField("PRODUIT EXONERES", max_length=20, choices= PRODUIT_EXONERES)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 7. ENTREPOSAGE
#=====================================================
class Entreposage(productbase.ProductBase):
	type_entreposage = models.CharField("TYPE ENTREPOSAGE", max_length=50, choices= TYPE_ENTREPOSAGE)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 8. ENVOI COLIS INTERNATIONAL
#=====================================================
class Envoicolisinternational(productbase.ProductBase):
	ville_de_depart= models.CharField("VILLE DEPART", max_length=20, choices= VILLE_DEPART)
	pays_destination = models.CharField("PAYS DESTINATION", max_length=50, choices= PAYS_DESTINATION)
	delai_de_livraison= models.CharField("DELAI LIVRAISON", max_length=20, choices= DELAI_LIVRAISON)
	poids= models.CharField("POIDS", max_length=20, choices= POIDS)
	type_envoie= models.CharField("TYPE D'ENVOIE", max_length=20, choices= TYPE_ENVOIE)
	prix = models.DecimalField("PRIX", max_digits=15, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# 9. ENVOI COURRIER INTERNATIONAL
#=====================================================
class Envoicourrierinternational(productbase.ProductBase):
	ville_de_depart= models.CharField("VILLE DEPART", max_length=20, choices= VILLE_DEPART)
	pays_destination = models.CharField("PAYS DESTINATION", max_length=50, choices= PAYS_DESTINATION)
	delai_de_livraison= models.CharField("DELAI LIVRAISON", max_length=20, choices= DELAI_LIVRAISON)
	poids= models.CharField("POIDS", max_length=20, choices= POIDS)
	type_envoie= models.CharField("TYPE D'ENVOIE", max_length=20, choices= TYPE_ENVOIE)
	prix = models.DecimalField("PRIX", max_digits=15, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 11.INTERNATIONAL PLUS 70KG
#=====================================================
class Envoicolisinternationalplus70kg(productbase.ProductBase):
	ville_de_depart= models.CharField("VILLE DEPART", max_length=20, choices= VILLE_DEPART)
	pays_destination = models.CharField("PAYS DESTINATION", max_length=50, choices= PAYS_DESTINATION)
	delai_de_livraison= models.CharField("DELAI LIVRAISON", max_length=20, choices= DELAI_LIVRAISON)
	prix = models.DecimalField("PRIX", max_digits=15, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_KG)
	#ordonner les produits
	class Meta:
		ordering = ['prix']
