from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from .models import *
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin

from import_export.widgets import ForeignKeyWidget
from django.contrib.contenttypes.models import ContentType

# Register your models here.

class ProductTypeResources(resources.ModelResource):
    category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'slug'))
    product_model = fields.Field(column_name='product_model', attribute='product_model', widget=ForeignKeyWidget(ContentType, 'model'))

    class Meta:
        model = ProductType
        #exclude = ('product_type_image',)



class CategoryAdmin(TreeAdmin):
    form = movenodeform_factory(Category)

class ProductTypeAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
    resource_class = ProductTypeResources
    list_display = ('name', 'description','product_type_image', 'category', 'product_model')


	#fields = ['name', 'slug','product_type_image', 'category','product_model', 'description']


admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductType, ProductTypeAdmin)