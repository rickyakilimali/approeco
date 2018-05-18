from django.db import models

# Create your models here.
#=====================================================
# 1. PAPETERIE
#=====================================================
class Papeterie(models.Model):
	nom_categorie=models.CharField("NOM DE LA CATEGORIE",max_length=50)
	image = models.ImageField(upload_to="")
	slug=models.CharField("SLUG",max_length=50)


