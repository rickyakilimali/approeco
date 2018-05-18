from django import template

register = template.Library()


# custom template tag that get real field from string representation
@register.filter
def from_string_to_field(instance, field_str):
	return getattr(instance, field_str)