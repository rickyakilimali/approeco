# tutorial/tables.py
import django_tables2 as tables
from django_tables2.utils import A
from .models import *

class ProductTable(tables.Table):
	vendeur = tables.LinkColumn('businessprofile-detail', args=[A('vendeur.pk')], attrs={'a': {'target': '_blank'}})


class LaptopTable(tables.Table):
	class Meta:
		model = Laptop
		exclude = exclude = ('id','category','polymorphic_ctype','is_active','productbase_ptr',)





class DesktopTable(tables.Table):
	class Meta:
		model = Desktop
		exclude = exclude = ('id','category','is_active','productbase_ptr',)

class ImprimanteTable(tables.Table):
	class Meta:
		model = Imprimante
		exclude = exclude = ('id','category','is_active','productbase_ptr',)

