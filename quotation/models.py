from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Quotation(models.Model):
	acheteur = models.ForeignKey('auth.User',on_delete=models.CASCADE,)
	criteria = models.CharField(max_length=1000)
	producttype = models.CharField(max_length=200)
	products = models.CharField(max_length=200)
	date_created = models.DateField(auto_now_add=True)
