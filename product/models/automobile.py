from product.models import *
from utils.product_attributes.automobile import *
from utils.unite_prix import *

# Create your models here.

#=====================================================
# 1. Pièce de rechange - Refroidissement
#=====================================================
class PieceDeRechangeRefroidissement(productbase.ProductBase):
	type_piece_refroidissement=models.CharField("TYPE_PIECE_REFROIDISSEMENT",max_length=50, choices=TYPE_PIECE_REFROIDISSEMENT)
	modele=models.CharField("MODELE",max_length=50, choices=PIECE_RECHANGE_MODELE)
	marque=models.CharField("MARQUE",max_length=50, choices=PIECE_RECHANGE_MARQUE)
	annee_debut=models.CharField("ANNEE DEBUT FABRICATION VEHICULE",max_length=50, choices=ANNEE_DEBUT_FABRICATION_VEHICULE)
	annee_fin=models.CharField("ANNEE FIN FABRICATION VEHICULE",max_length=50, choices=ANNEE_FIN_FABRICATION_VEHICULE)
	prix = models.DecimalField(max_digits=10, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 2. Pièce de rechange - Direction suspension
#=====================================================
class PieceDeRechangeDirectionSuspension(productbase.ProductBase):
    type_piece_direction_suspension=models.CharField("PIECE RECHANGE DIRECTION-SUSPENSION",max_length=50, choices=PIECE_DIRECTION_SUSPENSION)
    modele=models.CharField("MODELE",max_length=50, choices=PIECE_RECHANGE_MODELE)
    marque=models.CharField("MARQUE",max_length=50, choices=PIECE_RECHANGE_MARQUE)
    annee_debut=models.CharField("ANNEE DEBUT FABRICATION VEHICULE",max_length=50, choices=ANNEE_DEBUT_FABRICATION_VEHICULE)
    annee_fin=models.CharField("ANNEE FIN FABRICATION VEHICULE",max_length=50, choices=ANNEE_FIN_FABRICATION_VEHICULE)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 3. Pièce de rechange - Transmission
#=====================================================
class PieceDeRechangeTransmission(productbase.ProductBase):
	type_piece_transmission=models.CharField("PIECE RECHANGE TRANSMISSION",max_length=50, choices=PIECE_RECHANGE_TRANSMISSION)
	modele=models.CharField("MODELE",max_length=50, choices=PIECE_RECHANGE_MODELE)
	marque=models.CharField("MARQUE",max_length=50, choices=PIECE_RECHANGE_MARQUE)
	annee_debut=models.CharField("ANNEE DEBUT FABRICATION VEHICULE",max_length=50, choices=ANNEE_DEBUT_FABRICATION_VEHICULE)
	annee_fin=models.CharField("ANNEE FIN FABRICATION VEHICULE",max_length=50, choices=ANNEE_FIN_FABRICATION_VEHICULE)
	prix = models.DecimalField(max_digits=10, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 4. Pièce de rechange - Carrosserie
#=====================================================
class PieceDeRechangeCarrosserie(productbase.ProductBase):
	type_piece_carosserie=models.CharField("PIECE RECHANGE CARROSSERIE",max_length=50, choices=PIECE_RECHANGE_CARROSSERIE)
	modele=models.CharField("MODELE",max_length=50, choices=PIECE_RECHANGE_MODELE)
	marque=models.CharField("MARQUE",max_length=50, choices=PIECE_RECHANGE_MARQUE)
	annee_debut=models.CharField("ANNEE DEBUT FABRICATION VEHICULE",max_length=50, choices=ANNEE_DEBUT_FABRICATION_VEHICULE)
	annee_fin=models.CharField("ANNEE FIN FABRICATION VEHICULE",max_length=50, choices=ANNEE_FIN_FABRICATION_VEHICULE)
	prix = models.DecimalField(max_digits=10, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 5. Pièce de rechange - Electrique
#=====================================================
class PieceDeRechangeElectrique(productbase.ProductBase):
	type_piece_electrique=models.CharField("PIECE RECHANGE ELECTRIQUE",max_length=50, choices=PIECE_RECHANGE_ELECTRIQUE)
	modele=models.CharField("MODELE",max_length=50, choices=PIECE_RECHANGE_MODELE)
	marque=models.CharField("MARQUE",max_length=50, choices=PIECE_RECHANGE_MARQUE)
	annee_debut=models.CharField("ANNEE DEBUT FABRICATION VEHICULE",max_length=50, choices=ANNEE_DEBUT_FABRICATION_VEHICULE)
	annee_fin=models.CharField("ANNEE FIN FABRICATION VEHICULE",max_length=50, choices=ANNEE_FIN_FABRICATION_VEHICULE)
	prix = models.DecimalField(max_digits=10, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 6. Pièce de rechange - Embrayage
#=====================================================
class PieceDeRechangeEmbrayage(productbase.ProductBase):
	type_piece_embrayage =models.CharField("PIECE RECHANGE EMBRAYAGE",max_length=50, choices=PIECE_RECHANGE_EMBRAYAGE)
	modele=models.CharField("MODELE",max_length=50, choices=PIECE_RECHANGE_MODELE)
	marque=models.CharField("MARQUE",max_length=50, choices=PIECE_RECHANGE_MARQUE)
	annee_debut=models.CharField("ANNEE DEBUT FABRICATION VEHICULE",max_length=50, choices=ANNEE_DEBUT_FABRICATION_VEHICULE)
	annee_fin=models.CharField("ANNEE FIN FABRICATION VEHICULE",max_length=50, choices=ANNEE_FIN_FABRICATION_VEHICULE)
	prix = models.DecimalField(max_digits=10, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 7. Pièce de rechange - Freinage
#=====================================================
class PieceDeRechangeFreinage(productbase.ProductBase):
	pieces_rechange_freinage =models.CharField(max_length=50, choices=PIECE_RECHANGE_FREINAGE)
	modele=models.CharField("MODELE",max_length=50, choices=PIECE_RECHANGE_MODELE)
	marque=models.CharField("MARQUE",max_length=50, choices=PIECE_RECHANGE_MARQUE)
	annee_debut=models.CharField("ANNEE DEBUT FABRICATION VEHICULE",max_length=50, choices=ANNEE_DEBUT_FABRICATION_VEHICULE)
	annee_fin=models.CharField("ANNEE FIN FABRICATION VEHICULE",max_length=50, choices=ANNEE_FIN_FABRICATION_VEHICULE)
	prix = models.DecimalField(max_digits=10, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 8. Pièce révision moteur
#=====================================================
class PieceRevisionMoteur(productbase.ProductBase):
	pieces_revision_moteur =models.CharField(max_length=50, choices=PIECE_REVISION_MOTEUR)
	modele=models.CharField("MODELE",max_length=50, choices=PIECE_RECHANGE_MODELE)
	marque=models.CharField("MARQUE",max_length=50, choices=PIECE_RECHANGE_MARQUE)
	annee_debut=models.CharField("ANNEE DEBUT FABRICATION VEHICULE",max_length=50, choices=ANNEE_DEBUT_FABRICATION_VEHICULE)
	annee_fin=models.CharField("ANNEE FIN FABRICATION VEHICULE",max_length=50, choices=ANNEE_FIN_FABRICATION_VEHICULE)
	prix = models.DecimalField(max_digits=10, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)

#=====================================================
# 9. Pièce rechange moteur
#=====================================================
class PieceRechangeMoteur(productbase.ProductBase):
    pieces_rechange_moteur=models.CharField("PIECE RECHANGE MOTEUR", max_length=50, choices=PIECE_RECHANGE_MOTEUR)
    modele=models.CharField("MODELE",max_length=50, choices=PIECE_RECHANGE_MODELE)
    marque=models.CharField("MARQUE",max_length=50, choices=PIECE_RECHANGE_MARQUE)
    annee_debut=models.CharField("ANNEE DEBUT FABRICATION VEHICULE",max_length=50, choices=ANNEE_DEBUT_FABRICATION_VEHICULE)
    annee_fin=models.CharField("ANNEE FIN FABRICATION VEHICULE",max_length=50, choices=ANNEE_FIN_FABRICATION_VEHICULE)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    units = models.CharField(max_length=50, choices=UNITE)
#=====================================================
# 10. Entretien et reparation de vehicule
#=====================================================
class EntretienEtReparationDeVehicule(productbase.ProductBase):
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    units = models.CharField(max_length=50, choices=UNITE_POURC_DEVIS)

#=====================================================
# 10. LOCATION VEHICULE
#=====================================================
class LocationVehicule(productbase.ProductBase):
	type_vehicule = models.CharField("TYPE DE VEHICULE", max_length=20, choices= TYPE_VEHICULE)
	marque=models.CharField("MARQUE DU VEHICULE", max_length=100, choices= MARQUE_VOITURE)
	modele=models.CharField("MODELE DU VEHICULE", max_length=100, choices= MODELE)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_JOUR)
	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  VOITUREJEEPBUS
#=====================================================

class VoitureJeepBus(productbase.ProductBase):

	#les attributs
	type_vehicule = models.CharField("TYPE VEHICULE",max_length=100, choices=TYPE_VEHICULE)
	marque_voiture  = models.CharField("MARQUE",max_length=100, choices=MARQUE_VOITURE)
	modele_voiture  = models.CharField("MODELE",max_length=100, choices=MODELE_VOITURE)
	etat_voiture = models.CharField("ETAT",max_length=100, choices=ETAT_VOITURE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  MOTODEUXROUES
#=====================================================

class MotoDeuxRoues(productbase.ProductBase):

	#les attributs

	marque_moto  = models.CharField("MARQUE",max_length=100, choices=MARQUE_MOTO)
	modele_moto  = models.CharField("MODELE",max_length=100, choices=MODELE_MOTO)
	type_usage = models.CharField("TYPE USAGE",max_length=100, choices=TYPE_USAGE)
	puissance_moteur = models.CharField("PUISSANCE MOTEUR",max_length=100, choices=PUISSANCE_MOTEUR)
	type_demarrage = models.CharField("TYPE DEMARRAGE",max_length=100, choices=TYPE_DEMARRAGE)
	etat_moto = models.CharField("ETAT",max_length=100, choices=ETAT_MOTO)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  MOTODEUXROUES  ==>  AUTOMOBILE
#=====================================================

class MotoTroisRoues(productbase.ProductBase):

	#les attributs

	marque_moto  = models.CharField("MARQUE",max_length=100, choices=MARQUE_MOTO)
	modele_moto  = models.CharField("MODELE",max_length=100, choices=MODELE_MOTO)

	puissance_moteur = models.CharField("PUISSANCE MOTEUR",max_length=100, choices=PUISSANCE_MOTEUR)
	type_demarrage = models.CharField("TYPE DEMARRAGE",max_length=100, choices=TYPE_DEMARRAGE)
	etat_moto = models.CharField("ETAT",max_length=100, choices=ETAT_MOTO)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  CAMION
#=====================================================

class Camion(productbase.ProductBase):

	#les attributs
	marque= models.CharField("MARQUE",max_length=100, choices=MARQUE_VOITURE)
	modele= models.CharField("MODEL",max_length=100, choices=MODELE)
	type_camion= models.CharField("MODELE",max_length=100, choices=TYPE_CAMION)
	etat = models.CharField("ETAT",max_length=100, choices=ETAT_VOITURE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  MOTEUR
#=====================================================

class Moteur(productbase.ProductBase):

	#les attributs
	marque= models.CharField("MARQUE",max_length=100, choices=MARQUE_VOITURE)
	modele= models.CharField("MODEL",max_length=100, blank=True, null=True,choices=MODELE)
	nombre_cylindres= models.CharField("NOMBRE CYLINDRE",max_length=100, blank=True, null=True,choices=NOMBRE_CYLINDRE)
	etat = models.CharField("ETAT",max_length=100, choices=ETAT_VOITURE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']



#=====================================================
# BOUGIE
#=====================================================
class Bougie(productbase.ProductBase):

	marque_bougie=models.CharField("MARQUE BOUGIE", max_length=100, choices= MARQUE_BOUGIE)
	ordinaire_platine=models.CharField("ORDINAIRE OU PLATINE", max_length=100, choices= ORDINAIRE_PLATINE)
	nombre_electrode=models.CharField("NOMBRE D'ELECTRODE", max_length=100, choices= NOMBRE_ELECTRODE)
	prix = models.DecimalField("PRIX", max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# COSSE BATTERIE
#=====================================================
class CosseBatterie(productbase.ProductBase):


	prix = models.DecimalField("PRIX", max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# PNEU
#=====================================================
class Pneu(productbase.ProductBase):

	marque_pneu=models.CharField("MARQUE", max_length=100, choices= MARQUE_PNEU)
	dimension_pneu=models.CharField("DIMENSION", max_length=100, choices= DIMENSION_PNEU)

	prix = models.DecimalField("PRIX", max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# BATTERIE
#=====================================================
class Batterie(productbase.ProductBase):

	marque_batterie=models.CharField("MARQUE", max_length=100, choices= MARQUE_BATTERIE)
	capacite_batterie=models.CharField("CAPACITE(AMPERE-HEURE)", max_length=100, choices= CAPACITE_BATTERIE)
	garantie_batterie=models.CharField("GARANTIE", max_length=100, choices= GARANTIE_BATTERIE)
	entretien_batterie=models.CharField("ENTRETIEN", max_length=100, choices= ENTRETIEN_BATTERIE)
	forme_batterie=models.CharField("FORME", max_length=100, choices= FORME_BATTERIE)
	format_batterie=models.CharField("FORMAT", max_length=100, choices= FORMAT_BATTERIE)

	prix = models.DecimalField("PRIX", max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# CABLE DE REMORQUAGE
#=====================================================

class CableDeRemorquage(productbase.ProductBase):
	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

