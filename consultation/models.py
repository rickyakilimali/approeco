from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):

	nom = models.CharField(max_length=250)
	category = TreeForeignKey('Category',null=True,on_delete=models.CASCADE,blank=True)
	content = models.TextField('Content')
	slug = models.SlugField()
	item_image = models.ImageField("Image", upload_to='items/', blank=True,null=True, max_length=255)
	#vendeur = models.ManyToManyField('auth.User',through=u'ItemPrice', related_name='my_products')

	def __str__(self):
		return self.nom


class ItemPrice(models.Model):
	 product = models.ForeignKey(Item, on_delete=models.CASCADE)
	 vendeur = models.ForeignKey(User, on_delete=models.CASCADE)
	 price = models.DecimalField('Moins de 250 employés',max_digits=10,decimal_places=2)
	 price2 = models.DecimalField('Moins de 250 employés',max_digits=10,decimal_places=2)


class Category(MPTTModel):
	name = models.CharField(max_length=100, unique=True)
	parent = TreeForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE,db_index=True)
	slug = models.SlugField()
	category_image = models.ImageField("Image", upload_to='categories/', blank=True,null=True, max_length=255)

	class MPTTMeta:
		order_insertion_by = ['name']

	class Meta:
		unique_together = (('parent', 'slug',))
		verbose_name_plural = 'categories'

	def get_slug_list(self):
		try:
			ancestors = self.get_ancestors(include_self=True)
		except:
			ancestors = []
		else:
			ancestors = [ i.slug for i in ancestors]
			slugs = []
			for i in range(len(ancestors)):
				slugs.append('/'.join(ancestors[:i+1]))
			return slugs

	def __str__(self):
		return self.name


