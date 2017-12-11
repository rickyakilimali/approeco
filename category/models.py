from django.db import models
from treebeard.mp_tree import MP_Node
from django.template.defaultfilters import slugify
from django.contrib.contenttypes.models import ContentType
# Create your models here.


class Category(MP_Node):
	name = models.CharField("Nom de la catégorie", max_length=200)
	description = models.TextField("Description", blank=True)
	image = models.ImageField("Image", upload_to='categories/', blank=True,
null=True, max_length=255)
	slug = models.SlugField()

	node_order_by = ['name']

	_full_name_separator = ' > '

	class Meta:
		verbose_name = "Catégorie produit"

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)
		

	def __str__(self):
		return 'Category: %s' % self.name

   
	def get_ancestors_and_self(self):
		"""
		Gets ancestors and includes itself. Use treebeard's get_ancestors
		if you don't want to include the category itself. It's a separate
		function as it's commonly used in templates.
		"""
		return list(self.get_ancestors()) + [self]

	def get_descendants_and_self(self):
		"""
		Gets descendants and includes itself. Use treebeard's get_descendants
		if you don't want to include the category itself. It's a separate
		function as it's commonly used in templates.
		"""
		return list(self.get_descendants()) + [self]

	def has_children(self):
		return self.get_num_children() > 0

	def get_num_children(self):
		return self.get_children().count()

	def get_absolute_url(self):
		return "/category/%s/" % self.slug	


class ProductType(models.Model):
	""" 
	Représente un type de produit. Ex: voiture, ordinateur
	"""

	class Meta:
		verbose_name = "Type de produit"

	name = models.CharField("Nom du type de produit", max_length=255)
	description = models.TextField("Descriptif du type de produit", blank=True)
	product_model = models.ForeignKey('contenttypes.ContentType',on_delete=models.CASCADE,
    limit_choices_to={'app_label': 'product'},)
	category = models.ForeignKey(Category, verbose_name="Catégorie d'appartenance", related_name="producttypes")
	slug = models.SlugField()
	product_type_image = models.ImageField("Image", upload_to='producttypes/', blank=True,
null=True, max_length=255)
	



	class Meta:
		verbose_name = "Type de produit"

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(ProductType, self).save(*args, **kwargs)

	def __str__(self):
		return self.name 

	def get_absolute_url(self):
		return "/product/%s/" %self.product_model.model
		