from django.contrib import admin
from .models import *
from mptt.admin import MPTTModelAdmin

# Register your models here.

class ItemAdmin(admin.ModelAdmin):
	list_display = ('nom', 'category','content')
	list_filter = ('category',)
	fields = ['nom', 'category','item_image','slug']


admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(ItemPrice)
