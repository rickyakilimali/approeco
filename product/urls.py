from django.conf.urls import url
from django.views.generic.base import TemplateView
from .views import MyProductView, EditProductView
from product import views


urlpatterns = [

			url(r'^my-product/$', MyProductView.as_view(), name='my-product'),
			url(r'^edit-product/$', EditProductView.as_view(), name='edit-product'),


			url(r'^search/informatique/laptop/$', views.FilteredLaptopListView.as_view()),
			url(r'^search/informatique/desktop/$', views.FilteredDesktopListView.as_view()),
			url(r'^search/informatique/imprimante/$', views.FilteredImprimanteListView.as_view()),
			url(r'^search/ameublement/siegeetfauteuildebureau/$', views.FilteredSiegeEtFauteuilDeBureauListView.as_view()),
			url(r'^search/ameublement/armoire/$', views.FilteredArmoireListView.as_view()),
			url(r'^search/autombile/piecederechangerefroidissement/$', views.FilteredPieceDeRechangeRefroidissementListView.as_view()),
			url(r'^search/autombile/piecederechangedirectionsuspension/$', views.FilteredPieceDeRechangeDirectionSuspensionListView.as_view()),
			url(r'^search/autombile/piecederechangetransmission/$', views.FilteredPieceDeRechangeTransmissionListView.as_view()),
			url(r'^search/autombile/piecederechangecarrosserie/$', views.FilteredPieceDeRechangeCarrosserieListView.as_view()),
			url(r'^search/autombile/piecederechangeelectrique/$', views.FilteredPieceDeRechangeElectriqueListView.as_view()),
			url(r'^search/autombile/piecederechangeembrayage/$', views.FilteredPieceDeRechangeEmbrayageListView.as_view()),
			url(r'^search/autombile/piecederechangefreinage/$', views.FilteredPieceDeRechangeFreinageListView.as_view()),
			url(r'^search/autombile/piecerevisionmoteur/$', views.FilteredPieceRevisionMoteurListView.as_view()),
			url(r'^search/autombile/piecerechangemoteur/$', views.FilteredPieceRechangeMoteurListView.as_view()),
			url(r'^search/bureautique-impression/carteservice/$', views.FilteredCarteServiceListView.as_view()),
			url(r'^search/bureautique-impression/cartevisite/$', views.FilteredCarteVisiteListView.as_view()),
			url(r'^search/bureautique-impression/shoppingbag/$', views.FilteredShoppingBagListView.as_view()),
			url(r'^search/bureautique-impression/stylo/$', views.FilteredStyloListView.as_view()),
			url(r'^search/bureautique-impression/tshirtblanc/$', views.FilteredTShirtBlancListView.as_view()),
			url(r'^search/bureautique-impression/tshirt/$', views.FilteredTShirtListView.as_view()),
			url(r'^search/bureautique-impression/depliant/$', views.FilteredDepliantListView.as_view()),
			url(r'^search/bureautique-impression/pins/$', views.FilteredPinsListView.as_view()),
			url(r'^search/bureautique-impression/affiche/$', views.FilteredAfficheListView.as_view()),
			url(r'^search/bureautique-impression/farde/$', views.FilteredFardeListView.as_view()),
			url(r'^search/bureautique-impression/porteclef/$', views.FilteredPorteClefListView.as_view()),
			url(r'^search/bureautique-impression/laniere/$', views.FilteredLaniereListView.as_view()),
			url(r'^search/bureautique-impression/casquetteblanche/$', views.FilteredCasquetteBlancheListView.as_view()),
			url(r'^search/bureautique-impression/flyer/$', views.FilteredFlyerListView.as_view()),
			url(r'^search/bureautique-impression/carnet/$', views.FilteredCarnetListView.as_view()),
			url(r'^search/bureautique-impression/cachethumide/$', views.FilteredCachetHumideListView.as_view()),
			url(r'^search/bureautique-impression/cachetnumerique/$', views.FilteredCachetNumeriqueListView.as_view()),
			url(r'^search/bureautique-impression/cachetimprime/$', views.FilteredCachetImprimeListView.as_view()),
			url(r'^search/bureautique-impression/cachetsec/$', views.FilteredCachetSecListView.as_view()),
			url(r'^search/bureautique-impression/gravure/$', views.FilteredGravureListView.as_view()),
			url(r'^search/equipement-materiel/boitecuisiniere/$', views.FilteredBoiteCuisiniereListView.as_view()),
			url(r'^search/equipement-materiel/clefmolette/$', views.FilteredClefMoletteListView.as_view()),
			url(r'^search/equipement-materiel/disjoncteur/$', views.FilteredDisjoncteurListView.as_view()),
			url(r'^search/equipement-materiel/interrupteurdifferentiel/$', views.FilteredInterrupteurDifferentielListView.as_view()),
			url(r'^search/equipement-materiel/fusible/$', views.FilteredFusibleListView.as_view()),
			url(r'^search/equipement-materiel/equerre/$', views.FilteredEquerreListView.as_view()),
			url(r'^search/equipement-materiel/sechemain/$', views.FilteredSecheMainListView.as_view()),
			url(r'^search/equipement-materiel/montecharge/$', views.FilteredMonteChargeListView.as_view()),
			url(r'^search/equipement-materiel/interrupteurelectrique/$', views.FilteredInterrupteurElectriqueListView.as_view()),
			#url(r'^search/equipement-materiel/disjoncteurmoteur/$', views.FilteredDisjoncteurMoteurListView.as_view()),
			url(r'^search/equipement-materiel/paumelle/$', views.FilteredPaumelleListView.as_view()),
			url(r'^search/equipement-materiel/gant/$', views.FilteredGantListView.as_view()),
			url(r'^search/equipement-materiel/cylindre/$', views.FilteredCylindreListView.as_view()),
			url(r'^search/equipement-materiel/palanmecanique/$', views.FilteredPalanMecaniqueListView.as_view()),
			url(r'^search/equipement-materiel/inverseur/$', views.FilteredInverseurListView.as_view()),
			url(r'^search/equipement-materiel/appareildemesure/$', views.FilteredAppareilDeMesureListView.as_view()),
			url(r'^search/equipement-materiel/priseelectrique/$', views.FilteredPriseElectriqueListView.as_view()),
			url(r'^search/equipement-materiel/rallonge/$', views.FilteredRallongeListView.as_view()),
			url(r'^search/equipement-materiel/boitederivation/$', views.FilteredBoiteDerivationListView.as_view()),
			url(r'^search/equipement-materiel/coffretelectrique/$', views.FilteredCoffretElectriqueListView.as_view()),
			url(r'^search/equipement-materiel/contacteur/$', views.FilteredContacteurListView.as_view()),
			url(r'^search/equipement-materiel/mechebeton/$', views.FilteredMecheBetonListView.as_view()),
			url(r'^search/equipement-materiel/outilsjardinage/$', views.FilteredOutilsJardinageListView.as_view()),
			url(r'^search/equipement-materiel/balance/$', views.FilteredBalanceListView.as_view()),
			url(r'^search/equipement-materiel/tuyauterie/$', views.FilteredTuyauterieListView.as_view()),
			url(r'^search/equipement-materiel/accessoireshydrophore/$', views.FilteredAccessoiresHydrophoreListView.as_view()),
			url(r'^search/equipement-materiel/flexible/$', views.FilteredFlexibleListView.as_view()),
			url(r'^search/equipement-materiel/siphon/$', views.FilteredSiphonListView.as_view()),
			url(r'^search/equipement-materiel/reductionpvc/$', views.FilteredReductionPvcListView.as_view()),
			url(r'^search/equipement-materiel/ampouleelectrique/$', views.FilteredAmpouleElectriqueListView.as_view()),
			url(r'^search/equipement-materiel/motopompe/$', views.FilteredMotoPompeListView.as_view()),
			url(r'^search/equipement-materiel/chargeurbatterie/$', views.FilteredChargeurBatterieListView.as_view()),
			url(r'^search/equipement-materiel/enseignelumineuse/$', views.FilteredEnseigneLumineuseListView.as_view()),
			url(r'^search/equipement-materiel/pompehydrophore/$', views.FilteredPompeHydrophoreListView.as_view()),
			url(r'^search/equipement-materiel/pompeforage/$', views.FilteredPompeForageListView.as_view()),
			url(r'^search/equipement-materiel/pompeeau/$', views.FilteredPompeEauListView.as_view()),
			url(r'^search/equipement-materiel/machineateliernonportatif/$', views.FilteredMachineAtelierNonPortatifListView.as_view()),
			url(r'^search/equipement-materiel/machineatelierportatif/$', views.FilteredMachineAtelierPortatifListView.as_view()),
			url(r'^search/equipement-materiel/groupeelectrogene/$', views.FilteredGroupeElectrogeneListView.as_view()),
			url(r'^search/equipement-materiel/compresseur/$', views.FilteredCompresseurListView.as_view()),
			url(r'^search/equipement-materiel/detecteurintrusion/$', views.FilteredDetecteurIntrusionListView.as_view()),
			url(r'^search/equipement-materiel/moteurelectrique/$', views.FilteredMoteurElectriqueListView.as_view()),
			url(r'^search/equipement-materiel/convertisseur/$', views.FilteredConvertisseurListView.as_view()),
			url(r'^search/equipement-materiel/controleaccesetpointage/$', views.FilteredControleAccesEtPointageListView.as_view()),
			url(r'^search/equipement-materiel/enregistreurcamerasurveillance/$', views.FilteredEnregistreurCameraSurveillanceListView.as_view()),
			url(r'^search/profession-liberale/conseil/$', views.FilteredConseilListView.as_view()),
			url(r'^search/profession-liberale/redactiondesprocedures/$', views.FilteredRedactionDesProceduresListView.as_view()),
			url(r'^search/profession-liberale/assistancefiscale/$', views.FilteredAssistanceFiscaleListView.as_view()),
			url(r'^search/profession-liberale/auditetcontroleinterne/$', views.FilteredAuditEtControleInterneListView.as_view()),
			url(r'^search/profession-liberale/assistancecomptable/$', views.FilteredAssistanceComptableListView.as_view()),
			url(r'^search/profession-liberale/auditfinancier/$', views.FilteredAuditFinancierListView.as_view()),
			url(r'^search/profession-liberale/servicetraiteur/$', views.FilteredServiceTraiteurListView.as_view()),
			url(r'^search/services-divers/servicenettoyage/$', views.FilteredServiceNettoyageListView.as_view()),
			url(r'^search/services-divers/coursanglais/$', views.FilteredCoursAnglaisListView.as_view()),
			url(r'^search/services-divers/interpretariat/$', views.FilteredInterpretariatListView.as_view()),
			url(r'^search/services-divers/servicedetraduction/$', views.FilteredServiceDeTraductionListView.as_view()),
	
]

