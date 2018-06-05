from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic.list import ListView
from django.contrib.auth.decorators import user_passes_test
from utils.autorisation import acheteur_check
import json
import re
from django.db.models import Q

def normalize_query(query_string, findterms=re.compile(r'"([^"]+)"|(\S+)').findall, normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:

        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']

    '''

    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]


def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.

    '''

    query = None #Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query | or_query
    return query


# Create your views here.
@user_passes_test(acheteur_check,login_url='login')
def index(request):
	"""
	Vue qui donne access à l'accueil du catalogue de produits
	"""

	categories = Category.get_root_nodes()

	category = ''


	context_dict = {'categories' : categories, 'current_cat':category}
	return render(request, 'category/browse.html', context_dict)

@user_passes_test(acheteur_check,login_url='login')
def category_list(request, topcategory):
	"""
	Vue qui affiche le contenu d'une catégorie
	"""

	category_slugs = topcategory.split('/')

	category_slug = category_slugs[-1]

	sub_category_slug = category_slugs[0]




	category = Category.objects.get(slug=category_slug)
	sub_category = Category.objects.get(slug=sub_category_slug)
	hight_category= sub_category.get_ancestors_and_self()
	next_category_slug = hight_category[0]

	if category.is_leaf():
		producttypes = category.producttypes.all()
		producttypes = producttypes.order_by('name')
		context_dict = {'producttypes':producttypes, 'current_cat':category, 'sub_category':sub_category,'hight_category':hight_category,'next_category_slug':next_category_slug}
		r_template = 'category/product_type.html'
	else:
		sub_categories = category.get_children()
		context_dict = {'categories': sub_categories, 'current_cat':category}
		r_template = 'category/browse.html'

	return render(request, r_template, context_dict)


@user_passes_test(acheteur_check,login_url='login')
def search_product_type(request):

    if request.is_ajax():
        q = request.GET.get('term', '')
        producttype = ProductType.objects.filter(description__icontains = q)[:10]

        results = []
        for product in producttype:
            product_json = {}
            product_json['id'] = product.pk
            product_json['label'] = product.name
            product_json['value'] = product.name
            results.append(product_json)

        data = json.dump(results)

    else:
        data = 'fail'
    mimetype = 'application/json'

    return HttpResponse(data, mimetype)

@user_passes_test(acheteur_check,login_url='login')
def search_product_list_view(request):


    query_string=request.GET.get('q')

    entry_query = get_query(query_string, ['description',])

    product_types = ProductType.objects.all()

    found_products= product_types.filter(entry_query)[:20]

    #found_products= product_types.filter(description__icontains = query_string)[:10]


    return render(request, 'category/search_results.html',{'query_string':query_string, 'found_products':found_products})

def papeterie_wizard(request):


    message="la boucle est bouclée"

    return render(request, 'category/papeterie_wizard.html',{'message':message})


class CategoryProfileListView(ListView):
	model=Category
	context_object_name = 'my_categories'


	def get_queryset(self):
		print(self.request.user)
		return Category.objects.filter(productbase__vendeur__username=self.request.user.username).distinct()


