from product.models import *
from utils.product_attributes.ordinateurs import MARQUE_INFORMATIQUE, TYPE_DE_PROCESSEUR, CAPACITE_DISQUE_DUR, CAPAPCITE_MEMOIRE_RAM, SYSTEME_EXPLOITATION, TAILLE_ECRAN, TECHNOLOGIE_IMPRESSION, COULEUR, RECTOVERSO, MULTIFONCTION, FORMAT
from utils.unite_prix import UNITE

class Laptop(productbase.ProductBase):
	marque  = models.CharField(max_length=50, choices=MARQUE_INFORMATIQUE)
	type_processeur = models.CharField(max_length=50, choices=TYPE_DE_PROCESSEUR)
	disque_dur = models.CharField(max_length=50, choices=CAPACITE_DISQUE_DUR)
	memoire_ram = models.CharField(max_length=50, choices=CAPAPCITE_MEMOIRE_RAM)
	systeme_exploitation = models.CharField(max_length=50, choices=SYSTEME_EXPLOITATION)
	taille_ecran = models.CharField(max_length=50, choices=TAILLE_ECRAN)
	prix = models.DecimalField(max_digits=5, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)
	

	class Meta:
		ordering = ['prix']

	def __str__(self):
		return self.marque	


class Desktop(productbase.ProductBase):
	marque  = models.CharField(max_length=50, choices=MARQUE_INFORMATIQUE)
	type_processeur = models.CharField(max_length=50, choices=TYPE_DE_PROCESSEUR)
	capacite_disque_dur = models.CharField(max_length=50, choices=CAPACITE_DISQUE_DUR)
	capacite_ram = models.CharField(max_length=50, choices=CAPAPCITE_MEMOIRE_RAM)
	systeme_exploitation = models.CharField(max_length=50, choices=SYSTEME_EXPLOITATION)
	taille_ecran = models.CharField(max_length=50, choices=TAILLE_ECRAN)
	prix = models.DecimalField(max_digits=5, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)
	

class Imprimante(productbase.ProductBase):
	marque  = models.CharField(max_length=50, choices=MARQUE_INFORMATIQUE)
	technologie = models.CharField(max_length=50, choices=TECHNOLOGIE_IMPRESSION)
	couleur = models.CharField(max_length=50, choices=COULEUR)
	multifonction = models.CharField(max_length=50, choices=MULTIFONCTION)
	rectoverso=models.CharField(max_length=50, choices=RECTOVERSO)
	format_papier=models.CharField(max_length=50, choices=FORMAT)
	prix = models.DecimalField(max_digits=5, decimal_places=2)
	units = models.CharField(max_length=50, choices=UNITE)
	