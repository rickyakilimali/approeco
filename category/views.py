from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic.list import ListView

# Create your views here.

def index(request):
	"""
	Vue qui donne access à l'accueil du catalogue de produits
	"""

	categories = Category.get_root_nodes()
	 

	context_dict = {'categories' : categories}
	return render(request, 'category/browse.html', context_dict)


def category_list(request, topcategory):
	"""
	Vue qui affiche le contenu d'une catégorie
	"""

	category_slugs = topcategory.split('/')

	category_slug = category_slugs[-1]
	

	category = Category.objects.get(slug=category_slug)

	if category.is_leaf():
		producttypes = category.producttypes.all()
		context_dict = {'producttypes':producttypes}
		r_template = 'category/product_type.html'
	else:
		sub_categories = category.get_children()
		context_dict = {'categories': sub_categories}
		r_template = 'category/browse.html'

	return render(request, r_template, context_dict)	


class CategoryProfileListView(ListView):
	model=Category
	context_object_name = 'my_categories'
	

	def get_queryset(self):
		print(self.request.user)
		return Category.objects.filter(productbase__vendeur__username=self.request.user.username).distinct()


