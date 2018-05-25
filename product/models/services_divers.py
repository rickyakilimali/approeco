from product.models import *
from utils.product_attributes.services_divers import *
from utils.unite_prix import *

# Create your models here.


#=====================================================
# 3. Cours Langue Etrangère
#=====================================================
class CoursLangueEtrangere(productbase.ProductBase):
	langue_cours =models.CharField("LANGUE",max_length=20, choices=LANGUE_COURS)
	niveau_cours =models.CharField("NIVEAU DE COURS", max_length=20, choices=NIVEAU_COURS)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS", max_length=50, choices=UNITE_USD_PERSONNE)
#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# Cours Langue Nationale
#=====================================================
class CoursLangueNationale(productbase.ProductBase):
	langue_cours =models.CharField("LANGUE",max_length=20, choices=LANGUE_NATIONALE)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS", max_length=50, choices=UNITE_USD_HEURE)
#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 4. Interprétariat
#=====================================================
class Interpretariat(productbase.ProductBase):
	langue_interpretariat =models.CharField("LANGUE",max_length=20, choices=LANGUES_INTERPRETARIAT)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS", max_length=50, choices=UNITE_USD_JOUR)
#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 5. Service de traduction
#=====================================================
class ServiceDeTraduction(productbase.ProductBase):
	langue =models.CharField("LANGUE", max_length=20, choices=LANGUES)
	type_document =models.CharField("TYPE DE DOCUMENT",max_length=20, choices=TYPE_DOCUMENT)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS", max_length=50, choices=UNITE_USD_PAGE)

#========#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# 6. journal
#=====================================================
class AbonnementJournal(productbase.ProductBase):
	type_abonnement =models.CharField("TYPE ABONNEMENT", max_length=20, choices=TYPE_ABONNEMENT)
	periodicite_parution =models.CharField("PERIODICITÉ DE PARUTION",max_length=20, choices= PERIODICITE_PARUTION)
	duree_abonnement =models.CharField("DURÉE ABONNEMENT", max_length=20, choices=DUREE_ABONNEMENT)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS", max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']





#=====================================================
# 7. BUFFET
#=====================================================
class Buffet(productbase.ProductBase):
	choix_entree=models.CharField("CHOIX ENTRÉE", max_length=20, choices= CHOIX_ENTREE)
	choix_boisson_non_alcoolisee =models.CharField("CHOIX DE BOISSON NON ALCOOLISÉE", max_length=20, choices= CHOIX_BOISSON_FROIDE)
	choix_boisson_alcoolisee =models.CharField("CHOIX BOISSON ALCOOLISÉE", max_length=20, choices= CHOIX_BOISSON_ALCOOLISEE)
	choix_plats =models.CharField("CHOIX DU PLATS",max_length=20, choices= CHOIX_PLATS)
	choix_legumes =models.CharField("CHOIX DE LEGUMES", max_length=20, choices= CHOIX_DE_LEGUMES)
	choix_accompagnement =models.CharField("CHOIX ACCOMPAGNEMENT", max_length=20, choices= CHOIX_ACCOMPAGNEMENT)
	choix_dessert =models.CharField("CHOIX DESSERT", max_length=20, choices=CHOIX_DESSERT)
	lieu = models.CharField("LIEU", max_length=20, blank=True, null=True, choices=SUR_PLACE)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS", max_length=50, choices=UNITE_USD_PERSONNE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 8. COCKTAILS
#=====================================================
class cocktails(productbase.ProductBase):
	choix_amuse_gueule=models.CharField("CHOIX AMUSE GUEULE", max_length=20, choices= CHOIX_AMUSE_GUEULE)
	choix_boisson_non_alcoolisee =models.CharField("CHOIX DE BOISSON NON ALCOOLISÉE", max_length=20, choices= CHOIX_BOISSON_FROIDE)
	choix_boisson_alcoolisee =models.CharField("CHOIX BOISSON ALCOOLISÉE", max_length=20, choices= CHOIX_BOISSON_ALCOOLISEE)
	lieu = models.CharField("LIEU", max_length=20, blank=True, null=True, choices=SUR_PLACE)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS", max_length=50, choices=UNITE_USD_PERSONNE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# 9. PAUSE CAFE
#=====================================================
class PauseCafe(productbase.ProductBase):
	choix_amuse_gueule=models.CharField("CHOIX AMUSE GUEULE", max_length=20, choices= CHOIX_AMUSE_GUEULE)
	choix_boisson_froide =models.CharField("CHOIX DE BOISSON FROIDE", max_length=20, choices= CHOIX_BOISSON_FROIDE)
	choix_boisson_chaude =models.CharField("CHOIX BOISSON CHAUDE", max_length=20, choices= CHOIX_BOISSON_CHAUDE)
	choix_viennoiserie =models.CharField("CHOIX VIENNOISERIE", max_length=20, choices= CHOIX_VIENNOISERIE)
	lieu = models.CharField("LIEU", max_length=20, blank=True, null=True, choices=SUR_PLACE)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS", max_length=50, choices=UNITE_USD_PERSONNE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 10. SERVICE GARDIENNAGE
#=====================================================
class ServiceGardiennage(productbase.ProductBase):
	type_gardiennage =models.CharField("TYPE GARDIENNAGE", max_length=100, choices= TYPE_GARDIENNAGE)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS", max_length=50, choices=UNITE_USD_GARDIEN_MOIS)
	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# 11. SERVICE D'ACCUEIL
#=====================================================
class ServiceAccueil(productbase.ProductBase):
	periode_service=models.CharField("PERIODE SERVICE", max_length=20, choices= PERIODE_SERVICE)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS", max_length=50, choices=UNITE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# 13. PRODUIT DE NETTOYAGE
#=====================================================
class ProduitNettoyage(productbase.ProductBase):
	type_produit=models.CharField("TYPE PRODUIT", max_length=20, choices= TYPE_PRODUIT)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices= UNITE_LITRE)
	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# 14. ASSAINISSEMENT
#=====================================================
class Assainissement(productbase.ProductBase):
	type_assainissement=models.CharField("TYPE D'ASSAINISSEMENT", max_length=100, choices= TYPE_ASSAINISSEMENT)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_M2)
	#ordonner les produits
	class Meta:
		ordering = ['prix']


#=====================================================
# 15. SERVICES SPLIT
#=====================================================
class ServiceSplit(productbase.ProductBase):
	type_service_split=models.CharField("TYPE SERVICE SPLIT", max_length=20, choices= TYPE_SERVICE_SPLIT)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_SPLIT)
	#ordonner les produits
	class Meta:
		ordering = ['prix']



#=====================================================
# 16. ASSURANCE VOYAGE
#=====================================================
class AssuranceVoyage(productbase.ProductBase):
	periode =models.CharField("NOMBRE DES JOURS", max_length=20, choices= NOMBRE_JOUR)
	tranche_age =models.CharField("TRANCHE AGE", max_length=20, choices= TRANCHE_AGE)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_PERSONNE)
#ordonner les produits
	class Meta:
		ordering = ['prix']
#=====================================================
# 17. SERVICE AGENCE VOYAGE
#=====================================================
class ServiceAgenceVoyage(productbase.ProductBase):
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_PERSONNE)
#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# 18. ASSISTANCE OBTENTION VISA
#=====================================================
class AssistanceObtentionVisa(productbase.ProductBase):
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_PERSONNE)
#ordonner les produits
	class Meta:
		ordering = ['prix']

#=====================================================
# RESERVATION HOTEL A L'ETRANGER
#=====================================================
class ReservationHotelEtranger(productbase.ProductBase):
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_PERSONNE)
#ordonner les produits
	class Meta:
		ordering = ['prix']



#=====================================================
# 19. SALLE DE CONFERENCE
#=====================================================
class SalleConference(productbase.ProductBase):
	superficie =models.CharField("SUPERFICIE", max_length=20, choices= SUPERFICIE)
	micro_gratuit =models.CharField("MICRO GRATUIT", max_length=20, choices= MICRO_GRATUIT)
	retro_projecteur =models.CharField("RETRO PROJECTEUR", max_length=20, choices= RETRO_PROJECTEUR)
	baffle_gratuit =models.CharField("BAFFLE GRATUIT", max_length=20, choices= BAFFLE_GRATUIT)
	avenue =models.CharField("AVENUE", max_length=20, choices= AVENUE)
	commune =models.CharField("COMMUNE", max_length=20, choices= COMMUNE)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_JOUR)




#=====================================================
# 20. SALLE DE GYM
#=====================================================
class SalleGym(productbase.ProductBase):
	avenue =models.CharField("AVENUE", max_length=20, choices= AVENUE)
	commune =models.CharField("COMMUNE", max_length=20, choices= COMMUNE)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_PERSONNE_MOIS)


#=====================================================
# 21. NAVETTE AEROPORT
#=====================================================
class NavetteAeroport(productbase.ProductBase):
	nombre_personnes =models.CharField("NOMBRE PERSONNES", max_length=20, choices= NOMBRE_PERSONNES)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_PERSONNE)

#=====================================================
# 22. ACCUEIL AEROPORT
#=====================================================
class AccueilAeroport(productbase.ProductBase):
	nombre_personnes =models.CharField("NOMBRE PERSONNES", max_length=20, choices= NOMBRE_PERSONNES)
	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)



#=====================================================
# ESCORTE DE FONDS
#=====================================================
class EscorteFonds(productbase.ProductBase):

	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE)

#=====================================================
# PLACEMENT
#=====================================================
class Placement(productbase.ProductBase):

	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_POURC_SALAIRE)

#=====================================================
# RECRUTEMENT
#=====================================================
class Recrutement(productbase.ProductBase):

	prix = models.DecimalField("PRIX", max_digits=5, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_POURC_SALAIRE)



#=====================================================
# JARDINAGE
#=====================================================
class Jardinage(productbase.ProductBase):

	prix = models.DecimalField("PRIX", max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_M2)



#=====================================================
#   EVACUATION DES DECHETS
#=====================================================
class EvacuationDesDechets(productbase.ProductBase):
	frequence =models.CharField("FREQUENCE", max_length=100, choices= FREQUENCE_EVACUATION)
	prix = models.DecimalField("PRIX", max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_MOIS)


#=====================================================
#   FORMATION
#=====================================================
class Formation(productbase.ProductBase):

	prix = models.DecimalField("PRIX", max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_POURC_DEVIS)

#=====================================================
#   REPRODUCTION CLE
#=====================================================
class ReproductionCle(productbase.ProductBase):
	type_de_reproduction =models.CharField("TYPE DE REPRODUCTION", max_length=100, choices= TYPE_REPRODUCTION)
	prix = models.DecimalField("PRIX", max_digits=10, decimal_places=2)
	units = models.CharField("UNITÉS",max_length=50, choices=UNITE_USD_PIECE)

