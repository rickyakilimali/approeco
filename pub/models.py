from django.db import models

# Create your models here.
#=====================================================
# 1. Affichage publicité
#=====================================================
class Pub(models.Model):
	cat_image=models.CharField("CATEGORIE DE L'IMAGE", max_length=50)
	photo = models.ImageField(upload_to="photos/")
	nom_societe=models.CharField("NOM DE LA SOCIETE",max_length=50)
	date_debut =models.CharField("DATE DEBUT",max_length=50)
	date_fin =models.CharField("DATE FIN",max_length=50)

	def __str__(self):
		return self.cat_image