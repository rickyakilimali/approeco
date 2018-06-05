from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Permission, Group
from django.http import HttpResponse
from .models import *
from cart.cart import Cart
from django.shortcuts import get_list_or_404, get_object_or_404
from django.shortcuts import get_object_or_404, redirect, render


# Create your views here.


def show_category(request,hierarchy= None):
	category_slug = hierarchy.split('/')
	parent = None
	root = Category.objects.all()

	for slug in category_slug[:-1]:
		parent = root.get(parent=parent, slug = slug)

	try:
		instance = Category.objects.get(parent=parent,slug=category_slug[-1])
	except:
		instance = get_object_or_404(Category, slug = category_slug[-1])
		return render(request, "categories.html", {'instance':instance})
	else:
		return render(request, 'categories.html', {'instance':instance})


def index(request):
	parent = None
	root = Category.objects.all()
	instance = root.filter(parent=parent)
	return render(request, 'index.html',{'instance':instance})


def add(request):

	#item = Item.objects.get(id=request.GET.get('id'))
	#quantity = request.GET.get('quantity')

	cart = Cart(request.session)
	item = Item.objects.get(pk=request.GET.get('id'))
	cart.add(item, quantity=1)


	#return HttpResponse(item.nom)
	#return render(request, 'showCart.html')
	return redirect('category',hierarchy=item.category.slug)

def remove(request):
	cart = Cart(request.session)
	item = Item.objects.get(pk=request.GET.get('id'))
	cart.remove(item)
	#return HttpResponse("Removed")
	return redirect('category',hierarchy=item.category.slug)

def show(request):
	return render(request, 'show-cart.html')

def submit(request):

	group = Group.objects.get(name = 'cabinetavocat')
	cabinetavocat_sellers = group.user_set.all()
	cart = Cart(request.session)
	cart_products = cart.products
	resultat = dict()

	for seller in cabinetavocat_sellers:
		total = 0
		for prod in cart_products:
			price = ItemPrice.objects.get(product=prod, vendeur=seller).price
			total = total + price

		resultat[seller.pk] = total

	#return HttpResponse("Cart submited")
	return render(request, 'resultat.html',{'cabinetavocat_sellers':cabinetavocat_sellers,'resultat':resultat})


