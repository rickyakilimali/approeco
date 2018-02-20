from django import template
from category.models import Category

register = template.Library()

@register.inclusion_tag('navigation_sidebar.html')
def show_navigation_sidebar():
	root = Category.get_root_nodes()
	return {'categories':root}

@register.inclusion_tag('tree_nagation.html')
def show_sublevel(category):
	subcategories = category.get_children()
	return {'subcategories':subcategories}
