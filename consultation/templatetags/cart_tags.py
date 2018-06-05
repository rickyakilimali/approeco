from django import template

from cart.cart import Cart


register = template.Library()

def get_cart(context, session_key=None, cart_class=Cart):
    """
    Make the cart object available in template.
    Sample usage::
        {% load carton_tags %}
        {% get_cart as cart %}
        {% for product in cart.products %}
            {{ product }}
        {% endfor %}
    """
    request = context['request']
    return cart_class(request.session, session_key=session_key)

register.simple_tag(takes_context=True, name='get_cart')(get_cart)

