# sendemail/forms.py
from django import forms

class ContactForm(forms.Form):
	from_email = forms.EmailField(required=True)
	subject = forms.CharField(required=True)
	entreprise= forms.CharField(required=True)
	ville_depart= forms.CharField(required=True)
	ville_arrivee= forms.CharField(required=True)
	date_depart=forms.CharField(required=True)
	date_retour=forms.CharField(required=True)
	nombre_passager=forms.CharField(required=True)
	classe=forms.CharField(required=True)
	message = forms.CharField(widget=forms.Textarea, required=True)