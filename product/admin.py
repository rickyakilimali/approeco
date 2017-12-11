from django.contrib import admin
from product.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget

# Register your models here.

class LaptopResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Laptop	
		
@admin.register(Laptop)
class LaptopAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = LaptopResources	
	list_display = ('vendeur','nom', 'marque', 'type_processeur', 'disque_dur', 'memoire_ram', 'systeme_exploitation', 'taille_ecran', 'prix','units')	


#=======================================================
# 1. Siège et fauteuil de bureau
#=======================================================
class SiegeEtFauteuilDeBureauResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = SiegeEtFauteuilDeBureau

@admin.register(SiegeEtFauteuilDeBureau)
class SiegeEtFauteuilDeBureauAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = SiegeEtFauteuilDeBureauResources	
	list_display = ('vendeur','nom','type_siege','revetement_siege','prix','units')

#=======================================================
# 2. Armoire
#=======================================================
class ArmoireResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Armoire

@admin.register(Armoire)
class ArmoireAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ArmoireResources	
	list_display = ('vendeur','nom','type_armoire','type_porte','dimension_armoire','prix','units')



#=======================================================
# AUTOMOBILE
#=======================================================

#=======================================================
# 1. Pièce de rechange - Refroidissement
#=======================================================
class PieceDeRechangeRefroidissementResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = PieceDeRechangeRefroidissement

@admin.register(PieceDeRechangeRefroidissement)
class PieceDeRechangeRefroidissementAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = PieceDeRechangeRefroidissementResources	
	list_display = ('vendeur','nom','pieces_rechange_refroidissement','annee_debut_fabrication_vehicule','annee_fin_fabrication_vehicule','prix','units')

#=======================================================
# 2. Pièce de rechange - Direction suspension
#=======================================================
class PieceDeRechangeDirectionSuspensionResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = PieceDeRechangeDirectionSuspension

@admin.register(PieceDeRechangeDirectionSuspension)
class PieceDeRechangeDirectionSuspensionAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = PieceDeRechangeDirectionSuspensionResources	
	list_display = ('vendeur','nom','pieces_rechange_direction_suspension','annee_debut_fabrication_vehicule','annee_fin_fabrication_vehicule','prix','units')

#=======================================================
# 3. Pièce de rechange - Transmission
#=======================================================
class PieceDeRechangeTransmissionResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = PieceDeRechangeTransmission

@admin.register(PieceDeRechangeTransmission)
class PieceDeRechangeTransmissionAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = PieceDeRechangeTransmissionResources	
	list_display = ('vendeur','nom','pieces_rechange_transmission','annee_debut_fabrication_vehicule','annee_fin_fabrication_vehicule','prix','units')

#=======================================================
# 4. Pièce de rechange - Carrosserie
#=======================================================
class PieceDeRechangeCarrosserieResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = PieceDeRechangeCarrosserie

@admin.register(PieceDeRechangeCarrosserie)
class PieceDeRechangeCarrosserieAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = PieceDeRechangeCarrosserieResources	
	list_display = ('vendeur','nom','pieces_rechange_carrosserie','annee_debut_fabrication_vehicule','annee_fin_fabrication_vehicule','prix','units')

#=======================================================
# 5. Pièce de rechange - Electrique
#=======================================================
class PieceDeRechangeElectriqueResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = PieceDeRechangeElectrique

@admin.register(PieceDeRechangeElectrique)
class PieceDeRechangeElectriqueAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = PieceDeRechangeElectriqueResources	
	list_display = ('vendeur','nom','pieces_rechange_electrique','annee_debut_fabrication_vehicule','annee_fin_fabrication_vehicule','prix','units')

#=======================================================
# 6. Pièce de rechange - Embrayage
#=======================================================
class PieceDeRechangeEmbrayageResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = PieceDeRechangeEmbrayage

@admin.register(PieceDeRechangeEmbrayage)
class PieceDeRechangeEmbrayageAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = PieceDeRechangeEmbrayageResources	
	list_display = ('vendeur','nom','pieces_rechange_embrayage','annee_debut_fabrication_vehicule','annee_fin_fabrication_vehicule','prix','units')

#=======================================================
# 7. Pièce de rechange - Freinage
#=======================================================
class PieceDeRechangeFreinageResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = PieceDeRechangeFreinage

@admin.register(PieceDeRechangeFreinage)
class PieceDeRechangeFreinageAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = PieceDeRechangeFreinageResources	
	list_display = ('vendeur','nom','pieces_rechange_freinage','annee_debut_fabrication_vehicule','annee_fin_fabrication_vehicule','prix','units')

#=======================================================
# 8. Pièce révision moteur
#=======================================================
class PieceRevisionMoteurResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = PieceRevisionMoteur

@admin.register(PieceRevisionMoteur)
class PieceRevisionMoteurAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = PieceRevisionMoteurResources	
	list_display = ('vendeur','nom','pieces_revision_moteur','annee_debut_fabrication_vehicule','annee_fin_fabrication_vehicule','prix','units')

#=======================================================
# 9. Pièce rechange moteur
#=======================================================
class PieceRechangeMoteurResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = PieceRechangeMoteur

@admin.register(PieceRechangeMoteur)
class PieceRechangeMoteurAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = PieceRechangeMoteurResources	
	list_display = ('vendeur','nom','pieces_rechange_moteur','annee_debut_fabrication_vehicule','annee_fin_fabrication_vehicule','prix','units')



#=======================================================
# BUREAUTIQUE IMPRESSION
#=======================================================

#=======================================================
# 1. Carte Service
#=======================================================


class CarteServiceResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = CarteService



@admin.register(CarteService)
class CarteServiceAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = CarteServiceResources	
	list_display = ('vendeur','nom', 'face_impression', 'quantite', 'unite_vente', 'prix','units')

#=======================================================
# 2. Carte Visite
#=======================================================


class CarteVisiteResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = CarteVisite

@admin.register(CarteVisite)
class CarteVisiteAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = CarteVisiteResources	
	list_display = ('vendeur','nom','type_papier','face_impression','quantite','unite_vente','prix','units')

#=======================================================
# 3. Shopping bag
#=======================================================
class ShoppingBagResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = ShoppingBag

@admin.register(ShoppingBag)
class ShoppingBagAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ShoppingBagResources	
	list_display = ('vendeur','nom','quantite','unite_vente','prix','units')

#=======================================================
# 4. Stylo
#=======================================================
class StyloResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Stylo

@admin.register(Stylo)
class StyloAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = StyloResources	
	list_display = ('vendeur','nom','quantite','unite_vente','prix','units')

#=======================================================
# 5. T-shirt
#=======================================================
class TShirtResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = TShirt

@admin.register(TShirt)
class TShirtAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = TShirtResources	
	list_display = ('vendeur','nom','quantite','unite_vente','prix','units')

#=======================================================
# 6. Depliant
#=======================================================
class DepliantResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Depliant

@admin.register(Depliant)
class DepliantAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = DepliantResources	
	list_display = ('vendeur','nom','type_papier','face_impression','format_papier','quantite','unite_vente','prix','units')

#=======================================================
# 7. Pin's
#=======================================================
class PinsResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Pins

@admin.register(Pins)
class PinsAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = PinsResources	
	list_display = ('vendeur','nom','quantite','unite_vente','prix','units')

#=======================================================
# 8. Affiche
#=======================================================
class AfficheResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Affiche

@admin.register(Affiche)
class AfficheAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = AfficheResources	
	list_display = ('vendeur','nom','type_papier','face_impression','format_papier','quantite','unite_vente','prix','units')

#=======================================================
# 9. Farde
#=======================================================
class FardeResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Farde

@admin.register(Farde)
class FardeAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = FardeResources	
	list_display = ('vendeur','nom','type_papier','face_impression','format_papier','quantite','unite_vente','prix','units')

#=======================================================
# 10. Porte clef
#=======================================================
class PorteClefResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = PorteClef

@admin.register(PorteClef)
class PorteClefAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = PorteClefResources	
	list_display = ('vendeur','nom','quantite','unite_vente','prix','units')

#=======================================================
# 11. Lanière
#=======================================================
class LaniereResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Laniere

@admin.register(Laniere)
class LaniereAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = LaniereResources	
	list_display = ('vendeur','nom','quantite','unite_vente','prix','units')

#=======================================================
# 12. Lanière
#=======================================================
class CasquetteBlancheResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = CasquetteBlanche

@admin.register(CasquetteBlanche)
class CasquetteBlancheAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = CasquetteBlancheResources	
	list_display = ('vendeur','nom','quantite','unite_vente','prix','units')

#=======================================================
# 13. Flyers
#=======================================================
class FlyerResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Flyer

@admin.register(Flyer)
class FlyerAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = FlyerResources	
	list_display = ('vendeur','nom','type_papier','face_impression','format_papier','quantite','unite_vente','prix','units')

#=======================================================
# 14. Carnet
#=======================================================



class CarnetResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Carnet



@admin.register(Carnet)
class CarnetAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = CarnetResources	
	list_display = ('vendeur','nom','support_original','support_copie','support_souche','format_papier','quantite','unite_vente','prix','units')

#=======================================================
# 15. Cachet humide
#=======================================================

		
class CachetHumideResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = CachetHumide


@admin.register(CachetHumide)
class CachetHumideAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = CachetHumideResources	
	list_display = ('vendeur','nom','dimension','prix','units')

#=======================================================
# 16. Cachet numerique
#=======================================================
class CachetNumeriqueResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = CachetNumerique

@admin.register(CachetNumerique)
class CachetNumeriqueAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = CachetNumeriqueResources	
	list_display = ('vendeur','nom','dimension','prix','units')

#=======================================================
# 17. Cachet imprimé
#=======================================================


class CachetImprimeResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = CachetImprime


@admin.register(CachetImprime)
class CachetImprimeAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = CachetImprimeResources	
	list_display = ('vendeur','nom','type_cachet_imprime','prix','units')

#=======================================================
# 18. Cachet sec
#=======================================================


class CachetSecResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = CachetSec



@admin.register(CachetSec)
class CachetSecAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = CachetSecResources	
	list_display = ('vendeur','nom','type_cachet_sec','dimension','prix','units')

#=======================================================
# 18. Gravure
#=======================================================


class GravureResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Gravure



@admin.register(Gravure)
class GravureAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = GravureResources	
	list_display = ('vendeur','nom','support_gravure','prix','units')



#=======================================================
# EQUIPEMENT ET MATERIEL
#=======================================================

#=======================================================
# 1. Boite cuisinière
#=======================================================


class BoiteCuisiniereResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = BoiteCuisiniere



@admin.register(BoiteCuisiniere)
class BoiteCuisiniereAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = BoiteCuisiniereResources	
	list_display = ('vendeur','nom', 'dimension', 'prix','units')

#=======================================================
# 2. Clef à molette
#=======================================================


class ClefMoletteResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = ClefMolette



@admin.register(ClefMolette)
class ClefMoletteAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ClefMoletteResources	
	list_display = ('vendeur','nom','dimension_clef_molette','prix','units')

#=======================================================
# 3. Disjoncteur
#=======================================================


class DisjoncteurResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Disjoncteur


@admin.register(Disjoncteur)
class DisjoncteurAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = DisjoncteurResources	
	list_display = ('vendeur','nom','marque','intensite','nombre_phase','prix','units')

#=======================================================
# 4. Interrupteur differentiel
#=======================================================


class InterrupteurDifferentielResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = InterrupteurDifferentiel


@admin.register(InterrupteurDifferentiel)
class InterrupteurDifferentielAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = InterrupteurDifferentielResources	
	list_display = ('vendeur','nom','marque','intensite','nombre_phase','sensibilite','prix','units')

#=======================================================
# 5. Fusible
#=======================================================
class FusibleResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Fusible

@admin.register(Fusible)
class FusibleAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = FusibleResources	
	list_display = ('vendeur','nom','marque','intensite','prix','units')

#=======================================================
# 6. Equerre
#=======================================================
class EquerreResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Equerre

@admin.register(Equerre)
class EquerreAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = EquerreResources	
	list_display = ('vendeur','nom','dimension','prix','units')

#=======================================================
# 7. Seche main
#=======================================================


class SecheMainResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = SecheMain


@admin.register(SecheMain)
class SecheMainAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = SecheMainResources	
	list_display = ('vendeur','nom','matiere','prix','units')

#=======================================================
# 8. Monte charge
#=======================================================

class MonteChargeResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = MonteCharge

@admin.register(MonteCharge)
class MonteChargeAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = MonteChargeResources	
	list_display = ('vendeur','nom','poids','prix','units')

#=======================================================
# 9. Interrupeur électrique
#=======================================================

class InterrupteurElectriqueResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = InterrupteurElectrique

@admin.register(InterrupteurElectrique)
class InterrupteurElectriqueAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = InterrupteurElectriqueResources	
	list_display = ('vendeur','nom','marque','schema','prix','units')

#=======================================================
# 10. Disjoncteur moteur
#=======================================================
class DisjoncteurMoteurResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = DisjoncteurMoteur

@admin.register(DisjoncteurMoteur)
class DisjoncteurMoteurAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = DisjoncteurMoteurResources	
	list_display = ('vendeur','nom','marque','intensite','prix','units')

#=======================================================
# 11. Paumelle
#=======================================================
class PaumelleResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Paumelle

@admin.register(Paumelle)
class PaumelleAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = PaumelleResources	
	list_display = ('vendeur','nom','dimension','prix','units')

#=======================================================
# 12. Gant
#=======================================================


class GantResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Gant


@admin.register(Gant)
class GantAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = GantResources
	list_display = ('vendeur','nom','type_gant','prix','units')

#=======================================================
# 13. Cylindre
#=======================================================

class CylindreResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Cylindre


@admin.register(Cylindre)
class CylindreAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = CylindreResources
	list_display = ('vendeur','nom','type_cylindre','prix','units')

#=======================================================
# 14. Palan mécanique
#=======================================================
class PalanMecaniqueResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = PalanMecanique

@admin.register(PalanMecanique)
class PalanMecaniqueAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = PalanMecaniqueResources	
	list_display = ('vendeur','nom','poids','prix','units')

#=======================================================
# 15. Inverseur
#=======================================================

class InverseurResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Inverseur

@admin.register(Inverseur)
class InverseurAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = InverseurResources	
	list_display = ('vendeur','nom','intensite','nombre_prise','prix','units')


#=======================================================
# 16. Appareil de mesure
#=======================================================
class AppareilDeMesureResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = AppareilDeMesure

@admin.register(AppareilDeMesure)
class AppareilDeMesureAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = AppareilDeMesureResources	
	list_display = ('vendeur','nom','type_appareil_mesure','tension','prix','unite_prix')

#=======================================================
# 17. Prise électrique
#=======================================================
class PriseElectriqueResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = PriseElectrique

@admin.register(PriseElectrique)
class PriseElectriqueAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = PriseElectriqueResources	
	list_display = ('vendeur','nom','marque','type_prise','prix','units')

#=======================================================
# 18. Rallonge
#=======================================================
class RallongeResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Rallonge

@admin.register(Rallonge)
class RallongeAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = RallongeResources	
	list_display = ('vendeur','nom','longueur','nombre_prise','prix','units')

#=======================================================
# 19. Boite de dérivation
#=======================================================
class BoiteDerivationResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = BoiteDerivation

@admin.register(BoiteDerivation)
class BoiteDerivationAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = BoiteDerivationResources	
	list_display = ('vendeur','nom','marque','type_derivation','dimension','prix','units')

#=======================================================
# 20. Coffret électrique
#=======================================================
class CoffretElectriqueResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = CoffretElectrique

@admin.register(CoffretElectrique)
class CoffretElectriqueAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = CoffretElectriqueResources	
	list_display = ('vendeur','nom','marque','nombre_module','encastre_sailli','prix','units')

#=======================================================
# 21. Contacteur
#=======================================================
class ContacteurResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Contacteur

@admin.register(Contacteur)
class ContacteurAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ContacteurResources	
	list_display = ('vendeur','nom','marque','puissance','tension','intensite','nombre_pole','prix','units')

#=======================================================
# 22. Mèche à beton
#=======================================================
class MecheBetonResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = MecheBeton

@admin.register(MecheBeton)
class MecheBetonAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = MecheBetonResources	
	list_display = ('vendeur','nom','diametre','prix','units')

#=======================================================
# 23. Outils de jardinage
#=======================================================
class OutilsJardinageResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = OutilsJardinage

@admin.register(OutilsJardinage)
class OutilsJardinageAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = OutilsJardinageResources	
	list_display = ('vendeur','nom','type_outils','prix','units')

#=======================================================
# 24. Balance
#=======================================================
class BalanceResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Balance

@admin.register(Balance)
class BalanceAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = BalanceResources	
	list_display = ('vendeur','nom','type_balance','poids','prix','units')

#=======================================================
# 25. Tuyauterie
#=======================================================
class TuyauterieResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Tuyauterie

@admin.register(Tuyauterie)
class TuyauterieAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = TuyauterieResources	
	list_display = ('vendeur','nom','matiere_tuyauterie','localisation','diametre','prix','units')

#=======================================================
# 26. Accessoires hydrophore
#=======================================================
class AccessoiresHydrophoreResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = AccessoiresHydrophore

@admin.register(AccessoiresHydrophore)
class AccessoiresHydrophoreAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = AccessoiresHydrophoreResources	
	list_display = ('vendeur','nom','type_accessoires_hydrophore','prix','units')

#=======================================================
# 27. Flexible
#=======================================================
class FlexibleResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Flexible

@admin.register(Flexible)
class FlexibleAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = FlexibleResources	
	list_display = ('vendeur','nom','utilisation','prix','units')

#=======================================================
# 28. Siphon
#=======================================================
class SiphonResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Siphon

@admin.register(Siphon)
class SiphonAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = SiphonResources	
	list_display = ('vendeur','nom','sanitaire','prix','units')

#=======================================================
# 29. Réduction PVC
#=======================================================
class ReductionPvcResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = ReductionPvc

@admin.register(ReductionPvc)
class ReductionPvcAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ReductionPvcResources	
	list_display = ('vendeur','nom','reduction','prix','units')

#=======================================================
# 30. Ampoule  électrique
#=======================================================
class AmpouleElectriqueResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = AmpouleElectrique

@admin.register(AmpouleElectrique)
class AmpouleElectriqueAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = AmpouleElectriqueResources	
	list_display = ('vendeur','nom','type_ampoule','culot','puissance_ampoule','forme_ampoule','prix','units')

#=======================================================
# 31. Moto pompe
#=======================================================
class MotoPompeResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = MotoPompe

@admin.register(MotoPompe)
class MotoPompeAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = MotoPompeResources	
	list_display = ('vendeur','nom','moteur','section_moto_pompe','puissance_moto_pompe','prix','units')

#=======================================================
# 32. Chargeur Batterie
#=======================================================
class ChargeurBatterieResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = ChargeurBatterie

@admin.register(ChargeurBatterie)
class ChargeurBatterieAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ChargeurBatterieResources	
	list_display = ('vendeur','nom','marque_chargeur','capacite_chargeur','prix','units')

#=======================================================
# 33. Enseigne lumineuse
#=======================================================
class EnseigneLumineuseResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = EnseigneLumineuse

@admin.register(EnseigneLumineuse)
class EnseigneLumineuseAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = EnseigneLumineuseResources	
	list_display = ('vendeur','nom','format_enseigne','longueur','prix','units')

#=======================================================
# 34. Pompe hydrophore
#=======================================================
class PompeHydrophoreResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = PompeHydrophore

@admin.register(PompeHydrophore)
class PompeHydrophoreAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = PompeHydrophoreResources	
	list_display = ('vendeur','nom','marque_pompe','capacite_pompe','puissance_pompe','prix','units')

#=======================================================
# 35. Pompe de forage
#=======================================================
class PompeForageResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = PompeForage

@admin.register(PompeForage)
class PompeForageAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = PompeForageResources	
	list_display = ('vendeur','nom','marque_pompe','force_pompe','prix','units')

#=======================================================
# 36. Pompe à eau
#=======================================================
class PompeEauResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = PompeEau

@admin.register(PompeEau)
class PompeEauAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = PompeEauResources	
	list_display = ('vendeur','nom','marque_pompe','hauteur_pompe','puissance_pompe','debit_pompe','prix','units')

#=======================================================
# 37. Machine d'atelier non portatif
#=======================================================
class MachineAtelierNonPortatifResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = MachineAtelierNonPortatif

@admin.register(MachineAtelierNonPortatif)
class MachineAtelierNonPortatifAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = MachineAtelierNonPortatifResources	
	list_display = ('vendeur','nom','marque_marchine','type_machine_non_portatif','puissance_machine','prix','units')

#=======================================================
# 38. Machine d'atelier portatif
#=======================================================
class MachineAtelierPortatifResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = MachineAtelierPortatif

@admin.register(MachineAtelierPortatif)
class MachineAtelierPortatifAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = MachineAtelierPortatifResources	
	list_display = ('vendeur','nom','marque_marchine','type_machine_portatif','tension','prix','units')

#=======================================================
# 39. Groupe électrogène
#=======================================================
class GroupeElectrogeneResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = GroupeElectrogene

@admin.register(GroupeElectrogene)
class GroupeElectrogeneAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = GroupeElectrogeneResources	
	list_display = ('vendeur','nom','marque_marchine','moteur','silencieux','puissance_groupe','prix','units')

#=======================================================
# 40. Compresseur
#=======================================================
class CompresseurResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Compresseur

@admin.register(Compresseur)
class CompresseurAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = CompresseurResources	
	list_display = ('vendeur','nom','marque_marchine','capacite_compresseur','puissance_compresseur','pression','prix','units')

#=======================================================
# 41. Detecteur d'intrusion
#=======================================================
class DetecteurIntrusionResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = DetecteurIntrusion

@admin.register(DetecteurIntrusion)
class DetecteurIntrusionAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = DetecteurIntrusionResources	
	list_display = ('vendeur','nom','mode_detection','prix','units')

#=======================================================
# 42. Moteur électrique
#=======================================================
class MoteurElectriqueResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = MoteurElectrique

@admin.register(MoteurElectrique)
class MoteurElectriqueAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = MoteurElectriqueResources	
	list_display = ('vendeur','nom','marque_moteur','tension_moteur','puissance_moteur','nombre_pole','prix','units')

#=======================================================
# 43. Convertisseur
#=======================================================
class ConvertisseurResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Convertisseur

@admin.register(Convertisseur)
class ConvertisseurAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ConvertisseurResources	
	list_display = ('vendeur','nom','marque_convertisseur','puissance_convertisseur','tension_convertisseur','Chargeur_convertisseur','sinus_pur','prix','units')

#=======================================================
# 44. Controle d'accès et pointage
#=======================================================
class ControleAccesEtPointageResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = ControleAccesEtPointage

@admin.register(ControleAccesEtPointage)
class ControleAccesEtPointageAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ControleAccesEtPointageResources	
	list_display = ('vendeur','nom','marque_equipement','mode_fonctionnement','pointage_presence','prix','units')

#=======================================================
# 45. Enregistreur caméra de surveillance
#=======================================================
class EnregistreurCameraSurveillanceResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = EnregistreurCameraSurveillance

@admin.register(EnregistreurCameraSurveillance)
class EnregistreurCameraSurveillanceAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = EnregistreurCameraSurveillanceResources	
	list_display = ('vendeur','nom','nombre_canaux','prix','units')




#=======================================================
# PROFESSIONS LIBERALES
#=======================================================

#=======================================================
# 1. Conseil
#=======================================================
class ConseilResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Conseil

@admin.register(Conseil)
class ConseilAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ConseilResources	
	list_display = ('vendeur','nom','type_intervention','nombre_employes','prix','units')

#=======================================================
# 2. Rédaction des procédures
#=======================================================
class RedactionDesProceduresResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = RedactionDesProcedures

@admin.register(RedactionDesProcedures)
class RedactionDesProceduresAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = RedactionDesProceduresResources	
	list_display = ('vendeur','nom','type_intervention','nombre_employes','prix','units')

#=======================================================
# 3. Assistance fiscale 
#=======================================================
class AssistanceFiscaleResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = AssistanceFiscale

@admin.register(AssistanceFiscale)
class AssistanceFiscaleAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = AssistanceFiscaleResources	
	list_display = ('vendeur','nom','type_intervention','nombre_employes','prix','units')

#=======================================================
# 4. Audit et contrôle interne
#=======================================================
class AuditEtControleInterneResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = AuditEtControleInterne

@admin.register(AuditEtControleInterne)
class AuditEtControleInterneAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = AuditEtControleInterneResources	
	list_display = ('vendeur','nom','type_intervention','nombre_employes','prix','units')

#=======================================================
# 5. Assistance comptable
#=======================================================
class AssistanceComptableResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = AssistanceComptable

@admin.register(AssistanceComptable)
class AssistanceComptableAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = AssistanceComptableResources	
	list_display = ('vendeur','nom','type_intervention','nombre_employes','prix','units')

#=======================================================
# 6. Audit financier
#=======================================================
class AuditFinancierResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = AuditFinancier

@admin.register(AuditFinancier)
class AuditFinancierAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = AuditFinancierResources	
	list_display = ('vendeur','nom','type_intervention','nombre_employes','prix','units')



#=======================================================
# SERVICES ET DIVERS
#=======================================================

#=======================================================
# 1. Service traiteur
#=======================================================
class ServiceTraiteurResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = ServiceTraiteur

@admin.register(ServiceTraiteur)
class ServiceTraiteurAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ServiceTraiteurResources	
	list_display = ('vendeur','nom','type_service_traiteur','prix','units')

#=======================================================
# 2. Service nettoyage
#=======================================================
class ServiceNettoyageResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = ServiceNettoyage

@admin.register(ServiceNettoyage)
class ServiceNettoyageAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ServiceNettoyageResources	
	list_display = ('vendeur','nom','type_service_nettoyage','prix','units')

#=======================================================
# 3. Cours d'anglais
#=======================================================
class CoursAnglaisResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = CoursAnglais

@admin.register(CoursAnglais)
class CoursAnglaisAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = CoursAnglaisResources	
	list_display = ('vendeur','nom','niveau_cours','prix','units')

#=======================================================
# 4. Interpretariat
#=======================================================
class InterpretariatResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Interpretariat

@admin.register(Interpretariat)
class InterpretariatAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = InterpretariatResources	
	list_display = ('vendeur','nom','langue_interpretariat','prix','units')

#=======================================================
# 5. Service de traduction
#=======================================================
class ServiceDeTraductionResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))
	
	class Meta:
		model = ServiceDeTraduction

@admin.register(ServiceDeTraduction)
class ServiceDeTraductionAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ServiceDeTraductionResources	
	list_display = ('vendeur','nom','langue','type_document','prix','units')