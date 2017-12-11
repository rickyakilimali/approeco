from product.models import *
from utils.product_attributes.automobile import ANNEE_DEBUT_FABRICATION_VEHICULE, ANNEE_FIN_FABRICATION_VEHICULE, PIECE_RECHANGE_REFROIDISSEMENT, PIECE_RECHANGE_DIRECTION_SUSPENSION, PIECE_RECHANGE_TRANSMISSION, PIECE_RECHANGE_CARROSSERIE, PIECE_RECHANGE_ELECTRIQUE, PIECE_RECHANGE_EMBRAYAGE, PIECE_RECHANGE_FREINAGE, PIECE_REVISION_MOTEUR, PIECE_RECHANGE_MOTEUR
from utils.unite_prix import UNITE

# Create your models here.

#=====================================================
# 1. Pièce de rechange - Refroidissement
#=====================================================
class PieceDeRechangeRefroidissement(productbase.ProductBase):
	pieces_rechange_refroidissement=models.CharField(max_length=50, choices=PIECE_RECHANGE_REFROIDISSEMENT)
	annee_debut_fabrication_vehicule=models.CharField(max_length=50, choices=ANNEE_DEBUT_FABRICATION_VEHICULE)
	annee_fin_fabrication_vehicule=models.CharField(max_length=50, choices=ANNEE_FIN_FABRICATION_VEHICULE)
	
	prix = models.DecimalField(max_digits=5, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 2. Pièce de rechange - Direction suspension
#=====================================================
class PieceDeRechangeDirectionSuspension(productbase.ProductBase):
	pieces_rechange_direction_suspension=models.CharField(max_length=50, choices=PIECE_RECHANGE_DIRECTION_SUSPENSION)
	annee_debut_fabrication_vehicule=models.CharField(max_length=50, choices=ANNEE_DEBUT_FABRICATION_VEHICULE)
	annee_fin_fabrication_vehicule=models.CharField(max_length=50, choices=ANNEE_FIN_FABRICATION_VEHICULE)
	
	prix = models.DecimalField(max_digits=5, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 3. Pièce de rechange - Transmission
#=====================================================
class PieceDeRechangeTransmission(productbase.ProductBase):
	pieces_rechange_transmission=models.CharField(max_length=50, choices=PIECE_RECHANGE_TRANSMISSION)
	annee_debut_fabrication_vehicule=models.CharField(max_length=50, choices=ANNEE_DEBUT_FABRICATION_VEHICULE)
	annee_fin_fabrication_vehicule=models.CharField(max_length=50, choices=ANNEE_FIN_FABRICATION_VEHICULE)
	
	prix = models.DecimalField(max_digits=5, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 4. Pièce de rechange - Carrosserie
#=====================================================
class PieceDeRechangeCarrosserie(productbase.ProductBase):
	pieces_rechange_carrosserie=models.CharField(max_length=50, choices=PIECE_RECHANGE_CARROSSERIE)
	annee_debut_fabrication_vehicule=models.CharField(max_length=50, choices=ANNEE_DEBUT_FABRICATION_VEHICULE)
	annee_fin_fabrication_vehicule=models.CharField(max_length=50, choices=ANNEE_FIN_FABRICATION_VEHICULE)
	
	prix = models.DecimalField(max_digits=5, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 5. Pièce de rechange - Electrique
#=====================================================
class PieceDeRechangeElectrique(productbase.ProductBase):
	pieces_rechange_electrique=models.CharField(max_length=50, choices=PIECE_RECHANGE_ELECTRIQUE)
	annee_debut_fabrication_vehicule=models.CharField(max_length=50, choices=ANNEE_DEBUT_FABRICATION_VEHICULE)
	annee_fin_fabrication_vehicule=models.CharField(max_length=50, choices=ANNEE_FIN_FABRICATION_VEHICULE)
	
	prix = models.DecimalField(max_digits=5, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 6. Pièce de rechange - Embrayage 
#=====================================================
class PieceDeRechangeEmbrayage(productbase.ProductBase):
	pieces_rechange_embrayage =models.CharField(max_length=50, choices=PIECE_RECHANGE_EMBRAYAGE)
	annee_debut_fabrication_vehicule=models.CharField(max_length=50, choices=ANNEE_DEBUT_FABRICATION_VEHICULE)
	annee_fin_fabrication_vehicule=models.CharField(max_length=50, choices=ANNEE_FIN_FABRICATION_VEHICULE)
	
	prix = models.DecimalField(max_digits=5, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 7. Pièce de rechange - Embrayage 
#=====================================================
class PieceDeRechangeFreinage(productbase.ProductBase):
	pieces_rechange_freinage =models.CharField(max_length=50, choices=PIECE_RECHANGE_FREINAGE)
	annee_debut_fabrication_vehicule=models.CharField(max_length=50, choices=ANNEE_DEBUT_FABRICATION_VEHICULE)
	annee_fin_fabrication_vehicule=models.CharField(max_length=50, choices=ANNEE_FIN_FABRICATION_VEHICULE)
	
	prix = models.DecimalField(max_digits=5, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 8. Pièce révision moteur 
#=====================================================
class PieceRevisionMoteur(productbase.ProductBase):
	pieces_revision_moteur =models.CharField(max_length=50, choices=PIECE_REVISION_MOTEUR)
	annee_debut_fabrication_vehicule=models.CharField(max_length=50, choices=ANNEE_DEBUT_FABRICATION_VEHICULE)
	annee_fin_fabrication_vehicule=models.CharField(max_length=50, choices=ANNEE_FIN_FABRICATION_VEHICULE)
	
	prix = models.DecimalField(max_digits=5, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 9. Pièce rechange moteur 
#=====================================================
class PieceRechangeMoteur(productbase.ProductBase):
	pieces_rechange_moteur =models.CharField(max_length=50, choices=PIECE_RECHANGE_MOTEUR)
	annee_debut_fabrication_vehicule=models.CharField(max_length=50, choices=ANNEE_DEBUT_FABRICATION_VEHICULE)
	annee_fin_fabrication_vehicule=models.CharField(max_length=50, choices=ANNEE_FIN_FABRICATION_VEHICULE)
	
	prix = models.DecimalField(max_digits=5, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)