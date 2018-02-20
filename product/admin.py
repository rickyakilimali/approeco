from django.contrib import admin
from product.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget

# Register your models here.

#=======================================================
#  Informatique
#=======================================================

class LaptopResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Laptop

@admin.register(Laptop)
class LaptopAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = LaptopResources
	list_display = ('vendeur','nom', 'marque_laptop', 'type_processeur', 'capacite_disque_dur', 'memoire_ram', 'prix','units')


#=======================================================
#  Desktop
#=======================================================
class DesktopResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Desktop

@admin.register(Desktop)
class DesktopAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = DesktopResources
	list_display = ('vendeur','nom','marque_desktop','type_processeur','memoire_ram','capacite_disque_dur','prix','units')


#=======================================================
#  Serveur
#=======================================================
class ServeurResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Serveur

@admin.register(Serveur)
class ServeurAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ServeurResources
	list_display = ('vendeur','nom','marque','modele_serveur','type_serveur','type_processeur','capacite_ram_max','capacite_disque_dur','controleur_raid','prix','units')


#=======================================================
# Unite stockage
#=======================================================

class Unite_stockageResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Unite_stockage

@admin.register(Unite_stockage)
class Unite_StockageAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = Unite_stockageResources
	list_display = ('vendeur','nom','marque','type_stockage','capacite_memoire','prix','units')

#=======================================================
# Imprimante
#=======================================================

class ImprimanteResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Imprimante

@admin.register(Imprimante)
class ImprimanteAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ImprimanteResources
	list_display = ('vendeur','nom','marque_imprimante','technologie','modele','couleur','multifonction','format_max_papier','prix','units')


#=======================================================
# Imprimante
#=======================================================

class PhotocopieuseResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Photocopieuse

@admin.register(Photocopieuse)
class PhotocopieuseAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = PhotocopieuseResources
	list_display = ('vendeur','nom','marque_imprimante','technologie','recto_verso','reseau','format_max_papier','prix','units')

#=======================================================
# Cartouche tonet
#=======================================================

class CartoucheResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Cartouche

@admin.register(Cartouche)
class CartoucheAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = CartoucheResources
	list_display = ('vendeur','nom','marque_cartouche','numero_cartouche','couleur_cartouche','prix','units')


#=======================================================
# Switch
#=======================================================

class SwitchResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Switch

@admin.register(Switch)
class SwitchAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = SwitchResources
	list_display = ('vendeur','nom','marque','type_equipement','nombre_port','prix','units')



#=======================================================
# Videoprojecteur
#=======================================================

class VideoprojecteurResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Videoprojecteur

@admin.register(Videoprojecteur)
class UniteStockageAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = VideoprojecteurResources
	list_display = ('vendeur','nom','marque','puissance','prix','units')




#=======================================================
# Logiciekl
#=======================================================

class LogicielResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Logiciel

@admin.register(Logiciel)
class LogicielAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = LogicielResources
	list_display = ('vendeur','nom','marque','type_logiciel','licence','prix','units')


#=======================================================
# tABLETTE
#=======================================================

class TabletteResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Tablette

@admin.register(Tablette)
class TabletteAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = TabletteResources
	list_display = ('vendeur','nom','marque_tablette','modele_tablette','systeme_exploitation','memoire_tablette','prix','units')


#=======================================================
# Routeur
#=======================================================

class RouteurResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Routeur

@admin.register(Routeur)
class TabletteAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = RouteurResources
	list_display = ('vendeur','nom','marque','wifi','prix','units')


#=======================================================
# ModemWifi
#=======================================================

class ModemWifiResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = ModemWifi

@admin.register(ModemWifi)
class ModemWifiAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ModemWifiResources
	list_display = ('vendeur','nom','marque','prix','units')


#=======================================================
# CableInformatique
#=======================================================

class CableInformatiqueResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = CableInformatique

@admin.register(CableInformatique)
class CableInformatiqueAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = CableInformatiqueResources
	list_display = ('vendeur','nom','type_cable','longueur','prix','units')

#=======================================================
# CahierCharges
#=======================================================

class CahierChargesResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = CahierCharges

@admin.register(CahierCharges)
class CahierChargesAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = CahierChargesResources
	list_display = ('vendeur','nom','prix','units')


#=======================================================
# HEBERGEMENT WEB
#=======================================================

class HebergementSiteWebResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model =HebergementSiteWeb

@admin.register(HebergementSiteWeb)
class HebergementSiteWebAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = HebergementSiteWebResources
	list_display = ('vendeur','nom','prix','type_hebergement','units')

#=======================================================
# Helpdesk
#=======================================================

class HelpdeskResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model =Helpdesk

@admin.register(Helpdesk)
class HelpdeskAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = HelpdeskResources
	list_display = ('vendeur','nom','prix','units')

#=======================================================
# Installation Logiciel Serveur
#=======================================================

class InstallationLogicielServeurResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model =InstallationLogicielServeur

@admin.register(InstallationLogicielServeur)
class InstallationLogicielServeur(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = InstallationLogicielServeurResources
	list_display = ('vendeur','nom','prix','units')



#=======================================================
# Integration Customisation Standard
#=======================================================

class IntegrationCustomisationStandardResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model =IntegrationCustomisationStandard

@admin.register(IntegrationCustomisationStandard)
class IntegrationCustomisationStandard(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = IntegrationCustomisationStandardResources
	list_display = ('vendeur','nom','prix','units')

#=======================================================
# MaintenanceBackup
#=======================================================

class MaintenanceBackupResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model =MaintenanceBackup

@admin.register(MaintenanceBackup)
class MaintenanceBackup(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = MaintenanceBackupResources
	list_display = ('vendeur','nom','prix','units')

#=======================================================
# NumerisationDonnees
#=======================================================

class NumerisationDonneesResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model =NumerisationDonnees

@admin.register(NumerisationDonnees)
class NumerisationDonnees(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = NumerisationDonneesResources
	list_display = ('vendeur','nom','prix','units')

#=======================================================
# AdresseIpPublique
#=======================================================

class AdresseIpPubliqueResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model =AdresseIpPublique

@admin.register(AdresseIpPublique)
class AdresseIpPublique(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = AdresseIpPubliqueResources
	list_display = ('vendeur','nom','nombre_adresse_maximum','prix','units')


#=======================================================
# Clavier
#=======================================================

class ClavierResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model =Clavier

@admin.register(Clavier)
class Clavier(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ClavierResources
	list_display = ('vendeur','nom','type_clavier','prix','units')

#=======================================================
# Souris
#=======================================================

class SourisResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model =Souris

@admin.register(Souris)
class Souris(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = SourisResources
	list_display = ('vendeur','nom','avec_fil','prix','units')

#=====================================================
#  CreationSiteWebResources
#=====================================================
class CreationSiteWebResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = CreationSiteWeb

@admin.register(CreationSiteWeb)
class CreationSiteWebAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = CreationSiteWebResources
	list_display = ('vendeur','nom', 'type_site_web', 'prix','units')


#===========================================================================================================
#===========================================================================================================
#===========================================================================================================
# Categorie: Agribusiness
#===========================================================================================================
#===========================================================================================================
#===========================================================================================================


#===========================================================
#  Bouillie
#===========================================================


class BouillieResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Bouillie

@admin.register(Bouillie)
class BouillieAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = BouillieResources
	list_display = ('vendeur','nom','composition_bouillie','qualite_bouillie','prix','units')
#=====================================================
#  SEMENCE  ==> AGRIBUSINESS
#=====================================================
class SemenceResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Semence

@admin.register(Semence)
class SemenceAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = SemenceResources
	list_display = ('vendeur','nom', 'produit_agricole','variete','poids','prix','units')
#=====================================================
#  RIZ  ==> AGRIBUSINESS
#=====================================================
class RizResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Riz

@admin.register(Riz)
class RizAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = RizResources
	list_display = ('vendeur','nom', 'variete','type_riz','qualite','prix','units')

#=====================================================
#  BOUTURE MANIOC  ==> AGRIBUSINESS
#=====================================================
class BoutureManiocResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = BoutureManioc

@admin.register(BoutureManioc)
class BoutureManiocAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = BoutureManiocResources
	list_display = ('vendeur','nom', 'longueur','prix','units')
#=====================================================
#  HUILE  ==> AGRIBUSINESS
#=====================================================
class HuileResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Huile

@admin.register(Huile)
class HuileAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = HuileResources
	list_display = ('vendeur','nom', 'base','prix','units')
#=====================================================
#  FARINE  ==> AGRIBUSINESS
#=====================================================
class FarineResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Farine

@admin.register(Farine)
class FarineAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = FarineResources
	list_display = ('vendeur','nom','base','prix','units')
#=====================================================
#  TOURTEAU  ==> AGRIBUSINESS
#=====================================================
class TourteauResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Tourteau

@admin.register(Tourteau)
class TourteauAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = TourteauResources
	list_display = ('vendeur','nom','prix','units')



#=======================================================
# AMEUBLEMENT
#=======================================================
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
	list_display = ('vendeur','nom','type_armoire','hauteur','materiau_armoire','longueur','largeur','nombre_de_cases','prix','units')

#=======================================================
# 3. ETAGERE
#=======================================================
class EtagereResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Etagere

@admin.register(Etagere)
class EtagereAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = EtagereResources
	list_display = ('vendeur','nom','type_armoire','hauteur','materiau_armoire','longueur','largeur','prix','units')
#=======================================================
# 4. TABLE BUREAU
#=======================================================
class TableBureauResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = TableBureau

@admin.register(TableBureau)
class TableBureauAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = TableBureauResources
	list_display = ('vendeur','nom','forme','materiau_armoire','longueur','largeur','prix','units')

#=======================================================
# 4. TABLE BUREAU
#=======================================================
class TableReunionResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = TableReunion

@admin.register(TableReunion)
class TableReunionAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = TableReunionResources
	list_display = ('vendeur','nom','forme','longueur','prix','units')


#=======================================================
# 5. CHAISE DE SALLE D'ATTENTE
#=======================================================
class ChaiseSalleAttenteResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = ChaiseSalleAttente

@admin.register(ChaiseSalleAttente)
class ChaiseSalleAttenteAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ChaiseSalleAttenteResources
	list_display = ('vendeur','nom','nombre_de_places','prix','units')

#=======================================================
# 5. CHAISE DE BUREAU
#=======================================================
class ChaisebureauResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Chaisebureau

@admin.register(Chaisebureau)
class ChaisebureauAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ChaisebureauResources
	list_display = ('vendeur','nom','type_chaise','revetement','prix','units')
#=======================================================
# 4. BUREAU
#=======================================================
class BureauResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Bureau

@admin.register(Bureau)
class BureauAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = BureauResources
	list_display = ('vendeur','nom','materiau_bureau','type_bureau','model_bureau','longueur','prix','units')
#=====================================================
# 7. CONSULTANCE DECORATION
#=====================================================
class ConsultanceDecorationResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = ConsultanceDecoration

@admin.register(ConsultanceDecoration)
class ConsultanceDecorationAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ConsultanceDecorationResources
	list_display = ('vendeur','nom','prix','units')
#=====================================================
# 8. DECORATION AMENAGEMENT
#=====================================================
class DecorationAmenagementResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = DecorationAmenagement

@admin.register(DecorationAmenagement)
class DecorationAmenagementAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = DecorationAmenagementResources
	list_display = ('vendeur','nom','prix','units')
#=====================================================
# 8. DECORATION SURFACE
#=====================================================
class DecorationSurfaceResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = DecorationSurface

@admin.register(DecorationSurface)
class DecorationSurfaceAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = DecorationSurfaceResources
	list_display = ('vendeur','nom','prix','units')
#=====================================================
# 8. TABLEAU
#=====================================================
class TableauResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Tableau

@admin.register(Tableau)
class TableauAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = TableauResources
	list_display = ('vendeur','nom','dimension_tableau','prix','units')

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
# 10. LOCATION VEHICULE
#=======================================================
class LocationVehiculeResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = LocationVehicule

@admin.register(LocationVehicule)
class LocationVehiculeAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = LocationVehiculeResources
	list_display = ('vendeur','nom','type_vehicule','marque','modele','prix','units')

#=====================================================
#  VOITUREJEEPBUS
#=====================================================
class VoitureJeepBusResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = VoitureJeepBus

@admin.register(VoitureJeepBus)
class VoitureJeepBusAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = VoitureJeepBusResources
	list_display = ('vendeur','nom', 'type_vehicule','marque_voiture','modele_voiture','etat_voiture','prix','units')

#=====================================================
#  MOTODEUXROUES
#=====================================================
class MotoDeuxRouesResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = MotoDeuxRoues

@admin.register(MotoDeuxRoues)
class MotoDeuxRouesAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = MotoDeuxRouesResources
	list_display = ('vendeur','nom', 'marque_moto','modele_moto','type_usage','puissance_moteur','type_demarrage','etat_moto','prix','units')

#=====================================================
#  MOTODEUXROUES  ==>  AUTOMOBILE
#=====================================================
class MotoTroisRouesResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = MotoTroisRoues

@admin.register(MotoTroisRoues)
class MotoTroisRouesAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = MotoTroisRouesResources
	list_display = ('vendeur','nom', 'marque_moto','modele_moto','puissance_moteur','type_demarrage','etat_moto','prix','units')
#=====================================================
#  CAMION
#=====================================================
class CamionResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Camion

@admin.register(Camion)
class CamionAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = CamionResources
	list_display = ('vendeur','nom', 'marque','modele','type_camion','etat','prix','units')
#=====================================================
#  MOTEUR
#=====================================================
class MoteurResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Moteur

@admin.register(Moteur)
class MoteurAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = MoteurResources
	list_display = ('vendeur','nom', 'marque','modele','nombre_cylindres','etat','prix','units')


#=====================================================
#  BOUGIE
#=====================================================
class BougieResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Bougie

@admin.register(Bougie)
class BougieAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = BougieResources
	list_display = ('vendeur','nom', 'marque_bougie','ordinaire_platine','nombre_electrode','prix','units')


#=====================================================
#  COSSE BATTERIE
#=====================================================
class CosseBatterieResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = CosseBatterie

@admin.register(CosseBatterie)
class CosseBatterieAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = CosseBatterieResources
	list_display = ('vendeur','nom', 'prix','units')

#=====================================================
#  PNEU
#=====================================================
class PneuResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Pneu

@admin.register(Pneu)
class PneuAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = PneuResources
	list_display = ('vendeur','nom','marque_pneu','dimension_pneu', 'prix','units')

#=====================================================
#  BATTERIE
#=====================================================
class BatterieResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Batterie

@admin.register(Batterie)
class BatterieAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = BatterieResources
	list_display = ('vendeur','nom','marque_batterie','capacite_batterie','garantie_batterie','entretien_batterie','forme_batterie','format_batterie', 'prix','units')
#=====================================================
#  TRANSPORT
#=====================================================
#=====================================================
#  FRET ROUTIER
#=====================================================
class FretRoutierResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = FretRoutier

@admin.register(FretRoutier)
class FretRoutierAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = FretRoutierResources
	list_display = ('vendeur','nom', 'lieu_depart','lieu_destination','capacite_max','prix','units')
#=====================================================
#  TRANSPORT DES BIENS INTRA KINSHASA
#=====================================================
class TransportBienIntraKinshasaResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = TransportBienIntraKinshasa

@admin.register(TransportBienIntraKinshasa)
class TransportBienIntraKinshasaAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = TransportBienIntraKinshasaResources
	list_display = ('vendeur','nom', 'poids','assurance','duree_location','prix','units')

#=====================================================
#  LOCATION PORTE-CONTENEUR
#=====================================================
class LocationPorteConteneurResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = LocationPorteConteneur

@admin.register(LocationPorteConteneur)
class LocationPorteConteneurAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = LocationPorteConteneurResources
	list_display = ('vendeur','nom','prix','units')

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
	list_display = ('vendeur','nom', 'face_impression', 'quantite', 'prix','units')

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
	list_display = ('vendeur','nom','face_impression','quantite','prix','units')

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
	list_display = ('vendeur','nom','quantite','prix','units')

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
	list_display = ('vendeur','nom','type_stylo','quantite','prix','units')

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
	list_display = ('vendeur','nom','type_tshirt','quantite','prix','units')

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
	list_display = ('vendeur','nom','format_papier','quantite','prix','units')

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
	list_display = ('vendeur','nom','quantite','prix','units')

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
	list_display = ('vendeur','nom','format_papier','quantite','prix','units')

#=======================================================
# 9. Farde
#=======================================================

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
	list_display = ('vendeur','nom','quantite','prix','units')

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
	list_display = ('vendeur','nom','quantite','prix','units')

#=======================================================
# 12. Casquette
#=======================================================
class CasquetteResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Casquette

@admin.register(Casquette)
class CasquetteBlancheAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = CasquetteResources
	list_display = ('vendeur','nom','quantite','prix','units')

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
	list_display = ('vendeur','nom','face_impression','format_papier','quantite','prix','units')
#=====================================================
#  COUVERTURE PHOTO
#=====================================================

class CouverturePhotoResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = CouverturePhoto

@admin.register(CouverturePhoto)
class CouverturePhotoAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = CouverturePhotoResources
	list_display = ('vendeur','nom','prix','units')
#=====================================================
#  BroderieEcussons
#=====================================================

class BroderieEcussonsResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = BroderieEcussons

@admin.register(BroderieEcussons)
class BroderieEcussonsAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = BroderieEcussonsResources
	list_display = ('vendeur','nom','prix','units')
#=====================================================
#  IMPRESSION SUR TASSE
#=====================================================
class ImpressionTasseResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = ImpressionTasse

@admin.register(ImpressionTasse)
class ImpressionTasseAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class =ImpressionTasseResources
	list_display = ('vendeur','nom','prix','units')
#=======================================================
# 14. Carnet
#=======================================================





#=======================================================
# 15. Cachet humide
#=======================================================




#=======================================================
# 16. Cachet numerique
#=======================================================

#=======================================================
# 17. Cachet imprimé
#=======================================================




#=======================================================
# 18. Cachet
#=======================================================


class CachetResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Cachet



@admin.register(Cachet)
class CachetAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = CachetResources
	list_display = ('vendeur','nom','type_cachet','dimension_cachet','prix','units')

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
#  AutocollantVinyleAdhesif
#=======================================================
class AutocollantVinyleAdhesifResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = AutocollantVinyleAdhesif

@admin.register(AutocollantVinyleAdhesif)
class AutocollantVinyleAdhesifdAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = AutocollantVinyleAdhesifResources
	list_display = ('vendeur','nom','type_autocollant','prix','units')


#=======================================================
#  BackDrops
#=======================================================
class BackDropsResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = BackDrops

@admin.register(BackDrops)
class BackDropsAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = BackDropsResources
	list_display = ('vendeur','nom','dimension','prix','units')

#=======================================================
#  ImpressionBanderole
#=======================================================
class ImpressionBanderoleResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = ImpressionBanderole

@admin.register(ImpressionBanderole)
class ImpressionBanderoleAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ImpressionBanderoleResources
	list_display = ('vendeur','nom','type_support','prix','units')

#=======================================================
#  X stand
#=======================================================
class XStandResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = XStand

@admin.register(XStand)
class XStandAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = XStandResources
	list_display = ('vendeur','nom','type_support','dimensions','prix','units')

#=======================================================
#  Sachet
#=======================================================
class SachetResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Sachet

@admin.register(Sachet)
class SachetdAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = SachetResources
	list_display = ('vendeur','nom','quantite','prix','units')


#=======================================================
#  RollUp
#=======================================================
class RollUpResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = RollUp

@admin.register(RollUp)
class RollUpdAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = RollUpResources
	list_display = ('vendeur','nom','dimension','prix','units')


#=======================================================
#  RamePapier
#=======================================================
class RamePapierResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = RamePapier

@admin.register(RamePapier)
class RamePapierdAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = RamePapierResources
	list_display = ('vendeur','nom','format','prix','units')


#=======================================================
#  EvenementDeMasse
#=======================================================
class EvenementDeMasseResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = EvenementDeMasse

@admin.register(EvenementDeMasse)
class EvenementDeMassedAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = EvenementDeMasseResources
	list_display = ('vendeur','nom','type_evenement_de_masse','minimum_payable','prix','units')


#=======================================================
#  CommunicationGraphique
#=======================================================
class CommunicationGraphiqueResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = CommunicationGraphique

@admin.register(CommunicationGraphique)
class CommunicationGraphiqueAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = CommunicationGraphiqueResources
	list_display = ('vendeur','nom','type_conception_graphique','prix','units')


#=======================================================
#  ConceptionGraphique
#=======================================================
class ConceptionGraphiqueResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = ConceptionGraphique

@admin.register(ConceptionGraphique)
class ConceptionGraphiqueAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ConceptionGraphiqueResources
	list_display = ('vendeur','nom','type_conception_graphique','prix','units')


#=======================================================
#  CommunicationDeMasse
#=======================================================
class CommunicationDeMasseResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = CommunicationDeMasse

@admin.register(CommunicationDeMasse)
class CommunicationGraphiqueAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = CommunicationDeMasseResources
	list_display = ('vendeur','nom','type_communication_de_masse','prix','units')


#=======================================================
#  EcritureScenario
#=======================================================
class EcritureScenarioResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = EcritureScenario

@admin.register(EcritureScenario)
class EcritureScenarioAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = EcritureScenarioResources
	list_display = ('vendeur','nom','nombre_minute','prix','units')

#=======================================================
#  Postproduction
#=======================================================
class PostproductionResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Postproduction

@admin.register(Postproduction)
class PostproductionAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = PostproductionResources
	list_display = ('vendeur','nom','nombre_minute','prix','units')

#=======================================================
#  ProductionTournage
#=======================================================
class ProductionTournageResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = ProductionTournage

@admin.register(ProductionTournage)
class ProductionTournageAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ProductionTournageResources
	list_display = ('vendeur','nom','nombre_minute','prix','units')



#=======================================================
#  Fixeur
#=======================================================
class FixeurResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Fixeur

@admin.register(Fixeur)
class FixeurAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = FixeurResources
	list_display = ('vendeur','nom','prix','units')

#=====================================================
#  SPOT PUBLICITAIRE  ==> COMMUNICATION EDITION
#=====================================================

class DiffusionSpotPublicitaireResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = DiffusionSpotPublicitaire

@admin.register(DiffusionSpotPublicitaire)
class DiffusionSpotublicitaireAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = DiffusionSpotPublicitaireResources
	list_display = ('vendeur','nom', 'periode','prix','units')

#=====================================================
#  BANDE DEFILANTE  ==> COMMUNICATION EDITION
#=====================================================
class BandeDefilanteResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = BandeDefilante

@admin.register(BandeDefilante)
class BandeDefilanteAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = BandeDefilanteResources
	list_display = ('vendeur','nom', 'prix','units')
#=====================================================
#  COMMUNIQUÉ  ==> COMMUNICATION EDITION
#=====================================================
class CommuniqueResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Communique

@admin.register(Communique)
class CommuniqueAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = CommuniqueResources
	list_display = ('vendeur','nom', 'type_communique','prix','units')

#=====================================================
#  LOCATION STUDIO  ==> COMMUNICATION EDITION
#=====================================================

class LocationStudioResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = LocationStudio

@admin.register(LocationStudio)
class LocationStudioAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = LocationStudioResources
	list_display = ('vendeur','nom', 'duree_location','prix','units')
#=====================================================
#  AFFICHAGE LOGO SUR ECRAN  ==> COMMUNICATION EDITION
#=====================================================
class AffichageLogoSurEcranResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = AffichageLogoSurEcran

@admin.register(AffichageLogoSurEcran)
class AffichageLogoSurEcranAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = AffichageLogoSurEcranResources
	list_display = ('vendeur','nom', 'prix','units')
#=====================================================
#  REPORTAGE ET TELEPROMO  ==> COMMUNICATION EDITION
#=====================================================
class ReportageTelepromoResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = ReportageTelepromo

@admin.register(ReportageTelepromo)
class ReportageTelepromoAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ReportageTelepromoResources
	list_display = ('vendeur','nom','type_telepromo', 'prix','units')

#=====================================================
#  PAGE MAGAZINE  ==> COMMUNICATION EDITION
#=====================================================
class PageMagazineResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = PageMagazine

@admin.register(PageMagazine)
class PageMagazineAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = PageMagazineResources
	list_display = ('vendeur','nom','duree_magazine', 'prix','units')
#=====================================================
#  PUBLICITE SUR PLATEAU  ==> COMMUNICATION EDITION
#=====================================================
class PubliciteSurPlateauResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = PubliciteSurPlateau

@admin.register(PubliciteSurPlateau)
class PubliciteSurPlateauAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = PubliciteSurPlateauResources
	list_display = ('vendeur','nom','type_publicite', 'prix','units')
#=====================================================
#  PRESENCE PHYSIQUE SUR PLATEAU  ==> COMMUNICATION EDITION
#=====================================================
class PresencePhysiqueSurPlateauResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = PresencePhysiqueSurPlateau

@admin.register(PresencePhysiqueSurPlateau)
class PresencePhysiqueSurPlateauAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = PresencePhysiqueSurPlateauResources
	list_display = ('vendeur','nom','prix','units')
#=====================================================
#  RETRANSMISSION EN DIRECT  ==> COMMUNICATION EDITION
#=====================================================
class RetransmissionDirectResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = RetransmissionDirect

@admin.register(RetransmissionDirect)
class RetransmissionDirectAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = RetransmissionDirectResources
	list_display = ('vendeur','nom','duree_retransmission', 'prix','units')
#=====================================================
#  BRODERIE SUR TSHIRT  ==> COMMUNICATION EDITION
#=====================================================
class BroderieSurTshirtResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = BroderieSurTshirt

@admin.register(BroderieSurTshirt)
class BroderieSurTshirtAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = BroderieSurTshirtResources
	list_display = ('vendeur','nom', 'type_tshirt','support','quantite','prix','units')

#=======================================================
# EQUIPEMENT ET MATERIEL
#=======================================================


#=======================================================
#  Onduleur
#=======================================================
class OnduleurResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Onduleur

@admin.register(Onduleur)
class OnduleurAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = OnduleurResources
	list_display = ('vendeur','nom','marque','puissance','prix','units')



#=======================================================
#  Stabilisateur
#=======================================================
class StabilisateurResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Stabilisateur

@admin.register(Stabilisateur)
class OnduleurAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = StabilisateurResources
	list_display = ('vendeur','nom','marque','puissance','prix','units')




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
	list_display = ('vendeur','nom','dimension','prix','units')

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

#=====================================================
#  CONTACTEURS  ==> EQUIPEMENT MATERIEL
#=====================================================
class ContacteurResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Contacteur

@admin.register(Contacteur)
class ContacteurAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ContacteurResources
	list_display = ('vendeur','nom', 'marque','nombre_phase','intensite','tension','prix','units')


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
	list_display = ('vendeur','nom','prix','units')

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
class AmpouleResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Ampoule

@admin.register(Ampoule)
class AmpouleAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = AmpouleResources
	list_display = ('vendeur','nom','type_ampoule','puissance','prix','units')

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
	list_display = ('vendeur','nom','marque','moteur','section_moto_pompe','puissance_moto_pompe','hauteur_max','prix','units')

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
	list_display = ('vendeur','nom','prix','units')

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
	list_display = ('vendeur','nom','puissance_pompe','debit', 'hauteur_max','prix','units')

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
	list_display = ('vendeur','nom','prix','units')

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
	list_display = ('vendeur','nom','marque','silencieux','carburant','puissance_groupe','prix','units')

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
	list_display = ('vendeur','nom','marque_detecteur','type_detecteur','adressable','prix','units')

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
# 45. Fontaine d'eau
#=======================================================
class FontaineEauResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = FontaineEau

@admin.register(FontaineEau)
class FontaineEauAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = FontaineEauResources
	list_display = ('vendeur','nom','model','prix','units')

#=======================================================
# 45. SPLIT
#=======================================================
class SplitResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Split

@admin.register(Split)
class SplitAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = SplitResources
	list_display = ('vendeur','nom','marque','puissance','prix','units')
#=======================================================
# 45. CITERNE
#=======================================================
class CiterneResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Citerne

@admin.register(Citerne)
class CiterneAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = CiterneResources
	list_display = ('vendeur','nom','capacite','materiau','prix','units')

#=======================================================
# 45. EXTINCTEUR
#=======================================================
class ExtincteurResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Extincteur

@admin.register(Extincteur)
class ExtincteurAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ExtincteurResources
	list_display = ('vendeur','nom','agent','poids','prix','units')
#=======================================================
# 45. PANNEAU SIGNALISATION
#=======================================================
class PanneauSignalisationResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = PanneauSignalisation

@admin.register(PanneauSignalisation)
class PanneauSignalisationAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = PanneauSignalisationResources
	list_display = ('vendeur','nom','type_signalisation','prix','units')

#=====================================================
#  INTERRUPTEUR SECTIONNEUR  ==> EQUIPEMENT MATERIEL
#=====================================================
class InterrupteurSectionneurResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = InterrupteurSectionneur

@admin.register(InterrupteurSectionneur)
class InterrupteurSectionneurAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = InterrupteurSectionneurResources
	list_display = ('vendeur','nom','marque','nombre_phase','tension','intensite','prix','units')

#=====================================================
#  MINUTEUR POUR CONTACTEUR  ==> EQUIPEMENT MATERIEL
#=====================================================
class MinuteurContacteurResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = MinuteurContacteur

@admin.register(MinuteurContacteur)
class MinuteurContacteurAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = MinuteurContacteurResources
	list_display = ('vendeur','nom', 'type_temporisation','domaine_reglage','prix','units')

#=====================================================
#  DISJONCTEUR DIFFERENTIEL  ==> EQUIPEMENT MATERIEL
#=====================================================
class DisjoncteurDifferentielResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = DisjoncteurDifferentiel

@admin.register(DisjoncteurDifferentiel)
class DisjoncteurDifferentielAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = DisjoncteurDifferentielResources
	list_display = ('vendeur','nom','marque', 'nombre_phase','intensite','sensibilite','prix','units')
#=====================================================
#  BETONNIERE  ==> EQUIPEMENT MATERIEL
#=====================================================
class BetonniereResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Betonniere

@admin.register(Betonniere)
class BetonniereAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = BetonniereResources
	list_display = ('vendeur','nom', 'capacite_betonniere','type_betonniere','prix','units')

#=====================================================
#  COMPACTEUR  ==> EQUIPEMENT MATERIEL
#=====================================================
class CompacteurResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Compacteur

@admin.register(Compacteur)
class CompacteurAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = CompacteurResources
	list_display = ('vendeur','nom', 'type_compacteur','puissance_compacteur','carburant','prix','units')
#=====================================================
#  COMPRESSEUR AIR  ==> EQUIPEMENT MATERIEL
#=====================================================
class CompresseurAirResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = CompresseurAir

@admin.register(CompresseurAir)
class CompresseurAirAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = CompresseurAirResources
	list_display = ('vendeur','nom', 'capacite_compresseur','puissance_compresseur','debit','prix','units')
#=====================================================
#  PALAN  ==> EQUIPEMENT MATERIEL
#=====================================================
class PalanResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Palan

@admin.register(Palan)
class PalanAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = PalanResources
	list_display = ('vendeur','nom', 'puissance_palan','longueur','poids_max','type_palan','prix','units')



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
	list_display = ('vendeur','nom','secteur','type_intervention','nombre_employes','prix','units')

#=======================================================
# 2. Rédaction des procédures
#=======================================================
class RedactionProceduresResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = RedactionProcedures

@admin.register(RedactionProcedures)
class RedactionProceduresAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = RedactionProceduresResources
	list_display = ('vendeur','nom','secteur','type_intervention','nombre_employes','prix','units')

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
	list_display = ('vendeur','nom','secteur','type_intervention','nombre_employes','prix','units')

#=======================================================
# 4. Audit et contrôle interne
#=======================================================
class AuditControleInterneResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = AuditControleInterne

@admin.register(AuditControleInterne)
class AuditControleInterneAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = AuditControleInterneResources
	list_display = ('vendeur','nom','secteur','type_intervention','nombre_employes','prix','units')

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
	list_display = ('vendeur','nom','secteur','type_intervention','nombre_employes','prix','units')

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
	list_display = ('vendeur','nom','secteur','type_intervention','nombre_employes','prix','units')
#=====================================================
# 6. PUBLICATION
#=====================================================
class PublicationResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Publication

@admin.register(Publication)
class PublicationAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = PublicationResources
	list_display = ('vendeur','nom','titre','prix','units')


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
# 3. Cours LAngue
#=======================================================
class CoursLangueResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = CoursLangue

@admin.register(CoursLangue)
class CoursAnglaisAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = CoursLangueResources
	list_display = ('vendeur','nom','langue_cours','niveau_cours','prix','units')

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



#=======================================================
#  Bande Passante
#=======================================================
class BandePassanteResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = BandePassante

@admin.register(BandePassante)
class BandePassanteAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = BandePassanteResources
	list_display = ('vendeur','nom','type_bande_passante','debit_download','debit_upload','frais_installation','prix','units')


#=======================================================
#  Abonnement Journal
#=======================================================

class AbonnementJournalResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = AbonnementJournal

@admin.register(AbonnementJournal)
class AbonnementJournalAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = AbonnementJournalResources
	list_display = ('vendeur','nom','type_abonnement','periodicite_parution','duree_abonnement','prix','units')


#=======================================================
# InsertionPublicitaire
#=======================================================
class InsertionPublicitaireResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = InsertionPublicitaire

@admin.register(InsertionPublicitaire)
class InsertionPublicitaireAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = InsertionPublicitaireResources
	list_display = ('vendeur','nom','type_insertion','periodicite_parution','tirage','dimension','prix','units')


#=======================================================
# Buffet
#=======================================================
class BuffetResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Buffet

@admin.register(Buffet)
class BuffetAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = BuffetResources
	list_display = ('vendeur','nom','choix_entree','choix_plats','choix_legumes','choix_accompagnement','choix_dessert','sur_place','prix','units')


#=======================================================
# cocktails
#=======================================================
class cocktailsResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = cocktails

@admin.register(cocktails)
class cocktailsAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = cocktailsResources
	list_display = ('vendeur','nom','choix_amuse_gueule','choix_boisson_froide','choix_boisson_alcoolisee','sur_place','prix','units')


#=======================================================
# PauseCafe
#=======================================================
class PauseCafeResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = PauseCafe

@admin.register(PauseCafe)
class PauseCafeAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = PauseCafeResources
	list_display = ('vendeur','nom','choix_amuse_gueule','choix_boisson_froide','choix_boisson_chaude','choix_viennoiserie','sur_place','prix','units')


#=======================================================
# ServiceGardiennage
#=======================================================
class ServiceGardiennageResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = ServiceGardiennage

@admin.register(ServiceGardiennage)
class ServiceGardiennageAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ServiceGardiennageResources
	list_display = ('vendeur','nom','type_gardiennage','prix','units')


#=======================================================
# ServiceAccueil
#=======================================================
class ServiceAccueilResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = ServiceAccueil

@admin.register(ServiceAccueil)
class ServiceAccueilAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ServiceAccueilResources
	list_display = ('vendeur','nom','periode_service','prix','units')


#=======================================================
# EvacuationVidangePoubelles
#=======================================================
class EvacuationVidangePoubellesResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = EvacuationVidangePoubelles

@admin.register(EvacuationVidangePoubelles)
class EvacuationVidangePoubellesAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = EvacuationVidangePoubellesResources
	list_display = ('vendeur','nom','frequence','paiement','prix','units')



#=======================================================
# ProduitNettoyage
#=======================================================
class ProduitNettoyageResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = ProduitNettoyage

@admin.register(ProduitNettoyage)
class ProduitNettoyagePoubellesAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ProduitNettoyageResources
	list_display = ('vendeur','nom','type_produit','prix','units')



#=======================================================
# Assainissement
#=======================================================
class AssainissementResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Assainissement

@admin.register(Assainissement)
class AssainissementAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = AssainissementResources
	list_display = ('vendeur','nom','type_assainissement','prix','units')


#=======================================================
# ServiceSplit
#=======================================================
class ServiceSplitResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = ServiceSplit

@admin.register(ServiceSplit)
class ServiceSplitAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ServiceSplitResources
	list_display = ('vendeur','nom','type_service_split','prix','units')

#=======================================================
# AssuranceVoyage
#=======================================================
class AssuranceVoyageResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = AssuranceVoyage

@admin.register(AssuranceVoyage)
class AssuranceVoyageAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = AssuranceVoyageResources
	list_display = ('vendeur','nom','periode','tranche_age','prix','units')


#=======================================================
# ServiceAgenceVoyage
#=======================================================
class ServiceAgenceVoyageResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = ServiceAgenceVoyage

@admin.register(ServiceAgenceVoyage)
class serviceAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ServiceAgenceVoyageResources
	list_display = ('vendeur','nom','type_service','prix','units')


#=======================================================
# Chambre
#=======================================================
class ChambreResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Chambre

@admin.register(Chambre)
class serviceAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ChambreResources
	list_display = ('vendeur','nom','nombre_etoile','acces_wifi_gratuit','petit_dejeune_gratuit','type_lit','avenue','commune','prix','units')


#=======================================================
# SalleConference
#=======================================================
class SalleConferenceResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = SalleConference

@admin.register(SalleConference)
class SalleConferenceAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = SalleConferenceResources
	list_display = ('vendeur','nom','superficie','micro_gratuit','retro_projecteur','baffle_gratuit','avenue','commune','prix','units')

#=======================================================
# SalleGym
#=======================================================
class SalleGymResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = SalleGym

@admin.register(SalleGym)
class SalleGymAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = SalleGymResources
	list_display = ('vendeur','nom','avenue','commune','prix','units')


#=======================================================
# NavetteAeroport
#=======================================================
class NavetteAeroportResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = NavetteAeroport

@admin.register(NavetteAeroport)
class NavetteAeroportAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = NavetteAeroportResources
	list_display = ('vendeur','nom','nombre_personnes','prix','units')

#=======================================================
# AccueilAeroport
#=======================================================
class AccueilAeroportResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = AccueilAeroport

@admin.register(AccueilAeroport)
class AccueilAeroportAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = AccueilAeroportResources
	list_display = ('vendeur','nom','nombre_personnes','prix','units')

#=======================================================
# Placement
#=======================================================
class PlacementResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Placement

@admin.register(Placement)
class PlacementAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = PlacementResources
	list_display = ('vendeur','nom','prix','units')

#=======================================================
# ConceptionPageMagazine
#=======================================================
class ConceptionPageMagazineResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = ConceptionPageMagazine

@admin.register(ConceptionPageMagazine)
class ConceptionPageMagazineAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ConceptionPageMagazineResources
	list_display = ('vendeur','nom','prix','units')


#=======================================================
# Recrutement
#=======================================================
class RecrutementResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Recrutement

@admin.register(Recrutement)
class PlacementAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = RecrutementResources
	list_display = ('vendeur','nom','prix','units')

#=======================================================
# EscorteFonds
#=======================================================
class EscorteFondsResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = EscorteFonds

@admin.register(EscorteFonds)
class EscorteFondsAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = EscorteFondsResources
	list_display = ('vendeur','nom','prix','units')

#=======================================================
# demenagement
#=======================================================
class DemenagementResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Demenagement

@admin.register(Demenagement)
class DemenagementAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = DemenagementResources
	list_display = ('vendeur','nom','pays_source','ville_destination','prix','units')
#=======================================================
# DETECTEUR INCENDIE
#=======================================================
class DetecteurIncendieResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = DetecteurIncendie

@admin.register(DetecteurIncendie)
class DetecteurIncendieAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = DetecteurIncendieResources
	list_display = ('vendeur','nom','mode_detection','adressable','prix','units')





#=======================================================
# Telephonie Hitech
#=======================================================

#=======================================================
# Smartphones
#=======================================================

class SmartphoneResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Smartphone

@admin.register(Smartphone)
class SmartphoneAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = SmartphoneResources
	list_display = ('vendeur','nom','marque_smartphone','modele_smartphone','systeme_exploitation','prix','units')

#=======================================================
# Telephone mobile
#=======================================================

class TelephoneMobileSimpleResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = TelephoneMobileSimple

@admin.register(TelephoneMobileSimple)
class TelephoneMobileSimpleAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = TelephoneMobileSimpleResources
	list_display = ('vendeur','nom','marque_mobile','modele_mobile','prix','units')

#=======================================================
# BATIMENT ET CONSTRUCTION
#=======================================================
#=======================================================
# PEINTURE
#=======================================================
class PeintureResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Peinture

@admin.register(Peinture)
class PeintureAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = PeintureResources
	list_display = ('vendeur','nom', 'type_peinture', 'composition', 'teinte','prix','units')

#=======================================================
# PientureSpeciale
#=======================================================
class PeintureSpecialeResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = PeintureSpeciale

@admin.register(PeintureSpeciale)
class PeintureSpecialeAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = PeintureSpecialeResources
	list_display = ('vendeur','nom', 'type_produit', 'domaine_application', 'caracteristique','prix','units')

#=======================================================
# travauxPeinture
#=======================================================
class TravauxPeintureResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = TravauxPeinture

@admin.register(TravauxPeinture)
class TravauxPeintureAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = TravauxPeintureResources
	list_display = ('vendeur','nom','prix','units')

#=======================================================
#LocationDepot
#=======================================================

class LocationDepotResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = LocationDepot

@admin.register(LocationDepot)
class LocationDepotAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = LocationDepotResources
	list_display = ('vendeur','nom', 'plage_surface','avenue','commune','surface', 'prix','units')

#=====================================================
#  LOCATIONSTAND
#=====================================================
class LocationStandResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = LocationStand

@admin.register(LocationStand)
class LocationStandAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = LocationStandResources
	list_display = ('vendeur','nom', 'surface_stand','duree_maximum','prix','units')


#=====================================================
#  BRIQUE
#=====================================================
class BriqueResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Brique

@admin.register(Brique)
class BriqueAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = BriqueResources
	list_display = ('vendeur','nom', 'type_brique','largeur','prix','units')
#=====================================================
#  MOELLON  ==> BATIMENT CONSTRUCTION
#=====================================================
class MoellonResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Moellon

@admin.register(Moellon)
class MoellonAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = MoellonResources
	list_display = ('vendeur','nom', 'type_moellon','prix','units')

#=====================================================
#  MISSION DE CONTROLE CHANTIER  ==> BATIMENT CONSTRUCTION
#=====================================================
class MissionControleChantierResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = MissionControleChantier

@admin.register(MissionControleChantier)
class MissionControleChantierAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = MissionControleChantierResources
	list_display = ('vendeur','nom','prix','units')

#=====================================================
#  LOCATION CAMION  ==> BATIMENT CONSTRUCTION
#=====================================================
class LocationCamionResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = LocationCamion

@admin.register(LocationCamion)
class LocationCamionAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = LocationCamionResources
	list_display = ('vendeur','nom', 'tonnage','zone','prix','units')

#=====================================================
#  LOCATION REMORQUE MATADI-KIN  ==> BATIMENT CONSTRUCTION
#=====================================================
class LocationRemorqueMatadiResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = LocationRemorqueMatadi

@admin.register(LocationRemorqueMatadi)
class LocationRemorqueMatadiAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = LocationRemorqueMatadiResources
	list_display = ('vendeur','nom', 'nombre_pied','prix','units')
#=====================================================
#  ENERGIE
#=====================================================
#=====================================================
#  PANNEAU SOLAIRE
#=====================================================
class PanneauxSolaireResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = PanneauxSolaire

@admin.register(PanneauxSolaire)
class PanneauxSolaireAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = PanneauxSolaireResources
	list_display = ('vendeur','nom', 'marque','type_cellule','duree_vie','garantie','puissance','prix','units')

#=====================================================
#  CONVERTISSEUR
#=====================================================
class ConvertisseurResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Convertisseur

@admin.register(Convertisseur)
class ConvertisseurAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ConvertisseurResources
	list_display = ('vendeur','nom', 'marque_convertisseur','puissance_convertisseur','tension_convertisseur','chargeur','duree_vie','garantie','sinus_pur','prix','units')


#=====================================================
#  REGULATEUR
#=====================================================
class RegulateurResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Regulateur

@admin.register(Regulateur)
class RegulateurAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = RegulateurResources
	list_display = ('vendeur','nom', 'marque','type_regulation','intensite','prix','units')

#=====================================================
#  BATTERIE SOLAIRE
#=====================================================
class BatteriesolaireResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Batteriesolaire

@admin.register(Batteriesolaire)
class RegulateurAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = BatteriesolaireResources
	list_display = ('vendeur','nom', 'marque','tension','duree_vie','garantie','capacite','prix','units')
#=====================================================
# 6. INSTALLATION SOLAIRE
#=====================================================
class InstallationSolaireResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = InstallationSolaire

@admin.register(InstallationSolaire)
class InstallationSolaireAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = InstallationSolaireResources
	list_display = ('vendeur','nom', 'prix','units')
#=====================================================
# 6. REPARATION INSTALLATION SOLAIRE
#=====================================================
class ReparationInstallationSolaireResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = ReparationInstallationSolaire

@admin.register(ReparationInstallationSolaire)
class ReparationInstallationSolaireAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ReparationInstallationSolaireResources
	list_display = ('vendeur','nom', 'prix','units')



#=====================================================
#  REPARATION INSTALLATION SOLAIRE
#=====================================================
class OutillageManuelResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = OutillageManuel

@admin.register(OutillageManuel)
class OutillageManuelAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = OutillageManuelResources
	list_display = ('vendeur','nom','type_outillage', 'prix','units')


#=====================================================
#  POMPE IMMERGEE
#=====================================================
class PompeImmergeeResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = PompeImmergee

@admin.register(PompeImmergee)
class PompeImmergeeAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = PompeImmergeeResources
	list_display = ('vendeur','nom','hauteur_pompe','puissance_pompe','debit_pompe', 'prix','units')


#=====================================================
#  TRONCONNEUSE
#=====================================================
class TronconneuseResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Tronconneuse

@admin.register(Tronconneuse)
class TronconneuseAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = TronconneuseResources
	list_display = ('vendeur','nom','marque','modele_tronconneuse', 'prix','units')

#=====================================================
#  meuleuse
#=====================================================
class MeuleuseResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Meuleuse

@admin.register(Meuleuse)
class MeuleuseAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = MeuleuseResources
	list_display = ('vendeur','nom','puissance_meuleuse', 'diametre','prix','units')


#=====================================================
#  TONDEUSE
#=====================================================
class TondeuseResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Tondeuse

@admin.register(Tondeuse)
class TondeuseAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = TondeuseResources
	list_display = ('vendeur','nom','puissance_tondeuse','type_tondeuse','prix','units')


#=====================================================
#  AMPOULE SOLAIRE
#=====================================================
class AmpouleSolaireResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = AmpouleSolaire

@admin.register(AmpouleSolaire)
class AmpouleSolaireAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = AmpouleSolaireResources
	list_display = ('vendeur','nom','puissance','prix','units')



#=====================================================
#  CABLE MASSE
#=====================================================
class CableMasseResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = CableMasse

@admin.register(CableMasse)
class CableMasseAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = CableMasseResources
	list_display = ('vendeur','nom','section','prix','units')



#=====================================================
#  CABLE souple
#=====================================================
class CableSoupleResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = CableSouple

@admin.register(CableSouple)
class CableSoupleAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = CableSoupleResources
	list_display = ('vendeur','nom','type_cable','nombre_fil','section','prix','units')


#=====================================================
#  coffret divisionnaire
#=====================================================
class CoffretDivisionnaireResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = CoffretDivisionnaire

@admin.register(CoffretDivisionnaire)
class CoffretDivisionnaireAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = CoffretDivisionnaireResources
	list_display = ('vendeur','nom','nombre_circuit','marque','prix','units')




#=====================================================
#  coffret jeu barre
#=====================================================
class CoffretJeuBarreResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = CoffretJeuBarre

@admin.register(CoffretJeuBarre)
class CoffretJeuBarreAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = CoffretJeuBarreResources
	list_display = ('vendeur','nom','intensite','prix','units')


#=====================================================
#  disjoncteur compact
#=====================================================
class DisjoncteurCompactResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = DisjoncteurCompact

@admin.register(DisjoncteurCompact)
class DisjoncteurCompactAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = DisjoncteurCompactResources
	list_display = ('vendeur','nom','marque','intensite','prix','units')


#=====================================================
#  disjoncteur conatcteur
#=====================================================
class DisjoncteurContacteurResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = DisjoncteurContacteur

@admin.register(DisjoncteurContacteur)
class DisjoncteurContacteurAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = DisjoncteurContacteurResources
	list_display = ('vendeur','nom','marque','intensite','prix','units')


#=====================================================
#  fil plastqiru
#=====================================================
class FilPlastiqueResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = FilPlastique

@admin.register(FilPlastique)
class FilPlastiqueAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = FilPlastiqueResources
	list_display = ('vendeur','nom','nombre_fil','section','prix','units')


#=====================================================
#  INVERSEUR A COFFRET
#=====================================================
class InverseurCoffretResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = InverseurCoffret

@admin.register(InverseurCoffret)
class InverseurCoffretAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = InverseurCoffretResources
	list_display = ('vendeur','nom','marque','intensite','nombre_circuit','prix','units')



#=====================================================
#  plafonier a led
#=====================================================
class PlafonnierLedResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = PlafonnierLed

@admin.register(PlafonnierLed)
class PlafonnierLedAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = PlafonnierLedResources
	list_display = ('vendeur','nom','puissance','tension','prix','units')



#=====================================================
#  PROJECTEUR
#=====================================================
class ProjecteurResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Projecteur

@admin.register(Projecteur)
class ProjecteurAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ProjecteurResources
	list_display = ('vendeur','nom','puissance','prix','units')

#=====================================================
#  REGLETTE
#=====================================================
class regletteResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = reglette

@admin.register(reglette)
class regletteAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = regletteResources
	list_display = ('vendeur','nom','puissance','prix','units')



#=====================================================
#  ROULEAU_FLEXIBLE
#=====================================================
class RouleauFlexubleResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = RouleauFlexuble

@admin.register(RouleauFlexuble)
class RouleauFlexubleAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = RouleauFlexubleResources
	list_display = ('vendeur','nom','dimension','longueur','prix','units')


#=====================================================
#  TUBE
#=====================================================
class TubeResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Tube

@admin.register(Tube)
class TubeAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = TubeResources
	list_display = ('vendeur','nom','puissance','type_tube','prix','units')



#=====================================================
#  Sirene
#=====================================================
class SireneResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Sirene

@admin.register(Sirene)
class SireneAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = SireneResources
	list_display = ('vendeur','nom','marque','prix','units')


#=====================================================
#  Telephone de bureau
#=====================================================
class TelephoneBureauResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = TelephoneBureau

@admin.register(TelephoneBureau)
class TelephoneBureauAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = TelephoneBureauResources
	list_display = ('vendeur','nom','marque','interface','prix','units')


#=====================================================
#  IMPRIMANTE A BADGE
#=====================================================
class ImprimanteABadgeResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = ImprimanteABadge

@admin.register(ImprimanteABadge)
class ImprimanteABadgeAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ImprimanteABadgeResources
	list_display = ('vendeur','nom','marque_imprimante_badge','technologe_impression_badge','faces_imprimes','vitesse_impression','option_encodage','prix','units')



#=====================================================
#  REPARATION SPLIT
#=====================================================
class ReparationSplitResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = ReparationSplit

@admin.register(ReparationSplit)
class ReparationSplitAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ReparationSplitResources
	list_display = ('vendeur','nom','prix','units')


#=====================================================
#  INSTALLATION ELECTRIQUE
#=====================================================
class InstallationElectriqueResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = InstallationElectrique

@admin.register(InstallationElectrique)
class InstallationElectriqueAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = InstallationElectriqueResources
	list_display = ('vendeur','nom','prix','units')


#=====================================================
#  REBOISEMENT
#=====================================================
class ReboisementResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Reboisement

@admin.register(Reboisement)
class ReboisementAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ReboisementResources
	list_display = ('vendeur','nom','prix','units')


#=====================================================
#  PRODUIT DE NETTOYAGE
#=====================================================
class ProduitDeNettoyageResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = ProduitDeNettoyage

@admin.register(ProduitDeNettoyage)
class ProduitDeNettoyageAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ProduitDeNettoyageResources
	list_display = ('vendeur','nom','type_produit','prix','units')


#=====================================================
#  PRODUIT DE DERATISATION
#=====================================================
class ProduitDeDeratisationResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = ProduitDeDeratisation

@admin.register(ProduitDeDeratisation)
class ProduitDeDeratisationAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ProduitDeDeratisationResources
	list_display = ('vendeur','nom','type_produit','prix','units')


#=====================================================
#  JARDINAGE
#=====================================================
class JardinageResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Jardinage

@admin.register(Jardinage)
class JardinageAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = JardinageResources
	list_display = ('vendeur','nom','prix','units')


#=====================================================
#  EVACUATION DES DECHETS
#=====================================================
class EvacuationDesDechetsResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = EvacuationDesDechets

@admin.register(EvacuationDesDechets)
class EvacuationDesDechetsAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = EvacuationDesDechetsResources
	list_display = ('vendeur','nom','frequence','prix','units')




#=====================================================
#  AGRAFES
#=====================================================

class AgrafeResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Agrafe

@admin.register(Agrafe)
class AgrafeAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = AgrafeResources
	list_display = ('vendeur','nom', 'dimension_agrafe','quantite','prix','units')


#=====================================================
#  AGRAFEUSE
#=====================================================

class AgrafeuseResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Agrafeuse

@admin.register(Agrafeuse)
class AgrafeuseAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = AgrafeuseResources
	list_display = ('vendeur','nom', 'dimension_agrafeuse','prix','units')


#=====================================================
#  ALBUM CARTE DE VISITE
#=====================================================

class AlbumCarteDeVisiteResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = AlbumCarteDeVisite

@admin.register(AlbumCarteDeVisite)
class AlbumCarteDeVisiteAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = AlbumCarteDeVisiteResources
	list_display = ('vendeur','nom', 'prix','units')


#=====================================================
#  ANNEAU PLASTIQUE
#=====================================================

class AnneauPlastiqueResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = AnneauPlastique

@admin.register(AnneauPlastique)
class AnneauPlastiqueAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = AnneauPlastiqueResources
	list_display = ('vendeur','nom', 'taille_anneau','quantite','prix','units')


#=====================================================
#  ATTACHE
#=====================================================

class AttacheResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Attache

@admin.register(Attache)
class AttacheAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = AttacheResources
	list_display = ('vendeur','nom', 'taille_attache','contenant','nombre_boite','quantite_par_boite','prix','units')



#=====================================================
#  BAGUETTE
#=====================================================

class BaguetteResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Baguette

@admin.register(Baguette)
class BaguetteAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = BaguetteResources
	list_display = ('vendeur','nom', 'taille_baguette','contenant','quantite_par_paquet','prix','units')


#=====================================================
#  BAS A COURRIER
#=====================================================

class BacACourrierResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = BacACourrier

@admin.register(BacACourrier)
class BacACourrierAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = BacACourrierResources
	list_display = ('vendeur','nom', 'matiere','nombre_bac','prix','units')





#=====================================================
#  BANDE ADHESIVE
#=====================================================

class BandeAdhesiveResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = BandeAdhesive

@admin.register(BandeAdhesive)
class BandeAdhesiveAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = BandeAdhesiveResources
	list_display = ('vendeur','nom', 'prix','units')

#=====================================================
#  BATON DE COLLE
#=====================================================

class BatonDeColleResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = BatonDeColle

@admin.register(BatonDeColle)
class BatonDeColleAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = BatonDeColleResources
	list_display = ('vendeur','nom','marque','poids','prix','units')



#=====================================================
#  BLOC NOTE LIGNE
#=====================================================

class BlocNoteLigneResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = BlocNoteLigne

@admin.register(BlocNoteLigne)
class BlocNoteLigneAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = BlocNoteLigneResources
	list_display = ('vendeur','nom','format_papeterie','prix','units')


#=====================================================
#  BLOC NOTE MEMO
#=====================================================

class BlocNoteMemoResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = BlocNoteMemo

@admin.register(BlocNoteMemo)
class BlocNoteMemoAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = BlocNoteMemoResources
	list_display = ('vendeur','nom','prix','units')

#=====================================================
#  BOITE D ARCHIVE
#=====================================================

class BoiteDArchiveResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = BoiteDArchive

@admin.register(BoiteDArchive)
class BoiteDArchiveAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = BoiteDArchiveResources
	list_display = ('vendeur','nom','type_boite','dimension_boite','prix','units')

#=====================================================
#  CACHET DATEUR
#=====================================================

class CachetDateurResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = CachetDateur

@admin.register(CachetDateur)
class CachetDateurAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = CachetDateurResources
	list_display = ('vendeur','nom','type_cachet_dateur','prix','units')

#=====================================================
#  CAHIER
#=====================================================

class CahierResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Cahier

@admin.register(Cahier)
class CahierAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = CahierResources
	list_display = ('vendeur','nom','format','type_cahier','prix','units')

#=====================================================
#  CAlculatrice
#=====================================================

class CalculatriceResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Calculatrice

@admin.register(Calculatrice)
class CalculatriceAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = CalculatriceResources
	list_display = ('vendeur','nom','type_calculatrice','prix','units')

#=====================================================
#  CARBONNE
#=====================================================

class CarbonneResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Carbonne

@admin.register(Carbonne)
class CarbonneAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = CarbonneResources
	list_display = ('vendeur','nom','type_carbonne','contenant','quantite_par_paquet','prix','units')

#=====================================================
#  CARNET DE RECU
#=====================================================

class CarnetDeRecuResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = CarnetDeRecu

@admin.register(CarnetDeRecu)
class CarnetDeRecuAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = CarnetDeRecuResources
	list_display = ('vendeur','nom','prix','units')


#=====================================================
#  ROSE A RELIURE
#=====================================================

class RoseAReliureResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = RoseAReliure

@admin.register(RoseAReliure)
class RoseAReliureAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = RoseAReliureResources
	list_display = ('vendeur','nom','format_papeterie','contenant','quantite_par_paquet','prix','units')


#=====================================================
# CISEAU
#=====================================================

class CiseauResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Ciseau

@admin.register(Ciseau)
class CiseauAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = CiseauResources
	list_display = ('vendeur','nom','taille','prix','units')

#=====================================================
# CLASSEUR
#=====================================================

class ClasseurResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Classeur

@admin.register(Classeur)
class ClasseurAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ClasseurResources
	list_display = ('vendeur','nom','format_classeur','prix','units')


#=====================================================
# COLLE LIQUIDE
#=====================================================

class ColleLiquideResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = ColleLiquide

@admin.register(ColleLiquide)
class ColleLiquideAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ColleLiquideResources
	list_display = ('vendeur','nom','quantite_colle','prix','units')

#=====================================================
# CORRECTEUR LIQUIDE
#=====================================================

class CorrecteurLiquideResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = CorrecteurLiquide

@admin.register(CorrecteurLiquide)
class CorrecteurLiquideAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = CorrecteurLiquideResources
	list_display = ('vendeur','nom','prix','units')

#=====================================================
# DESAGRAFEUSE
#=====================================================

class DesagrafeuseResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Desagrafeuse

@admin.register(Desagrafeuse)
class DesagrafeuseAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = DesagrafeuseResources
	list_display = ('vendeur','nom','prix','units')


#=====================================================
# DESAGRAFEUSE
#=====================================================

class EtiquetteDymoResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = EtiquetteDymo

@admin.register(EtiquetteDymo)
class EtiquetteDymoAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = EtiquetteDymoResources
	list_display = ('vendeur','nom','prix','units')


#=====================================================
# ECRITOIRE
#=====================================================

class EcritoireResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Ecritoire

@admin.register(Ecritoire)
class EcritoireAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = EcritoireResources
	list_display = ('vendeur','nom','matiere_ecritoire','prix','units')


#=====================================================
# ELASTIQUES
#=====================================================

class ElastiquesResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Elastiques

@admin.register(Elastiques)
class ElastiquesAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ElastiquesResources
	list_display = ('vendeur','nom','contenant','quantite','prix','units')


#=====================================================
# ENVELOPPES
#=====================================================

class EnveloppeResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Enveloppe

@admin.register(Enveloppe)
class EnveloppeAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = EnveloppeResources
	list_display = ('vendeur','nom','format_enveloppe','contenant','quantite_par_paquet','prix','units')


#=====================================================
# ETUI
#=====================================================

class EtuiResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Etui

@admin.register(Etui)
class EtuiAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = EtuiResources
	list_display = ('vendeur','nom','format_etui','contenant','quantite_par_paquet','prix','units')

#=====================================================
# FARDE
#=====================================================

class FardeResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Farde

@admin.register(Farde)
class FardeAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = FardeResources
	list_display = ('vendeur','nom','type_farde','prix','units')


#=====================================================
# GOMME
#=====================================================

class GommeResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Gomme

@admin.register(Gomme)
class GommeAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = GommeResources
	list_display = ('vendeur','nom','prix','units')


#=====================================================
# INTERCALAIRE
#=====================================================

class IntercalaireResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Intercalaire

@admin.register(Intercalaire)
class IntercalaireAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = IntercalaireResources
	list_display = ('vendeur','nom','contenant','quantite_par_jeu','prix','units')


#=====================================================
# LATTE
#=====================================================

class LatteResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Latte

@admin.register(Latte)
class LatteAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = LatteResources
	list_display = ('vendeur','nom','longueur','prix','units')

#=====================================================
# MARQUEUR
#=====================================================

class MarqueurResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Marqueur

@admin.register(Marqueur)
class MarqueurAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = MarqueurResources
	list_display = ('vendeur','nom','marque','contenant','quantite_par_paquet','prix','units')

#=====================================================
# PAPIER
#=====================================================

class PapierResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Papier

@admin.register(Papier)
class PapierAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = PapierResources
	list_display = ('vendeur','nom','type_papier','format_papier','contenant','quantite_par_contenant','prix','units')

#=====================================================
# PERFORATEUR
#=====================================================

class PerforateurResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Perforateur

@admin.register(Perforateur)
class PerforateurAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = PerforateurResources
	list_display = ('vendeur','nom','format_perforateur','prix','units')


#=====================================================
# PILE
#=====================================================

class PileResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Pile

@admin.register(Pile)
class PileAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = PileResources
	list_display = ('vendeur','nom','format_pile','contenant','quantite_par_paquet','prix','units')


#=====================================================
# PORTE CLE
#=====================================================

class PorteCleResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = PorteCle

@admin.register(PorteCle)
class PorteCleAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = PorteCleResources
	list_display = ('vendeur','nom','prix','units')


#=====================================================
# POST IT
#=====================================================

class PostItResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = PostIt

@admin.register(PostIt)
class PostItAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = PostItResources
	list_display = ('vendeur','nom','type_postit','contenant','dimension_postit','prix','units')


#=====================================================
# POUBELLE
#=====================================================

class PoubelleResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Poubelle

@admin.register(Poubelle)
class PoubelleAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = PoubelleResources
	list_display = ('vendeur','nom','matiere','prix','units')


#=====================================================
# PUNAISE
#=====================================================

class PunaiseResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Punaise

@admin.register(Punaise)
class PunaiseAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = PunaiseResources
	list_display = ('vendeur','nom','contenant','quantite_par_boite','prix','units')




#=====================================================
# REGISTRE-INDICATEUR-DE-COURRIER
#=====================================================

class RegistreIndicateurDeCourrierResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = RegistreIndicateurDeCourrier

@admin.register(RegistreIndicateurDeCourrier)
class RegistreIndicateurDeCourrierAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = RegistreIndicateurDeCourrierResources
	list_display = ('vendeur','nom','nombre_feuilles','prix','units')

#=====================================================
# SCOTCH
#=====================================================

class ScotchResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Scotch

@admin.register(Scotch)
class ScotchAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = ScotchResources
	list_display = ('vendeur','nom','longueur','prix','units')


#=====================================================
# SIGNATAIRE
#=====================================================

class SignataireResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Signataire

@admin.register(Signataire)
class SignataireAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = SignataireResources
	list_display = ('vendeur','nom','nombre_compartiments','prix','units')


#=====================================================
# SOULIGNEUR
#=====================================================

class SouligneurResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Souligneur

@admin.register(Souligneur)
class SouligneurAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = SouligneurResources
	list_display = ('vendeur','nom','marque','prix','units')


#=====================================================
# STYLO FEUTRE
#=====================================================

class StyloFeutreResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = StyloFeutre

@admin.register(StyloFeutre)
class StyloFeutreAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = StyloFeutreResources
	list_display = ('vendeur','nom','prix','units')

#=====================================================
# STYLO
#=====================================================

class StyloPapeterieResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = StyloPapeterie

@admin.register(StyloPapeterie)
class StyloPapeterieAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = StyloPapeterieResources
	list_display = ('vendeur','nom','marque','contenant','quantite_par_paquet','prix','units')


#=====================================================
# TRANSPARENT A RELIURE
#=====================================================

class TransparentAReliureResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = TransparentAReliure

@admin.register(TransparentAReliure)
class TransparentAReliureAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = TransparentAReliureResources
	list_display = ('vendeur','nom','format_transparent','contenant','quantite_par_paquet','prix','units')


#=====================================================
# FORMATION
#=====================================================

class FormationResources(resources.ModelResource):
	vendeur = fields.Field(column_name='vendeur', attribute='vendeur', widget=ForeignKeyWidget(User, 'username'))
	category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))

	class Meta:
		model = Formation

@admin.register(Formation)
class FormationAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
	resource_class = FormationResources
	list_display = ('vendeur','nom','prix','units')
