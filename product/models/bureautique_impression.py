from product.models import *
from utils.product_attributes.bureautique_impression import FORMAT_PAPIER,COULEUR_TSHIRT,TAILLE_Tshirt,UNITE_VENTE, QUANTITE, FACE_IMPRIMEE, TYPE_PAPIER, TYPE_TShirt, SUPPORT_CARNET, DIMENSION_CACHET, TYPE_CACHET, TYPE_CACHET_SEC, SUPPORT_GRAVURE
from utils.unite_prix import UNITE

#=====================================================
# 1. Carte de service
#=====================================================
class CarteService(productbase.ProductBase):
	face_impression = models.CharField(max_length=50, choices=FACE_IMPRIMEE)
	quantite = models.CharField(max_length=50, choices=QUANTITE)
	unite_vente = models.CharField(max_length=50, choices=UNITE_VENTE)
	prix = models.DecimalField(max_digits=12, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 2. Carte de visite
#=====================================================
class CarteVisite(productbase.ProductBase):
	type_papier = models.CharField(max_length=50, choices=TYPE_PAPIER)
	face_impression = models.CharField(max_length=50, choices=FACE_IMPRIMEE)
	quantite = models.CharField(max_length=50, choices=QUANTITE)
	unite_vente = models.CharField(max_length=50, choices=UNITE_VENTE)
	prix = models.DecimalField(max_digits=12, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 3. Shopping bag
#=====================================================
class ShoppingBag(productbase.ProductBase):
	quantite = models.CharField(max_length=50, choices=QUANTITE)
	unite_vente = models.CharField(max_length=50, choices=UNITE_VENTE)
	prix = models.DecimalField(max_digits=12, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 4. Stylo
#=====================================================
class Stylo(productbase.ProductBase):
	quantite = models.CharField(max_length=50, choices=QUANTITE)
	unite_vente = models.CharField(max_length=50, choices=UNITE_VENTE)
	prix = models.DecimalField(max_digits=12, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 5. T-shirt blanc
#=====================================================
class TShirtBlanc(productbase.ProductBase):
	quantite = models.CharField(max_length=50, choices=QUANTITE)
	unite_vente = models.CharField(max_length=50, choices=UNITE_VENTE)
	prix = models.DecimalField(max_digits=12, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 6. T-shirt
#=====================================================
class TShirt(productbase.ProductBase):
	type_tshirt = models.CharField(max_length=50, choices=TYPE_TShirt)
	taille_tshirt = models.CharField(max_length=50, choices=TAILLE_Tshirt)
	couleur_tshirt = models.CharField(max_length=50, choices=COULEUR_TSHIRT)
	quantite = models.CharField(max_length=50, choices=QUANTITE)
	unite_vente = models.CharField(max_length=50, choices=UNITE_VENTE)
	prix = models.DecimalField(max_digits=12, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 7. Depliant
#=====================================================
class Depliant(productbase.ProductBase):
	type_papier = models.CharField(max_length=50, choices=TYPE_PAPIER)
	face_impression = models.CharField(max_length=50, choices=FACE_IMPRIMEE)
	format_papier = models.CharField(max_length=50, choices=FORMAT_PAPIER)
	quantite = models.CharField(max_length=50, choices=QUANTITE)
	unite_vente = models.CharField(max_length=50, choices=UNITE_VENTE)
	prix = models.DecimalField(max_digits=12, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 8. Pin's
#=====================================================
class Pins(productbase.ProductBase):
	quantite = models.CharField(max_length=50, choices=QUANTITE)
	unite_vente = models.CharField(max_length=50, choices=UNITE_VENTE)
	prix = models.DecimalField(max_digits=12, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 9. Affiche
#=====================================================
class Affiche(productbase.ProductBase):
	type_papier = models.CharField(max_length=50, choices=TYPE_PAPIER)
	face_impression = models.CharField(max_length=50, choices=FACE_IMPRIMEE)
	format_papier = models.CharField(max_length=50, choices=FORMAT_PAPIER)
	quantite =models.CharField(max_length=50, choices=QUANTITE)
	unite_vente = models.CharField(max_length=50, choices=UNITE_VENTE)
	prix = models.DecimalField(max_digits=12, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 10. Farde
#=====================================================
class Farde(productbase.ProductBase):
	type_papier = models.CharField(max_length=50, choices=TYPE_PAPIER)
	face_impression = models.CharField(max_length=50, choices=FACE_IMPRIMEE)
	format_papier = models.CharField(max_length=50, choices=FORMAT_PAPIER)
	quantite = models.CharField(max_length=50, choices=QUANTITE)
	unite_vente = models.CharField(max_length=50, choices=UNITE_VENTE)
	prix = models.DecimalField(max_digits=12, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 11. Porte clef
#=====================================================
class PorteClef(productbase.ProductBase):
	quantite = models.CharField(max_length=50, choices=QUANTITE)
	unite_vente = models.CharField(max_length=50, choices=UNITE_VENTE)
	prix = models.DecimalField(max_digits=12, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 12. Porte clef
#=====================================================
class Laniere(productbase.ProductBase):
	quantite = models.CharField(max_length=50, choices=QUANTITE)
	unite_vente = models.CharField(max_length=50, choices=UNITE_VENTE)
	prix = models.DecimalField(max_digits=12, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 13. Casquette blanche
#=====================================================
class CasquetteBlanche(productbase.ProductBase):
	quantite = models.CharField(max_length=50, choices=QUANTITE)
	unite_vente = models.CharField(max_length=50, choices=UNITE_VENTE)
	prix = models.DecimalField(max_digits=12, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 14. Flyers
#=====================================================
class Flyer(productbase.ProductBase):
	type_papier = models.CharField(max_length=50, choices=TYPE_PAPIER)
	face_impression = models.CharField(max_length=50, choices=FACE_IMPRIMEE)
	format_papier = models.CharField(max_length=50, choices=FORMAT_PAPIER)
	quantite = models.CharField(max_length=50, choices=QUANTITE)
	unite_vente = models.CharField(max_length=50, choices=UNITE_VENTE)
	prix = models.DecimalField(max_digits=12, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 15. Carnets
#=====================================================
class Carnet(productbase.ProductBase):
	support_original = models.CharField(max_length=50, choices=SUPPORT_CARNET)
	support_copie = models.CharField(max_length=50, choices=SUPPORT_CARNET)
	support_souche = models.CharField(max_length=50, choices=SUPPORT_CARNET)
	format_papier =models.CharField(max_length=50, choices=FORMAT_PAPIER)
	quantite = models.CharField(max_length=50, choices=QUANTITE)
	unite_vente = models.CharField(max_length=50, choices=UNITE_VENTE)
	prix = models.DecimalField(max_digits=12, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 16. Cachet humide
#=====================================================
class CachetHumide(productbase.ProductBase):
	dimension = models.CharField(max_length=50, choices=DIMENSION_CACHET)
	prix = models.DecimalField(max_digits=12, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 17. Cachet Numerique
#=====================================================
class CachetNumerique(productbase.ProductBase):
	dimension = models.CharField(max_length=50, choices=DIMENSION_CACHET)
	prix = models.DecimalField(max_digits=12, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 18. Cachet imprimé
#=====================================================
class CachetImprime(productbase.ProductBase):
	type_cachet_imprime = models.CharField(max_length=50, choices=TYPE_CACHET)
	prix = models.DecimalField(max_digits=12, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 19. Cachet sec
#=====================================================
class CachetSec(productbase.ProductBase):
	type_cachet_sec = models.CharField(max_length=50, choices=TYPE_CACHET_SEC)
	dimension = models.CharField(max_length=50, choices=DIMENSION_CACHET)
	prix = models.DecimalField(max_digits=12, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 20. Gravure
#=====================================================
class Gravure(productbase.ProductBase):
	support_gravure = models.CharField(max_length=50, choices=SUPPORT_GRAVURE)
	prix = models.DecimalField(max_digits=12, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)