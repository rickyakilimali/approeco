from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .tables import ProductTable
from .filters import 
from .models import *


class FilteredProductListView(SingleTableMixin, FilterView):
	table_class = ProductTable
	model = Laptop
	template_name = 'productfilter.html'

	filterset_class = ProductFilter