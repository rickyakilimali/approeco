from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from .models import *

# Register your models here.

class CategoryAdmin(TreeAdmin):
    form = movenodeform_factory(Category)


class ProductTypeAdmin(admin.ModelAdmin):
	list_display = ('name', 'description','product_type_image', 'category')
	list_filter = ('category',)
	fields = ['name', 'slug','product_type_image', 'category','product_model', 'description']


admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductType, ProductTypeAdmin)