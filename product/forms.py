from django import forms
from .models import *







class _ProductForm(forms.Form):

	def __init__(self,criteria,model, *args,**kwargs):
		super(_ProductForm,self).__init__(*args,**kwargs)
		self.fields['model'] = forms.CharField(label='model', initial=model)
		for key,value in criteria.items():
			self.fields[key]=forms.CharField(label=key,initial=value)




