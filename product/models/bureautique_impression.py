from product.models import *
from utils.product_attributes.bureautique_impression import *
from utils.unite_prix import *

#=====================================================
# 1. Carte de service
#=====================================================
class CarteService(productbase.ProductBase):
	face_impression = models.CharField("FACE A IMPRIMER",max_length=50, choices=FACE_IMPRIMEE)
	quantite = models.CharField("QUANTITE",max_length=50, choices=QUANTITE_CARTE_SERVICE)

	prix = models.DecimalField("PRIX",max_digits=12, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 2. Carte de visite
#=====================================================
class CarteVisite(productbase.ProductBase):

	face_impression = models.CharField("FACE A IMPRIMER",max_length=50, choices=FACE_IMPRIMEE)
	quantite = models.CharField("QUANTITE",max_length=50, choices=QUANTITE_CARTE_VISITE)

	prix = models.DecimalField("PRIX",max_digits=12, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 4. Stylo
#=====================================================
class Stylo(productbase.ProductBase):
	quantite = models.CharField("QUANTITE",max_length=50, choices=QUANTITE_STYLO)
	type_stylo=models.CharField("TYPE DE STYLO",max_length=50, choices=TYPE_STYLO)
	prix = models.DecimalField("PRIX",max_digits=12, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 5. T-shirt blanc
#=====================================================
class TShirtBlanc(productbase.ProductBase):
	quantite = models.CharField("QUANTITE",max_length=50, choices=QUANTITE)
	prix = models.DecimalField("PRIX",max_digits=12, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 6. T-shirt
#=====================================================
class TShirt(productbase.ProductBase):
	type_tshirt = models.CharField("TYPE",max_length=50, choices=TYPE_TSHIRT)

	quantite = models.CharField("QUANTITE",max_length=50, choices=QUANTITE_TSHIRT)

	prix = models.DecimalField("PRIX",max_digits=12, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 7. Depliant
#=====================================================
class Depliant(productbase.ProductBase):

	format_papier = models.CharField("FORMAT",max_length=50, choices=FORMAT_PAPIER)
	quantite = models.CharField("QUANTITE",max_length=50, choices=QUANTITE_4)

	prix = models.DecimalField("PRIX",max_digits=12, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 8. Pin's
#=====================================================
class Pins(productbase.ProductBase):
	quantite = models.CharField("QUANTITE",max_length=50, choices=QUANTITE_5)

	prix = models.DecimalField("PRIX",max_digits=12, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 9. Affiche
#=====================================================
class Affiche(productbase.ProductBase):


	format_papier = models.CharField("FORMAT",max_length=50, choices=FORMAT_PAPIER)
	quantite =models.CharField("QUANTITE",max_length=50, choices=QUANTITE_AFFICHE)

	prix = models.DecimalField("PRIX",max_digits=12, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)
#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 11. Porte clef
#=====================================================
class PorteClef(productbase.ProductBase):
	quantite = models.CharField("QUANTITE",max_length=50, choices=QUANTITE_PORTECLEF)

	prix = models.DecimalField("PRIX",max_digits=12, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 12. LANIERE
#=====================================================
class Laniere(productbase.ProductBase):
	quantite = models.CharField("QUANTITE",max_length=50, choices=QUANTITE_1)

	prix = models.DecimalField("PRIX",max_digits=12, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)
#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# 13. Casquette blanche
#=====================================================
class Casquette(productbase.ProductBase):
	quantite = models.CharField("QUANTITE",max_length=50, choices=QUANTITE_CASQUETTE)

	prix = models.DecimalField("PRIX",max_digits=12, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)
#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# 14. Flyers
#=====================================================
class Flyer(productbase.ProductBase):

	face_impression = models.CharField("FACE A IMPRIMER",max_length=50, choices=FACE_IMPRIMEE)
	format_papier = models.CharField("FORMAT",max_length=50, choices=FORMAT_PAPIER)
	quantite = models.CharField("QUANTITE",max_length=50, choices=QUANTITE_FLYER)

	prix = models.DecimalField("PRIX",max_digits=12, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 15. Carnets
#=====================================================
class Carnet(productbase.ProductBase):

	format_papier =models.CharField("FORMAT",max_length=50, choices=FORMAT_PAPIER)
	quantite = models.CharField("QUANTITE",max_length=50, choices=QUANTITE)

	prix = models.DecimalField("PRIX",max_digits=12, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 16. Poster
#=====================================================





#=====================================================
# 17.
#=====================================================


#=====================================================
# 18. Cachet
#=====================================================


#=====================================================
# 19. Cachet
#=====================================================
class Cachet(productbase.ProductBase):
	type_cachet = models.CharField("TYPE DE CACHET",max_length=50, choices=TYPE_CACHET)
	dimension_cachet = models.CharField("DIMENSION DE CACHET(MILLIMETRE)",max_length=50, choices=DIMENSION_CACHET)
	prix = models.DecimalField("PRIX",max_digits=12, decimal_places=2)
	units = models.CharField("UNITS",max_length=50, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 20. Gravure
#=====================================================
class Gravure(productbase.ProductBase):
	support_gravure = models.CharField("SUPPORT DE GRAVURE", max_length=50, choices=SUPPORT_GRAVURE)
	prix = models.DecimalField("PRIX",max_digits=12, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# AUTOCOLLANT
#=====================================================

class Autocollant(productbase.ProductBase):
	#les attributs
	quantite= models.CharField("QUANTITE", max_length=50, choices=QUANTITE_AUTOCOLLANT)
	format_autocollant= models.CharField("FORMAT", max_length=50, choices=FORMAT_AUTOCOLLANT)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 21. AUTOCOLLANT VINYLE ADHESIF
#=====================================================
class AutocollantVinyleAdhesif(productbase.ProductBase):
	type_autocollant = models.CharField("TYPE", max_length=50, choices=TYPE_AUTOCOLLANT)
	quantite = models.CharField("QUANTITE", max_length=50, choices=QUANTITE_VINYLE)
	prix = models.DecimalField("PRIX",max_digits=12, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_M2)
#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 22. BACK DROPS
#=====================================================
class BackDrops(productbase.ProductBase):

	dimension = models.CharField("DIMENSION", max_length=50, choices=DIMENSION_2)
	quantite = models.CharField("QUANTITE", max_length=50, choices=QUANTITE_BACKDROP)
	prix = models.DecimalField("PRIX",max_digits=12, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)
#ordonner les produits
	class Meta:
		ordering = ['prix']



#=====================================================
# 23. IMPRESSION BANDEROLE
#=====================================================
class ImpressionBanderole(productbase.ProductBase):
	type_support = models.CharField("TYPE SUPPORT", max_length=50, choices=TYPE_SUPPORT)
	quantite = models.CharField("TYPE SUPPORT", max_length=50, choices=QUANTITE_BANDEROLE)
	prix = models.DecimalField("PRIX",max_digits=12, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_M2)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 24. X-STAND
#=====================================================

class XStand(productbase.ProductBase):
	type_support = models.CharField("TYPE SUPPORT",max_length=50, choices=TYPE_SUPPORT_X)
	prix = models.DecimalField("PRIX",max_digits=12, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 25. SACHET
#=====================================================
class Sachet(productbase.ProductBase):
	quantite = models.CharField("QUANTITE",max_length=50, choices=QUANTITE_SACHET)
	prix = models.DecimalField(max_digits=12, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE_USD_PIECE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 26. ROLL UP
#=====================================================
class RollUp(productbase.ProductBase):
	dimension = models.CharField("DIMENSION",max_length=50, choices= DIMENSION_3)
	quantite = models.CharField("QUANTITE",max_length=50, choices= QUANTITE_ROLLUP)
	prix = models.DecimalField("PRIX",max_digits=12, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 1. EVENEMENTIEL
#=====================================================
class Evenemententiel(productbase.ProductBase):
	type_evenement_de_masse =models.CharField("TYPE D'EVENEMENT", max_length=100, choices=TYPE_EVENEMENT_DE_MASSE)
	minimum_payable = models.CharField("MINIMUM PAYABLE", max_length=20, blank=True, null=True, choices=MINIMUM_PAYABLE)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_POURC_DEVIS)
	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# 2. COMMUNICATION GRAPHIQUE
#=====================================================
class CommunicationGraphique(productbase.ProductBase):
	type_conception_graphique =models.CharField("TYPE DE COMMUNICATION GRAPHIQUE",max_length=100, choices=TYPE_COMMUNICATION_GRAPHIQUE)
	prix = models.DecimalField("PRIX", max_digits=10, decimal_places=2)
	units = models.CharField("UNITE", max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# 2. CONCEPTION GRAPHIQUE
#=====================================================
class ConceptionGraphique(productbase.ProductBase):
	type_conception_graphique =models.CharField("TYPE DE CONCEPTION GRAPHIQUE",max_length=100, choices=TYPE_CONCEPTION_GRAPHIQUE)
	prix = models.DecimalField("PRIX", max_digits=10, decimal_places=2)
	units = models.CharField("UNITE", max_length=50, choices=UNITE_USD_THEME)
	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# 3. COMMUNICATION DE MASSE
#=====================================================
class CommunicationDeMasse(productbase.ProductBase):
	type_communication_de_masse = models.CharField("TYPE DE COMMUNICATION DE MASSE", max_length=100, choices= TYPE_COMMUNICATION_DE_MASSE)
	prix = models.DecimalField("PRIX", max_digits=10, decimal_places=2)
	units = models.CharField("UNITE", max_length=50, choices=UNITE_USD_PERSONNE_JOUR)
	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# 3.
#=====================================================


#=====================================================
# 4. ECRITURE SCENARIO
#=====================================================
class EcritureScenario(productbase.ProductBase):
	nombre_minute = models.CharField("DUREE DU SCENARIO(MINUTE)", max_length=20, choices= NOMBRE_MINUTE_ECRITURE_SCENARIO)
	prix = models.DecimalField("PRIX", max_digits=10, decimal_places=2)
	units = models.CharField("UNITE", max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# 5. POSTPRODUCTION
#=====================================================
class Postproduction(productbase.ProductBase):
	nombre_minute = models.CharField("DUREE DE LA PRODUCTION(MINUTE)", max_length=20, choices= NOMBRE_MINUTE_POST_PRODUCTION)
	prix = models.DecimalField("PRIX", max_digits=10, decimal_places=2)
	units = models.CharField("UNITE", max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# 5. PRODUCTION ET TOURNAGE
#=====================================================
class ProductionTournage(productbase.ProductBase):
	nombre_minute = models.CharField("DUREE DU TOURNAGE(MINUTE)", max_length=20, choices= NOMBRE_MINUTE_PRODUCTION_TOURNAGE)
	prix = models.DecimalField("PRIX", max_digits=10, decimal_places=2)
	units = models.CharField("UNITE", max_length=50, choices=UNITE)
#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# 5. FIXEUR
#=====================================================
class Fixeur(productbase.ProductBase):

	prix = models.DecimalField("PRIX", max_digits=10, decimal_places=2)
	units = models.CharField("UNITE", max_length=50, choices=UNITE_USD_PERSONNE_JOUR)
#ordonner les produits
	class Meta:
		ordering = ['prix']



#=====================================================
# 6. insertion publicitaire
#=====================================================
class InsertionPublicitaire(productbase.ProductBase):
	type_insertion =models.CharField("TYPE INSERTION", max_length=20, choices=TYPE_ABONNEMENT)
	periodicite_parution =models.CharField("PERIODICITÉ DE PARUTION",max_length=20, choices= PERIODICITE_PARUTION)
	tirage =models.CharField("TIRAGE", max_length=20, choices=TIRAGE)
	dimension =models.CharField("DIMENSION INSERTION", max_length=100, choices=DIMENSION)

	prix = models.DecimalField("PRIX", max_digits=10, decimal_places=2)
	units = models.CharField("UNITE", max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 6. Conception page magazine
#=====================================================
class ConceptionPageMagazine(productbase.ProductBase):
	prix = models.DecimalField("PRIX", max_digits=10, decimal_places=2)
	units = models.CharField("UNITE", max_length=50, choices=UNITE_USD_PAGE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  SPOT PUBLICITAIRE  ==> COMMUNICATION EDITION
#=====================================================

class DiffusionSpotPublicitaire(productbase.ProductBase):

	#les attributs
	periode  = models.CharField("PERIODE",max_length=100, choices=PERIODE)

	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_SECONDE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  BANDE DEFILANTE  ==> COMMUNICATION EDITION
#=====================================================

class BandeDefilante(productbase.ProductBase):

	#les attributs


	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_JOUR)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  COMMUNIQUÉ  ==> COMMUNICATION EDITION
#=====================================================

class Communique(productbase.ProductBase):

	#les attributs
	type_communique  = models.CharField("TYPE COMMUNIQUÉ",max_length=100, choices=TYPE_COMMUNIQUE)

	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_COMMUNIQUE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  LOCATION STUDIO  ==> COMMUNICATION EDITION
#=====================================================

class LocationStudio(productbase.ProductBase):

	#les attributs
	duree_location  = models.CharField("DUREE DE LOCATION",max_length=100, choices=DUREE_LOCATION)

	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
#  AFFICHAGE LOGO SUR ECRAN  ==> COMMUNICATION EDITION
#=====================================================

class AffichageLogoSurEcran(productbase.ProductBase):

	#les attributs


	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_HEURE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  REPORTAGE TELEPROMO  ==> COMMUNICATION EDITION
#=====================================================

class ReportageTelepromo(productbase.ProductBase):

	#les attributs

	type_telepromo  = models.CharField("TYPE DE TELEPROMO",max_length=100, choices=TYPE_TELEPROMO)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  PAGE MAGAZINE  ==> COMMUNICATION EDITION
#=====================================================

class PageMagazine(productbase.ProductBase):

	#les attributs

	duree_magazine  = models.CharField("DUREE DU MAGAZINE",max_length=100, choices=DUREE_MAGAZINE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  PUBLICITE SUR PLATEAU  ==> COMMUNICATION EDITION
#=====================================================

class PubliciteSurPlateau(productbase.ProductBase):

	#les attributs

	type_publicite  = models.CharField("TYPE DE PUBLICITE",max_length=100, choices=TYPE_PUBLICITE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  PRESENCE PHYSIQUE SUR PLATEAU  ==> COMMUNICATION EDITION
#=====================================================

class PresencePhysiqueSurPlateau(productbase.ProductBase):

	#les attributs


	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_MIN)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  RETRANSMISSION EN DIRECT  ==> COMMUNICATION EDITION
#=====================================================

class RetransmissionDirect(productbase.ProductBase):

	#les attributs

	duree_retransmission  = models.CharField("DUREE DE LA RETRANSMISSION",max_length=100, choices=DUREE_RETRANSMISSION)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  BRODERIE SUR TSHIRT  ==> COMMUNICATION EDITION
#=====================================================

class BroderieSurTshirt(productbase.ProductBase):

	#les attributs
	type_tshirt = models.CharField("TYPE DE TSHIRT",max_length=100, choices=TYPE_TSHIRT)
	support = models.CharField("SUPPORT",max_length=100, choices=SUPPORT)
	quantite = models.CharField("QUANTITE",max_length=100, choices=QUANTITE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  COUVERTURE PHOTO
#=====================================================

class CouverturePhoto(productbase.ProductBase):

	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_HEURE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
#  BRODERIE ECUSSONS
#=====================================================

class BroderieEcussons(productbase.ProductBase):

	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  IMPRESSION SUR TASSE
#=====================================================

class ImpressionTasse(productbase.ProductBase):

	#les attributs
	quantite = models.CharField("SUPPORT",max_length=100, choices=QUANTITE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  IMPRESSION SUR PAPIER PHOTO
#=====================================================

class ImpressionSurPapierPhoto(productbase.ProductBase):

	#les attributs
	quantite = models.CharField("SUPPORT",max_length=100, choices=QUANTITE_3)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_M2)

	#ordonner les produits
	class Meta:
		ordering = ['prix']



#=====================================================
#  AGRAFES
#=====================================================

class Agrafe(productbase.ProductBase):

	#les attributs
	dimension_agrafe = models.CharField("DIMENSION",max_length=100, choices=DIMENSION_AGRAFE)
	quantite = models.CharField("QUANTITE PAR BOITE",max_length=100, choices=QUANTITE_PAPETERIE)

	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_BOITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  AGRAFEUSE
#=====================================================

class Agrafeuse(productbase.ProductBase):

	#les attributs
	dimension_agrafeuse = models.CharField("DIMENSION",max_length=100, choices=DIMENSION_AGRAFE)


	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  ALBUM CARTE DE VISITE
#=====================================================

class AlbumCarteDeVisite(productbase.ProductBase):

	#les attributs



	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  ALBUM CARTE DE VISITE
#=====================================================

class AnneauPlastique(productbase.ProductBase):

	#les attributs
	taille_anneau = models.CharField("TAILLE DE L'ANNEAU",max_length=100, choices=TAILLE_ANNEAU)
	quantite = models.CharField("QUANTITE",max_length=100, choices=QUANTITE_PAPETERIE)


	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PAQUET)

	#ordonner les produits
	class Meta:
		ordering = ['prix']



#=====================================================
#  ATTACHE
#=====================================================

class Attache(productbase.ProductBase):

	#les attributs
	taille_attache = models.CharField("TAILLE DE L'ATTACHE",max_length=100, choices=TAILLE_ATTACHE)

	contenant = models.CharField("CONTENANT",max_length=100, choices=CONTENANT)
	nombre_boite = models.CharField("",max_length=100, choices=QUANTITE_CONTENANT)
	quantite_par_boite = models.CharField("NOMBRE DE BOITE",max_length=100, choices=QUANTITE_PAR_PAQUET)


	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_BOITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  BAGUETTE
#=====================================================

class Baguette(productbase.ProductBase):

	#les attributs
	taille_baguette = models.CharField("TAILLE ANNEAU",max_length=100, choices=TAILLE_BAGUETTE)

	contenant = models.CharField("CONTENANT",max_length=100, choices=CONTENANT)
	quantite_par_paquet = models.CharField("QUANTITE PAR PAQUET",max_length=100, choices=QUANTITE_CONTENANT)


	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PAQUET)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  BAS A COURRIER
#=====================================================

class BacACourrier(productbase.ProductBase):

	#les attributs
	matiere = models.CharField("MATIERE",max_length=100, choices=MATIERE)
	nombre_bac = models.CharField("NOMBRE DE BAC",max_length=100, choices=NOMBRE_BAC)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  BANDE ADHESIVE
#=====================================================

class BandeAdhesive(productbase.ProductBase):

	#les attributs

	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']



#=====================================================
#  BATON DE COLLE
#=====================================================

class BatonDeColle(productbase.ProductBase):

	#les attributs
	marque = models.CharField("MARQUE",max_length=100, choices=MARQUE_PAPETERIE)
	poids = models.CharField("POIDS",max_length=100, choices=POIDS)



	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']



#=====================================================
#  BLOC NOTE LIGNE
#=====================================================

class BlocNoteLigne(productbase.ProductBase):

	#les attributs
	format_papeterie = models.CharField("FORMAT",max_length=100, choices=FORMAT_PAPETERIE)




	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  BLOC NOTE MEMO
#=====================================================

class BlocNoteMemo(productbase.ProductBase):

	#les attributs



	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  BOITE D'ARCHIVE
#=====================================================

class BoiteDArchive(productbase.ProductBase):

	#les attributs

	type_boite = models.CharField("TYPE DE BOITE",max_length=100, choices=TYPE_BOITE)
	dimension_boite = models.CharField("DIMENSION",max_length=100,blank=True, null=True, choices=DIMENSION_BOITE)


	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  CACHET DATEUR
#=====================================================

class CachetDateur(productbase.ProductBase):

	#les attributs
	type_cachet_dateur = models.CharField("TYPE DE CACHET",max_length=100,blank=True, null=True, choices=TYPE_CACHET_DATEUR)



	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  CAHIER
#=====================================================

class Cahier(productbase.ProductBase):

	#les attributs
	format = models.CharField("FORMAT",max_length=100,blank=True, null=True, choices=FORMAT_PAPETERIE)
	type_cahier = models.CharField("TYPE DE CAHIER",max_length=100,blank=True, null=True, choices=TYPE_CAHIER)



	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  CALCULATRICE
#=====================================================

class Calculatrice(productbase.ProductBase):

	#les attributs
	type_calculatrice = models.CharField("TYPE DE CALCULATRICE",max_length=100,blank=True, null=True, choices=TYPE_CALCULATRICE)




	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  CARBONNE
#=====================================================

class Carbonne(productbase.ProductBase):

	#les attributs
	type_carbonne = models.CharField("TYPE DE CARBONNE",max_length=100,blank=True, null=True, choices=TYPE_CARBONNE)
	contenant = models.CharField("CONTENANT",max_length=100, choices=CONTENANT)
	quantite_par_paquet = models.CharField("QUANTITE",max_length=100, choices=QUANTITE_PAR_PAQUET)



	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PAQUET)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  CARNET DE RECU
#=====================================================

class CarnetDeRecu(productbase.ProductBase):

	#les attributs



	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  ROSE A RELIURE
#=====================================================

class RoseAReliure(productbase.ProductBase):

	#les attributs
	format_papeterie = models.CharField("FORMAT",max_length=100, choices=FORMAT_PAPETERIE)
	contenant = models.CharField("CONTENANT",max_length=100, choices=CONTENANT)
	quantite_par_paquet = models.CharField("QUANTITE",max_length=100, choices=QUANTITE_PAR_PAQUET)

	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PAQUET)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  CISIEAU
#=====================================================

class Ciseau(productbase.ProductBase):

	#les attributs
	taille = models.CharField("TAILLE EN CENTIMETRE",max_length=100, choices=TAILLE_CISEAU)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  CLASSEUR
#=====================================================

class Classeur(productbase.ProductBase):

	#les attributs
	format_classeur = models.CharField("FORMAT",max_length=100, choices=FORMAT_CLASSEUR)


	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  COLLE LIQUIDE
#================================

class ColleLiquide(productbase.ProductBase):

	#les attributs
	quantite_colle = models.CharField("TAILLE",max_length=100, choices=TAILLE_COLLE)


	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  CORRECTEUR LIQUIDE
#================================

class CorrecteurLiquide(productbase.ProductBase):

	#les attributs



	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  DESAGRAFEUSE
#================================

class Desagrafeuse(productbase.ProductBase):

	#les attributs



	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']



#=====================================================
#  ETIQUETTE DYMO
#================================

class EtiquetteDymo(productbase.ProductBase):

	#les attributs



	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  ECRITOIRE
#================================

class Ecritoire(productbase.ProductBase):

	#les attributs
	matiere_ecritoire = models.CharField("MATIERE DE L'ECRITOIRE",max_length=100, choices=TYPE_ECRITOIRE)


	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  ELASTIQUES
#================================

class Elastiques(productbase.ProductBase):

	#les attributs
	contenant = models.CharField("CONTENANT",max_length=100, choices=CONTENANT)
	quantite = models.CharField("QUANTITE EN GRAMMES",max_length=100, choices=QUANTITE_CONTENANT)


	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PAQUET)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  ENVELOPPES
#================================

class Enveloppe(productbase.ProductBase):

	#les attributs
	format_enveloppe = models.CharField("FORMAT",max_length=100, choices=FORMAT_PAPETERIE)
	contenant = models.CharField("CONTENANT",max_length=100, choices=CONTENANT)
	quantite_par_paquet = models.CharField("QUANTITE PAR PAQUET",max_length=100, choices=QUANTITE_PAR_PAQUET)


	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PAQUET)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  ETUI
#================================

class Etui(productbase.ProductBase):

	#les attributs
	format_etui = models.CharField("FORMAT",max_length=100, choices=FORMAT_PAPETERIE)
	contenant = models.CharField("CONTENANT",max_length=100, choices=CONTENANT)
	quantite_par_paquet = models.CharField("QUANTITE PAR PAQUET",max_length=100, choices=QUANTITE_PAR_PAQUET)


	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PAQUET)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  FARDE
#================================

class Farde(productbase.ProductBase):

	#les attributs
	type_farde = models.CharField("TYPE DE FARDE",max_length=100, choices=TYPE_FARDE)



	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  GOMME
#================================

class Gomme(productbase.ProductBase):

	#les attributs




	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  INTERCALAIRE
#================================

class Intercalaire(productbase.ProductBase):

	#les attributs
	contenant = models.CharField("CONTENANT",max_length=100, choices=CONTENANT)
	quantite_par_jeu = models.CharField("QUANTITE PAR JEU",max_length=100, choices=QUANTITE_PAR_JEU)



	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_JEU)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  LATTE
#================================

class Latte(productbase.ProductBase):

	#les attributs
	longueur = models.CharField("LONGUEUR EN CENTIMETRE",max_length=100, choices=LONGUEUR)




	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  MARQUEUR
#================================

class Marqueur(productbase.ProductBase):

	#les attributs
	marque = models.CharField("MARQUE",max_length=100, choices=MARQUE_PAPETERIE)
	contenant = models.CharField("CONTENANT",max_length=100, choices=CONTENANT)
	quantite_par_paquet = models.CharField("QUANTITE PAR PAQUET",max_length=100, choices=QUANTITE_PAR_PAQUET)




	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PAQUET)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  PAPIER
#================================

class Papier(productbase.ProductBase):

	#les attributs
	type_papier = models.CharField("TYPE PAPIER",max_length=100, choices=TYPE_PAPIER)
	format_papier = models.CharField("FORMAT",max_length=100,blank=True,null=True, choices=FORMAT_PAPETERIE)
	contenant = models.CharField("CONTENANT",max_length=100, choices=CONTENANT)
	quantite_par_contenant = models.CharField("QUANTITE PAR CONTENANT",max_length=100, choices=QUANTITE_PAR_PAQUET)


	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_CONTENANT)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  PERFORATEUR
#================================

class Perforateur(productbase.ProductBase):

	#les attributs

	format_perforateur = models.CharField("FORMAT DU PERFORATEUR",max_length=100, choices=FORMAT_PERFORATEUR)



	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  PILE
#================================

class Pile(productbase.ProductBase):

	#les attributs

	format_pile = models.CharField("FORMAT DE LA PILE",max_length=100, choices=FORMAT_PILE)
	contenant = models.CharField("CONTENANT",max_length=100, choices=CONTENANT)
	quantite_par_paquet = models.CharField("QUANTITE PAR PAQUET",max_length=100, choices=QUANTITE_PAR_PAQUET)



	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PAQUET)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  PORTE CLE
#================================

class PorteCle(productbase.ProductBase):

	#les attributs


	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  POST IT
#=====================================================

class PostIt(productbase.ProductBase):

	#les attributs

	type_postit = models.CharField("TYPE DE POST-IT",max_length=100, choices=TYPE_POSTIT)
	contenant = models.CharField("CONTENANT",max_length=100, choices=CONTENANT)
	dimension_postit = models.CharField("DIMENSION EN MILLIMETRE",max_length=100, choices=DIMENSION_POSTIT)



	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_CARNET)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  POUBELLE
#================================

class Poubelle(productbase.ProductBase):

	#les attributs

	matiere = models.CharField("MATIERE",max_length=100, choices=MATIERE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  PUNAISE
#================================

class Punaise(productbase.ProductBase):

	#les attributs

	contenant = models.CharField("CONTENANT",max_length=100, choices=CONTENANT)
	quantite_par_boite = models.CharField("QUANTITE PAR BOITE",max_length=100, choices=QUANTITE_PAR_PAQUET)


	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_BOITE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']




#=====================================================
#  REGISTRE INDICATEUR DE COURRIER
#================================

class RegistreIndicateurDeCourrier(productbase.ProductBase):

	#les attributs

	nombre_feuilles = models.CharField("NOMBRE DE FEUILLES",max_length=100, choices=NOMBRE_FEUILLES)



	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  SCOTCH
#================================

class Scotch(productbase.ProductBase):

	#les attributs

	longueur = models.CharField("LONGUEUR EN METRE",max_length=100, choices=LONGUEUR)



	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  SIGNATAIRE
#================================

class Signataire(productbase.ProductBase):

	#les attributs

	nombre_compartiments = models.CharField("NOMBRE DE COMPARTIMENTS",max_length=100, choices=NOMBRE_COMPARTIMENTS)



	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
#  SOULIGNEUR
#================================

class Souligneur(productbase.ProductBase):

	#les attributs

	marque = models.CharField("MARQUE",max_length=100, choices=MARQUE_PAPETERIE)



	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  STYLO FEUTRE
#================================

class StyloFeutre(productbase.ProductBase):

	#les attributs


	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  STYLO PAPETERIE
#================================

class StyloPapeterie(productbase.ProductBase):

	#les attributs
	marque = models.CharField("MARQUE",max_length=100, choices=MARQUE_PAPETERIE)
	contenant = models.CharField("CONTENANT",max_length=100, choices=CONTENANT)
	quantite_par_paquet = models.CharField("QUANTITE PAR PAQUET",max_length=100, choices=QUANTITE_PAR_PAQUET)




	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PAQUET)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
#  TRANSPARENT A RELIURE
#================================

class TransparentAReliure(productbase.ProductBase):

	#les attributs
	format_transparent = models.CharField("FORMAT",max_length=100, choices=FORMAT_PAPETERIE)
	contenant = models.CharField("CONTENANT",max_length=100, choices=CONTENANT)
	quantite_par_paquet = models.CharField("QUANTITE PAR PAQUET",max_length=100, choices=QUANTITE_PAR_PAQUET)




	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PAQUET)

	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 6. GILLET
#=====================================================
class GiletKaki(productbase.ProductBase):
    quantite = models.CharField("QUANTITE",max_length=50, choices=QUANTITE_2)
    prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
    units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)

#ordonner les produits
class Meta:
		ordering = ['prix']

#=====================================================
# 7. CALENDRIER
#=====================================================
class Calendrier(productbase.ProductBase):
    format_calendrier = models.CharField("FORMAT",max_length=50, choices=FORMAT_CALENDRIER)
    quantite = models.CharField("QUANTITE",max_length=50, choices=QUANTITE_CALENDRIER)
    prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
    units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)
#ordonner les produits
class Meta:
		ordering = ['prix']

#=====================================================
# BRIQUET
#=====================================================
class ImpressionSurBriquet(productbase.ProductBase):
	quantite = models.CharField("QUANTITE",max_length=50, choices=QUANTITE_BRIQUET)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)
#ordonner les produits
class Meta:
		ordering = ['prix']

#=====================================================
# GRAPHISME ET ANIMATION 3D et 2D
#=====================================================
class GraphismeEtAnimation3D(productbase.ProductBase):

	type_animation = models.CharField(max_length=50, choices=TYPE_ANIMATION)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_SECONDE)

#ordonner les produits
class Meta:
		ordering = ['prix']


#=====================================================
# COMBINAISON
#=====================================================
class Combinaison(productbase.ProductBase):
	quantite = models.CharField("QUANTITE",max_length=50, choices=QUANTITE_COMBINAISON)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)

#ordonner les produits
class Meta:
		ordering = ['prix']


#=====================================================
# CHEMISE
#=====================================================
class Chemise(productbase.ProductBase):
	quantite = models.CharField("QUANTITE",max_length=50, choices=QUANTITE_CHEMISE)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)

#ordonner les produits
class Meta:
		ordering = ['prix']

#=====================================================
# PRESENTOIR
#=====================================================
class Presentoir(productbase.ProductBase):
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE)

#ordonner les produits
class Meta:
		ordering = ['prix']

#=====================================================
# BRANDING VEHICULE FULL
#=====================================================
class BrandingVehiculeFull(productbase.ProductBase):
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_M2)

#ordonner les produits
class Meta:
		ordering = ['prix']

#=====================================================
# IMPRESSION ABS
#=====================================================
class ImpressionABS(productbase.ProductBase):
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_M2)

#ordonner les produits
class Meta:
		ordering = ['prix']

#=====================================================
# IMPRESSION SUR ONE WAY
#=====================================================
class ImpressionOneWay(productbase.ProductBase):
	quantite = models.CharField("QUANTITE",max_length=50, choices=QUANTITE_ONEWAY)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_M2)

#ordonner les produits
class Meta:
		ordering = ['prix']

#=====================================================
# BOX LIGHT
#=====================================================
class BoxLight(productbase.ProductBase):
	nombre_face = models.CharField("NOMBRE DE FACE",max_length=50, choices=NOMBRE_FACE_BOXLIGHT)
	quantite = models.CharField("QUANTITE",max_length=50, choices=QUANTITE_BOXLIGHT)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)

#ordonner les produits
class Meta:
		ordering = ['prix']
#=====================================================
# SAC
#=====================================================
class Sac(productbase.ProductBase):
	quantite = models.CharField("QUANTITE",max_length=50, choices=QUANTITE_SAC)
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_USD_PIECE)

#ordonner les produits
class Meta:
		ordering = ['prix']


#====== 29-05-2018 =================================
# DIFFUSION DE CONTENU MEDIATIQUE
#===================================================

class DiffusionContenuMediatique(productbase.ProductBase):
	#les attributs
	prix = models.DecimalField("PRIX",max_digits=10, decimal_places=2)
	units = models.CharField("UNITE",max_length=50, choices=UNITE_POURC_DEVIS)

	#ordonner les produits
	class Meta:
		ordering = ['prix']


