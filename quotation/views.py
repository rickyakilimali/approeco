from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.contenttypes.models import ContentType
from django_tables2.tables import *
from product.tables import *
from django.http import HttpResponse
from django.template.loader import render_to_string
#from weasyprint import HTML
import tempfile
from django.contrib.auth.decorators import user_passes_test
from utils.autorisation import acheteur_check
# Create your views here.


ALL_FIELDS_TABLE= ('id','category','polymorphic_ctype','is_active','productbase_ptr',)
def producttable_factory(modele, exclude=ALL_FIELDS_TABLE):
	the_model = ContentType.objects.get(app_label="product", model=modele).model_class()
	meta = type(str('Meta'), (object,), {'model': the_model, 'exclude': exclude})

	table_class = type(str('%sTable' %the_model._meta.object_name),(ProductTable,), {'Meta': meta})
	return table_class


class MaQuotationView(TemplateView):
	template_name = 'quotation/ma-quotation.html'

#@user_passes_test(acheteur_check,login_url='login')
#def addquotation(request):
#	if request.method == 'POST':
#		postdata=request.POST.copy()

		#Recuperation du type de produit et de la requete
#		the_product_model = postdata.get('model','')
#		the_searchquery = postdata.get('query','')
#		the_searchquery1 = the_searchquery.replace("{", "")
#		the_searchquery2 = the_searchquery1.replace("}","")
#		the_searchcriteria = dict(s.split(':') for s in the_searchquery2.split(','))

		#Suppression de ces données du post
#		del postdata['model']
#		del postdata['csrfmiddlewaretoken']
#		del postdata['query']


#		product_app_label="product"
#		product_model= the_product_model
#		product_type = ContentType.objects.get(app_label=product_app_label, model = product_model)
#		product_dtable = product_type.model_class()
#		product_id_list = postdata.getlist('id')
#		product_id_list = list(map(int, product_id_list))
#		product_list = product_dtable.objects.filter(pk__in=product_id_list)

#		table_class = producttable_factory(product_model)
#		table = table_class(product_list)


		#Create PDF
#		html_string = render_to_string('result.html', {'table':table ,'criteria':the_searchcriteria,'searchcriteria':the_searchquery,'product_model':the_product_model, 'username': request.user})
#		html = HTML(string=html_string)
#		result = html.write_pdf()

		# Creating http response
#		response = HttpResponse(content_type='application/pdf;')
#		response['Content-Disposition'] = 'inline; filename=list_people.pdf'
#		response['Content-Transfer-Encoding'] = 'binary'
#		with tempfile.NamedTemporaryFile(delete=True) as output:
#			output.write(result)
#			output.flush()
#			output = open(output.name, 'rb')
#			response.write(output.read())


		#return render(request,'result.html', {'table':table ,'searchcriteria':the_searchquery,'product_model':the_product_model})
#		return response


def extractfields(classmodel):
	all_fields= classmodel._meta.get_fields(include_parents=False, include_hidden=False)
	attribute_fields = all_fields[5:len(all_fields)]
	product_fields = []
	for field in attribute_fields:
		product_fields.append(field.name)

	return product_fields

@user_passes_test(acheteur_check,login_url='login')
def addnewquotation(request):
	if request.method == 'POST':
		postdata=request.POST.copy()

		#Recuperation du type de produit et de la requete
		the_product_model = postdata.get('model','')
		the_searchquery = postdata.get('query','')
		the_searchquery1 = the_searchquery.replace("{", "")
		the_searchquery2 = the_searchquery1.replace("}","")
		if the_searchquery2 == '':
		    the_searchcriteria = dict()
		else:
		    the_searchcriteria = dict(s.split(':') for s in the_searchquery2.split(','))

		#Suppression de ces données du post
		del postdata['model']
		del postdata['csrfmiddlewaretoken']
		del postdata['query']


		product_app_label="product"
		product_model= the_product_model
		product_type = ContentType.objects.get(app_label=product_app_label, model = product_model)
		product_dtable = product_type.model_class()
		product_id_list = postdata.getlist('id')
		product_id_list = list(map(int, product_id_list))
		product_list = product_dtable.objects.filter(pk__in=product_id_list)
		productfields=extractfields(ContentType.objects.get(app_label="product", model=product_model).model_class())


		return render(request, 'quotation/product-quotation.html', {'fields':productfields,'product_list':product_list, 'criteria':the_searchcriteria,'query':the_searchquery,'product_model':the_product_model, 'username': request.user})


@user_passes_test(acheteur_check,login_url='login')
def addnewquotationnoattributes(request):
	if request.method == 'POST':
		postdata=request.POST.copy()

		#Recuperation du type de produit et de la requete
		the_product_model = postdata.get('model','')
		the_searchquery = postdata.get('query','')
		the_searchquery1 = the_searchquery.replace("{", "")
		the_searchquery2 = the_searchquery1.replace("}","")


		#Suppression de ces données du post
		del postdata['model']
		del postdata['csrfmiddlewaretoken']
		del postdata['query']


		product_app_label="product"
		product_model= the_product_model
		product_type = ContentType.objects.get(app_label=product_app_label, model = product_model)
		product_dtable = product_type.model_class()
		product_id_list = postdata.getlist('id')
		product_id_list = list(map(int, product_id_list))
		product_list = product_dtable.objects.filter(pk__in=product_id_list)
		productfields=extractfields(ContentType.objects.get(app_label="product", model=product_model).model_class())


		return render(request, 'quotation/product-quotation.html', {'fields':productfields,'product_list':product_list, 'query':the_searchquery,'product_model':the_product_model, 'username': request.user})