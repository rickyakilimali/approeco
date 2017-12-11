from django import forms
from .models import *

class LaptopSearchForm(forms.ModelForm):
	class Meta:
		model = Laptop
		fields=('marque', 'type_processeur', 'disque_dur', 'memoire_ram', 'systeme_exploitation', 'taille_ecran',)







class _ProductForm(forms.Form):

	def __init__(self,criteria,model, *args,**kwargs):
		super(_ProductForm,self).__init__(*args,**kwargs)
		self.fields['model'] = forms.CharField(label='model', initial=model)
		for key,value in criteria.items():
			self.fields[key]=forms.CharField(label=key,initial=value)

		


