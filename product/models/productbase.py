from django.db import models
from django.contrib.auth.models import User
from category.models import Category
from polymorphic.models import PolymorphicModel

class ProductBase(models.Model):
	
	vendeur = models.ForeignKey('auth.User',on_delete=models.CASCADE,)	
	category = models.ForeignKey('category.Category',on_delete=models.CASCADE,)
	nom = models.CharField(max_length=250)
	is_active = models.BooleanField()

	class Meta:
		abstract = True

	def __str__(self):
		return self.nom
	
	

