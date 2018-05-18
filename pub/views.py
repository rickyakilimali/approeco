from django.shortcuts import render
from .models import Pub
# Create your views here.
def imageviewer(request):
	voirimage=Pub.objects.all()
	context= {'latest_voirimage':voirimage}
	return render(request,'image.html', context)

def imageviewer1(request):
	voirimage=Pub.objects.filter(cat_image="Energie")
	context= {'latest_voirimage':voirimage}
	return render(request,'image.html', context)

def imageviewer2(request):
	voirimage=Pub.objects.filter(cat_image="Impression-tshirt")
	context= {'latest_voirimage':voirimage}
	return render(request,'image.html', context)

def imageviewer3(request):
	voirimage=Pub.objects.filter(cat_image="Gardiennage maison")
	context= {'latest_voirimage':voirimage}
	return render(request,'image.html', context)
